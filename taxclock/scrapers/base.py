import boto3
import logging
import requests
import json

from bs4 import BeautifulSoup

from taxclock import settings as env


log = logging.getLogger(__name__)


class Scraper(object):
    '''
    This is a base class inherited by other scraper classes.
    '''

    def __init__(self):
        self.url = None
        # TODO: Move S3 configuration to another file
        self.s3 = boto3.client('s3', **{
            'aws_access_key_id': env.AWS_ACCESS_KEY,
            'aws_secret_access_key': env.AWS_SECRET_KEY,
            'region_name': env.AWS_REGION
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
        with open(env.DATA_DIR + site_name + '.json', 'w') as output_file:
            json.dump(data, output_file, indent=2)

    def aws_store(self, data, site_name):
        '''Writes the data to AWS S3.
        Usage::
            writes data to AWS S3.

        '''
        try:
            self.s3.put_object(
                # TODO: Pull bucket from settings
                Bucket='taxclock.codeforkenya.org',
                ACL='public-read',
                Key='data/' + site_name + '.json',
                Body=json.dumps(data))
        except Exception as err:
            self.local_store(data, site_name)
            log.error(str(err))
