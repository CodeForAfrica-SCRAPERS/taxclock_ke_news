import unittest
import requests

from ..config import scrap_sites, base_urls


class ConfigTest(unittest.TestCase):

    def test_sites_url(self):
        """Tests whether all the\
        site url's are working."""
        for keys in scrap_sites.keys():
            resp = requests.get(scrap_sites[keys])
        self.assertEqual(resp.status_code, 200)

    def test_base_url(self):
        """Tests whether all the \
        base url's  are working."""
        for keys in base_urls.keys():
            resp = requests.get(base_urls[keys])
        self.assertEqual(resp.status_code, 200)
