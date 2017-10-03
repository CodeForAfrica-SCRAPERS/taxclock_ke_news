import os
import boto3
import logging
import requests
import json

from bs4 import BeautifulSoup
from taxclock.config import AWS, log_file

logging.basicConfig(filename=log_file['log_file'], level=logging.INFO)
log = logging.getLogger(__name__)


class Scraper(object):
    '''
    This is a base class inherited by other scraper classes.
    '''

    def __init__(self):
        self.url = None
        self.s3 = boto3.client('s3', **{
            'aws_access_key_id': AWS['aws_access_key_id'],
            'aws_secret_access_key': AWS['aws_secret_access_key'],
            'region_name': AWS['region_name']
        })

    def get_html_content(self, url):
        '''Returns a soup object.
        Usage::
            pass the site url to the method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''

        try:
            res = requests.get(url)
            html = BeautifulSoup(res.content, 'html.parser')
            return html

        except Exception as err:
            log.error(str(err))

    def local_store(self, data, site_name):
        '''Writes content from the website to file.
        Usage::
             file name to write data
        :param_train_data: the filename
        :rtype: outputs data to a file.
        '''
        with open(os.path.dirname(__file__) + '/data/' +
                  site_name + '.json', 'w') as output_file:
            json.dump(data, output_file, indent=2)

    def aws_store(self, data, site_name):
        '''Writes the data to AWS.
        Usage::
            writes data to aws.

        '''
        try:
            self.s3.put_object(
                Bucket='taxclock.codeforkenya.org',
                ACL='public-read',
                Key='data/' + site_name + '.json',
                Body=json.dumps(data))
        except Exception as err:
            self.local_store(data, site_name)
            log.error(str(err))
