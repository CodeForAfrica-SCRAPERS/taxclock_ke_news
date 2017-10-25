import logging

from taxclock.scrapers.capital import CapitalMedia
from taxclock.scrapers.the_star import StarMedia
from taxclock.scrapers.nation import NationMedia
from taxclock.scrapers.standard import StandardMedia
from taxclock.scrapers.base import Scraper


# Set up logging
logging.basicConfig(level=logging.INFO)

'''
Intialize scraper classes
'''
standard = StandardMedia()
capital = CapitalMedia()
star = StarMedia()
nation = NationMedia()


# Scrapers for the media websites.
standard_news = standard.scrape_page()
capital_news = capital.scrape_page()
star_news = star.scrape_page()
nation_news = nation.scrape_page()

try:
    all_news = standard_news + capital_news +\
        star_news + nation_news
    scraper = Scraper()
    scraper.aws_store(all_news)
except Exception as err:
    print(err)
