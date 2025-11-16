import scrapy
from urllib.parse import urljoin
from bookscraper.items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def __init__(self, max_items=500, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_items = int(max_items)
        self.collected = 0

    def parse(self, response):
        for book in response.css("article.product_pod"):
            if self.collected >= self.max_items:
                break

            link = book.css("h3 a::attr(href)").get()
            full = urljoin(response.url, link)

            yield scrapy.Request(full, callback=self.parse_book, meta={"product_page": full})

        if self.collected < self.max_items:
            next_page = response.css("li.next a::attr(href)").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        item = BookItem()
        item["product_page"] = response.meta["product_page"]
        item["title"] = response.css("div.product_main h1::text").get()
        item["price"] = response.css("p.price_color::text").get()

        rating = response.css("p.star-rating").attrib.get("class", "")
        item["rating"] = rating.replace("star-rating", "").strip()

        stock = response.css("p.instock.availability::text").getall()
        item["stock"] = "".join(stock).strip()

        img = response.css("div.product_gallery img::attr(src)").get()
        if img:
            item["image_url"] = urljoin(response.url, img)

        self.collected += 1
        yield item
