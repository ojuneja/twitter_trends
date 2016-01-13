from __future__ import print_function 
import boto3
import json
import urllib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TwitterTweets')


def parser(data,count):
	i = 0
	
	counter = int(count)
	try: js = json.loads(str(data))
	except: js = None
	
	tweets = js[0]["user"]["statuses_count"]
	#print tweets
	if counter >= int(tweets): counter = tweets
	string = ""
	while i < counter:
		twitter_tweet = js[i]["text"]
		twitter_screen_name = js[i]["user"]["screen_name"]
		twitter_favourites_count = js[i]["user"]["favourites_count"]
		twitter_name = js[i]["user"]["name"]
		twitter_created_at = js[i]["user"]["created_at"]
		twitter_location = js[i]["user"]["location"]
		twitter_id = js[i]["id"]
		twitter_friends_count = js[i]["user"]["friends_count"]
		twitter_followers_count = js[i]["user"]["followers_count"]
		
		response = table.put_item(
			Item={
				'id' : str(twitter_id),
				'name':twitter_name,
				'screen_name':twitter_screen_name,
				'following':twitter_friends_count,
				'followers':twitter_followers_count,
				'favorites':twitter_favourites_count,
				'location':twitter_location,
				'created_at':twitter_created_at,
				'tweet':twitter_tweet	
			}
		)
		i+=1
		string  = string + "\n" + twitter_tweet + twitter_screen_name + str(twitter_favourites_count) + twitter_name + twitter_created_at + twitter_location + str(twitter_id) + str(twitter_friends_count) + str(twitter_followers_count)
		
	return string
