from taxclock.scrapers.capital import CapitalMedia
from taxclock.scrapers.the_star import StarMedia
from taxclock.scrapers.nation import NationMedia
from taxclock.scrapers.standard import StandardMedia
from taxclock.scrapers.base import Scraper


'''
Instances of all the classes.
'''

standard = StandardMedia()
capital = CapitalMedia()
star = StarMedia()
nation = NationMedia()


# Scrapers for the media websites.
nation_news = nation.scrape_page()
standard_news = standard.scrape_page()
capital_news = capital.scrape_page()
star_news = star.scrape_page()

try:
    all_news = nation_news + standard_news +\
        capital_news + star_news
    scraper = Scraper()
    scraper.aws_store(all_news[:7])    
except Exception as err:
	print(err)
