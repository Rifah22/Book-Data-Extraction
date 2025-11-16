# Book Data Extraction — Web Scraping Intern Assignment

**Candidate:** Rifah Sanzida  
**Email:** rifahsanzida512@gmail.com

## Website URL
https://books.toscrape.com/

## Fields Extracted
- title
- price
- rating
- stock
- product_page
- image_url

## Total Records Collected
Up to 500 book records (configurable via `max_items` parameter).

## Pagination Method
The spider automatically follows the "Next" page link on the website to navigate through multiple pages. It continues scraping until it reaches the maximum number of items specified (`max_items=500`) or there are no more pages left.

## Challenges Faced and Solutions
- **Handling Pagination:** Correctly detecting and following the "Next" page link to scrape all pages.
- **Responsible Scraping:** Added delays between requests to avoid overloading the server and abide by polite scraping practices.
- **Data Cleaning:** Cleaned and formatted fields such as rating and stock availability for consistent output.
- **Encoding Issues:** Handled character encoding to ensure special characters in book titles and other fields are processed correctly.
- **Limiting Scraped Items:** Implemented a parameter to limit the total number of records scraped to control runtime and output size.

## Step-by-Step Instructions to Run the Script

1. Clone or download the repository to your local machine.

2. Create and activate a Python virtual environment:

   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

Run spider:
python -m scrapy crawl books -a max_items=500 -o output.csv

