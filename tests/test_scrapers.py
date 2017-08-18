import unittest
from .. scrapers.base import Scraper
from .. scrapers.config import scrap_sites, base_urls

class ScraperTest(object):

	def setUp(self):
		"""this method instantiates all objects before each test is run."""
		self.scraper = Scraper()
		

	def test_get_html_content(self):
		"""this method tests that the get html content works well."""
		

	def tearDown(self):
		"""this destroys all objects after each test is run."""
		pass	