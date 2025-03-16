# Crawler-and-Scrapper
# Web Scraper and Crawler

## Overview
This repository contains a web scraper and a crawler designed to extract and process web content from any desired URL. The scraper fetches and transforms web pages into structured text data, while the crawler systematically explores links on the website.

## Features
- **Web Scraper:** Uses `AsyncChromiumLoader` from LangChain to load web pages and `Html2TextTransformer` to extract readable text.
- **Web Crawler:** Built with Scrapy, it follows links on the provided URL and stores unique links.
- **Data Storage:** Extracted data is saved in json file.
- **Respects Robots.txt:** The crawler follows ethical scraping practices.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Scraper
```bash
python scrapper.py
```

### Running the Web Crawler
First, navigate to the `scrapper/crawler/webcrawler/webcrawler/spiders` directory:
```bash
cd crapper/crawler/webcrawler/webcrawler/spiders
```
Then, run the crawler using the following command:
```bash
scrapy crawl linkspider
```

## Files
- `scrapper.py`: Extracts and processes content from specified URLs.
- `crawler.py`: Crawls links from the given URL and saves unique URLs.


