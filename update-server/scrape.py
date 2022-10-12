#!/bin/env python3

import requests
from bs4 import BeautifulSoup as BS
import re

url = 'https://www.minecraft.net/en-us/download/server/bedrock'

headers = { 
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}

res = requests.get(url, headers=headers)
html = BS(res.text, features="html.parser")
link = html.find(class_='downloadlink')['href']

bedrock_server_version = re.search('\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}', link).group()

print(bedrock_server_version)