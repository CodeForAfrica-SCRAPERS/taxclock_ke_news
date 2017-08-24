import json

from .base import Scraper
from .config import scrape_sites, base_urls


class StarMedia(Scraper):

    def __init__(self):
        super(StarMedia, self).__init__()
        self.url = scrape_sites["the_star"]
        self.base = Scraper()

    def scrape_page(self):
        """this method scrapes data from\
        http://www.the-star.co.ke/sections/business_c29663
        """
        urls = []
        if self.pagination():
            urls = self.pagination()
            for url in urls:
                result_html = self.base.get_html_content(url)
            result_html
        else:
            result_html = self.base.get_html_content(self.url)
        if result_html:
            data = []
            items = result_html.find_all(
                "div", class_="field field-name-field-converge-image")
            for item in items:
                img_url = item.find("img").get("src")
                if not img_url:
                    img_url = "https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png"
                text = item.find("img").get("title")
                link = base_urls["the_star"] + item.find("a").get("href")
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
            print "The ideal html content could not be retrieved."

    def pagination(self):
        """this method gets the urls for the pages\
         in the star website. It returns the urls\
          for the pages"""

        result_html = self.base.get_html_content(self.url)
        if result_html:
            ul = result_html.find("ul", class_="pager")
            items = ul.find_all("li", class_="pager__item")
            urls = []
            for links in items[1:]:
                link = base_urls["the_star"] + links.find("a").get("href")
                urls.append(link)
            return urls
