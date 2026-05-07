import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup


# Base URL website latihan scraping.
BASE_URL = "https://books.toscrape.com/"
START_URL = urljoin(BASE_URL, "catalogue/page-1.html")
OUTPUT_FILE = "output.csv"
CSV_SEPARATOR = ";"

# Delay kecil agar request tidak terlalu cepat.
REQUEST_DELAY = 0.1

# Kolom dibuat konstan agar struktur CSV selalu rapi.
CSV_COLUMNS = [
    "book_title",
    "price",
    "rating",
    "stock_availability",
    "product_link",
]


def get_headers():
    """Membuat headers request sederhana seperti browser."""
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
    }


def get_page_html(url):
    """Mengambil HTML dari URL dengan error handling sederhana."""
    try:
        response = requests.get(url, headers=get_headers(), timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"[ERROR] Gagal mengambil halaman {url}: {error}")
        return None


def clean_text(text):
    """Membersihkan spasi berlebih agar data lebih rapi."""
    if not text:
        return "N/A"

    return " ".join(text.split())


def convert_rating(class_list):
    """Mengubah rating dari class CSS menjadi angka."""
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    for class_name in class_list:
        if class_name in rating_map:
            return rating_map[class_name]

    return "N/A"


def parse_book_cards(html, page_url):
    """Mengambil data dasar buku dari satu halaman katalog."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    # Setiap buku pada halaman katalog ada di dalam article.product_pod.
    for card in soup.select("article.product_pod"):
        title_element = card.select_one("h3 a")
        price_element = card.select_one(".price_color")
        rating_element = card.select_one(".star-rating")
        stock_element = card.select_one(".availability")

        title = title_element.get("title", "N/A") if title_element else "N/A"
        price = clean_text(price_element.get_text()) if price_element else "N/A"
        rating = convert_rating(rating_element.get("class", [])) if rating_element else "N/A"
        stock_availability = clean_text(stock_element.get_text()) if stock_element else "N/A"

        relative_link = title_element.get("href", "") if title_element else ""
        product_link = urljoin(page_url, relative_link)

        books.append(
            {
                "book_title": title,
                "price": price,
                "rating": rating,
                "stock_availability": stock_availability,
                "product_link": product_link,
            }
        )

    return books


def get_next_page_url(html, current_url):
    """Mencari link pagination berikutnya dari halaman katalog."""
    soup = BeautifulSoup(html, "html.parser")
    next_element = soup.select_one("li.next a")

    if next_element is None:
        return None

    return urljoin(current_url, next_element.get("href"))


def scrape_all_books(start_url):
    """Scrape semua halaman katalog sampai pagination habis."""
    all_books = []
    current_url = start_url
    page_number = 1

    while current_url:
        print(f"Scraping page {page_number}: {current_url}")
        html = get_page_html(current_url)

        if html is None:
            print("[WARNING] Halaman dilewati karena gagal diambil.")
            break

        books = parse_book_cards(html, current_url)

        all_books.extend(books)

        print(f"  -> {len(books)} buku ditemukan di halaman ini.")

        current_url = get_next_page_url(html, current_url)
        page_number += 1
        time.sleep(REQUEST_DELAY)

    return all_books


def save_to_csv(books, filename):
    """Menyimpan hasil scraping ke file CSV."""
    dataframe = pd.DataFrame(books, columns=CSV_COLUMNS)
    dataframe.to_csv(
        filename,
        sep=CSV_SEPARATOR,
        index=False,
        encoding="utf-8-sig",
    )


def print_summary(books):
    """Menampilkan ringkasan hasil scraping di terminal."""
    print("\n=== Scraping Summary ===")
    print(f"Total data berhasil discrape: {len(books)}")
    print(f"File output: {OUTPUT_FILE}")

    if books:
        print("Contoh data pertama:")
        print(f"- Title: {books[0]['book_title']}")
        print(f"- Price: {books[0]['price']}")
        print(f"- Rating: {books[0]['rating']}")
        print(f"- Stock: {books[0]['stock_availability']}")


def main():
    """Fungsi utama untuk menjalankan scraper."""
    print("Mulai scraping Books to Scrape...")

    books = scrape_all_books(START_URL)
    save_to_csv(books, OUTPUT_FILE)
    print_summary(books)


if __name__ == "__main__":
    main()
