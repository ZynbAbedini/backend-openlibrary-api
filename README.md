# 📚 OpenLibrary Books Fetcher & Filter

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.31+-005571?style=for-the-badge)
![API](https://img.shields.io/badge/API-OpenLibrary-02735E?style=for-the-badge)
![Output](https://img.shields.io/badge/Output-CSV-E36209?style=for-the-badge)

A clean and lightweight Python script that queries the public [OpenLibrary Search API](https://openlibrary.org/dev/docs/api/search) for 50 books, filters those published strictly after the year 2000 (`first_publish_year > 2000`), and exports the curated dataset into an organized CSV file.

---

## 🇬🇧 English Guide

### 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

3. **(Optional) Run unit tests:**
   ```bash
   python -m unittest test_main.py -v
   ```

### 📊 Output Schema (`books.csv`)

The exported `books.csv` file uses UTF-8 BOM encoding (`utf-8-sig`) for Excel compatibility and contains the following columns:

| Column | Description | Example |
| :--- | :--- | :--- |
| **Title** | Name of the book | *Fluent Python* |
| **Authors** | Author(s) of the book | *Luciano Ramalho* |
| **First Publish Year** | Year of first publication (`> 2000`) | *2015* |
| **Publisher** | Publisher name | *O'Reilly* |
| **Pages** | Page count | *821* |
| **Language** | Language code | *eng* |
| **ISBN** | Standard Book Number | *9781491957660* |
| **OpenLibrary URL** | Direct link to the work | `https://openlibrary.org/works/...` |

---

## 🇮🇷 راهنمای فارسی

این پروژه یک اسکریپت ساده و استاندارد پایتون است که اطلاعات ۵۰ کتاب را از API عمومی OpenLibrary دریافت کرده، کتاب‌های منتشر شده بعد از سال ۲۰۰۰ را فیلتر می‌کند و در نهایت در فایل مرتب `books.csv` ذخیره می‌نماید.

### 🚀 نحوه اجرا

۱. **نصب وابستگی‌ها:**
   ```bash
   pip install -r requirements.txt
   ```

۲. **اجرای اسکریپت:**
   ```bash
   python main.py
   ```

۳. **اجرای تست‌های واحد (اختیاری):**
   ```bash
   python -m unittest test_main.py -v
   ```

### 📁 ستون‌های فایل خروجی (`books.csv`)

فایل خروجی با فرمت استاندارد `utf-8-sig` (جهت باز شدن صحیح در مایکروسافت اکسل) ذخیره می‌شود و شامل ستون‌های زیر است:
- **Title**: عنوان کتاب
- **Authors**: نویسنده(گان)
- **First Publish Year**: سال اولین انتشار (فقط بعد از سال ۲۰۰۰)
- **Publisher**: ناشر
- **Pages**: تعداد صفحات
- **Language**: زبان
- **ISBN**: شابک
- **OpenLibrary URL**: لینک مستقیم به صفحه کتاب در سایت OpenLibrary
