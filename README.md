## Taxclock Scraper
This is a set of scrapers that gets information from some of the media houses' websites' in the country.

The scraper get data from the following sites:
* Standard Media :https://www.standardmedia.co.ke/business/category/19/business-news
* Nation Media :http://www.nation.co.ke/business/corporates/1954162-1954162-u0riql/index.html
* The Star Media: http://www.the-star.co.ke/sections/business_c29663
* Capital Media: http://www.capitalfm.co.ke/business/section/kenya
<br/>

This is a scraper that runs on [Morph](https://morph.io). To get started [see the documentation](https://morph.io/documentation)
 ## Getting started.
 ### How the taxclock scraper works.
 * Each website has it's own scraper. This is because sites are designed differently.
 * The python library that this scraper uses is beautiful soup. 
 * Beautiful soup generates a result set containing the html content of the site url passed to it.
 * With the html content you can retrieve the data that you want. 
 * It is necessary to understand html tags to be able to unpack data from the websites.
 * For the scrapers in this project, each scraper gets data from a div tag that contains the data.
 * Since the data is dynamic and in different formats, there is need to get the html tags of the data that you want.
 * Taxclock needs the stories with the properties link, image, title and date the story was published.
 * The html tags for the properties are a(from this we get the href),img (from this we get the src) and h(1-6)-this gives us text  for the date and title.

 * After obtaining this data there is need to store it. In our case we store it in a file locally and cloud storage(amazon webservice). You can read more on amazon webservices and how they work [here](https://aws.amazon.com/s3/).


Setting up the application to run on our machine.
## Installation
Clone the repository using the link.<br/>
``` https://github.com/CodeForAfrica-SCRAPERS/taxclock_ke_news.git```

Navigate to the folder. <br/>
```taxclock_ke_news```

Install the project dependencies. <br/>
``` pip install -r requirements.txt```

Before you run the project ensure you have the following environment variables set in your virtual environment.
```
   export MORPH_AWS_ACCESS_KEY=<aws_access_key>
   export MORPH_AWS_SECRET_KEY=<aws_secret_key>
   export TIMEOUT=<default_timeout>
   export CHANNEL_TOKEN=<channel_token>
   export CHANNEL_NAME=<slack_channel_name>
   export LOG_FILE=<log_file_name>

```
After the above steps and everything is set.<br/> 
Run ```python scraper.py```. <br/>
This command runs all the scrapers.


## Error Handling
The application captures errors by logging them to a file and sending slack messages to slack.
<br/>
Sending slack messages is achieved using the library. 
``` slack_log_handler```

Logging is achieved using: 
```python logging```

## Tests
Scraping websites is a very dynamic process. Sites' design change regularly. This means, anytime the scraper can fail due to change in the div it uses to get data from. This is the main reason for writing  tests. I have some tests for checking whether the div tag that is being used to scrape the site is still the one in the website html content. If you run the tests and any of them fails and it  checks for a div there is need to revisit the website and check the new div holding the data. The main reason for tests is to check whether your code is working as expected.<br/>
To run tests:<br/>
Run the command below in your root folder.
<br/>
```nosetests -v```
