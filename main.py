"""اسکریپت دریافت، فیلتر و ذخیره‌سازی اطلاعات کتاب‌ها از OpenLibrary API."""

import csv
import sys
import requests


API_URL = "https://openlibrary.org/search.json"
PARAMS = {
    "q": "python",  
    "limit": 50,    
    "fields": "title,author_name,first_publish_year,publisher,language,number_of_pages_median,isbn,key",
}
HEADERS = {
    "User-Agent": "BootcampBookFetcher/1.0"
}


def fetch_books() -> list[dict]:
    
    try:
        print("[*] Fetching 50 books from OpenLibrary API...")
        response = requests.get(API_URL, params=PARAMS, headers=HEADERS, timeout=20)
        response.raise_for_status() 
        books = response.json().get("docs", [])
        print(f"[+] Successfully fetched {len(books)} books from API.")
        return books
    except requests.RequestException as error:
        print(f"[-] API request failed: {error}")
        sys.exit(1)


def filter_books_after_2000(books: list[dict]) -> list[dict]:
    
    filtered = []
    for book in books:
        year = book.get("first_publish_year")

        if year and year > 2000:

            authors = ", ".join(book.get("author_name", [])) if book.get("author_name") else "Unknown"
            publishers = ", ".join(book.get("publisher", [])[:2]) if book.get("publisher") else "N/A"
            languages = ", ".join(book.get("language", [])[:2]) if book.get("language") else "N/A"
            isbn = book.get("isbn")[0] if book.get("isbn") else "N/A"
            pages = book.get("number_of_pages_median") or "N/A"
            key = book.get("key", "")
            url = f"https://openlibrary.org{key}" if key else "N/A"

            filtered.append({
                "Title": book.get("title", "Untitled"),
                "Authors": authors,
                "First Publish Year": year,
                "Publisher": publishers,
                "Pages": pages,
                "Language": languages,
                "ISBN": isbn,
                "OpenLibrary URL": url,
            })

    print(f"[+] Filtered {len(filtered)} books published after year 2000.")
    return filtered


def save_to_csv(books: list[dict], filename: str = "books.csv") -> None:
    if not books:
        print("[-] No books to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(books[0].keys()))
        writer.writeheader()
        writer.writerows(books)

    print(f"[+] Successfully saved {len(books)} books to '{filename}'.")


def main():
    print("=" * 60)
    print("OpenLibrary Books Fetcher & Filter")
    print("=" * 60)

    raw_books = fetch_books()

    filtered_books = filter_books_after_2000(raw_books)

    save_to_csv(filtered_books, "books.csv")

    print("=" * 60)
    print("[+] Process completed successfully.")


if __name__ == "__main__":
    main()
