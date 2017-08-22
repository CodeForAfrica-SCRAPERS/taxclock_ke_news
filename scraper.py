from scrapers.config import scrap_sites, base_urls
from scrapers.base import Scraper
from scrapers.capital import CapitalMedia
from scrapers.the_star import StarMedia
# from scrapers.nation import NationMedia

scraper = Scraper()
scraper.scrape(scrap_sites["standard"], base_urls["standard"])

capital = CapitalMedia()
capital.scrap_page()

star = StarMedia()
star.scrap_page()

# nation = NationMedia()
# nation.scrap_page()