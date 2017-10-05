import logging

from base import Scraper
from taxclock.settings import scrape_sites, base_urls


log = logging.getLogger(__name__)


class NationMedia(Scraper):
    def __init__(self):
        super(NationMedia, self).__init__()
        self.url = scrape_sites['nation']
        self.base = Scraper()

    def scrape_page(self):
        '''Scrapes stories from nation media.
        Usage::
              use the class object
              pass the site url to\
              get_html_content method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''
        result = self.base.get_html_content(self.url)
        if result:
            try:
                data = []
                items = result.find_all(
                    'div', class_='story-teaser medium-teaser')
                for item in items:
                    img_src = item.find('img').get('src')
                    if img_src:
                        img_url = base_urls['nation'] + img_src
                    else:
                        img_url = 'https://github.com/CodeForAfrica/TaxClock/\
                                    blob/kenya/img/placeholder.png'
                    link = base_urls['nation'] + item.find('a').get('href')
                    text = item.find('img').get('alt')
                    data.append({
                        'link': link,
                        'img': img_url,
                        'title': text
                    })
                self.base.aws_store(data, 'nation-news')
            except Exception as err:
                log.error(str(err))
            return data
        else:
            log.error(result)
