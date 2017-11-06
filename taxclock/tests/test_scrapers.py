from taxclock.tests import BaseTest
from taxclock.settings import scrape_sites


class ScraperTests(BaseTest):
    '''scraper tests.
    '''

    def test_get_html_content(self):
        '''Gets the content of webpage.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the page html content
        '''
        result_html = self.scraper.get_html_content(
            scrape_sites['standard'])
        data = result_html.find_all('h1')
        self.assertTrue(data)

    def test_nationmedia_scraper(self):
        '''Tests the scraper for nation media.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''

        result_html = self.scraper.get_html_content(
            scrape_sites['nation'])
        items = result_html.find_all(
            'div', class_='story-teaser top-teaser')
        self.assertTrue(items)

    def test_standardmedia_scraper(self):
        '''Tests the scraper for standard media.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''

        result_html = self.scraper.get_html_content(
            scrape_sites['standard'])
        ul = result_html.find('ul', class_='business-lhs')
        items = ul.find_all('div', class_='col-xs-6')
        self.assertTrue(items)

    def test_the_star_scraper(self):
        '''Tests the scraper for the star.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''

        result_html = self.scraper.get_html_content(
            scrape_sites['the_star'])
        items = result_html.find_all(
            'div', class_='field field-name-field-converge-image')
        self.assertTrue(items)

    def test_capitalfm(self):
        '''Tests the scraper for capitalfm.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the stories image,link, title.
        '''
        result_html = self.scraper.get_html_content(
            scrape_sites['capital'])
        items = result_html.find_all('div', class_='article-wrapper')
        self.assertTrue(items)

    def test_pagination(self):
        '''Tests the pagination links.
        Usage::
              create the class object
              using the object call the method
        :param_train_data: the url of the site
        :rtype: the urls of all pages in the site.
        '''
        urls = self.the_star.pagination()
        self.assertTrue(urls)

    def test_standard(self):
        '''Tests data is returned by the_standard scraper
        Usage::
               the method doesn't require any argument
        :rtype: It returns a list of data obtained from
                the html page of the site url.
                the data is title, link, image
        '''
        standard_data = self.standard.scrape_page()
        self.assertTrue(standard_data)

    def test_star(self):
        '''Tests data is returned by the_star scraper
        Usage::
               the method doesn't require any argument
        :rtype: It returns a list of data obtained from
                the html page of the site url.
                the data is title, link, image
        '''
        the_star_data = self.the_star.scrape_page()
        self.assertTrue(the_star_data)

    def test_capital(self):
        '''Tests data is returned by capital scraper
        Usage::
               the method doesn't require any argument
        :rtype: It returns a list of data obtained from
                the html page of the site url.
                the data is title, link, image
        '''
        capital_data = self.capital.scrape_page()
        self.assertTrue(capital_data)

    def test_nation(self):
        '''Tests data is returned by nation scraper
        Usage::
               the method doesn't require any argument
        :rtype: It returns a list of data obtained from
                the html page of the site url.
                the data is title, link, image
        '''
        nation_data = self.nation.scrape_page()
        self.assertTrue(nation_data)

    def test_sort_data(self):
        '''Tests data is sorted by date
        Usage::
            the method accepts data
        :rtype: It returns sorted data.
        '''
        the_star_data = self.the_star.scrape_page()
        self.assertTrue(self.scraper.sort_data_by_date(the_star_data))
        