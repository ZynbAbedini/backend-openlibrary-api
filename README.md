# 📚 OpenLibrary Books Fetcher & PostgreSQL API

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![uv](https://img.shields.io/badge/Package_Manager-uv-DE5FE9?style=for-the-badge)

A clean and production-ready backend service that fetches 50 books from the public [OpenLibrary Search API](https://openlibrary.org/dev/docs/api/search), filters works published strictly after year 2000 (`first_publish_year > 2000`), and securely stores them in **PostgreSQL** using **FastAPI** & **SQLAlchemy ORM** with bulk upsert operations.

---

## 🇬🇧 English Guide

### 🚀 Quick Start (using `uv` or `pip`)

1. **Configure Environment Variables:**
   Create a `.env` file based on `.env.example`:
   ```env
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=books_db
   ```
   *(Ensure the database `books_db` is created in pgAdmin / PostgreSQL).*

2. **Install Dependencies:**
   ```bash
   uv pip install -r requirements.txt
   # Or using standard pip:
   # pip install -r requirements.txt
   ```

3. **Run the Application:**
   * **Direct CLI script execution:**
     ```bash
     uv run main.py
     ```
   * **FastAPI Web Server (Swagger UI):**
     ```bash
     uv run uvicorn main:app --reload
     ```
     Access interactive documentation at `http://127.0.0.1:8000/docs`.

### 📊 Database Schema (`books` table)

| Column | Type | Index / Constraints | Description |
| :--- | :--- | :--- | :--- |
| **id** | Integer | Primary Key | Auto-incrementing identifier |
| **openlibrary_key** | String(100) | Unique, Indexed (B-Tree) | Unique key (prevents duplicates) |
| **title** | String(500) | Indexed (B-Tree) | Book title |
| **authors** | String(500) | None | Comma-separated author(s) |
| **first_publish_year** | Integer | Indexed (B-Tree) | First publication year (`> 2000`) |
| **publisher** | String(500) | Nullable | Publisher name |
| **pages** | Integer | Nullable | Median page count |
| **language** | String(100) | Nullable | Language code(s) |
| **isbn** | String(50) | Nullable | International Standard Book Number |
| **openlibrary_url** | String(255) | Nullable | Direct OpenLibrary link |

---

## 🇮🇷 راهنمای فارسی

این پروژه یک وب‌سرویس استاندارد و بهینه است که اطلاعات ۵۰ کتاب را از API عمومی OpenLibrary دریافت کرده، کتاب‌های بعد از سال ۲۰۰۰ را فیلتر نموده و با استفاده از **FastAPI** و **SQLAlchemy ORM** به همراه تکنیک درج دسته‌ای (Bulk Upsert) در پایگاه داده **PostgreSQL** ذخیره می‌نماید.

### 🚀 نحوه راه‌اندازی و اجرا (با `uv` یا `pip`)

۱. **تنظیم اطلاعات دیتابیس در فایل `.env`:**
   یک فایل با نام `.env` مشابه `.env.example` بسازید و رمز دیتابیس خود را قرار دهید:
   ```env
   DB_USER=postgres
   DB_PASSWORD=رمز_پستگرس_شما
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=books_db
   ```
   *(از قبل دیتابیس `books_db` را در pgAdmin بسازید).*

۲. **نصب وابستگی‌ها:**
   ```bash
   uv pip install -r requirements.txt
   # یا با pip معمولی:
   # pip install -r requirements.txt
   ```

۳. **اجرای پروژه:**
   * **اجرای مستقیم اسکریپت:**
     ```bash
     uv run main.py
     ```
   * **اجرای وب‌سرور FastAPI:**
     ```bash
     uv run uvicorn main:app --reload
     ```
     سپس به آدرس `http://127.0.0.1:8000/docs` جهت تست اندپوینت‌های Swagger بروید.

### 📁 ساختار جدول دیتابیس (`books`)

- **id**: شناسه ردیف (کلید اصلی)
- **openlibrary_key**: کلید اختصاصی اثر با ایندکس یکتا (جلوگیری از درج تکراری)
- **title**: عنوان کتاب (ایندکس‌شده جهت جستجوی سریع)
- **authors**: نام نویسنده(گان)
- **first_publish_year**: سال اولین انتشار (ایندکس‌شده جهت مرتب‌سازی و فیلتر بهینه)
- **publisher**: نام ناشر
- **pages**: تعداد صفحات (عدد صحیح `Integer`)
- **language**: زبان
- **isbn**: شابک
- **openlibrary_url**: لینک مستقیم به صفحه کتاب در OpenLibrary
