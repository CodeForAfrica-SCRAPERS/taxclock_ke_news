from taxclock.scrapers.capital import CapitalMedia
from taxclock.scrapers.the_star import StarMedia
from taxclock.scrapers.nation import NationMedia
from taxclock.scrapers.standard import StandardMedia

import json
'''
Instances of all the classes.
'''

standard = StandardMedia()
capital = CapitalMedia()
star = StarMedia()
nation = NationMedia()


# Scrapes the nation media site.
nation.scrape_page()
# scraps for the standard media site
standard.scrape_page()

# Scrapes the capitalfm site
capital.scrape_page()

# Scrapes the star site
star.scrape_page()
