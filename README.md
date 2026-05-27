# 📚 Book Data Extraction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scrapy-60A839?style=for-the-badge&logo=scrapy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Web_Scraping-FF6F00?style=for-the-badge&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white"/>
</p>

> A Scrapy-based web scraper that extracts book data from [books.toscrape.com](https://books.toscrape.com) — collecting titles, prices, ratings, stock status, product URLs, and image URLs across all paginated pages, with output saved to CSV.

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Output](#-output)
- [Configuration](#-configuration)
- [Author](#-author)

---

## 📖 About the Project

**Book Data Extraction** is a web scraping intern assignment that targets [books.toscrape.com](https://books.toscrape.com) — a sandbox site built for scraping practice. The spider crawls through the paginated book catalogue, visits each book's detail page, and collects structured data which is exported to a CSV file.

The scraper is built with **Scrapy** and follows polite scraping practices: it respects `robots.txt`, uses configurable request delays, randomises delay intervals, and includes auto-throttling and retry logic.

---

## ✨ Features

- Crawls all paginated pages automatically by following the "Next" link
- Visits each book's detail page to extract full data
- Configurable item limit via `max_items` parameter (default: 500)
- Cleans extracted fields (strips whitespace from title, price, stock)
- Polite scraping: respects `robots.txt`, delays, auto-throttling, retries
- Exports data directly to CSV with UTF-8 encoding

---

## 🛠️ Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Language      | Python 3.12        |
| Scraping      | Scrapy ≥ 2.6       |
| Output Format | CSV                |
| Target Site   | books.toscrape.com |

---

## 📁 Project Structure

```
Book-Data-Extraction-main/
│
├── books_spider.py       # Main spider — crawls pages and extracts book data
├── items.py              # BookItem definition (scrapy.Item)
├── pipelines.py          # Data cleaning pipeline (strips whitespace)
├── settings.py           # Scrapy settings (throttle, delays, retries, pipeline)
├── scrapy.cfg            # Scrapy project config
├── __init__.py           # Package init
├── requirements.txt      # Python dependencies (Scrapy>=2.6)
├── output.csv            # Scraped data — 1,000 book records
└── pyvenv.cfg            # Virtual environment config (Python 3.12)
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rifah22/Book-Data-Extraction.git
   cd Book-Data-Extraction
   ```

2. **Create and activate a virtual environment**

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the spider and export to CSV:

```bash
python -m scrapy crawl books -a max_items=500 -o output.csv
```

To collect more or fewer records, change `max_items`:

```bash
# Scrape up to 100 books
python -m scrapy crawl books -a max_items=100 -o output.csv

# Scrape up to 1000 books (full catalogue)
python -m scrapy crawl books -a max_items=1000 -o output.csv
```

> ⚠️ If `output.csv` already exists, Scrapy will **append** to it rather than overwrite. Delete the file first if you want a fresh run.

---

## 📊 Output

The scraper produces a CSV file with the following fields:

| Field          | Description                                      | Example |
|----------------|--------------------------------------------------|---------|
| `title`        | Book title                                       | `Sapiens: A Brief History of Humankind` |
| `price`        | Price in GBP (£)                                 | `£54.23` |
| `rating`       | Star rating as a word                            | `Five` |
| `stock`        | Availability status                              | `In stock (20 available)` |
| `product_page` | Full URL to the book's detail page               | `https://books.toscrape.com/catalogue/...` |
| `image_url`    | URL to the book cover image                      | `https://books.toscrape.com/media/...` |

The included `output.csv` contains **1,000 scraped book records**.

---

## 🔧 Configuration

Key settings in `settings.py`:

| Setting | Value | Description |
|---------|-------|-------------|
| `ROBOTSTXT_OBEY` | `True` | Respects the site's robots.txt |
| `CONCURRENT_REQUESTS` | `8` | Max parallel requests |
| `DOWNLOAD_DELAY` | `1.0` | Seconds between requests |
| `RANDOMIZE_DOWNLOAD_DELAY` | `True` | Randomises delay (0.5×–1.5× of base) |
| `AUTOTHROTTLE_ENABLED` | `True` | Auto-adjusts speed based on server load |
| `AUTOTHROTTLE_MAX_DELAY` | `10` | Max seconds the throttle can impose |
| `RETRY_TIMES` | `3` | Retries failed requests up to 3 times |
| `LOG_LEVEL` | `INFO` | Console log verbosity |

---

## 👩‍💻 Author

**Rifah Sanzida**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rifah-sanzida-b58141290/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Rifah22)

---

## 📄 License

This project is open source and available for educational purposes.
