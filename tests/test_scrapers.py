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
        self.assertTrue(data)

    def test_nationmedia_scraper(self):
        """this method tests the scraper\
        for nation media."""

        result_html = self.scraper.get_html_content(
            scrape_sites["nation"])
        items = result_html.find_all(
            "div", class_="story-teaser medium-teaser")
        self.assertTrue(items)

    def test_standardmedia_scraper(self):
        """this method tests the scraper\
        for standard media."""

        result_html = self.scraper.get_html_content(
            scrape_sites["standard"])
        ul = result_html.find("ul", class_="business-lhs")
        items = ul.find_all("div", class_="col-xs-6")
        self.assertTrue(items)

    def test_the_star_scraper(self):
        """this method tests the scraper\
        for the star."""

        result_html = self.scraper.get_html_content(
            scrape_sites["the_star"])
        items = result_html.find_all(
            "div", class_="field field-name-field-converge-image")
        self.assertTrue(items)

    def test_capitalfm(self):
        """this method tests the scraper\
        for capitalfm."""

        result_html = self.scraper.get_html_content(
            scrape_sites["capital"])
        items = result_html.find_all("div", class_="article-wrapper")
        self.assertTrue(items)

    def tearDown(self):
        """this destroys all objects\
        after each test is run."""

        del self.scraper
        del self.capital
        del self.nation
        del self.the_star
