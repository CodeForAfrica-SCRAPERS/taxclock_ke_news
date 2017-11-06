import re

from taxclock import set_logging
from taxclock.scrapers.base import Scraper
from taxclock.settings import scrape_sites, IMG_PLACEHOLDER


log = set_logging()


class CapitalMedia(Scraper):
    '''
    This is a capital scraper it gets data from capital website.
    '''

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
                        img_url = IMG_PLACEHOLDER
                    link = item.find('a').get('href')
                    text = item.find('h2').text
                    get_data = self.base.get_html_content(link)
                    date_content = get_data.find("strong").text
                    date_string = date_content,
                    reg_exp = re.match(
                        '^(\w+)(\W+)(\w+)(\W+)(\w+)(\W+)(\d+)', str(date_string))
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
                log.error(err, extra={'notify_slack': True}, exc_info=True)
            return data
        else:
            log.error(result)
            