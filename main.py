"""دریافت کتاب‌ها از OpenLibrary و ذخیره‌سازی بهینه در PostgreSQL با FastAPI و SQLAlchemy."""

import sys
import requests
from fastapi import Depends, FastAPI
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine, get_db
from models import Book
from schemas import BookResponse

API_URL = "https://openlibrary.org/search.json"
PARAMS = {
    "q": "python",
    "limit": 50,
    "fields": "key,title,author_name,first_publish_year,publisher,language,number_of_pages_median,isbn",
}
HEADERS = {"User-Agent": "BootcampBookFetcher/1.0"}

app = FastAPI(title="OpenLibrary Books API")


def fetch_and_filter_books() -> list[dict]:
    """دریافت ۵۰ کتاب و فیلتر موارد بعد از سال ۲۰۰۰ با پیچیدگی زمانی O(N)."""
    response = requests.get(API_URL, params=PARAMS, headers=HEADERS, timeout=20)
    response.raise_for_status()
    docs = response.json().get("docs", [])

    filtered = []
    for doc in docs:
        year = doc.get("first_publish_year")
        key = doc.get("key")
        if year and year > 2000 and key:
            pages = doc.get("number_of_pages_median")
            filtered.append({
                "openlibrary_key": key,
                "title": doc.get("title", "Untitled"),
                "authors": ", ".join(doc.get("author_name", [])) if doc.get("author_name") else "Unknown",
                "first_publish_year": year,
                "publisher": ", ".join(doc.get("publisher", [])[:2]) if doc.get("publisher") else None,
                "pages": pages if isinstance(pages, int) and pages > 0 else None,
                "language": ", ".join(doc.get("language", [])[:2]) if doc.get("language") else None,
                "isbn": doc.get("isbn")[0] if doc.get("isbn") else None,
                "openlibrary_url": f"https://openlibrary.org{key}",
            })
    return filtered


def save_books_to_db(db: Session, books_data: list[dict]) -> int:
    """درج دسته‌ای (Bulk Insert) در یک کوئری واحد بدون تکرار داده‌ها."""
    if not books_data:
        return 0

    stmt = (
        pg_insert(Book)
        .values(books_data)
        .on_conflict_do_nothing(index_elements=["openlibrary_key"])
    )
    result = db.execute(stmt)
    db.commit()
    return result.rowcount


@app.post("/books/sync")
def sync_books(db: Session = Depends(get_db)):
    """اندپوینت دریافت کتاب‌ها از OpenLibrary و ذخیره در دیتابیس."""
    Base.metadata.create_all(bind=engine)
    books_data = fetch_and_filter_books()
    inserted_count = save_books_to_db(db, books_data)
    return {
        "filtered_after_2000": len(books_data),
        "newly_inserted": inserted_count,
    }


@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    """اندپوینت مشاهده تمام کتاب‌های ذخیره‌شده به ترتیب سال انتشار."""
    return db.query(Book).order_by(Book.first_publish_year.desc()).all()


def main():
    print("[*] Creating 'books' table in PostgreSQL (if not exists)...")
    Base.metadata.create_all(bind=engine)

    print("[*] Fetching 50 books and filtering (year > 2000)...")
    books_data = fetch_and_filter_books()
    print(f"[+] Filtered {len(books_data)} books published after 2000.")

    with SessionLocal() as db:
        inserted = save_books_to_db(db, books_data)
        total = db.query(Book).count()

    print(f"[+] Newly inserted: {inserted} | Total books in DB: {total}")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"[-] Error: {err}")
        sys.exit(1)
