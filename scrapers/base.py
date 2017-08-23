import boto3
import json
import logging
import os
import requests


from bs4 import BeautifulSoup
from time import gmtime, strftime


from .config import AWS

class Scraper(object):
    """
    This is a base class inherited by other scraper classes.
    """
    def __init__(self):
        self.url = None
        self.s3 = boto3.client("s3", **{
            "aws_access_key_id": AWS["aws_access_key_id"],
            "aws_secret_access_key": AWS["aws_secret_access_key"],
            "region_name": AWS["region_name"]
        })

    def get_html_content(self, url):
        """This method returns the entire\
         html content of a page."""

        try:
            res = requests.get(url)
            html = BeautifulSoup(res.content, 'html.parser')
            return html

        except Exception as err:
            print "Url is not reachable. Error logged on: {}".format(
                strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            logging.exception(str(err))

    def scrape(self, url, base_url):
        """This method is used as a sraper for 
        the website url's that are passed to it.In 
        this case the standard media urls'.
        """
        result_html = self.get_html_content(url)
        data = []
        if result_html:
            ul = result_html.find("ul", class_="business-lhs")
            items = ul.find_all("div", class_="col-xs-6")
            for item in items:
                img_src = item.find("img").get("src")
                img_url = base_url + img_src
                if not img_url:
                    img_url = "https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png"
                text = item.find("h4").text
                link = item.find("h4").find("a").get("href")
                data.append({
                    'title': text,
                    'link': link,
                    'img': img_url
                })
            print (json.dumps(data, indent=2))
            self.s3.put_object(
                Bucket='taxclock.codeforkenya.org',
                ACL='public-read',
                Key='data/standard-news.json',
                Body=json.dumps(data))
            return result_html
        else:
            print "The ideal html content could not be retrieved."
