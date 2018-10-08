# import statements
import unittest
import json
import requests

## IMPORTANT NOTES:

## In general, this course expects you to run Python files via the command prompt. In some cases, even if you do not do so, assignments will work. This assignment, depending upon your setup, is VERY UNLIKELY to work if you do not run it via the command prompt (Git Bash or Terminal).

## Remember: run your program early and often to determine what it is doing and whether it is working as you expect it to! DO NOT turn your program in without first running it to make sure that all of the test output is shown and it runs properly. We do not grade files that do not run.

## We recommend reading through the whole file first, and reading directions carefully, and then beginning with the first problem, with an understanding of what you will be doing throughout the problem set.

## You should NOT be writing any additional calls to input (besides the one that already exists / will run if you do not include your flickr_key).

#########

## [PROBLEM 1]
print("\n***** PROBLEM 1 *****\n") # (Print statements like this throughout the problem set are provided to help you figure out where things are when you see output. You should leave them alone.)

## We have provided a sample dictionary in the format that Flickr returns it, saved in a JSON file (much like the nested_data.json file you were provided in Problem Set 6).

## Write code to open the file sample_diction.json and load its contents as a Python object into the variable sample_photo_rep. Then close the file (that'll keep you from running into easily-avoidable errors later on!). There are unit tests for this problem.

## (You may also find it useful, for later in the problem set, to open the file "sample_diction.json" in a text editor, or copy and paste its contents into http://www.jsoneditoronline.org/ to see what the nested data in this dictionary will be structured like.)

file_rev = open("sample_diction.json", "r")
file_read = file_rev.read() 
sample_photo_rep = json.loads(file_read)
file_rev.close()


## [PROBLEM 2] -- Code setup (get and paste in your Flickr API key)
print("\n***** PROBLEM 2 *****\n")
## Set up code so you, too, can access the Flickr API. (You have probably already done this in class, but it is necessary to complete this assignment.)

## You will need a Yahoo!/Hotmail account in order to sign in to Flickr. You need such an account in order to complete this assignment. But it does not need to be a "real" account that you will use for anything else besides this, and you do not need to use your real name for it if you do not want to.
## Follow the instructions in the Flickr chapter to get a key for the Flickr API so that you can get data from Flickr.
## There are no tests for this problem; your problem set will not work if you do not complete it.

FLICKR_KEY = "4b339d1bc1218d76872989246a08a9e2" # paste your flickr API key here, between those quotation marks, such that the variable flickr_key will contain a string (your flickr key!).

## DO NOT CHANGE ANYTHING ELSE ABOUT THE CODE IN THIS PROBLEM, BELOW THIS COMMENT.
## Normally you should not share API keys with others. But if you include your key in your problem set submission file here, we will not use it for anything nefarious, and we will show you how you can regenerate it later.
if FLICKR_KEY == "" or not FLICKR_KEY:
    FLICKR_KEY = input("Enter your flickr API key now, or paste it in the assignment .py file to avoid this prompt in the future. (Do NOT include quotes around it when you type it in to the command prompt!) \n>>")


## [PROBLEM 3] - Photo data investigation
print("\n***** PROBLEM 3 *****\n")

## The sample_photo_rep variable you defined in Problem 1 should contain a complex Python object. That represents data about a single photo on Flickr.

## Write code to access the nested data inside sample_flickr_obj to create a list of all of the tags of that photo. Save the list of tags in a variable called sample_tags_list.

## You will need to do a bunch of nested data investigation and nested iteration in order to complete this. Copying the contents of the sample_diction.json file into jsoneditoronline.org may help. Remember, go slowly and step-by-step; understand, then extract, then understand the next bit...

## When you have completed this problem, the tags list in sample_tags_list should look like this: [u'nature', u'mist', u'mountain']
## HINT: Check out the '_content' keys' values deep inside the nested dictionary... (Don't use the values of the "raw" keys.)
## There are tests for this problem.
 
sample_tags_list = []
for tag in sample_photo_rep["photo"]["tags"]["tag"]:
    sample_tags_list.append(tag['_content'])

## [PROBLEM 4] - More Flickr data investigation
print("\n***** PROBLEM 4 *****\n")

## We have also provided a file called sample_flickr_response.json. This file contains data that has been retrieved from the Flickr API in response to a request for 50 photos tagged with the word "river", but the data from the API has been altered slightly so that it is properly formatted in a JSON way (as discussed in class). Note that this is DIFFERENT data than the data from Problem 3 -- this is data that represents a search for photos. The data in problem 3 represented a request for info about ONE photo only.

## Write code to open that sample_flickr_response.json file and load the data inside that file into a variable called search_result_diction. Remember to close any file you open once you're done with it!

file_flickr = open("sample_flickr_response.json", "r")
file_flickr_read = file_flickr.read() 
search_result_diction = json.loads(file_flickr_read)
file_flickr.close()


## After you have done that, the variable search_result_diction should now contain a very complex dictionary representing information about a bunch of photos that are tagged "river". Each photo has an id.

## Write code to create a list of all of the photo ids from each photo that the search_result_diction data represents, and save that list in a variable called sample_photo_ids.

## There are tests for this problem.

sample_photo_ids = []
for ids in search_result_diction['photos']['photo']:
    sample_photo_ids.append(ids['id'])
print(sample_photo_ids)


## [PROBLEM 5] - Set up the pattern for caching data
print("\n***** PROBLEM 5 *****\n")

## This problem set will now combine some of the work you've done already with work a lot like what you did in Problem Set 6 -- but this time you will be caching your data, so your code will only make a request to the internet when you don't already have the data you need.

## Translate the following English into code, as described in the REST APIs & Caching document and in class, in order to set up a pattern so you can cache the data you get in this problem set.

## We suggest keeping the comments and writing the code translations above OR below OR to the left of each of them...

## This code will work in conjunction with code you write later, so it can't all be tested until you've completed the whole problem set. There are tests for later problems that rely upon this working correctly.

CACHE_FNAME = "pset7_cached_data.json" # PROVIDED FOR YOU, DO NOT CHANGE

# Begin a try/except statement. Inside the try block:
## Open a file with the CACHE_FNAME file name.
## Read the file into one big string.
## Load the string into a Python object, saved in a variable called CACHE_DICTION.
# Begin the except clause of the try/except statement:
## Create a variable called CACHE_DICTION and give it the value of an empty dictionary.

# (In total, this should be five or six lines of code. It can be a 1:1 comment:line of code relationship.)

try:
    f = open(CACHE_FNAME, 'r')
    fstr = f.read()
    CACHE_DICTION = json.loads(f)
except:
    CACHE_DICTION = {}


## [PROBLEM 6]
print("\n***** PROBLEM 6 *****\n")

### Utility function definition provided for your use here (do not change):
## Function to create a unique representation of each request without private data like API keys
def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)



## DEFINE A FUNCTION called get_flickr_data, which accepts 2 inputs:
## - a REQUIRED parameter: any string representing a tag to search for on Flickr (e.g. if you wanted to search for data on photos tagged with "mountains", you would pass in "mountains" for this parameter)
## - an OPTIONAL parameter whose default value is 50 (representing how many photos you want in your response data)

## The RETURN VALUE of the function should be a Python dictionary representing a bunch of search data from the Flickr Photos Search API.

## The following is an extended description of what the function you're defining in this problem should do.

## FUNCTION BEHAVIOR:
## This function should use the provided utility function called params_unique_combination to get a unique identifier for this particular data request to the Flickr API (searching for this tag phrase and this number of photos).

## The function should check whether or not the unique identifier for each request exists in your cache data, and if it does, should access the Python object that represents that data from the CACHE_DICTION.

## BUT if there is no such data in your cache, the function should make a request to the Flickr Photos Search API for photos tagged with your input string.
## Your request should use the tag_mode "all" so that if your query string represents multiple tags, it will search for photos with ALL of those tags. (Check out the examples from class!)

## It should then modify the string that is returned from the Flickr API so that it is properly JSON formatted. (You want a version of the string without the first 14 characters and without the very last character -- see the textbook example!)

## And then, load that modified string into a Python object. The function should add the new dictionary of data to your cache dictionary, associated with the unique identifier key, and should write ALL the data in the cache dictionary, now with an additional key-value pair, to your cache file!

## RETURN VALUE: The get_flickr_data function's return value, regardless of whether it got data from the cache or made a new request and saved data to the cache, should be a big dictionary representing a bunch of search data from the Flickr Photos Search API.

## API docs here: flickr.com/services/api/flickr.photos.search.html

## The base URL for the Flickr API is: "https://api.flickr.com/services/rest/"

## Recall that all Flickr API endpoints have the same base url, but different values of the "method" parameter! For the Photos Search API, that value should be "flickr.photos.search"

## Recall also that you have a variable FLICKR_KEY in this file which you could reuse in this function, since it is intended as a global variable for your whole program.


## The examples from class and from the REST APIs & Caching document example, and talking through them carefully, will be VERY helpful here. The work you did in Problem Set 6 may also be a helpful reference, though remember that the functions you wrote in PS6 did NOT cache any data, and the flickr API requires more query parameters than the FAA API does!

## There are tests for this problem, and the autograde script will run an additional test (invoking the function with new input to see if the caching works correctly!).

def get_flickr_data(string, param_d = 50):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["tags"] = string
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = param_d
    params_diction["format"] = "json"
    unique_ident = params_unique_combination(baseurl, params_diction)
    if unique_ident in CACHE_DICTION:
        print("Getting data from cache...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        flickr_resp = requests.get(baseurl, params_diction)
        flickr_text = flickr_resp.text
        flickr_text_fixed = flickr_text[14:-1]
        CACHE_DICTION[unique_ident] = json.loads(flickr_text_fixed)
        flickr_file = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(flickr_file)
        fw.close()
        return CACHE_DICTION[unique_ident]

rhymes_with_spring = get_flickr_data("spring")
rhymes_with_winter = get_flickr_data("winter")
print(rhymes_with_spring)
print(rhymes_with_winter)

## [PROBLEM 7]
print("\n***** PROBLEM 7 *****\n")

## Make an invocation to your get_flickr_data function with the input "mountains" (use the default second parameter). Save the result in the variable flickr_mountains_result. There are tests for this problem.

## (Whether or not this works is also an additional test for your Problem 6, since this won't work without the get_flickr_data function you defined above.)

flickr_mountains_result = get_flickr_data("mountains")
print(flickr_mountains_result)

## [PROBLEM 8]
print("\n***** PROBLEM 8 *****\n")

## Remember the code you wrote in Problem 4? Refer to that code, and now, write code to get a list of all of the photo IDs in the data that's in your flickr_mountains_result variable. Save that list in a variable called photo_ids. There are tests for this problem.

photo_ids = []
for photo in flickr_mountains_result['photos']['photo']:
    photo_ids.append(photo['id'])
print(photo_ids)


## [CHALLENGE]
print("*** CHALLENGE ***\n")

## Continuing from this, you can write code to build a tag recommender: given a search for a certain tag on Flickr, your code could tell you 5 other tags which most frequently co-occur with the tag you searched for.

## We will be looking at code to do this in class in the future, but if you're looking for a challenge, try writing it now! (We will not offer extra credit for this at this point, but it's a good idea to try it out, or if not, try thinking about it: what would your plan be to do this, in English?)

## Hint: It will be useful to make requests to the Photo Info endpoint of the Flickr API
## Hint 2: It will be useful to make a dictionary of all of the tags... and to do a bit of sorting.

## MAKE SURE that if you write the code inside this file, it does not keep your file from running, though!
## We have NOT provided tests for this yet.

def get_photo_info(photo_id):
    baseurl = "https://api.flickr.com/services/rest/"
    params_d['method'] = "flicksearflickr.photos.getInfoch"
    params_d['api_key'] = FLICKR_KEY
    params_d['id'] = photo_id

    resp = requests.get(baseurl, params = params_d)
    resp_d = json.loads(resp.text[14:-1])
    return resp_d


print("*************\n")
##### Code for running tests is below this line. Don't change any code below this line!######

class Problem1(unittest.TestCase):
    def test_sample_photo_rep(self):
        self.assertEqual(sample_photo_rep,{u'photo': {u'people': {u'haspeople': 0}, u'dateuploaded': u'1467709435', u'owner': {u'username': u'Ansel Adams', u'realname': u'', u'path_alias': None, u'iconserver': u'7332', u'nsid': u'48093195@N03', u'location': u'', u'iconfarm': 8}, u'publiceditability': {u'canaddmeta': 1, u'cancomment': 1}, u'id': u'27820301400', u'title': {u'_content': u'Photo1'}, u'media': u'photo', u'tags': {u'tag': [{u'machine_tag': False, u'_content': u'nature', u'author': u'48093195@N03', u'raw': u'Nature', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-5470'}, {u'machine_tag': False, u'_content': u'mist', u'author': u'48093195@N03', u'raw': u'Mist', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-852'}, {u'machine_tag': False, u'_content': u'mountain', u'author': u'48093195@N03', u'raw': u'Mountain', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-1695'}]}, u'comments': {u'_content': u'0'}, u'secret': u'c86034becf', u'usage': {u'canblog': 0, u'canshare': 1, u'candownload': 0, u'canprint': 0}, u'description': {u'_content': u''}, u'isfavorite': 0, u'views': u'4', u'farm': 8, u'visibility': {u'isfriend': 0, u'isfamily': 0, u'ispublic': 1}, u'rotation': 0, u'dates': {u'taken': u'2016-07-05 11:03:52', u'takenunknown': u'1', u'posted': u'1467709435', u'lastupdate': u'1467709679', u'takengranularity': 0}, u'license': u'0', u'notes': {u'note': []}, u'server': u'7499', u'safety_level': u'0', u'urls': {u'url': [{u'type': u'photopage', u'_content': u'https://www.flickr.com/photos/48093195@N03/27820301400/'}]}, u'editability': {u'canaddmeta': 0, u'cancomment': 0}}, u'stat': u'ok'})

class Problem3(unittest.TestCase):
    def test_sample_tags_list(self):
        self.assertEqual(sample_tags_list,[u'nature', u'mist', u'mountain'])

class Problem4(unittest.TestCase):
    def test_search_result_diction(self):
        self.assertEqual(type(search_result_diction),type({}), "Testing that search_result_diction is a dictiionary")
    def test_search_result_diction2(self):
        self.assertTrue("photos" in search_result_diction, "Testing that the photos key is in the loaded flickr response, as it should be")
    def test_sample_photo_ids(self):
        self.assertEqual(type(sample_photo_ids),type([]),"Testing that sample_photo_ids is a list")
    def test_sample_photo_ids2(self):
        self.assertTrue(sample_photo_ids[2] != sample_photo_ids[23], "Testng that not all the sample photo ids are the same id")
    def test_sample_photo_ids3(self):
        self.assertEqual(len(sample_photo_ids),50,"Testing there are 50 photo ids in the sample_photo_ids list")

class Problem5(unittest.TestCase):
    def test_cache_diction_existence(self):
        self.assertEqual(type(CACHE_DICTION),type({}),"Testing that CACHE_DICTION is a dictionary")

class Problem6(unittest.TestCase):
    def test_get_flickr_data1(self):
        self.assertEqual(sorted(list(get_flickr_data("alps").keys())),sorted([u'photos', u'stat']), "Testing the keys of the return value of get_flickr_data")
    def test_get_flickr_data2(self):
        self.assertEqual(sorted(list(get_flickr_data("alps")["photos"]["photo"][49].keys())),sorted([u'isfamily', u'title', u'farm', u'ispublic', u'server', u'isfriend', u'secret', u'owner', u'id']), "Testing the keys of one of the photos inside the get_flickr_data response")
    def test_get_flickr_data_resp_type(self):
        self.assertIsInstance(get_flickr_data("alps")["photos"]["photo"][49],dict, "Testing that the value of one of the photos in the function's return value is a dictionary")
    def test_get_all_diff_photos(self):
        self.assertTrue(get_flickr_data("sunset")["photos"]["photo"][30]["id"] != get_flickr_data("sunset")["photos"]["photo"][15]["id"], "Testing that the list of photos is not a composed list of all the same photo")
    def test_default_num_photos(self):
        self.assertEqual(len(get_flickr_data("sunset")["photos"]["photo"]),50,"Testing that the default num_photos response has 50 photos")
    def test_cache_in_function(self):
        testfile = open("pset7_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("mountains" in testfilestr,"Testing that the mountains request was cached")
    def test_cache_in_function2(self):
        testfile = open("pset7_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("per_page-50" in testfilestr, "Testing (in part) that the params_unique_combination was used properly in the cache setup")
    def test_cache_in_function3(self):
        get_flickr_data("summer 2013",112) # specific params
        testfile = open("pset7_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("https://api.flickr.com/services/rest/format-json_method-flickr.photos.search_per_page-112_tag_mode-all_tags-summer 2013" in testfilestr, "Testing that params and unique identifer setup are correct in get_flickr_data function")

class Problem7(unittest.TestCase):
    def test_flickr_mountains_result_keys(self):
        self.assertEqual(sorted(list(flickr_mountains_result.keys())),sorted([u'photos', u'stat']),"Testing the keys of the value of flickr_mountains_result, which should be a dictionary")
    def test_fmr_res_type(self):
        self.assertEqual(type(flickr_mountains_result),type({}),"Testing that the type of flickr_mountains_result is a dictionary")
    def test_num_photos_flickr_mountains_res(self):
        self.assertEqual(len(flickr_mountains_result["photos"]["photo"]),50,"Testing that there are 50 photos in flickr_mountains_result")

class Problem8(unittest.TestCase):
    def test_photo_ids_len(self):
        self.assertEqual(len(photo_ids),50,"Testing that there are 50 photo ids")
    def test_diff_photo_ids(self):
        self.assertTrue(photo_ids[0] != photo_ids[40], "Testing that the photo ids are different, not just 50 of the same one (check out your nested iteration, maybe)")
    def test_ids_in_cache(self):
        testfile = open("pset7_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue(photo_ids[4] in testfilestr,"Testing that one of the ids, like the other response data, is inside the cache file")

if __name__ == "__main__":
    unittest.main(verbosity=2)
