"""
Logika Cleaning Data.
Prinsip: Setiap fungsi bersifat murni yaitu -> (input DataFrame -> output DataFrame)
tanpa Input/Output sehingga mudah diuji dan dipakai ulang diluar CLI
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype, is_numeric_dtype

from .reports import CleaningReport

NA_TOKENS = frozenset({"", "na", "n/a", "nan", "null", "none", "-", "?", "tidak ada"})
_ISO_DATE = re.compile(r"^\d{4}-\d{1,2}-\d{1,2}")
_CURRENCY = re.compile(r"(?i)rp\.?|idr|usd|[$\s]")


def snake_case(name: str) -> str:
    # camelCase -> camel_case
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name.strip())
    name = re.sub(r"[^\w]+", "_", name)
    return re.sub(r"_+", "_", name).strip("_").lower()


@dataclass(frozen=True)
class CleanConfig:
    date_col: tuple[str, ...] = ()
    numeric_col: tuple[str, ...] = ()
    required_col: tuple[str, ...] = ()
    decimal: str = "."
    dayfirst: bool = True

    def normalized(self) -> CleanConfig:
        """Samakan nama kolom di config dengan nama kolom setelah di snake_case"""
        return CleanConfig(
            tuple(map(snake_case, self.date_col)),
            tuple(map(snake_case, self.numeric_col)),
            tuple(map(snake_case, self.required_col)),
            self.decimal,
            self.dayfirst,
        )


def _text_columns(df: pd.DataFrame) -> list[str]:
    return [
        c
        for c in df.columns
        if not is_numeric_dtype(df[c]) and not is_datetime64_any_dtype(df[c])
    ]


def normalize_col(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, str]]:
    """Ubah nama kolom ke snake_case; tangani kolom kembar dengan akhiran _2, _3, ..."""
    seen: dict[str, int] = {}
    mapping: dict[str, str] = {}
    for original in df.columns:
        new = snake_case(str(original)) or "kolom"
        seen[new] = seen.get(new, 0) + 1
        if seen[new] > 1:
            new = f"{new}_{seen[new]}"
        mapping[original] = new
    renamed = {o: n for o, n in mapping.items() if o != n}
    out = df.copy()
    out.columns = list(mapping.values())
    return out, renamed


def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in _text_columns(out):
        out[col] = out[col].map(lambda v: v.strip() if isinstance(v, str) else v)
    return out


def standardize_missing(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Ubah token kosong ('', 'N/A', 'null', '-', ...) menjadi NA yang konsisten."""
    out = df.copy()
    total = 0
    for col in _text_columns(out):
        mask = out[col].map(lambda v: isinstance(v, str) and v.lower() in NA_TOKENS)
        total += int(mask.sum())
        out[col] = out[col].mask(mask, pd.NA)
    return out, total


def _parse_date_series(s: pd.Series, dayfirst: bool) -> pd.Series:
    """Format ISO (2024-03-06) diparse terpisah: `dayfirst=True` akan salah membaliknya
    menjadi 3 Juni. Format lain (05/03/2024, 07 Mar 2024) memakai aturan dayfirst."""
    is_iso = s.astype("string").str.match(_ISO_DATE).fillna(False).astype(bool)
    iso = pd.to_datetime(s.where(is_iso), errors="coerce", format="ISO8601")
    other = pd.to_datetime(
        s.where(~is_iso & s.notna()), errors="coerce", format="mixed", dayfirst=dayfirst
    )
    return iso.fillna(other)


def parse_date(
    df: pd.DataFrame, columns: tuple[str, ...], dayfirst: bool
) -> tuple[pd.DataFrame, dict[str, int]]:
    out = df.copy()
    failures: dict[str, int] = {}
    for col in columns:
        parsed = _parse_date_series(out[col], dayfirst)
        failures[col] = int((out[col].notna() & parsed.isna()).sum())
        out[col] = parsed
    return out, failures


def parse_numbers(
    df: pd.DataFrame, columns: tuple[str, ...], decimal: str
) -> tuple[pd.DataFrame, dict[str, int]]:
    out = df.copy()
    failures: dict[str, int] = {}
    for col in columns:
        text = out[col].astype("string").str.replace(_CURRENCY, "", regex=True)
        if decimal == ",":
            text = text.str.replace(".", "", regex=False).str.replace(
                ",", ".", regex=False
            )
        else:
            text = text.str.replace(",", "", regex=False)
        parsed = pd.to_numeric(text, errors="coerce")
        failures[col] = int((out[col].notna() & parsed.isna()).sum())
        out[col] = parsed
    return out, failures


def _check_columns(df: pd.DataFrame, config: CleanConfig) -> None:
    wanted = set(config.date_col) | set(config.numeric_col) | set(config.required_col)
    missing = sorted(wanted - set(df.columns))
    if missing:
        raise ValueError(
            f"Kolom tidak ditemukan: {missing}. Kolom tersedia: {list(df.columns)}"
        )


def clean(df: pd.DataFrame, config: CleanConfig) -> tuple[pd.DataFrame, CleaningReport]:
    """Pipeline utama. Urutan: normalisasi nama -> strip -> NA -> tipe -> duplikat -> wajib isi."""
    report = CleaningReport(rows_in=len(df))

    out, report.columns_renamed = normalize_col(df)
    config = config.normalized()
    _check_columns(out, config)

    out = strip_whitespace(out)
    out, report.values_set_to_na = standardize_missing(out)

    out, date_fail = parse_date(out, config.date_col, config.dayfirst)
    out, num_fail = parse_numbers(out, config.numeric_col, config.decimal)
    report.parse_fail = {**date_fail, **num_fail}

    before = len(out)
    out = out.drop_duplicates()
    report.duplicates_remove = before - len(out)

    if config.required_col:
        before = len(out)
        out = out.dropna(subset=list(config.required_col))
        report.rows_missing_drop = before - len(out)

    out = out.reset_index(drop=True)
    report.rows_out = len(out)
    return out, report
