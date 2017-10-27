import unittest
import requests

from taxclock.settings import scrape_sites, base_urls


class ConfigTest(unittest.TestCase):

    def test_sites_url(self):
        '''Tests whether all the\
        site url's are working.'''

        for keys in scrape_sites.keys():
            resp = requests.get(scrape_sites[keys])
        self.assertEqual(resp.status_code, 200)

    def test_base_url(self):
        '''Tests whether all the \
        base url's  are working.'''

        for keys in base_urls.keys():
            resp = requests.get(base_urls[keys])
        self.assertEqual(resp.status_code, 200)