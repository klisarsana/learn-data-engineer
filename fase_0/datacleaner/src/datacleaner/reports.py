"""
Laporan Hasil pembersihan data:
apa saja data yang diubah, agar proses transparan
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CleaningReport:
    rows_in: int = 0
    rows_out: int = 0
    columns_renamed: dict[str, str] = field(default_factory=dict)
    values_set_to_na: int = 0
    duplicates_remove: int = 0
    rows_missing_drop: int = 0
    # kolom -> jumlah nilai yang gagal di-parse (menjadi kosong)
    parse_fail: dict[str, int] = field(default_factory=dict)

    def summary_lines(self) -> list[str]:
        lines = [
            f"Baris masuk                   : {self.rows_in}",
            f"Baris keluar                  : {self.rows_out}",
            f"Nama kolom diubah             : {self.columns_renamed}",
            f"Nilai kosong distandarisasi   : {self.values_set_to_na}",
            f"Duplikat yang dihapus         : {self.duplicates_remove}",
            f"Baris yang dibuang            : {self.rows_missing_drop}",
        ]
        for col, n in self.parse_fail.items():
            if n:
                lines.append(f"Gagal parse di '{col}': {n} nilai -> di kosongkan")
        return lines
