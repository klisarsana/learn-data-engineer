from pathlib import Path

import pandas as pd

from datacleaner.cli import main

SAMPLE = Path(__file__).parent.parent / "data" / "sample" / "messy_sales.csv"


def run(tmp_path, *extra):
    out = tmp_path / "out.csv"
    code = main([str(SAMPLE), "-o", str(out), *extra])
    return code, out


def test_happy_path(tmp_path):
    code, out = run(
        tmp_path,
        "--date-cols",
        "Order Date",
        "--numeric-cols",
        "Amount",
        "--decimal",
        ",",
        "--required-cols",
        "Order ID",
    )
    assert code == 0
    df = pd.read_csv(out)
    assert "order_date" in df.columns
    assert df["order_id"].is_unique


def test_missing_input_returns_2(tmp_path):
    assert main([str(tmp_path / "nope.csv")]) == 2


def test_bad_column_returns_1(tmp_path):
    code, _ = run(tmp_path, "--numeric-cols", "kolom_gaib")
    assert code == 1


def test_refuses_overwrite_without_force(tmp_path):
    code, out = run(tmp_path)
    assert code == 0
    assert main([str(SAMPLE), "-o", str(out)]) == 2
    assert main([str(SAMPLE), "-o", str(out), "--force"]) == 0


def test_never_overwrites_input(tmp_path):
    copy = tmp_path / "in.csv"
    copy.write_text(SAMPLE.read_text())
    assert main([str(copy), "-o", str(copy), "--force"]) == 2


def test_dry_run_writes_nothing(tmp_path):
    code, out = run(tmp_path, "--dry-run")
    assert code == 0 and not out.exists()


def test_parquet_output(tmp_path):
    out = tmp_path / "out.parquet"
    assert main([str(SAMPLE), "-o", str(out)]) == 0
    assert pd.read_parquet(out).shape[0] > 0
