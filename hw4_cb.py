# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 00:02:06 2014

@author: Cheryl
"""
 
url = "http://www.alchemyapi.com/products/alchemylanguage/keyword-extraction/"
url2 = "http://indianapublicmedia.org/arts/decoding-dude-academics-tackle-big-lebowski-book/"

from bs4 import BeautifulSoup
import urllib


html = urllib.urlopen(url2).read()
handylist = list()

#  create list of tags
soup = BeautifulSoup(html)

tags = soup('h1')
for tag in tags:
    title = str((tag.string)).encode('ascii', 'ignore')
    
section =  soup.find('div', attrs = {'class' : 'entry'})
ps = section('p')
for tag in ps:
    if (tag.string):
        try:   # skip anythin that has it's own class
            x = tag.attrs['class']
        except:
            string = str(tag.string).encode('ascii', 'ignore')
            handylist.append(string)

sometext = ''.join(handylist)

##### assume we ever get the api code
from alchemyapi import AlchemyAPI
import pandas as pd
alchemyapi = AlchemyAPI()

response = alchemyapi.keywords("text", sometext)
keylist = response['keywords']
s1 = pd.Series()
s2 = pd.Series()
for x in keylist:
    k1 = pd.Series([str(x.values()[1])])
    k2 = pd.Series([float(x.values()[0])])
    s1 = s1.append(k1)
    s2 = s2.append(k2)

df = pd.concat([s1,s2], axis = 1)
df.columns  = ["text", "relevance"]
df.sort(columns="relevance")

print
print
print 'website: ', url
print title
print 'Top 10 keywords are: '
print df.head(10)



