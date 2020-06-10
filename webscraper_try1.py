import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://www.talkinfrench.com/most-common-verbs-in-french/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

soup.findAll('a')
a_tags = soup.findAll('a')

print(a_tags)
