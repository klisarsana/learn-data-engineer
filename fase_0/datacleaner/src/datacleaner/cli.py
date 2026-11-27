"""CLI Interface.
Tipis: Parse Argumen, panggil fungsi, atur exit code
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from . import __version__
from .cleaning import CleanConfig, clean
from .io import read_table, write_table

log = logging.getLogger("datacleaner")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="datacleaner",
        description="Bersihkan CSV: nama kolom, spasi, nilai kosong, tanggal, angka, duplikat",
    )
    p.add_argument("input", type=Path, help="path file CSV input")
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        help="path output (.csv/.parquet); default <input>_clean.csv",
    )
    p.add_argument(
        "--date-cols", nargs="*", default=[], metavar="COL", help="kolom tanggal"
    )
    p.add_argument(
        "--numeric-cols", nargs="*", default=[], metavar="COL", help="kolom angka"
    )
    p.add_argument(
        "--required-cols",
        nargs="*",
        default=[],
        metavar="COL",
        help="baris dengan nilai kosong di dalam kolom ini dibuang",
    )
    p.add_argument(
        "--decimal",
        choices=[".", ","],
        default=".",
        help="pemisah desimal angka (default '.')",
    )
    p.add_argument(
        "--monthfirst", action="store_true", help="tanggal ambigu dibaca bulan/hari"
    )
    p.add_argument("--sep", default=",", help="pemisah kolom CSV (default ',')")
    p.add_argument("--encoding", default="utf-8", help="encoding input (default utf-8)")
    p.add_argument(
        "--dry-run", action="store_true", help="tampilkan laporan tanpa menulis file"
    )
    p.add_argument(
        "--force", action="store_true", help="timpa file output jika sudah ada"
    )
    p.add_argument("-v", "--verbose", action="store_true", help="log_detail (DEBUG)")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,
    )

    src: Path = args.input
    dst: Path = args.output or src.with_name(f"{src.stem}_clean.csv")

    if not src.is_file():
        log.error("File input tidak ditemukan: %s", src)
        return 2
    if dst.resolve() == src.resolve():
        log.error("Output tidak boleh sama dengan input (data asli harus tetap utuh)")
        return 2
    if dst.exists() and not args.force and not args.dry_run:
        log.error("Output sudah ada: %s (pakai --force untuk menimpa)", dst)
        return 2

    config = CleanConfig(
        date_col=tuple(args.date_cols),
        numeric_col=tuple(args.numeric_cols),
        required_col=tuple(args.required_cols),
        decimal=args.decimal,
        dayfirst=not args.monthfirst,
    )

    try:
        df = read_table(src, sep=args.sep, encoding=args.encoding)
        log.info("Memabaca %s (%d baris, %d kolom)", src, len(df), len(df.columns))
        cleaned, report = clean(df, config)
        for line in report.summary_lines():
            log.info(line)
        if args.dry_run:
            log.info("Dry run: tidak ada file ditulis")
            return 0
        write_table(cleaned, dst)
    # Kesalahan input pengguna
    except (ValueError, UnicodeDecodeError) as e:
        log.error("%s", e)
        return 1
    except Exception:
        log.exception("Terjadi kesalahan tak terduga")
        return 1

    log.info("Selesai -> %s", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
