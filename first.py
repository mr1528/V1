#!/usr/bin/env python
# coding: utf-8
# 1st new line


# TO DO ADDED 2
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.itico.ir')
#r.text
soup = BeautifulSoup(r.text, "html.parser")
print( soup.prettify())
#print(soup.find(text="TourBarg"))
print(soup)



