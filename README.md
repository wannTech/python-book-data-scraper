# Books Catalog Data Scraper

Python web scraper that extracts structured catalog data from a multi-page e-commerce style website using BeautifulSoup, requests, and pandas.

The scraper automatically collects:
- book title
- price
- rating
- stock availability
- product URL

and exports the data into a clean structured CSV dataset.

## Features

- Multi-page pagination scraping
- Structured product data extraction
- Automatic CSV export
- User-Agent headers
- Error handling for failed requests
- Clean and consistent dataset formatting
- Terminal scraping summary

## Tech Stack

- Python
- requests
- BeautifulSoup4
- pandas

## Project Structure

```text
.
|-- scraper.py
|-- requirements.txt
|-- README.md
`-- output.csv

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
