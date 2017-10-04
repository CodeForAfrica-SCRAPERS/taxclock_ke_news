import logging

from base import Scraper
from taxclock.config import scrape_sites, base_urls, log_file

logging.basicConfig(filename=log_file['log_file'], level=logging.INFO)
log = logging.getLogger(__name__)


class StandardMedia(Scraper):
    def __init__(self):
        super(StandardMedia, self).__init__()
        self.url = scrape_sites['standard']
        self.base = Scraper()

    def scrape_page(self):
        '''Scrapes stories from standard media.
        Usage::
              use the class object
              pass the site url to\
              get_html_content method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''

        result = self.get_html_content(self.url)
        data = []
        if result:
            try:
                ul = result.find('ul', class_='business-lhs')
                items = ul.find_all('div', class_='col-xs-6')
                for item in items:
                    img_src = item.find('img').get('src')
                    if img_src:
                        img_url = base_urls['standard'] + img_src
                    else:
                        img_url = 'https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png'
                    text = item.find('h4').text
                    link = item.find('h4').find('a').get('href')
                    get_data = self.base.get_html_content(link)
                    date_content = get_data.find_all('span', class_='writer')
                    list_date = date_content[0:1]
                    get_text = list_date[0].get_text()
                    encode = get_text.encode('ascii', 'ignore')
                    date = encode.split(',')[1]
                    data.append({
                        'title': text,
                        'link': link,
                        'img': img_url,
                        'date_published': date
                    })
            except Exception as err:
                log.error(str(err) +
                          ' :- ' + str(self.base.get_local_time()))
            return data
        else:
            log.info(result +
                     ' :- ' + str(self.base.get_local_time()))
