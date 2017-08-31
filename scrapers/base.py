import boto3
import logging
import requests


from bs4 import BeautifulSoup
from time import gmtime, strftime


from .config import AWS

log = logging.getLogger(__name__)


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
        """Returns the html content,\
            a soup object.
        Usage::
            pass the site url to the method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        """

        try:
            res = requests.get(url)
            html = BeautifulSoup(res.content, 'html.parser')
            return html

        except Exception as err:
            print "Url is not reachable. Error logged on: {}".format(
                strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            log.info(str(err))
