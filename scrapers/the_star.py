import json
import logging

from .base import Scraper
from .config import scrape_sites, base_urls

log = logging.getLogger(__name__)


class StarMedia(Scraper):

    def __init__(self):
        super(StarMedia, self).__init__()
        self.url = scrape_sites["the_star"]
        self.base = Scraper()

    def scrape_page(self):
        """Scrapes stories from star media.
        Usage::
              create the class object
              using the object call the  url to\
              get_html_content method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
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
            log.info("The html content could not be retrieved.")

    def pagination(self):
        """Gets pages links from the star.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the urls of all pages in the site.
        """

        result_html = self.base.get_html_content(self.url)
        if result_html:
            ul = result_html.find("ul", class_="pager")
            if ul:
                items = ul.find_all("li", class_="pager__item")
                urls = []
                for links in items[1:]:
                    link = base_urls["the_star"] + links.find("a").get("href")
                    urls.append(link)
                    return urls
            else:
                print "Pagination links could not be retrieved."
        else:
            log.info("The html content for the pages could not be retrieved.")
