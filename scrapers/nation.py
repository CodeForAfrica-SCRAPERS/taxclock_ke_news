import json
import logging

from .base import Scraper
from .config import scrape_sites, base_urls

log = logging.getLogger(__name__)


class NationMedia(Scraper):
    def __init__(self):
        super(NationMedia, self).__init__()
        self.url = scrape_sites["nation"]
        self.base = Scraper()

    def scrape_page(self):
        """this method scrapes data from\
        http://www.nation.co.ke/business/corporates/\
        1954162-1954162-u0riql/index.html"""

        result_html = self.base.get_html_content(self.url)
        if result_html:
            data = []
            items = result_html.find_all(
                "div", class_="story-teaser medium-teaser")
            for item in items:
                img_src = item.find("img").get("src")
                if img_src:
                    img_url = base_urls["nation"] + img_src
                img_url = "https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png"
                link = base_urls["nation"] + item.find("a").get("href")
                text = item.find("img").get("alt")
                data.append({
                    'link': link,
                    'img': img_url,
                    'title': text
                })
            print (json.dumps(data, indent=2))
            self.base.s3.put_object(
                Bucket='taxclock.codeforkenya.org',
                ACL='public-read',
                Key='data/standard-news.json',
                Body=json.dumps(data)
            )
            return result_html
        else:
            log.info("The ideal html content could not be retrieved.")
