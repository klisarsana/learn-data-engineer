# datacleaner

CLI untuk membersihkan file CSV yang berantakan: nama kolom, spasi, nilai kosong,
tanggal, angka (format Indonesia), duplikat, dan baris tanpa data wajib.

## Instalasi

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Pemakaian

```bash
datacleaner data/sample/messy_sales.csv -o out/clean.csv \
  --date-cols "Order Date" --numeric-cols Amount --decimal , \
  --required-cols "Order ID"
```

| Opsi | Fungsi |
|---|---|
| `-o, --output` | Tujuan (`.csv` / `.parquet`). Default `<input>_clean.csv` |
| `--date-cols` / `--numeric-cols` | Kolom yang dikonversi tipenya (nama asli boleh, otomatis di-snake_case) |
| `--required-cols` | Baris dengan nilai kosong di kolom ini dibuang |
| `--decimal` | `,` untuk format `1.500,75`; default `.` |
| `--monthfirst` | Tanggal ambigu dibaca bulan/hari (default hari/bulan) |
| `--dry-run` | Hanya tampilkan laporan, tidak menulis file |
| `--force` | Izinkan menimpa output yang sudah ada |

**Exit code:** `0` sukses, `1` data/konfigurasi bermasalah, `2` salah pemakaian (file tidak ada, output = input, dll).

## Contoh sebelum → sesudah

| Order ID | Order Date | Amount | City |
|---|---|---|---|
| 1001 | `05/03/2024` | `Rp 1.500.000` | Jakarta |
| 1002 | `2024-03-06` | `250.000,50` | `N/A` |
| 1002 | `2024-03-06` | `250.000,50` | `N/A` |
| *(kosong)* | `08/03/2024` | `75.000` | `-` |

→ `2024-03-05`, `1500000.0`, duplikat dibuang, baris tanpa ID dibuang, `N/A` dan `-` menjadi kosong.
Tiap perubahan dicatat di laporan yang tampil saat dijalankan.

## Keputusan desain

- **Baca semua kolom sebagai teks** (`dtype=str`): pandas tidak menebak tipe diam-diam (ID `0812` tidak berubah jadi `812`). Konversi tipe hanya untuk kolom yang kamu sebut.
- **Fungsi cleaning murni**, terpisah dari I/O dan CLI: mudah diuji dan dipakai ulang.
- **Data asli tidak pernah diubah**: output ≠ input, tidak menimpa tanpa `--force`, penulisan atomik (file sementara lalu rename).
- **Tidak ada yang hilang diam-diam**: nilai yang gagal di-parse dihitung dan dilaporkan.
- **Tanggal ISO diparse terpisah** agar `dayfirst` tidak membalik `2024-03-06` menjadi 3 Juni (ada regression test).

## Pengembangan

```bash
make test     # pytest + coverage
make lint     # ruff
make format
```

## Batasan & rencana

- File sangat besar (> RAM): belum ada pemrosesan `chunksize`.
- Strategi missing value baru "buang baris"; imputasi belum ada.
- Ide lanjutan: konfigurasi lewat file YAML, ekspor laporan ke JSON, dukungan Excel.