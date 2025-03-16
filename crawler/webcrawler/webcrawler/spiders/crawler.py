
import scrapy
from scrapy.linkextractors import LinkExtractor

class LinkSpider(scrapy.Spider):
    name = 'linkspider'
    start_urls = [
            ''
    ]

    custom_settings = {
        'USER_AGENT': 'linkspider (+',
        'COOKIES_ENABLED': True,
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
    }

    def __init__(self, *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        self.visited_urls = set()
        self.allowed_domains = ['']
        self.unique_links = set()

    def parse(self, response):
        links = LinkExtractor(allow_domains=self.allowed_domains).extract_links(response)

        for link in links:
            if link.url not in self.visited_urls:
                self.visited_urls.add(link.url)
                if link.url not in self.unique_links:
                    self.unique_links.add(link.url)
                    yield scrapy.Request(link.url, callback=self.parse)

        if self.unique_links:
            with open('links.py', 'w') as f:
                f.write('unique_links = [\n')
                for link in self.unique_links:
                    f.write(f'    "{link}",\n')
                f.write(']\n')
            self.log(f'Saved {len(self.unique_links)} unique links to links.py')
            self.unique_links.clear()