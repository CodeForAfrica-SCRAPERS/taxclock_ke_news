import logging
from bs4 import BeautifulSoup
import requests
import os
import boto3
import json

s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ['MORPH_AWS_ACCESS_KEY'],
    aws_secret_access_key=os.environ['MORPH_AWS_SECRET_KEY'],
    region_name='eu-west-1'
)

try:
    res = requests.get("https://www.standardmedia.co.ke/business/category/19/business-news")
    raw = res.content
    html = BeautifulSoup(raw, 'html.parser')
    data = []
    base_url = "https://www.standardmedia.co.ke"
    ul = html.find("ul", class_="business-lhs")
    items = ul.find_all("div", class_="col-xs-6")
    for item in items:
        img_src = item.find("img").get("src")
        img_url = base_url+img_src
        text = item.find("h4").text
        link = item.find("h4").find("a").get("href")
    data.append({
        'title':text,
        'link':link,
        'img':img_url
        })
    s3.put_object(
        Bucket='taxclock.codeforkenya.org',
        ACL='public-read',
        Key='data/standard-news.json',
        Body=json.dumps(data)
        )
except Exception as err:
    logging.exception(str(err))