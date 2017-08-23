from scrapers.config import scrape_sites, base_urls
from scrapers.base import Scraper
from scrapers.capital import CapitalMedia
from scrapers.the_star import StarMedia
from scrapers.nation import NationMedia

scraper = Scraper()
scraper.scrape(scrape_sites["standard"], base_urls["standard"])

capital = CapitalMedia()
capital.scrape_page()

star = StarMedia()
star.scrape_page()

nation = NationMedia()
nation.scrape_page()
