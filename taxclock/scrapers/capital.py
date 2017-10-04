import logging
import re

from base import Scraper
from taxclock.config import scrape_sites, log_file

logging.basicConfig(filename=log_file['log_file'], level=logging.INFO)
log = logging.getLogger(__name__)


class CapitalMedia(Scraper):
    def __init__(self):
        super(CapitalMedia, self).__init__()
        self.url = scrape_sites['capital']
        self.base = Scraper()

    def scrape_page(self):
        '''Scrapes stories from capitalfm media.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''
        result = self.base.get_html_content(self.url)
        if result:
            try:
                data = []
                items = result.find_all('div', class_='article-wrapper')
                for item in items:
                    img_url = item.find('img').get('src')
                    if not img_url:
                        img_url = 'https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png'
                    link = item.find('a').get('href').encode('ascii', 'ignore')
                    text = item.find('h2').text
                    get_data = self.base.get_html_content(link)
                    date_content = get_data.find("strong").text
                    date_string = date_content.encode('ascii', 'ignore')
                    reg_exp = re.match(
                        '^(\w+)(\W+)(\w+)(\W+)(\w+)(\W+)(\d+)', date_string)
                    result_value = reg_exp.groups(
                    )[4], ' ', reg_exp.groups()[6]
                    date = ''.join(result_value)
                    data.append({
                        'link': link,
                        'img': img_url,
                        'title': text,
                        'date_published': date
                    })
            except Exception as err:
                log.error(str(err) +
                          ' :- ' + str(self.base.get_local_time()))
            return data
        else:
            log.error(result +
                      ' :- ' + str(self.base.get_local_time()))
