"""مدل‌های Pydantic جهت اعتبارسنجی داده‌ها طبق استاندارد FastAPI."""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    openlibrary_key: str
    title: str
    authors: str
    first_publish_year: int
    publisher: Optional[str] = None
    pages: Optional[int] = None
    language: Optional[str] = None
    isbn: Optional[str] = None
    openlibrary_url: Optional[str] = None


class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
