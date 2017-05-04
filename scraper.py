from bs4 import BeautifulSoup
import requests
import os
import boto3


res = requests.get("https://www.standardmedia.co.ke/business/category/19/business-news")

raw = res.content

html = BeautifulSoup(raw, 'html.parser')

data = []

ul = html.find("ul", class_="business-lhs")

items = ul.find_all("div", class_="col-xs-6")

for item in items:
    img_src = item.find("img").get("src")
    text = item.find("h4").text
    link = item.find("h4").find("a").get("href")
    data.append({
        'title':text,
        'link':link,
        'img':img_src
        })

data = json.dumps(data)
    
