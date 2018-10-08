__authors__ = 'Steve Oney and Jackie Cohen'
## 506 F17
## Problem Set 9
# NOTE: This problem set requires using the Facebook API. If you do not have a Facebook account or would prefer not to use your personal account for this project, please create a new account. You can delete it after this project is over!

import json
import webbrowser
import unittest
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from your_app_data import APP_ID, APP_SECRET


# Global facebook_session variable, needed for handling FB access below
facebook_session = False
global classes
# Function to make a request to Facebook provided.
# Reference: https://requests-oauthlib.readthedocs.io/en/latest/examples/facebook.html
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

# [PROBLEM 1]
# [PROBLEM 1A] Fill in the APP_ID and APP_SECRET variables by following the directions in your_app_data.py.

# [PROBLEM 1B] Then use the provided makeFacebookRequest function to make a request to the Facebook Graph API at: https://graph.facebook.com/me.

# Using json.loads, store the Python version of the result in the variable current_user. It should have keys 'name' and 'id.'

# Write code for PROBLEM 1B here:

response = makeFacebookRequest('https://graph.facebook.com/me')
current_user = json.loads(response.text)
print(current_user)


### BEGIN PROVIDED CODE
# This code makes lists of positive words and negative words, saving them in the variables pos_ws and neg_ws.
# DO NOT CHANGE THIS CODE, you'll need it later in the PSet.
f = open('positive_words.txt', 'r')
pos_ws = []
for l in f.readlines()[35:]:
    pos_ws.append(l.strip())
f.close()

neg_ws = []
f = open('negative_words.txt', 'r')
for l in f.readlines()[35:]:
    neg_ws.append(l.strip())
f.close()
## END PROVIDED CODE

# [PROBLEM 2]
# Fill in the definition of the class Post (begun below) to hold information about one post that you've made on Facebook.
# You need to pull out the appropriate data from the json representation of a single post.
# You can find a sample in the file samplepost.json.
# There are tests that check whether you've pulled out the right data.
# Below, in the comments, we've listed the things you'll need to do in the following class Post, representing one Facebook post, to complete it.

# [PROBLEM 2A] Add to the __init__ method additional code to set the instance variables comments and likes.
# [PROBLEM 2B] If the post dictionary has a 'comments' key, set an instance variable self.comments to the list of comment dictionaries you extract from post_dict. Otherwise, set self.comments to be an empty list: []

# NOTE: Something similar has already been done for the contents (message) of the original post, which is the value of the 'message' key in the dictionary, when it is present (photo posts don't have a message). See above. BUT,
# Extracting the list of comment dictionaries from a post_dict is a little bit harder. Take a look at the sample of what a post_dict looks like in the file samplepost.txt to figure out where to find the right information.

# [PROBLEM 2C] Now, similarly, if the post has any likes, set self.likes to the value of the list of likes dictionaries. Otherwise, if there are no 'likes', set self.likes to an empty list.

# [PROBLEM 2D] In the Post class, fill in these three methods:
# -- positive() returns the number of words in the message that are in the list of positive words called pos_ws (provided in our code)
# -- negative() returns the number of words in the message that are in the list of negative words called neg_ws (provided in our code)
# -- emo_score returns an integer: the difference between positive and negative scores
# The beginnings of these functions are below -- fill in the rest of the method code! There are tests of these methods later on.

class Post():
    '''object representing status update'''
    def __init__(self, post_dict={}):
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = []
        if 'comments' in post_dict:
            self.comments = post_dict['comments']['data']
        else:
            self.comments = []
        if 'likes' in post_dict:
            self.likes = post_dict['likes']['data']
        else:
            self.likes = []   

    def positive(self):
        p = 0
        for i in self.message.split():
            if i in pos_ws:
                p += 1
        return p

    def negative(self):
        n = 0
        for i in self.message.split():
            if i in neg_ws:
                n += 1
        return n

    def emo_score(self):
        p = 0
        n = 0
        for i in self.message.split():
            if i in pos_ws:
                p += 1
            if i in neg_ws:
                n += 1
        e = p - n
        return e

# [PROBLEM 3]
# Add comments for these lines of code explaining what is happening in them. HINT: One instance of class Post -- one Post instance -- is being created in the third line... No tests for this, because it's comments!

sample_file = open('samplepost.json')       # Open file 'samplepost.json', and save it to variable sample_file. 
sample_text = sample_file.read()            # Read the file, and save the text to variable sample_text.
sample_file.close()                         # Close the file.
sample_post_dict = json.loads(sample_text)  # Using json.loads method to store the Python version of the result(dictionary) in the variable sample_post_dict.
p = Post(sample_post_dict)                  # Call the class Post with the dictionary of sample_post_dict, and save the result to variable p.

# NOTE: Use the next lines of code if you're having trouble getting the tests to pass. They will help you understand what a post_dict contains, and what your code has actually extracted from it and assigned to the comments and likes instance variables.
# TODO: IMPORTANT - Please re-comment these lines of code (make sure they ARE commented out) before submitting your problem set!
#print(json.dumps(sample_post_dict, indent=4))
#print(json.dumps(p.comments, indent=4))
#print(json.dumps(p.likes, indent=4))


# [PROBLEM 4]
# Now, get a json-formatted version of your last 100 posts on Facebook. Save the result you get from Facebook, unprocessed except for being loaded into a Python object, in a variable hundred_posts_data.

# (If you do not have any data in your feed, you can also use the feed of a public group to get the last 100 posts in the group. Make sure you use a PUBLIC group, that any one in the class could access, not a Facebook group that YOU are an admin of. Don't worry -- if you use your own feed, we won't get your private data. We'll get ours.)

# Baseurl provided
baseurl = 'https://graph.facebook.com/me/feed' # Replace "me" with the group id if you are using a public group instead

# OK, now: What function do you need to invoke with what input to make this happen? HINT: Use the Facebook Graph API Explorer (https://developers.facebook.com/tools/explorer/) to test the parameters of your request. The response should return data for the message, likes, and comments of each post.

# Write code for PROBLEM 4 here:

response_str = makeFacebookRequest(baseurl, params = {"fields": "likes, comments, message", "limit": "100"})
hundred_posts_data = json.loads(response_str.text)
print(hundred_posts_data)

# [PROBLEM 5]
# Create a list of Post instances,
# using the data you saved in hundred_posts_data in PROBLEM 4.

# For each of those posts in the feed you got back,
    # create an instance of your class Post.
# Save all the post instances you create in a list called post_insts.

# If you passed the tests above, all this should work just fine if you create one instance per post and save them all in a list.
# This requires understanding -- but not too many lines of code!

# Write code for PROBLEM 5 here:

post_insts = []
for i in hundred_posts_data['data']:
    post_insts.append(Post(i))

print(post_insts)


# [PROBLEM 6]
# Write code to output a .csv file called emo_scores.csv that will let you make a scatterplot (in Excel or Google sheets) showing net positivity (emo_scores) on x-axis and comment-counts and like-counts on the y-axis.
# Each row should represent one post, and should include: emo score, comment count, and like count, in that order.

# Write code for PROBLEM 6 here:

file_rev = open('emo_scores.csv', 'w')
file_rev.write("emo score, comment count, like count\n")

for i in hundred_posts_data['data']:
    file_rev.write("{}, {}, {}\n".format(Post(i).emo_score, len(Post(i).comments), len(Post(i).likes)))
file_rev.close()

# OPTIONAL: Post a screenshot of your scatterplot to Piazza!

# You can see what the scatterplot might look like
# in emo_scores.xlsx, included in the assignment. (In the example case, there's not an obvious correlation between positivity and how many comments or likes. There may not be, but you find that out by exploring the data!)

# Can you see any trends or possible relationships between likes, comments, and emo_scores? (Something to consider. Not graded.)

# When you're finished, upload this file to Canvas.
# TODO: On canvas, ONLY SUBMIT THIS FILE (no other files in the directory)

# [PROBLEM 7] - 400 Points for Final Project Plan, separate from PS9's 1000 points.
# Fill out the Final Project Plan document in English. Graded separately!

############################################################
##                                                        ##
##          DO NOT MODIFY THE TEST CODE BELOW             ##
##             WE USE IT TO TEST YOUR CODE                ##
##                                                        ##
############################################################

class Problem1(unittest.TestCase):
    def test_current_user(self):
        self.assertTrue('name' in current_user)
        self.assertTrue('id' in current_user)

class Problem2(unittest.TestCase):
    def setUp(self):
        sample_file = open('samplepost.json')
        sample_text = sample_file.read()
        sample_file.close()
        sample_post_dict = json.loads(sample_text)
        self.post = Post(sample_post_dict)
        self.post.message = 'adaptive acumen abuses acerbic aches for everyone'
    def test_comments_1(self):
        self.assertIsInstance(self.post.comments, list, 'testing type of Post.comments')
    def test_comments_2(self):
        self.assertEqual(len(self.post.comments), 4, 'testing length of Post.comments')
    def test_comments_3(self):
        self.assertIsInstance(self.post.comments[0], dict, 'testing type of Post.comments[0]')
    def test_likes_1(self):
        self.assertIsInstance(self.post.likes, list, 'testing type of Post.likes')
    def test_likes_2(self):
        self.assertEqual(len(self.post.likes), 4, 'testing length of Post.likes')
    def test_likes_3(self):
        self.assertIsInstance(self.post.likes[0], dict, 'testing type of Post.likes[0]')
    def test_positive(self):
        self.assertEqual(self.post.positive(), 2, 'testing return value of Post.positive()')
    def test_negative(self):
        self.assertEqual(self.post.negative(), 3, 'testing return value of Post.negative()')
    def test_emo_score(self):
        self.assertEqual(self.post.emo_score(), -1, 'testing return value of Post.emo_score()')

class Problem4(unittest.TestCase):
    def test_hundred_posts_data(self):
        self.assertIsInstance(hundred_posts_data, dict, 'testing type of hundred_posts_data')
        self.assertIn('data', hundred_posts_data, 'testing keys of hundred_posts_data')

class Problem5(unittest.TestCase):
    def setUp(self):
        sample_file = open('samplepost.json')
        sample_text = sample_file.read()
        sample_file.close()
        sample_post_dict = json.loads(sample_text)
        self.post = Post(sample_post_dict)
    def test_post_insts(self):
        self.assertIsInstance(post_insts,list,'Testing that post_insts is a list')
    def test_posts_in_list(self):
        self.assertIsInstance(post_insts[0],Post,'Testing that the first item in the list is class Post')
        self.assertEqual(type(post_insts[-1]),type(self.post),'Testing that last item in the list is class Post, in a different way')

class Problem6(unittest.TestCase):
    def setUp(self):
        self.emo_file = open('emo_scores.csv','r')
        self.emo_contents = self.emo_file.readlines()
        self.emo_file.close()
    def test_emo_scores(self):
        self.assertTrue(self.emo_file,'Testing that a file emo_scores.csv exists in directory')
        self.assertTrue(self.emo_contents,'Testing that the file can be opened and read')
    def test_emo_contents(self):
        self.assertEqual(len(self.emo_contents[0].split(',')),3,'Testing that there are 3 columns in the CSV file')
    def test_emo_contents2(self):
        self.assertTrue(len(self.emo_contents) > 3, 'Testing that there are at least 3 lines in the CSV file generated, so multiple posts were processed for the file')

if __name__ == '__main__':
    unittest.main(verbosity=2)
