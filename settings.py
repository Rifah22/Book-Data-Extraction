BOT_NAME = "bookscraper"
SPIDER_MODULES = ["bookscraper.spiders"]
NEWSPIDER_MODULE = "bookscraper.spiders"

ROBOTSTXT_OBEY = True
USER_AGENT = "BookScraperBot (your-email@example.com)"

CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 1.0
RANDOMIZE_DOWNLOAD_DELAY = True

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

RETRY_ENABLED = True
RETRY_TIMES = 3

ITEM_PIPELINES = {
    "bookscraper.pipelines.BookscraperPipeline": 300,
}

LOG_LEVEL = "INFO"
FEED_EXPORT_ENCODING = "utf-8"
