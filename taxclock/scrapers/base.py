import os
import boto3
import logging
import requests
import json


from bs4 import BeautifulSoup
from dateutil.parser import parse

from taxclock import settings as env


log = logging.getLogger(__name__)


class Scraper(object):
    '''
    This is a base class inherited by other scraper classes.
    '''

    def __init__(self):
        self.url = None
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
            res = requests.get(url, timeout=int(env.TIMEOUT_TIME))
            html = BeautifulSoup(res.content, 'html.parser')
            return html

        except Exception as err:
            log.error(str(err))

    def local_store(self, data):
        '''Writes content from the website to file.
        Usage::
             file name to write data
        :param_train_data: the filename
        :rtype: outputs data to a file.
        '''

        with open(os.path.dirname(__file__) +
                  '/data/news.json', 'w') as output_file:
            # writes data to the output file.
            json.dump(data, output_file, indent=2)

    def aws_store(self, data):
        '''Writes the data to AWS.
        '''
        if data:
            data = self.sort_data_by_date(data)
            try:
                self.s3.put_object(
                    Bucket=env.AWS_S3_BUCKET,
                    ACL='public-read',
                    Key='data/news.json',
                    Body=json.dumps(data[:7]))
            except Exception as err:
                self.local_store(data[:7])
                log.info(str(err))
        else:
            log.error('No data to save')

    def sort_data_by_date(self, data):
        '''Sorts data by date.
        Usage::
            Pass the data to sort.
        :rtype: outputs the sorted data.
        '''
        if not data:
            log.info('No data was found for sorting.')
        return sorted(data, key=lambda k: parse(k['date_published']),
                      reverse=True)
