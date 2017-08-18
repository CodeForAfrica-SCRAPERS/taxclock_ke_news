from scrapers.config import scrap_sites, base_urls

from scrapers.base import Scraper


scraper = Scraper()
scraper.scrape(scrap_sites["standard"], base_urls["standard"])

