import unittest


from taxclock.scrapers.base import Scraper
from taxclock.scrapers.capital import CapitalMedia
from taxclock.scrapers.nation import NationMedia
from taxclock.scrapers.the_star import StarMedia
from taxclock.scrapers.standard import StandardMedia


class BaseTest(unittest.TestCase):

    def setUp(self):
        '''Base class for scraper tests.
        '''

        self.scraper = Scraper()
        self.capital = CapitalMedia()
        self.nation = NationMedia()
        self.the_star = StarMedia()
        self.standard = StandardMedia()

    def tearDown(self):
        '''This destroys all objects\
        after each test is run.
        '''
        del self.scraper
        del self.capital
        del self.nation
        del self.the_star
