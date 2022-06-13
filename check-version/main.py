#!/bin/env python

import json
import requests
from bs4 import BeautifulSoup as BS
import re

with open('../config.json', 'r') as f:
    config = json.loads(f.read())
    
current_version = config['minecraft-server-version']

url = 'https://www.minecraft.net/en-us/download/server/bedrock'

headers = { 
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}

res = requests.get(url, headers=headers)
html = BS(res.text, features="html.parser")
link = html.find(class_='downloadlink')['href']

bedrock_server_version = re.search('\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}', link).group()

if (current_version != bedrock_server_version):
    print('New Bedrock Server version available')
    
    config['minecraft-server-version'] = bedrock_server_version
    
    with open('../config.json', 'w') as f:
        f.write(json.dumps(config, indent=2))