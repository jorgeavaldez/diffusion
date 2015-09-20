#!/usr/bin/env python

# diffusion - the text language diff engine for baobao
# 
# copyright (c) 2015 - jorge valdez
# javaldez@smu.edu
#
# created for the engaged learning project with Alex Saladna

# these imports come from krill
# i'll be modifying them for their feed parsing and blurb extraction

import re
import requests
import sys
# import time
import json

# import feedparser
from bs4 import BeautifulSoup

class FeedMe(object):
    @staticmethod
    def soup_pull_article(url):
        data = urlopen(url).read()
        doc = BeautifulSoup(data, 'html.parser')
        
        f = open('out.txt', 'w')
        f.write(doc.get_text().encode('utf-8'))
        
    @staticmethod
    def readability_article_clean_test(url):
        # I'm gonna try to do the same article test here but using the
        # readability API so that I can get some clean text.
        base_url = 'http://readability.com/api/content/v1/parser'

        key_text = open('readability_key.txt', 'r')
        api_key = key_text.readlines()[0].strip()

        readability_payload = {'token' : api_key, 'url' : url}
        res = requests.get(base_url, params=readability_payload)

        key_text.close()
        
        res_obj = json.loads(res.text.encode('utf-8'))

        bsoup_dump = BeautifulSoup(res_obj['content'], 'html.parser')
        print(bsoup_dump.get_text().encode('utf-8').strip())

def main():
    url = raw_input('url: ')

    FeedMe.readability_article_clean_test(url)

main()
