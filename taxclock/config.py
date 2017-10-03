import os


scrape_sites = {
    'standard': 'https://www.standardmedia.co.ke/business/category/19/business-news',
    'nation': 'http://www.nation.co.ke/business/corporates/1954162-1954162-u0riql/index.html',
    'the_star': 'http://www.the-star.co.ke/sections/business_c29663',
    'capital': 'http://www.capitalfm.co.ke/business/section/kenya/'

}

base_urls = {

    'standard': 'https://www.standardmedia.co.ke',
    'nation': 'http://www.nation.co.ke',
    'the_star': 'http://www.the-star.co.ke',
    'capital': 'http://www.capitalfm.co.ke',

}

# defining the access keys
AWS = {
    'aws_access_key_id': os.environ['MORPH_AWS_ACCESS_KEY'],
    'aws_secret_access_key': os.environ['MORPH_AWS_SECRET_KEY'],
    'region_name': 'eu-west-1'
}

# config for the log file.
log_file = {
    'log_file': os.environ.get('LOG_FILE', 'taxclock.log')
}