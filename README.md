# Books to Scrape Web Scraper

Project Python sederhana untuk mengambil data buku dari website edukasi:

https://books.toscrape.com/

Website ini memang dibuat untuk latihan web scraping, sehingga cocok untuk belajar penggunaan `requests`, `BeautifulSoup`, dan `pandas`.

## Fitur Project

- Scrape semua halaman katalog dengan pagination
- Ambil book title
- Ambil price
- Ambil rating
- Ambil stock availability
- Ambil product link
- Export hasil ke `output.csv`
- User-Agent headers
- Error handling sederhana saat request gagal
- Struktur data bersih dan konsisten
- Terminal summary jumlah data yang berhasil discrape

## Struktur Project

```text
.
|-- scraper.py
|-- requirements.txt
|-- README.md
`-- output.csv
```

## Cara Install

Pastikan Python sudah terinstall, lalu jalankan:

```bash
pip install -r requirements.txt
```

## Cara Run

Jalankan scraper dengan command:

```bash
python scraper.py
```

Jika berhasil, data akan tersimpan ke file:

```text
output.csv
```

File CSV diexport dengan `encoding="utf-8-sig"`, `sep=";"`, dan `index=False` agar lebih kompatibel saat dibuka di Microsoft Excel.

Di terminal juga akan muncul summary seperti:

```text
=== Scraping Summary ===
Total data berhasil discrape: 1000
File output: output.csv
```

## Contoh Output CSV

```csv
book_title;price;rating;stock_availability;product_link
A Light in the Attic;GBP 51.77;3;In stock;https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
Tipping the Velvet;GBP 53.74;1;In stock;https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html
```

## Catatan

Gunakan scraper ini untuk edukasi. Saat scraping website lain, selalu cek aturan website tersebut, termasuk `robots.txt` dan Terms of Service. Hindari request terlalu cepat agar tidak membebani server.
