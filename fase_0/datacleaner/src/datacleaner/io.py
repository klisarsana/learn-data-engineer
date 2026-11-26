"""Baca / tulis file. Dipisah dari logika cleaning agar cleaning tetap murni"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd

SUPPORTED_OUTPUT = {".csv", ".parquet"}


def read_table(path: Path, sep: str = ",", encoding: str = "utf-8") -> pd.DataFrame:
    # dtype=str + keep_default_na=False: jangan biarkan pandas menebak tipe diam-diam
    # Contoh: (ID "0812" menjadi 812). Konversi tipe dilakukan eksplisit di cleaning.
    return pd.read_csv(path, sep=sep, encoding=encoding, dtype=str, keep_date_col=False)


def write_table(df: pd.DataFrame, path: Path) -> None:
    """Tulis atomik: sementara dulu, baru di rename.
    Mencegah output setengah jadi"""
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_OUTPUT:
        raise ValueError(
            f"Format output '{suffix}' tidak didukung. Pilih: {sorted(SUPPORTED_OUTPUT)}"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.stem}.tmp{suffix}")
    try:
        if suffix == ".csv":
            df.to_csv(tmp, index=False)
        else:
            df.to_parquet(tmp, index=False)
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)
