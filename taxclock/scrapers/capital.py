import logging

from base import Scraper
from taxclock.settings import scrape_sites


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
                        img_url = 'https://github.com/CodeForAfrica/TaxClock/\
                                    blob/kenya/img/placeholder.png'
                    link = item.find('a').get('href')
                    text = item.find('h2').text
                    data.append({
                        'link': link,
                        'img': img_url,
                        'title': text
                    })
                self.aws_store(data, 'capital-news')
            except Exception as err:
                log.error(str(err))
            return data
        else:
            log.error(result)
