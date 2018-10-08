SI 506 FINAL PROJECT README


* In ~2-3 sentences, what does your project do?

If you fill out your_app_data.py with your Facebook information and run the program, the project will find the most common word in the most recent 25 Facebook posts of NBA, create a CSV file of songs from a search on iTunes of the most common word.


* What files (by name) are included in your submission? List them all! MAKE SURE YOU INCLUDE EVERY SINGLE FILE YOUR PROGRAM NEEDS TO RUN, as well as a sample of its output file.

1. Files for program to run:
SI506_finalproject.py, your_app_data.py, stop_words.txt
2. Output files:
Cache file - SI506finalproject_cache.json
Output sample file - iTunes_songs.csv
3. Other:
README.txt

* What Python modules must be pip installed in order to run your submission? List them ALL (e.g. including requests, requests_oauthlib... anything someone running it will need!). Note that your project must run in Python 3.

import json
import string
import webbrowser
import unittest
import requests
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from your_app_data import APP_ID, APP_SECRET

* Explain SPECIFICALLY how to run your code. We should very easily know, after reading this:
    - What file to run (e.g. python SI506_finalproject.py). That's what we expect -- but tell us specifically, just in case.

	Run SI506_finalproject.py

    - Anything else (e.g. "There will be a prompt asking you to enter a word. You'll definitely get good data if you enter the word 'mountains', but you can try anything", or "You need to fill out secret_data.py with the Facebook key and secret" -- if you have to do something like this, you should include the FULL INSTRUCTIONS, just like we did. Not enough to say "just like PS9". Provide text or a link to tell someone exactly what to do to fill out a file they need to include.

    Once the file SI506_finalproject.py is running, a browser window will pop out showing a long url. Copy that url link provided in the browser page to the terminal, and press "enter".

    - Anything someone should know in order to understand what's happening in your program as it runs

    The following items will be printed in the terminal after SI506_finalproject.py runs successfully:
	1. The numbers and messages of requested 25 posts from the official Facebook page of NBA
	2. The most common word among the posts, and its time of appearance.
	3. “Getting cached data…” or “Making a request for new data”, which depends on whether the requested content is in cache file or not.
	4. The searching results of songs and their artists, collections and duration.

    - If your project requires secret data of YOUR OWN, and won't work with OURS (e.g. if you are analyzing data from a private group that is just yours and not ours), you must include the secret data we need in a file for us and explain that you are doing that. (We don't expect this to happen, but if it does, we still need to be able to run your program in order to grade it.)

    No. I requested data from Facebook public page.

* Where can we find all of the project technical requirements in your code? Fill in with the requirements list below.
-- NOTE: You should list (approximately) every single line on which you can find a requirement. If you have requirements written in different files, you should also specify which filename it is in! For example, ("Class definition: 26" -- if you begin a class definition on line 26 of your Python file)
It's ok to be off by a line or 2 but you do need to give us 100% of this information -- it makes grading much easier!

1. Get data from iTunes API & FaceBook API: 266 ; 125
2. Cache data from REST API: 193
3. Define class Post & Song: 16 ; 273
4. Create instance of class Post & class Song: 45 , 285 
5. Use instances of class Post & class Song: 72 ; 305
6. Perform sort with a key parameter: 298
7. Functions outside the class definition: 92, 206, 218
8. Create an output file: 317

REQUIREMENTS LIST:
* Get and cache data from 2 REST APIs (list the lines where the functions to get & cache data begin and where they are invoked):
    * If you relied upon FB data and did not cache it, say so here:
* Define at least 2 classes, each of which fulfill the listed requirements:
* Create at least 1 instance of each class:
* Invoke the methods of the classes on class instances:
* At least one sort with a key parameter:
* Define at least 2 functions outside a class (list the lines where function definitions begin):
* Invocations of functions you define:
* Create a readable file:
END REQUIREMENTS LIST

* Put any citations you need below. If you borrowed code from a 506 problem set directly, or from the textbook directly, note that. If you borrowed code from a friend/classmate or worked in depth with a friend/classmate, note that. If you borrowed code from someone else's examples on a website, note that.

I cited the code to create cache file (line 206-212) and function params_unique_combination from the textbook, section “More about Caching Response Content”.
The function makeFacebookRequest (line 92-111) is from problem set 9.
The stop_words.txt file is from https://www.ranks.nl/stopwords.

* Explain in a couple sentences what should happen as a RESULT of your code running: what CSV or text file will it create? What information does it contain? What should we expect from it in terms of how many lines, how many columns, which headers...?

It will create a CSV format file which contains the “Song Title”, “Artist Name”, “Song Duration”, “Album Name” of a couple of songs by searching the most common used word using iTunes API. The results was arranged by the length of song - from the longest to the shortest.
In the file, it has four columns with headers - “Title”, “Artist”, “Duration”, “Album”

* Make sure you include a SAMPLE version of the file this project outputs (this should be in your list of submitted files above!).

* Is there anything else we need to know or that you want us to know about your project? Include that here!
