from scrapers.capital import CapitalMedia
from scrapers.the_star import StarMedia
from scrapers.nation import NationMedia
from scrapers.standard import StandardMedia


'''
Instances of all the classes.
'''

standard = StandardMedia()
capital = CapitalMedia()
star = StarMedia()
nation = NationMedia()

# scraps for the standard media site
standard.scrape_page()

# Scrapes the capitalfm site
capital.scrape_page()

# Scrapes the star site
star.scrape_page()

# Scrapes the nation media site.
nation.scrape_page()
