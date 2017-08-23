import unittest


from .. scrapers.base import Scraper
from .. scrapers.config import scrape_sites, base_urls
from .. scrapers.capital import CapitalMedia
from .. scrapers.nation import NationMedia
from .. scrapers.the_star import StarMedia


class ScraperTest(unittest.TestCase):

    def setUp(self):
        """this method instantiates all objects\
         before each test is run."""

        self.scraper = Scraper()
        self.capital = CapitalMedia()
        self.nation = NationMedia()
        self.the_star = StarMedia()

    def test_get_html_content(self):
        """this method tests that the get\
         html content works well."""
        result_html = self.scraper.get_html_content(
            scrape_sites["standard"])
        data = result_html.find_all('h1')
        self.assertIn('<h1><span>Business News</span></h1>', data)


    def tearDown(self):
        """this destroys all objects\
        after each test is run."""

        del self.scraper
        del self.capital
        del self.nation
        del self.the_star
