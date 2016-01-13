#!/usr/bin/env python
import urllib
import twurl
import json
import helper

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'


acct = raw_input('Enter Twitter Account:')
count = raw_input('Enter Number of Tweets:')
url = twurl.augment(TWITTER_URL,
      {'screen_name': acct, 'count': count} )
print 'Retrieving', url
try:
	connection = urllib.urlopen(url)
	data = connection.read()
	helper.parser(data,count)
except: print "Wrong twitter account"

