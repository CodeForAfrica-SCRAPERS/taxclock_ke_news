import os
import boto3
import logging
import requests
import json
import pytz

from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime
from slacker_log_handler import SlackerLogHandler, NoStacktraceFormatter

from taxclock.config import AWS, log_file, timeout, slack, error_severity

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
        self.error_details = {'error': '',
                              'site_url': '',
                              'severity': ''}

    def get_html_content(self, site_url):
        '''Returns a soup object.
        Usage::
            pass the site url to the method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''

        try:
            res = requests.get(site_url, timeout=timeout['timeout'])
            html = BeautifulSoup(res.content, 'html.parser')
            return html
        except requests.exceptions.Timeout as err:
            log.error(str(err) + ' :- ' + str(self.get_local_time()))
            self.error_details['error'] = str(err)
            self.error_details['site_url'] = site_url
            self.error_details['severity'] = error_severity['severity'][1]
            self.send_error_log(self.error_details)
        except requests.exceptions.RequestException as err:
            log.error(str(err) + ' :- ' + str(self.get_local_time()))
            self.error_details['error'] = str(err)
            self.error_details['site_url'] = site_url
            self.error_details['severity'] = error_severity['severity'][1]
            self.send_error_log(self.error_details)

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
                    Bucket='taxclock.codeforkenya.org',
                    ACL='public-read',
                    Key='data/news.json',
                    Body=json.dumps(data))
            except Exception as err:
                self.local_store(data)
                log.info(str(err) +
                         ' :- ' + str(self.get_local_time()))
                self.error_details['error'] = str(err)
                self.error_details['severity'] = error_severity['severity'][1]
                self.send_error_log(self.error_details)
        else:
            log.error('No data to save' +
                      ' :- ' + str(self.get_local_time()))

    def sort_data_by_date(self, data):
        '''Sorts data by date.
        Usage::
            Pass the data to sort.
        :rtype: outputs a list of sorted data.
        '''
        if not data:
            log.info('No data was found for sorting.' +
                     ' :- ' + str(self.get_local_time()))
        return sorted(data, key=lambda k: parse(k['date_published']),
                      reverse=True)

    def get_local_time(self):
        '''Returns the current local time.
        :rytype: current time
        '''
        tz = pytz.timezone('Africa/Nairobi')
        local_time = tz.localize(datetime.now(), is_dst=None)
        return local_time

    def format_error(self, error):
        '''Formats the error message
        Usage::
            pass the error
        :rtype: returns the message well formatted.
        '''
        message = json.dumps({
            'origin': 'Taxclock Scraper',
            'origin_url': error['site_url'],
            'error_details': [
                {
                    'error': error['error'],
                    'severity': error['severity'],
                    'labels': {
                        'Product': 'TaxClock Kenya',
                        'Team': 'Code for Kenya Team',
                    },
                    'type': 'Web Scraping Application',
                }
            ]
        }, indent=2)
        return message

    def send_error_log(self, error):
        '''Sends message to slack
        Usage::
           pass the error message.
        :rtype: outputs the error to slack.
        '''
        slack_handler = SlackerLogHandler(slack['channel_token'],
                                          slack['channel_name'],
                                          stack_trace=True)
        # Create logger
        logger = logging.getLogger('debug_application')
        logger.addHandler(slack_handler)
        formatter = NoStacktraceFormatter(
            "{'log_date':%(asctime)s, 'message': %(message)s}")
        slack_handler.setFormatter(formatter)
        # Define the minimum level of log messages you want to send to Slack
        slack_handler.setLevel(logging.DEBUG)
        # Test logging
        logger.error(self.format_error(error))
