import unittest

from .. scrapers.base import Scraper
from .. scrapers.config import scrape_sites
from .. scrapers.capital import CapitalMedia
from .. scrapers.nation import NationMedia
from .. scrapers.the_star import StarMedia


class ScraperTest(unittest.TestCase):

    def setUp(self):
        """This method instantiates all objects\
         before each test is run."""

        self.scraper = Scraper()
        self.capital = CapitalMedia()
        self.nation = NationMedia()
        self.the_star = StarMedia()

    def test_get_html_content(self):
        """Gets the content of webpage.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the page html content      
        """

        result_html = self.scraper.get_html_content(
            scrape_sites["standard"])
        data = result_html.find_all('h1')
        self.assertTrue(data)

    def test_nationmedia_scraper(self):
        """Tests the scraper for nation media.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        """

        result_html = self.scraper.get_html_content(
            scrape_sites["nation"])
        items = result_html.find_all(
            "div", class_="story-teaser medium-teaser")
        self.assertTrue(items)

    def test_standardmedia_scraper(self):
        """Tests the scraper for standard media.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        """

        result_html = self.scraper.get_html_content(
            scrape_sites["standard"])
        ul = result_html.find("ul", class_="business-lhs")
        items = ul.find_all("div", class_="col-xs-6")
        self.assertTrue(items)

    def test_the_star_scraper(self):
        """Tests the scraper for the star.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        """

        result_html = self.scraper.get_html_content(
            scrape_sites["the_star"])
        items = result_html.find_all(
            "div", class_="field field-name-field-converge-image")
        self.assertTrue(items)

    def test_capitalfm(self):
        """Tests the scraper for capitalfm.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title."""

        result_html = self.scraper.get_html_content(
            scrape_sites["capital"])
        items = result_html.find_all("div", class_="article-wrapper")
        self.assertTrue(items)

    def test_pagination(self):
        """Tests the pagination links.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the urls of all pages in the site."""
        urls = self.the_star.pagination()
        self.assertTrue(urls)

    def tearDown(self):
        """This destroys all objects\
        after each test is run."""

        del self.scraper
        del self.capital
        del self.nation
        del self.the_star
