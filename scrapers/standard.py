import json
import logging

from .base import Scraper
from .config import scrape_sites, base_urls

log = logging.getLogger(__name__)


class StandardMedia(Scraper):
    def __init__(self):
        super(StandardMedia, self).__init__()
        self.url = scrape_sites["standard"]
        self.base = Scraper()

    def scrape_page(self):
        """Scrapes stories from standard media.
        Usage::
              use the class object
              pass the site url to\
              get_html_content method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        """

        result_html = self.get_html_content(self.url)
        data = []
        if result_html:
            ul = result_html.find("ul", class_="business-lhs")
            items = ul.find_all("div", class_="col-xs-6")
            for item in items:
                img_src = item.find("img").get("src")
                if img_src:
                    img_url = base_urls["standard"] + img_src
                img_url = "https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png"
                text = item.find("h4").text
                link = item.find("h4").find("a").get("href")
                data.append({
                    'title': text,
                    'link': link,
                    'img': img_url
                })
            print (json.dumps(data, indent=2))
            self.base.s3.put_object(
                Bucket='taxclock.codeforkenya.org',
                ACL='public-read',
                Key='data/standard-news.json',
                Body=json.dumps(data))
            return result_html
        else:
            log.info("The ideal html content could not be retrieved.")
