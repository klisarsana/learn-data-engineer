# 🛠️ Roadmap Data Engineer dari Nol — Project Based Learning

> Dari nol sampai siap kerja dalam **± 7–9 bulan** (10–15 jam/minggu).
> Setiap fase ditutup dengan **project nyata** yang masuk ke portofolio GitHub kamu.

---

## 📌 Daftar Isi

1. [Cara Memakai Roadmap Ini](#1-cara-memakai-roadmap-ini)
2. [Gambaran Besar: Apa Itu Data Engineer?](#2-gambaran-besar-apa-itu-data-engineer)
3. [Peta Tech Stack](#3-peta-tech-stack)
4. [Ringkasan Timeline](#4-ringkasan-timeline)
5. [Fase 0 — Fondasi](#fase-0--fondasi-minggu-14)
6. [Fase 1 — SQL & Data Modeling](#fase-1--sql--data-modeling-minggu-58)
7. [Fase 2 — Python untuk Data Pipeline (ETL)](#fase-2--python-untuk-data-pipeline-etl-minggu-912)
8. [Fase 3 — Docker & Orkestrasi dengan Airflow](#fase-3--docker--orkestrasi-dengan-airflow-minggu-1315)
9. [Fase 4 — Data Warehouse & Transformasi dengan dbt](#fase-4--data-warehouse--transformasi-dengan-dbt-minggu-1620)
10. [Fase 5 — Cloud & Data Lake](#fase-5--cloud--data-lake-minggu-2124)
11. [Fase 6 — Big Data Processing dengan Spark](#fase-6--big-data-processing-dengan-spark-minggu-2528)
12. [Fase 7 — Streaming dengan Kafka](#fase-7--streaming-dengan-kafka-minggu-2931)
13. [Fase 8 — Kualitas Data, CI/CD, IaC & Observability](#fase-8--kualitas-data-cicd-iac--observability-minggu-3234)
14. [Fase 9 — Capstone End-to-End](#fase-9--capstone-end-to-end-minggu-3540)
15. [Fase 10 — Persiapan Kerja](#fase-10--persiapan-kerja-minggu-4144)
16. [Standar Kualitas Project](#standar-kualitas-project)
17. [Template Struktur Repo](#template-struktur-repo)
18. [Checklist Kesiapan Kerja](#checklist-kesiapan-kerja)
19. [Sumber Belajar](#sumber-belajar)
20. [Tips dari Senior](#tips-dari-senior)

---

## 1. Cara Memakai Roadmap Ini

**Prinsip Project Based Learning (PBL) di roadmap ini:**

1. **Build dulu, pahami mendalam kemudian.** Baca konsep secukupnya, lalu langsung bangun project. Teori diperdalam saat kamu mentok.
2. **Satu fase = satu project wajib.** Tidak boleh lanjut fase berikutnya sebelum project fase ini lolos *Definition of Done* (DoD).
3. **Semua project di-push ke GitHub** dengan README yang rapi. Ini adalah portofolio kamu.
4. **Pakai data nyata.** Hindari dataset mainan; pakai data dengan volume dan "kotoran" yang realistis.
5. **Dokumentasikan keputusan.** Kenapa memilih tool A, bukan B? Kemampuan menjelaskan trade-off adalah pembeda junior biasa vs junior yang menonjol.

**Ritme mingguan yang disarankan:**

| Aktivitas | Porsi |
|---|---|
| Belajar konsep (baca / video) | 20% |
| Mengerjakan project (hands-on) | 60% |
| Debug, dokumentasi, refleksi | 20% |

---

## 2. Gambaran Besar: Apa Itu Data Engineer?

Data engineer bertugas **membangun dan merawat sistem yang memindahkan, mengubah, dan menyimpan data** agar tim analis, data scientist, dan aplikasi bisa memakainya secara andal.

```
 Sumber Data          Ingestion        Storage            Transformasi        Serving
┌────────────┐      ┌───────────┐    ┌─────────────┐     ┌─────────────┐    ┌──────────────┐
│ API        │      │ Batch     │    │ Data Lake   │     │ Cleaning    │    │ BI Dashboard │
│ Database   │ ───► │ (Airflow) │───►│ (S3/GCS)    │────►│ Modeling    │───►│ ML Features  │
│ File/CSV   │      │ Streaming │    │ Data        │     │ (dbt/Spark) │    │ Aplikasi     │
│ Event/Log  │      │ (Kafka)   │    │ Warehouse   │     │             │    │              │
└────────────┘      └───────────┘    └─────────────┘     └─────────────┘    └──────────────┘
                     ◄──────── Orkestrasi, Monitoring, Data Quality, CI/CD ────────►
```

**Skill inti yang dicari perusahaan:**

- SQL tingkat lanjut (paling sering diuji saat interview)
- Python untuk pipeline
- Data modeling & warehousing
- Orkestrasi pipeline (Airflow)
- Cloud (AWS / GCP / Azure)
- Pemrosesan skala besar (Spark) dan dasar streaming (Kafka)
- Praktik rekayasa perangkat lunak: Git, testing, CI/CD, Docker

---

## 3. Peta Tech Stack

Fokus pada **satu stack utama** dulu. Jangan mencoba menguasai semuanya sekaligus.

| Lapisan | Pilihan Utama (dipakai di roadmap) | Alternatif |
|---|---|---|
| Bahasa | Python, SQL | Scala (opsional) |
| Database OLTP | PostgreSQL | MySQL |
| Containerization | Docker, Docker Compose | Podman |
| Orkestrasi | Apache Airflow | Prefect, Dagster |
| Transformasi | dbt | SQLMesh, Spark SQL |
| Warehouse | BigQuery / DuckDB (lokal) | Snowflake, Redshift |
| Data Lake | GCS / S3 (+ Parquet) | Azure Data Lake |
| Batch processing | Apache Spark (PySpark) | Dask, Polars |
| Streaming | Apache Kafka | Redpanda, Pulsar |
| IaC | Terraform | Pulumi |
| CI/CD | GitHub Actions | GitLab CI |
| Data quality | Great Expectations / dbt tests | Soda |
| Visualisasi | Metabase / Looker Studio | Superset |

> 💡 **Rekomendasi jalur cloud:** pilih **satu** cloud saja (GCP lebih ramah pemula karena free tier BigQuery; AWS paling banyak lowongan). Konsepnya 90% transferable.

---

## 4. Ringkasan Timeline

| Fase | Topik | Durasi | Project Utama |
|---|---|---|---|
| 0 | Fondasi (Linux, Git, Python dasar) | 4 minggu | CLI Data Cleaner |
| 1 | SQL & Data Modeling | 4 minggu | Mini Data Warehouse E-Commerce |
| 2 | Python ETL | 4 minggu | Pipeline Ingestion API → PostgreSQL |
| 3 | Docker & Airflow | 3 minggu | Pipeline Terjadwal Berbasis Docker |
| 4 | Data Warehouse & dbt | 5 minggu | Analytics Engineering Project |
| 5 | Cloud & Data Lake | 4 minggu | Cloud Data Lake + Warehouse |
| 6 | Spark | 4 minggu | Batch Processing Skala Besar |
| 7 | Streaming Kafka | 3 minggu | Real-Time Event Pipeline |
| 8 | Quality, CI/CD, IaC, Observability | 3 minggu | Produksi-kan Pipeline Sebelumnya |
| 9 | Capstone | 6 minggu | End-to-End Data Platform |
| 10 | Persiapan Kerja | 4 minggu | Portofolio, CV, Latihan Interview |

---

## Fase 0 — Fondasi (Minggu 1–4)

**Tujuan:** nyaman memakai terminal, Git, dan menulis Python yang rapi.

### Materi

- **Linux & Terminal:** navigasi, `grep`, `awk`, `sed`, `cron`, permission, pipe, environment variable
- **Git & GitHub:** commit, branch, pull request, resolve conflict, `.gitignore`
- **Python dasar:** tipe data, list/dict comprehension, fungsi, OOP dasar, error handling, file I/O, virtual environment (`venv`/`uv`), type hints
- **Library:** `pandas` dasar, `requests`, `argparse`, `logging`, `pytest` dasar

### 🚀 Project 0 — CLI Data Cleaner

Bangun aplikasi command-line yang membaca file CSV berantakan lalu membersihkannya.

**Fitur minimal:**
- Menerima path file lewat argumen CLI
- Menangani nilai kosong, duplikat, tipe data salah, dan format tanggal tidak konsisten
- Menyimpan hasil bersih ke CSV/Parquet
- Menulis log proses (berapa baris dibuang, diperbaiki)

**Definition of Done:**
- [ ] Repo punya README dengan cara pakai
- [ ] Minimal 5 unit test dengan `pytest`
- [ ] Commit history rapi (bukan satu commit raksasa)
- [ ] Kode lolos linter (`ruff` atau `flake8`)

---

## Fase 1 — SQL & Data Modeling (Minggu 5–8)

**Tujuan:** menulis SQL kompleks dengan percaya diri dan merancang skema data yang benar.

### Materi

- **SQL dasar → lanjut:** `JOIN` semua jenis, `GROUP BY`, subquery, **CTE**, **window function** (`ROW_NUMBER`, `RANK`, `LAG/LEAD`, running total), `CASE WHEN`, manipulasi tanggal
- **Performa:** index, `EXPLAIN ANALYZE`, partisi dasar
- **Normalisasi:** 1NF–3NF, kapan denormalisasi
- **Dimensional modeling (Kimball):** fact table, dimension table, **star schema**, grain, **Slowly Changing Dimension (SCD Tipe 1 & 2)**
- **OLTP vs OLAP**, row-store vs column-store

### 🚀 Project 1 — Mini Data Warehouse E-Commerce

Gunakan dataset publik **Olist Brazilian E-Commerce** (Kaggle).

**Langkah:**
1. Jalankan PostgreSQL lokal (Docker lebih baik).
2. Muat data mentah ke skema `raw`.
3. Rancang **star schema** (`fact_orders`, `dim_customer`, `dim_product`, `dim_seller`, `dim_date`).
4. Tulis SQL transformasi dari `raw` → `warehouse`.
5. Buat 10 query analitik bisnis (top produk, retensi pelanggan, rata-rata waktu pengiriman, dll.) memakai CTE dan window function.

**Definition of Done:**
- [ ] ERD (gambar) untuk skema sumber dan star schema
- [ ] Dokumen keputusan: grain fact table dan alasan desain dimensi
- [ ] 10 query analitik beserta penjelasan hasilnya
- [ ] Satu contoh implementasi SCD Tipe 2
- [ ] Minimal 2 query dioptimasi dengan index, dibuktikan lewat `EXPLAIN ANALYZE` sebelum/sesudah

---

## Fase 2 — Python untuk Data Pipeline (ETL) (Minggu 9–12)

**Tujuan:** membangun pipeline ETL/ELT yang **idempoten**, terstruktur, dan bisa diuji.

### Materi

- **Konsep:** ETL vs ELT, batch vs incremental load, **idempotency**, full refresh vs upsert, backfill
- **Ingest dari API:** pagination, rate limit, retry dengan exponential backoff, autentikasi
- **Format file:** CSV, JSON, **Parquet**, Avro — dan kenapa Parquet dipakai
- **Python lanjut:** `pandas` skala menengah, `Polars`/`DuckDB`, `SQLAlchemy`, `pydantic` untuk validasi skema, struktur package, konfigurasi via `.env`
- **Testing:** unit test untuk fungsi transformasi, mocking API

### 🚀 Project 2 — Pipeline Ingestion API → PostgreSQL

Pilih sumber data hidup, misalnya: **API cuaca (BMKG/Open-Meteo)**, **GitHub API**, **CoinGecko**, atau **data publik Indonesia (data.go.id)**.

**Langkah:**
1. Ekstrak data dari API secara berkala dengan penanganan error dan retry.
2. Simpan data mentah apa adanya (JSON/Parquet) di folder `raw/`.
3. Transformasi dan validasi dengan `pydantic`.
4. Muat ke PostgreSQL dengan **upsert** (jalan dua kali, hasilnya tidak duplikat).
5. Dukung **incremental load** (hanya ambil data baru).

**Definition of Done:**
- [ ] Pipeline idempoten (dibuktikan dengan test)
- [ ] Logging terstruktur dan penanganan kegagalan
- [ ] Konfigurasi & secret tidak hard-coded
- [ ] Test coverage fungsi transformasi ≥ 70%
- [ ] README berisi diagram alur data

---

## Fase 3 — Docker & Orkestrasi dengan Airflow (Minggu 13–15)

**Tujuan:** menjalankan pipeline secara terjadwal, terpantau, dan dapat direproduksi.

### Materi

- **Docker:** image, container, volume, network, `Dockerfile`, **Docker Compose**
- **Airflow:** DAG, task, operator, scheduler, executor, XCom, sensor, retry, SLA, **backfill**, TaskFlow API
- **Desain DAG yang baik:** task kecil dan idempoten, tanpa logika berat di top-level DAG, parameterisasi tanggal (`logical_date`)

### 🚀 Project 3 — Pipeline Terjadwal Berbasis Docker

Ambil **Project 2**, lalu:

1. Bungkus seluruh stack (PostgreSQL + Airflow + pipeline) dalam **satu `docker-compose.yml`**.
2. Ubah pipeline menjadi **DAG Airflow** harian dengan task: `extract → validate → load → notify`.
3. Tambahkan notifikasi saat gagal (email/Telegram/Slack webhook).
4. Lakukan **backfill** data 30 hari ke belakang.

**Definition of Done:**
- [ ] `docker compose up` langsung menjalankan seluruh sistem
- [ ] DAG punya retry, timeout, dan alert kegagalan
- [ ] Backfill berhasil tanpa duplikasi data
- [ ] Screenshot Airflow UI (graph & riwayat run) di README

---

## Fase 4 — Data Warehouse & Transformasi dengan dbt (Minggu 16–20)

**Tujuan:** menguasai pola **ELT modern** dan analytics engineering.

### Materi

- **Warehouse cloud:** BigQuery (partitioning, clustering, biaya per query) atau Snowflake/Redshift. Alternatif lokal: **DuckDB**
- **Arsitektur berlapis:** `raw/staging → intermediate → marts` (medallion: bronze/silver/gold)
- **dbt:** model, `ref()`, `source()`, materialization (view/table/incremental), **tests**, dokumentasi, macro, snapshot (SCD), seeds
- **Modeling lanjut:** One Big Table vs star schema, metrik & semantic layer (konsep)

### 🚀 Project 4 — Analytics Engineering Project

Gunakan dataset besar-ish: **NYC Taxi Trips** atau **GitHub Archive**.

**Langkah:**
1. Muat data mentah ke warehouse (BigQuery atau DuckDB).
2. Bangun layer `staging`, `intermediate`, `marts` dengan **dbt**.
3. Tambahkan test (`unique`, `not_null`, `relationships`, `accepted_values`) dan test kustom.
4. Buat model **incremental** untuk tabel besar.
5. Generate dokumentasi dbt (`dbt docs`) lengkap dengan lineage graph.
6. Buat dashboard (Metabase / Looker Studio) dari layer marts.

**Definition of Done:**
- [ ] Lineage graph dbt terlihat jelas di README
- [ ] Semua model utama punya test dan deskripsi
- [ ] Minimal satu model incremental dan satu snapshot
- [ ] Dashboard dengan ≥ 4 visual yang menjawab pertanyaan bisnis
- [ ] Catatan optimasi biaya/performa (partisi, clustering)

---

## Fase 5 — Cloud & Data Lake (Minggu 21–24)

**Tujuan:** memindahkan pipeline ke cloud dengan arsitektur data lake yang benar.

### Materi

- **Dasar cloud:** IAM (least privilege), region, billing & budget alert, service account
- **Object storage:** GCS / S3, struktur folder, partisi berbasis tanggal, lifecycle policy
- **Format kolumnar:** Parquet, kompresi, partition pruning
- **Arsitektur:** data lake vs warehouse vs **lakehouse** (konsep Delta Lake / Iceberg)
- **Layanan terkelola:** Cloud Composer/MWAA (konsep), Cloud Functions/Lambda, Pub/Sub/SQS

### 🚀 Project 5 — Cloud Data Lake + Warehouse

1. Ingest data dari sumber (API/file) ke **bucket raw** (format asli).
2. Konversi ke **Parquet terpartisi** di layer `curated`.
3. Muat ke **warehouse cloud** sebagai external/native table.
4. Orkestrasi dengan Airflow (lokal/Docker boleh) yang memanggil layanan cloud.
5. Pasang **budget alert** dan terapkan IAM least privilege.

**Definition of Done:**
- [ ] Diagram arsitektur cloud (draw.io / Excalidraw)
- [ ] Struktur bucket terdokumentasi (`raw/`, `curated/`, `analytics/`)
- [ ] Tidak ada credential di repo (pakai service account + secret manager/env)
- [ ] Estimasi biaya bulanan ditulis di README

> ⚠️ **Hati-hati biaya cloud.** Selalu pasang budget alert di hari pertama dan matikan resource setelah selesai.

---

## Fase 6 — Big Data Processing dengan Spark (Minggu 25–28)

**Tujuan:** memproses data berukuran besar secara terdistribusi.

### Materi

- **Konsep terdistribusi:** partisi, shuffle, narrow vs wide transformation, lazy evaluation
- **PySpark:** DataFrame API, Spark SQL, join strategy (broadcast join), window function, UDF (dan kenapa dihindari)
- **Optimasi:** skew data, caching, repartition vs coalesce, membaca Spark UI
- **Format:** Parquet, Delta Lake (pengenalan)

### 🚀 Project 6 — Batch Processing Skala Besar

1. Proses dataset ≥ **10 GB** (mis. NYC Taxi multi-tahun atau GitHub Archive) dengan **PySpark**.
2. Lakukan agregasi, join dengan tabel referensi, dan window function.
3. Tulis hasil sebagai **Parquet terpartisi**.
4. Bandingkan waktu eksekusi: versi naif vs versi teroptimasi (broadcast join, partisi tepat, tanpa UDF).

**Definition of Done:**
- [ ] Perbandingan performa sebelum/sesudah optimasi (tabel + penjelasan)
- [ ] Screenshot Spark UI dengan analisis bottleneck
- [ ] Job bisa dijalankan via `spark-submit` / container
- [ ] Penjelasan tertulis: kapan Spark layak dipakai vs cukup DuckDB/Polars

---

## Fase 7 — Streaming dengan Kafka (Minggu 29–31)

**Tujuan:** memahami pemrosesan data real-time dan event-driven.

### Materi

- **Kafka:** topic, partition, producer, consumer, consumer group, offset, retention, replication
- **Delivery semantics:** at-most-once, at-least-once, exactly-once (konsep)
- **Stream processing:** windowing, watermark, late data (Spark Structured Streaming / Faust / Flink — pilih satu)
- **Pola:** CDC (Change Data Capture) dengan **Debezium** (pengenalan), Schema Registry

### 🚀 Project 7 — Real-Time Event Pipeline

1. Buat **producer** yang mensimulasikan event (klik e-commerce / sensor IoT / transaksi).
2. Kirim ke **Kafka** (Docker Compose).
3. Buat **consumer / stream processor** yang menghitung agregasi per jendela waktu (mis. jumlah transaksi per menit).
4. Simpan hasil ke PostgreSQL / warehouse dan tampilkan di dashboard near-real-time.
5. (Bonus) Tambahkan CDC dari PostgreSQL ke Kafka dengan Debezium.

**Definition of Done:**
- [ ] Penanganan late/duplicate event dijelaskan dan diimplementasikan
- [ ] Diagram arsitektur streaming
- [ ] Demo (GIF/video singkat) dashboard yang ter-update real-time
- [ ] Catatan trade-off: kapan streaming benar-benar dibutuhkan vs micro-batch

---

## Fase 8 — Kualitas Data, CI/CD, IaC & Observability (Minggu 32–34)

**Tujuan:** menaikkan level project dari "jalan di laptop" menjadi **siap produksi**.

### Materi

- **Data quality:** dimensi kualitas (akurasi, kelengkapan, konsistensi, ketepatan waktu), Great Expectations / dbt tests / Soda, data contract
- **CI/CD:** GitHub Actions — lint, test, build image, deploy DAG
- **IaC:** Terraform untuk bucket, dataset, IAM, dan resource lain
- **Observability:** logging terstruktur, metrik, alerting, SLA/SLO pipeline, lineage (OpenLineage — pengenalan)
- **Keamanan & tata kelola:** secret management, masking PII, kontrol akses, retensi data

### 🚀 Project 8 — Produksi-kan Pipeline Kamu

Pilih **salah satu project sebelumnya** (disarankan Project 4 atau 5) lalu:

1. Tambahkan **data quality checks** yang menggagalkan pipeline bila data rusak.
2. Buat **CI pipeline** (GitHub Actions): lint → unit test → `dbt build` pada data sampel.
3. Definisikan infrastruktur cloud dengan **Terraform**.
4. Tambahkan monitoring: jumlah baris, freshness, durasi run, dan alert.
5. Tulis **runbook**: apa yang dilakukan jika pipeline gagal.

**Definition of Done:**
- [ ] Badge CI hijau di README
- [ ] `terraform apply` membuat infrastruktur dari nol
- [ ] Runbook insiden minimal 3 skenario kegagalan
- [ ] Data quality report terdokumentasi

---

## Fase 9 — Capstone End-to-End (Minggu 35–40)

**Tujuan:** menggabungkan semua skill menjadi satu **data platform lengkap** — ini adalah "kartu nama" utama kamu saat melamar.

### Spesifikasi Capstone

Bangun platform data untuk satu domain nyata (pilih satu):

| Ide Domain | Sumber Data |
|---|---|
| Analitik harga & pasar kripto/saham | CoinGecko / Yahoo Finance API |
| Monitoring cuaca & kualitas udara Indonesia | BMKG / OpenAQ |
| Analitik lowongan kerja | Scraping/API job board (patuhi ToS) |
| E-commerce (data sintetis realistis) | Generator data + Olist |
| Transportasi publik / ride | NYC Taxi / GTFS |
| UMKM (mis. sistem pencatatan penjualan) | Data transaksi sintetis atau data nyata yang dianonimkan |

### Komponen Wajib

- ✅ **Ingestion** batch **dan** streaming
- ✅ **Data lake** (raw → curated) + **warehouse**
- ✅ **Transformasi** dengan dbt (dan/atau Spark)
- ✅ **Orkestrasi** dengan Airflow
- ✅ **Data quality** & testing otomatis
- ✅ **CI/CD** + **IaC (Terraform)**
- ✅ **Dashboard** BI
- ✅ **Dokumentasi:** diagram arsitektur, ERD, data dictionary, runbook, catatan keputusan (ADR)

### Rencana 6 Minggu

| Minggu | Fokus |
|---|---|
| 35 | Pilih domain, definisikan pertanyaan bisnis, desain arsitektur & skema |
| 36 | Infrastruktur (Terraform) + ingestion batch |
| 37 | Ingestion streaming + data lake |
| 38 | Transformasi (dbt/Spark) + data quality |
| 39 | Orkestrasi, CI/CD, monitoring |
| 40 | Dashboard, dokumentasi, video demo 5–10 menit |

**Definition of Done:**
- [ ] README level "produk": masalah, arsitektur, cara menjalankan, hasil, trade-off
- [ ] Diagram arsitektur profesional
- [ ] Video demo (≤ 10 menit)
- [ ] Bagian "Apa yang saya pelajari & apa yang akan saya perbaiki"
- [ ] Orang lain bisa menjalankan project hanya dengan mengikuti README

---

## Fase 10 — Persiapan Kerja (Minggu 41–44)

**Tujuan:** mengubah skill menjadi **tawaran kerja**.

### 10.1 Portofolio & Branding

- Rapikan **GitHub**: pin 4–5 repo terbaik (Project 1, 4, 6/7, Capstone), README konsisten
- Tulis **2–3 artikel teknis** (Medium / dev.to / blog pribadi), misalnya: "Cara saya mendesain star schema untuk Olist" atau "Belajar dari kesalahan: biaya BigQuery membengkak"
- Perbarui **LinkedIn** dengan kata kunci: *Data Engineer, Airflow, dbt, Spark, BigQuery/AWS, Python, SQL*

### 10.2 CV (format ATS-friendly)

- 1 halaman, fokus pada **dampak terukur**, bukan daftar tool
  - ❌ "Membuat pipeline dengan Airflow"
  - ✅ "Membangun pipeline harian Airflow yang memproses 2 juta baris, memangkas waktu pemrosesan dari 45 menit menjadi 6 menit dengan partisi & incremental load"
- Cantumkan link GitHub, artikel, dan demo capstone

### 10.3 Latihan Interview

| Topik | Latihan |
|---|---|
| **SQL** | LeetCode (SQL 50), StrataScratch, DataLemur — target 100+ soal, fokus window function & CTE |
| **Python** | Soal manipulasi data, struktur data dasar, penulisan fungsi bersih |
| **Data modeling** | Rancang skema untuk kasus (ride-hailing, e-commerce, streaming musik) |
| **System design** | "Rancang pipeline untuk X": jelaskan sumber, ingestion, storage, transformasi, serving, monitoring, trade-off |
| **Konsep** | Idempotency, partitioning, CAP, batch vs streaming, ETL vs ELT, SCD, exactly-once |
| **Behavioral** | Metode STAR: ceritakan pengalaman debug, konflik teknis, belajar cepat |

### 10.4 Strategi Melamar

- Target judul: **Junior/Associate Data Engineer, Analytics Engineer, Data Platform Engineer, BI/ETL Developer** (pintu masuk yang realistis)
- Kirim **20–30 lamaran berkualitas** per bulan dengan CV yang disesuaikan job description
- Manfaatkan: **LinkedIn, Glints, Kalibrr, Jobstreet, komunitas data lokal, referral alumni**
- Ikut **magang / proyek open-source / freelance kecil** bila belum ada pengalaman formal
- Lakukan **mock interview** dengan teman atau mentor setiap minggu

---

## Standar Kualitas Project

Setiap project **harus** memenuhi standar berikut sebelum dianggap selesai:

| Aspek | Standar |
|---|---|
| **Reproducible** | Jalan dengan 1–3 perintah (`docker compose up`, `make run`) |
| **Terdokumentasi** | README: masalah, arsitektur, cara pakai, hasil, trade-off |
| **Teruji** | Ada unit test / data test dan CI |
| **Aman** | Tidak ada secret di repo; `.env.example` disediakan |
| **Idempoten** | Menjalankan ulang tidak merusak/menggandakan data |
| **Terukur** | Ada metrik: jumlah baris, durasi, biaya, performa |
| **Rapi** | Struktur folder jelas, linter lolos, commit message bermakna |

---

## Template Struktur Repo

```
nama-project/
├── README.md                 # Ringkasan, arsitektur, cara menjalankan
├── docs/
│   ├── architecture.png      # Diagram arsitektur
│   ├── erd.png               # ERD / skema
│   ├── decisions/            # ADR: catatan keputusan teknis
│   └── runbook.md            # Panduan saat pipeline gagal
├── infra/                    # Terraform / IaC
├── dags/                     # DAG Airflow
├── src/                      # Kode ekstraksi, transformasi, loading
│   └── nama_project/
├── dbt/                      # Model, test, macro dbt
├── tests/                    # Unit test & integration test
├── data/
│   └── sample/               # Data sampel kecil (JANGAN commit data besar)
├── docker-compose.yml
├── Makefile                  # Shortcut: make up, make test, make lint
├── pyproject.toml / requirements.txt
├── .env.example
├── .gitignore
└── .github/workflows/ci.yml  # GitHub Actions
```

---

## Checklist Kesiapan Kerja

Centang jika kamu bisa melakukannya **tanpa melihat contekan**:

**SQL & Modeling**
- [ ] Menulis query dengan CTE + window function untuk soal analitik
- [ ] Merancang star schema dan menjelaskan grain
- [ ] Menjelaskan SCD Tipe 1 vs 2 dan kapan memakainya
- [ ] Membaca `EXPLAIN` dan mengoptimasi query lambat

**Python & Pipeline**
- [ ] Menulis ETL idempoten dengan retry & logging
- [ ] Menjelaskan full load vs incremental load
- [ ] Menulis unit test untuk fungsi transformasi

**Tooling**
- [ ] Membuat DAG Airflow dengan retry, backfill, dan alert
- [ ] Membangun model dbt incremental lengkap dengan test
- [ ] Menjalankan job PySpark dan membaca Spark UI
- [ ] Membuat producer/consumer Kafka sederhana
- [ ] Membungkus sistem dengan Docker Compose

**Cloud & Produksi**
- [ ] Membuat bucket, IAM, dan dataset dengan Terraform
- [ ] Menyusun CI di GitHub Actions
- [ ] Menjelaskan strategi monitoring & data quality

**Komunikasi**
- [ ] Mempresentasikan capstone dalam 10 menit
- [ ] Menjelaskan trade-off pilihan arsitektur dengan jelas
- [ ] Menjawab "rancang pipeline untuk X" secara terstruktur

---

## Sumber Belajar

> Sumber gratis/terbuka diprioritaskan. Pilih **satu sumber utama per topik** agar tidak tersesat di *tutorial hell*.

| Topik | Sumber |
|---|---|
| **Data Engineering end-to-end** | **DataTalksClub – Data Engineering Zoomcamp** (gratis, berbasis project, sangat sejajar dengan roadmap ini) |
| **SQL** | Mode SQL Tutorial, SQLBolt, PostgreSQL Tutorial, DataLemur, StrataScratch |
| **Data modeling** | *The Data Warehouse Toolkit* (Kimball), blog dbt tentang dimensional modeling |
| **Python** | Dokumentasi resmi Python, *Automate the Boring Stuff*, Real Python |
| **Buku wajib** | *Fundamentals of Data Engineering* (Reis & Housley), *Designing Data-Intensive Applications* (Kleppmann) |
| **Airflow** | Dokumentasi resmi & Astronomer Academy |
| **dbt** | dbt Learn (gratis) |
| **Spark** | *Spark: The Definitive Guide*, dokumentasi PySpark, Databricks Academy (gratis) |
| **Kafka** | Confluent Developer (kursus gratis) |
| **Cloud** | Google Cloud Skills Boost / AWS Skill Builder (free tier) |
| **Dataset** | Kaggle, data.go.id, NYC TLC, GitHub Archive, Open-Meteo, OpenAQ |
| **Komunitas** | DataTalksClub Slack, r/dataengineering, komunitas data Indonesia di LinkedIn/Telegram/Discord |

---

## Tips dari Senior

1. **SQL adalah raja.** Jika harus memilih satu skill untuk didalami, pilih SQL. Hampir semua interview menguji ini.
2. **Pipeline sederhana yang andal > arsitektur canggih yang rapuh.** Jangan pakai Spark/Kafka kalau masalahnya selesai dengan SQL + cron.
3. **Idempotency adalah kebiasaan.** Rancang setiap job agar aman dijalankan ulang.
4. **Selalu hitung biaya.** Kemampuan memperkirakan biaya cloud adalah nilai tambah besar.
5. **Belajar mendokumentasikan.** Data engineer yang baik menulis runbook dan README yang bisa dipahami orang lain.
6. **Jangan mengejar semua tool.** Kedalaman di satu stack lebih berharga daripada permukaan di sepuluh stack.
7. **Pelajari bisnisnya.** Data engineer terbaik memahami *kenapa* data itu dibutuhkan, bukan hanya *bagaimana* memindahkannya.
8. **Konsisten > intens.** 1–2 jam setiap hari mengalahkan maraton akhir pekan yang sporadis.
9. **Bangun di depan publik.** Push kode, tulis artikel, bagikan progres. Rekruter menemukan orang yang terlihat.
10. **Terima kegagalan sebagai bahan belajar.** Pipeline yang rusak adalah guru terbaik.

---

## 🎯 Penutup

Roadmap ini bukan perlombaan. Jika satu fase butuh waktu lebih lama, itu wajar — yang penting setiap fase menghasilkan **project nyata yang bisa dijelaskan dan didemokan**. Saat kamu sudah menyelesaikan Fase 9, kamu bukan lagi "orang yang belajar data engineering", tetapi **orang yang sudah membangun sistem data end-to-end**.

**Selamat membangun, dan semoga cepat dapat offer pertama! 🚀**
