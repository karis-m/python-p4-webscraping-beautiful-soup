# from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://Moringaschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')
infos = doc.select('.ms-button')

for info in infos: 
  print(info.contents[0].strip())