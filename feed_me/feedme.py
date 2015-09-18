#!/usr/bin/env python

# diffusion - the text language diff engine for baobao
# 
# copyright (c) 2015 - Jorge Valdez
# javaldez@smu.edu
#
# created for the engaged learning project with Alex Saladna

# these imports come from krill
# i'll be modifying them for their feed parsing and blurb extraction

try:
    # python 3
    from urllib.request import urlopen

except ImportError:
    # python 2
    from urllib2 import urlopen

import re
import sys
import time

import feedparser
from bs4 import BeautifulSoup

class FeedMe(object):
    @staticmethod
    def pull_article(url):
        data = urlopen(url).read()
        doc = BeautifulSoup(data, 'html.parser')

        for txt in doc.find_all('p'):
            print(txt)

def main():
    url = raw_input('url: ')

    FeedMe.pull_article(url)

main()
