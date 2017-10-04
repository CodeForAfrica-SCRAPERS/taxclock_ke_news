import logging


from base import Scraper
from taxclock.config import scrape_sites, base_urls, log_file

logging.basicConfig(filename=log_file['log_file'], level=logging.INFO)
log = logging.getLogger(__name__)


class StarMedia(Scraper):

    def __init__(self):
        super(StarMedia, self).__init__()
        self.url = scrape_sites['the_star']
        self.base = Scraper()

    def scrape_page(self):
        '''Scrapes stories from star media.
        Usage::
              create the class object
              using the object call the  url to\
              get_html_content method.
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''
        result = self.base.get_html_content(self.url)
        if result:
            try:
                data = []
                items = result.find_all(
                    'div', class_='field field-name-field-converge-image')
                for item in items:
                    img_url = item.find('img').get('src')
                    if not img_url:
                        img_url = 'https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/placeholder.png'
                    link = base_urls['the_star'] + item.find('a').get('href')
                    get_data = self.base.get_html_content(link)
                    text = get_data.find('h1').text
                    date = get_data.find('time').text
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

    def pagination(self):
        '''Gets pages links from the star.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the urls of all pages in the site.
        '''

        result = self.base.get_html_content(self.url)
        if result:
            ul = result.find('ul', class_='pager')
            if ul:
                items = ul.find_all('li', class_='pager__item')
                urls = []
                for links in items[1:]:
                    link = base_urls['the_star'] + links.find('a').get('href')
                    urls.append(link)
                return urls
            else:
                log.error(ul +
                          ' :- ' + str(self.base.get_local_time()))
        else:
            log.error(result +
                      ' :- ' + str(self.base.get_local_time()))
