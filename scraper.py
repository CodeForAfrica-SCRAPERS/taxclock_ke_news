import logging

#from taxclock.settings import LOG_FILE

from taxclock.scrapers.capital import CapitalMedia
from taxclock.scrapers.the_star import StarMedia
from taxclock.scrapers.nation import NationMedia
from taxclock.scrapers.standard import StandardMedia


# Set up logging
logging.basicConfig(level=logging.INFO)


'''
Intialize scraper classes
'''
standard = StandardMedia()
capital = CapitalMedia()
star = StarMedia()
nation = NationMedia()


'''
Run the scrapers
'''
nation.scrape_page()
standard.scrape_page()
capital.scrape_page()
star.scrape_page()
