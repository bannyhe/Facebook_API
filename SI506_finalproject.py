import string
import json
import webbrowser
import unittest
import requests
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from your_app_data import APP_ID, APP_SECRET


# Step 1: Define a class 'Post'
# Instance variables: message, comments, likes
# Methods: constructor, string, non_stopwords, most_common_word


class Post():

	# Define the constructor function
	def __init__(self, post_dict={}):

		# Find the message content from a post. 
		if 'message' in post_dict:
			self.message = post_dict['message']
		else:
			self.message = ''

		if 'comments' in post_dict:
			self.comments = post_dict['comments']['data'] 
		else:
			self.comments = []

		if 'likes' in post_dict:
			self.likes = post_dict['likes']['data']
		else:
			self.likes = []


	# Define a string method for class Post
	def __str__(self):
		return ("In this post, message is: {}, comments are: {}, likes are by: {}".format(self.message, self.comments, self.likes))


	# Define another method in class Post, which returns a list contains words 

	def non_stopwords(self):
		# Open and read the file contains all stopwords called stop_words.txt
		f = open("stop_words.txt","r")
		stop_words = []
		for w in f.readlines():
			stop_words.append(w.strip())
		f.close()
		# Delete all punctuations in message.
		message = self.message
		for b in string.punctuation:
			if b in message:
				message = message.replace(b,"")
		# Create a new list for words not in stop_words.txt
		non_stop_words = []
		# If a character in message is not in stop_words.txt, append this character to non_stop_words
		for word in message.split():
			if word.lower() not in stop_words:
				non_stop_words.append(word)
		return non_stop_words


	# This method is to find words and their frequency in the message (without stopword) of the post
	# Add return a dictionary containing words and their frequency
	def word_count(self):
		# Create a dictionary to hold words and their frequency in message (excluding stopwords)as key-value pair.
		dic = {}
		# Create a list contains all words in message excluding stopwords.
		new_lst = self.non_stopwords()
		# If this post does not have message, new_lst would be a void list. 
		# I set the return list to be ["a",0] because 0 will not add to frequency 

		# Add words and their frequency as key-value pairs into dictonary dic.
		for word in new_lst:
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1

		return dic


# Step 2: Request data of 25 posts from Facebook

# Global facebook_session variable, needed for handling FB access below
facebook_session = False

# Function to make a request to Facebook provided.
def makeFacebookRequest(baseURL, params = {}):
    global facebook_session
    if not facebook_session:
        # OAuth endpoints given in the Facebook API documentation
        authorization_base_url = 'https://www.facebook.com/dialog/oauth'
        token_url = 'https://graph.facebook.com/oauth/access_token'
        redirect_uri = 'https://www.programsinformationpeople.org/runestone/oauth'

        scope = ['user_posts','pages_messaging','user_managed_groups','user_status','user_likes']
        facebook = OAuth2Session(APP_ID, redirect_uri=redirect_uri, scope=scope)
        facebook_session = facebook_compliance_fix(facebook)

        authorization_url, state = facebook_session.authorization_url(authorization_base_url)
        print('Opening browser to {} for authorization'.format(authorization_url))
        webbrowser.open(authorization_url)

        redirect_response = input('Paste the full redirect URL here: ')
        facebook_session.fetch_token(token_url, client_secret=APP_SECRET, authorization_response=redirect_response.strip())

    return facebook_session.get(baseURL, params=params)




# Baseurl provided
baseurl = 'https://graph.facebook.com/nba/feed'

# Add key-value pair into dictionary parameters.
parameters = {}
parameters["limit"] = 25
parameters['fields'] = 'message,comments,likes'

# Request data from Facebook
response = makeFacebookRequest(baseurl, params = parameters)

# Use json.loads to convert json data into python data.
posts_data = json.loads(response.text)


# Step 3: Create a list of instance of class Post
# Create a list of instances of class "Post"
post_insts = []
for item in posts_data['data']:
	post_insts.append(Post(item))

#	print 25 posts messages.
print("Requested 25 posts data from the Facebook page of 'nba', here are the messages of the posts:")

num = 0
for post in post_insts:
	num += 1
	print ("post No." + str(num) + ", message: ")
	print (post.message)
	print("\n")
	

# Step 4: Find the most common word among all posts

# 	Find the most common word that is not a “stopword”  among all of those posts.

# Create a dictionary to store the "word"-"frequency" key-value pair 
dic_w_c = {}

for post in post_insts:
	# if the most common word in this post is not in dic_w_c, add a key-value pair: most common word - its frequency in this post into dic_w_c
	
	# Get the word frequency dictionary in this post.
	post_dic = post.word_count()
	# Add word-frequency as key-value pair into dic_w_c.
	for key in post_dic:
		if key not in dic_w_c:
			dic_w_c[key] = post_dic[key]
		else: 
			dic_w_c[key] += post_dic[key]
		# Initialize the overall most common word 
		most_common_word = key


# Find the overall most common word.
for word in dic_w_c:
	if dic_w_c[word] > dic_w_c[most_common_word]:
		most_common_word = word


###
### Print the most common word.
###
print("Among all words in all post messages, the most common word is: ")
print(most_common_word)
print("The frequency of the most common word is: ")
print(dic_w_c[most_common_word])
print("\n")
print("\n")


# Step 5: Create a cache file for storing requested data.		
# Create a cache file for wrting caching data into it later.
CACHE_FNAME = "SI506finalproject_cache.json" 
try:  
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {} 


# Step 6: Define functions to request data from iTunes and cache file 
#		For the requesting data function:
#			- input: the word from step 3
#			- output: a list of songs titles and durations based on the keyword


## Function to create a unique representation of each request without private data like API keys
def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


# Define a function called get_from_itunes
# - Input: the word for searching & the type for searching (defult is "song")
# - Return: songs about this word 
def get_from_itunes(search, name = 'song'):
	# Base url
	baseurl = 'https://itunes.apple.com/search'

	# Create parameters
	params = {}
	params["term"] = search
	params["entity"] = name

	# Create unique_ident using the defined function params_unique_combination
	unique_ident = params_unique_combination(baseurl, params)

	# if unique ident in CACHI_DICTION, get data from this local file.
	if unique_ident in CACHE_DICTION:
		print("Getting cached data...")
		return CACHE_DICTION[unique_ident]

    # Else, request data from the Internet.
	else:
		print("Making a request for new data...")

        
        # Make a request and assign the text from requested data to variable resp 
		resp = requests.get(baseurl, params)
		resp_text = resp.text

		# Convert the requested json data text into pyhton data.
		song_results = json.loads(resp_text)

		# Find needed song data in the requested nested data 
		song_data = []
		for i in song_results["results"]:
			song_data.append((i['artistName'], i["collectionName"], i["trackName"], i["trackTimeMillis"]))

		# Add them to CACHE_DICTION
		CACHE_DICTION[unique_ident] = song_data

		# Convert python data into json data and write into the cache file.
		dumped_json_cache = json.dumps(CACHE_DICTION)
		fw = open(CACHE_FNAME,"w")
		fw.write(dumped_json_cache)
		fw.close() # Close the open file

		return CACHE_DICTION[unique_ident]


# Step 7: Request data from iTunes using the function defined in step 5.			

song_data_lst = get_from_itunes(most_common_word)


# Step 8: Define a class "Song"


# Define a class 'Song'.
class Song():

	def __init__(self, name, collection, track_name, duration):
		self.artist_name = name
		self.collection = collection
		self.track_name = track_name
		self.track_duration = duration

	def __str__(self):
		return("{}'s {} is in collection {}.".format(self.artist_name, self.track_name, self.collection))


	def name_duration(self):
		return("The duration of the song '{}' is {}.".format(self.track_name, self.track_duration))


# Step 9: Create a list of instances of class `Song` using the requested data.

song_lst = []
for song in song_data_lst:
	song_lst.append(Song(*song))


# Step 10: Sort the song instances from iTunes by the songs’ length, longest to shortest.

sorted_song_lst = sorted(song_lst, reverse = True, key = lambda x : x.track_duration)


#Print sorted songs from longest duration to shortest.
print("\n\nSearching for the most common word: '" + most_common_word + "', we got some songs. \nAfter sorting them by their length, longest to shortest, here are the results: ")
for asong in sorted_song_lst:
	print(asong)
	print(asong.name_duration())
	print("\n")


# Step 11: Create a CSV file with information about all of those songs:
#			- The song title
#			- The artist of the song   
#			- The length of the song
#			- The album the song is on   
#			- Other column(s) of information you want


f = open('iTunes_songs.csv','w')

# Write some explainations and headers for people to read and understand the file
w_str0 = "We got some songs by searching the word ' " + most_common_word + " ' using iTunes API. \nHere are the results after sorting the songs by their length - longest to shortest: \n"
f.write(w_str0 + '\n')
f.write("  \n\n")
w_str1 = "Title, Artist, Duration(ms), Album"
f.write(w_str1 + '\n')

for song in sorted_song_lst:
	w_str  = "{}, {}, {}, {}".format(song.track_name, song.artist_name, song.track_duration, song.collection)
	f.write(w_str  + '\n')
	
f.close()









