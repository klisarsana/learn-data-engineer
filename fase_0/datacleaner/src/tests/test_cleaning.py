import pandas as pd
import pytest

from datacleaner.cleaning import (
    CleanConfig,
    clean,
    normalize_col,
    parse_date,
    parse_numbers,
    snake_case,
    standardize_missing,
)


@pytest.mark.parametrize(
    "raw,expected",
    [
        (" Order Date ", "order_date"),
        ("orderDate", "order_date"),
        ("Harga (Rp)", "harga_rp"),
        ("A--B", "a_b"),
    ],
)
def test_snake_case(raw, expected):
    assert snake_case(raw) == expected


def test_normalize_columns_handles_duplicates():
    df = pd.DataFrame([[1, 2]], columns=["Nama", " nama "])
    out, renamed = normalize_col(df)
    assert list(out.columns) == ["nama", "nama_2"]
    assert renamed


def test_standardize_missing_counts_and_replace():
    df = pd.DataFrame({"a": ["x", "N/A", "", "null", "ok"]})
    out, n = standardize_missing(df)
    assert n == 3
    assert out["a"].isna().sum() == 3


@pytest.mark.parameterize(
    "value,decimal,expected",
    [
        ("Rp 1.500.000", ",", 1_500_000.0),
        ("250.000,50", ",", 250000.5),
        ("1,234.5", ".", 1234.5),
    ],
)
def test_parse_numbers_formats(value, decimal, expected):
    out, fail = parse_numbers(pd.DataFrame({"x": [value]}), ("x",), decimal)
    assert out["x"].iloc[0] == pytest.approx(expected)
    assert fail["x"] == 0


def test_parse_numbers_report_failure():
    out, fail = parse_numbers(pd.DataFrame({"x": ["abc", "10"]}), ("x",), ".")
    assert fail["x"] == 1
    assert out["x"].isna().sum() == 1


def _messy():
    return pd.DataFrame(
        {
            "Order ID": ["1", "2", "2", "", "3"],
            "Order Date": [
                "05/03/2024",
                "2024-03-06",
                "2024-03-06",
                "08/03/2024",
                "salah",
            ],
            "Amount": ["1.000,5", "2.000", "2.000", "3", "x"],
        }
    )


CFG = CleanConfig(("Order Date",), ("Amount",), ("Order ID",), decimal=",")


def test_clean_end_to_end():
    out, rep = clean(_messy(), CFG)
    assert rep.rows_in == 5
    assert rep.duplicates_remove == 1
    assert rep.rows_missing_drop == 1  # ID Kosong
    assert rep.rows_out == len(out) == 3
    assert pd.api.types.is_datetime64_any_dtype(out["order_date"])
    assert rep.parse_fail["order_date"] == 1


def test_clean_does_not_mutate_input():
    df = _messy()
    snapshot = df.copy(deep=True)
    clean(df, CFG)
    pd.testing.assert_frame_equal(df, snapshot)


def test_clean_unknown_column_raises():
    with pytest.raises(ValueError, match="Kolom tidak ditemukan"):
        clean(_messy(), CleanConfig(numeric_col=("tidak_ada",)))


def test_parse_dates_iso_not_swapped_by_dayfirst():
    # regres: dengan dayfirst=True, "2024-03-05" sempat terbaca 3 juni
    df = pd.DataFrame({"d": ["2024-03-06", "05/03/2024", "07 Mar 2024", "salah", None]})
    out, fail = parse_date(df, ("d",), dayfirst=True)
    got = out["d"].dt.strftime("%Y-%m-%d").tolist()
    assert got[:3] == ["2024-03-06", "2024-03-05", "2024-03-07"]
    assert fail["d"] == 1
