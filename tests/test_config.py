import unittest
import requests

from ..config import scrap_sites, base_urls

class ConfigTest(unittest.TestCase):

    def test_sites_url(self):
        """Tests whether all the site url's are working."""

        resp = requests.get(scrap_sites["standard"])
        self.assertEqual(resp.status_code, 200)
        
       
        resp1 = requests.get(scrap_sites["nation"])
        self.assertEqual(resp1.status_code, 200)

        resp2 = requests.get(scrap_sites["the_star"])
        self.assertEqual(resp2.status_code, 200)

        resp3 = requests.get(scrap_sites["capital"])
        self.assertEqual(resp3.status_code, 200)

    def test_base_url(self):
        """Tests whether all the base url's  are working."""

        resp =  requests.get(base_urls["standard"])
        self.assertEqual(resp.status_code, 200)

        resp1 = requests.get(base_urls["nation"])
        self.assertEqual(resp1.status_code, 200)

        resp2 = requests.get(base_urls["the_star"])
        self.assertEqual(resp2.status_code, 200)

        resp3 = requests.get(base_urls["capital"])
        self.assertEqual(resp3.status_code, 200)
            
