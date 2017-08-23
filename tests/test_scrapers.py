import unittest
from .. scrapers.base import Scraper
from .. scrapers.config import scrape_sites, base_urls
from .. scrapers.capital import CapitalMedia
from .. scrapers.nation import NationMedia
from .. scrapers.the_star import StarMedia


class ScraperTest(object):

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
        self.assertContains(self.scraper.test_get_html_content(
            scrape_sites["standard"]), "business-lhs")

    def test_scrapers(self):
        """this method tests the site scrapers."""
        self.assertContains(self.capital.scrape_page(),
                            "article-wrapper")
        self.assertContains(self.nation.scrape_page(),
                            "story-teaser tiny-teaser")
        self.assertContains(self.the_star.scrape_page(),
                            "field field-name-field-converge-image")

    def tearDown(self):
        """this destroys all objects\
        after each test is run."""
        del self.scraper
        del self.capital
        del self.nation
        del self.the_star
