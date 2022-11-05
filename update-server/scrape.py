#!/bin/env python3

import requests
from bs4 import BeautifulSoup as BS
import re

url = 'https://www.minecraft.net/en-us/download/server/bedrock'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}

try:
    res = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
except Exception as e:
    print(e)
    with open('update-server/scrape.log', 'w') as log:
        log.write('ERROR: ' + e)

html = BS(res.text, features="html.parser")
link = html.find(class_='downloadlink')['href']

bedrock_server_version = re.search(r'\d+\.\d+\.\d+\.\d+', link).group()

with open('update-server/scrape.log', 'w') as log:
    log.write('bedrock version: ' + bedrock_server_version)

print(bedrock_server_version)
