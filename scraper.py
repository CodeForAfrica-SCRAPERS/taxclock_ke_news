from scrapers.config import scrape_sites, base_urls
from scrapers.base import Scraper
from scrapers.capital import CapitalMedia
from scrapers.the_star import StarMedia
from scrapers.nation import NationMedia

'''
 This file contains the instances\
  of the scraper classes
 It's the entry point\
 to all scraping.
'''

'''
Instances of all the classes.
'''

scraper = Scraper()
capital = CapitalMedia()
star = StarMedia()
nation = NationMedia()

# scraps for the standard media site
scraper.scrape(scrape_sites["standard"], base_urls["standard"])

# Scrapes the capitalfm site
capital.scrape_page()

# Scrapes the star site
star.scrape_page()

# Scrapes the nation media site.
nation.scrape_page()
