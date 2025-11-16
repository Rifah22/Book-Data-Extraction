class BookscraperPipeline:
    def process_item(self, item, spider):
        if item.get("title"):
            item["title"] = item["title"].strip()
        if item.get("price"):
            item["price"] = item["price"].strip()
        if item.get("stock"):
            item["stock"] = item["stock"].strip()
        return item
