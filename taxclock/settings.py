import os


# SITES TO BE SCRAPED
# TODO: Combine base_urls and scrape_sites into one

# Base urls are used to ...
base_urls = {
    'standard': 'https://www.standardmedia.co.ke',
    'nation': 'http://www.nation.co.ke',
    'the_star': 'http://www.the-star.co.ke',
    'capital': 'http://www.capitalfm.co.ke',
}

# Actual pages we'll be scraping
scrape_sites = {
    'standard': 'https://www.standardmedia.co.ke/business/category/19/business\
                -news',
    'nation': 'http://www.nation.co.ke/business/corporates/1954162-1954162-u0r\
                iql/index.html',
    'the_star': 'http://www.the-star.co.ke/sections/business_c29663',
    'capital': 'http://www.capitalfm.co.ke/business/section/kenya/'
}


# AWS SETTINGS
AWS_ACCESS_KEY = os.getenv('MORPH_TAXCLOCK_AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('MORPH_TAXCLOCK_AWS_SECRET_KEY')
AWS_REGION = os.getenv('MORPH_TAXCLOCK_AWS_REGION', 'eu-west-1')

AWS_S3_BUCKET = os.getenv('MORPH_TAXCLOCK_AWS_S3_BCUKET', 'taxclock.codefor\
                                                            kenya.org')

# DATA DIRECTORY
# Local data directory to save scraped data
DATA_DIR = os.path.dirname(__file__) + '/data/'


# OTHER SETTINGS
# Placeholder image when none found on scrape
IMG_PLACEHOLDER = 'https://github.com/CodeForAfrica/TaxClock/blob/kenya/img/\
                    placeholder.png'

# timeout for the url request.
TIMEOUT_TIME = os.getenv('MORPH_TAXCLOCK_TIMEOUT', 30)
