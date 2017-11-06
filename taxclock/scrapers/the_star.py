from taxclock import set_logging
from taxclock.scrapers.base import Scraper
from taxclock.settings import scrape_sites, base_urls, IMG_PLACEHOLDER


log = set_logging()


class StarMedia(Scraper):
    '''
    This the star scraper that gets data from the star website.
    '''

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
                        img_url = IMG_PLACEHOLDER
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

                log.error(err, extra={'notify_slack': True}, exc_info=True)
            return data
        else:
            log.error(result)

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
                log.error(ul, extra={'notify_slack': True}, exc_info=True)
                