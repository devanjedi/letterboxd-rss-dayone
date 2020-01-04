#!/usr/bin/python3

import feedparser
import ssl
import datetime

#Update with your username!
letterboxd_username="devanjedi"
rss_url='https://letterboxd.com/'+letterboxd_username+'/rss'

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

d = feedparser.parse(rss_url)

for entry in d.entries:
    if 'letterboxd_watcheddate' in entry:
        my_date = datetime.datetime.strptime(entry['letterboxd_watcheddate'], "%Y-%m-%d")
        print("\tDate: \t"+my_date.strftime("%b %d, %Y") + " at 09:00:00 PM EST" + "\n\n" + entry['title'] + "\n\n\n\n")
    #print(entry)
