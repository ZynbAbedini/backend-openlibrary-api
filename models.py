from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    # کلید یکتا برای جلوگیری از درج تکراری در زمان O(1)
    openlibrary_key = Column(String(100), unique=True, nullable=False, index=True)
    title = Column(String(500), nullable=False, index=True)
    authors = Column(String(500), nullable=False)
    # ایندکس روی سال انتشار برای جستجو و فیلتر سریع
    first_publish_year = Column(Integer, nullable=False, index=True)
    publisher = Column(String(500), nullable=True)
    pages = Column(Integer, nullable=True)
    language = Column(String(100), nullable=True)
    isbn = Column(String(50), nullable=True)
    openlibrary_url = Column(String(255), nullable=True)
