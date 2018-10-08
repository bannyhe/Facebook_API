import json
import unittest
import random


## [PROBLEM 1]
print("\n\n***** Problem 1 *****")

## We have provided the definition of a class Photo. Given this class definition, write one line of code below it to create an instance of the class Photo whose title is 'Photo1', whose artist is 'Ansel Adams', and whose tags are the list ['river','yosemite']. Save the instance in a variable single_photo.

class Photo(object):
    def __init__(self, title_str, photo_by, tags_list):
        self.title = title_str
        self.artist = photo_by
        self.tags = tags_list

    def __str__(self):
        return "{} by {}".format(self.title,self.artist)

## Write your line of code here:
single_photo = Photo('Photo1', 'Ansel Adams', ['river','yosemite'])

## You could uncomment this line to check out the result:
print(single_photo)

## [PROBLEM 2]
print ("\n\n***** Problem 2 *****")

## Now we have provided a list of tuples in the variable tups_list, each tuple of which contains 2 strings and a list. Write code to create a list of Photo instances, where each Photo instance uses the data from each tuple in the tups_list. and save that list in a variable photo_insts.

## (HINT: tuple unpacking can be very useful here, though you do not need it. You will, of course, need to use the accumulator pattern and some of the same syntax you used in Problem 1!)

tups_list = [("Portrait 2","Gordon Parks",["chicago", "society"]),("Children in School","Dorothea Lange",["children","school","1930s"]),("Airplanes","Margaret Bourke-White",["war","sky","landscape"])]

## Write your code here:
photo_insts = []
for i in tups_list:
    photo_tuple = Photo(i[0], i[1], i[2])
    photo_insts.append(photo_tuple)

# You can uncomment this code to test out whether some of it works:
for i in photo_insts:
    print(i)

## [PROBLEM 3]
print ("\n\n***** Problem 3 *****")
## We've provided the beginning of a definition of a class Student.

class Student(object):
    def __init__(self, name, years_at_umich=1):
        self.name = name
        self.years_UM = years_at_umich
        self.bonus_points = random.randrange(1000)
        self.programs_written = 0

    def shout(self, phrase_to_shout):
        print(phrase_to_shout)  # remember, print is for ppl!

    def year_at_umich(self):
        return self.years_UM

    ## Define a __str__ method for this class here so that when an instance of class Student is printed, it prints something of the format: My name is ___. I've been at UMich for __ years and I've written __ programs.
    # HINT: String formatting will be useful here!
    # Note that it is OK, and expected in the tests, to have single numbers still have plural language here, e.g. "1 programs" or "1 years".

    def __str__(self):
        return "My name is {}. I've been at UMich for {} years and I've written {} programs.".format(self.name, self.years_UM, self.programs_written)

    ## Define a method write_programs for this class which takes an optional parameter called progs, whose default value is 1. When the method is invoked, the value of progs should be added to the programs_written instance variable.
    # HINT: This only really needs 2 lines of code.

    def write_programs(self, progs = 1):
        self.programs_written += progs

#### Done w/ student class definition ####


#### Sample code using the Student class definition, which will all work once this problem is completed, is below. Uncomment it to try it out:

# s = Student("Lyra")
# print (s) # Should print: My name is Lyra. I've been at UMich for 1 years and I've written 0 programs.
# s.shout("I'm doing awesome on this problem set") # Should result in this printing: I'm doing awesome on this problem set
# print (s.year_at_umich()) # Should print 1
# s.write_programs()
# print(s.programs_written) # Should print 1
# s.write_programs(6)
# print(s.programs_written) # Should print 7
# print(s) # Should print: My name is Lyra. I've been at UMich for 1 years and I've written 7 programs.
# s.write_programs(progs=4)
# print(s) # Should print: My name is Lyra. I've been at UMich for 1 years and I've written 11 programs.

#### END SAMPLE CODE ####


## [PROBLEM 4]
print ("\n\n***** Problem 4 *****")

## Define a class Apple. It should require 4 constructor inputs: the color (color), the name of the apple variety (variety_name), the size (size), and the place it grew in (place_grown), in that order. Those inputs should be assigned to the following instance variables: color, variety, size, grown_in

## It should have a method for_pies. The for_pies method should return the boolean value True if the variety is "Granny Smith", "Braeburn", or "Golden Delicious", and if the variety value for that Apple instance is anything else, the method should return the boolean value False.

## This class Apple should also have a string method, which should return a string of the following format:
## A <SIZE> <COLOR> apple of the <VARIETY> variety, grown in <PLACE GROWN IN>.

## For example, if the following code appeared after your class definition:
# ap = Apple("red","Braeburn","medium","WA")
# print(ap) # Should print: A medium red apple of the Braeburn variety, grown in WA.

## Write your class definition here:
class Apple(object):
    def __init__(self, color, variety_name, size, place_grown):
        self.color = color
        self.variety = variety_name
        self.size = size
        self.grown_in = place_grown

    def for_pies(self):
        lst = ["Granny Smith", "Braeburn", "Golden Delicious"]
        if self.variety in lst:
            return True
        else:
            return False

    def __str__(self):
        return "A {} {} apple of the {} variety, grown in {}.".format(self.size, self.color, self.variety, self.grown_in)


## You can uncomment the following code to test if it works. (There are also tests for this problem, but this may be easier to see.) Feel free to write your own test code here as well -- but make sure that you do not keep the code file from running so that you can see the test output!

ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
print(ap2) # Should print: A large green apple of the Granny Smith variety, grown in Sydney, Australia.
print(ap2.for_pies()) # should print True

ap3 = Apple("red","Mystery", "small","Michigan")
print(ap3.for_pies()) # should print False
print(ap3) # should print: A small red apple of the Mystery variety, grown in Michigan.



## [PROBLEM 5]
print ("\n\n***** Problem 5 *****")

## Fill in the rest of the constructor method of the class Car so that the following code will run successfully. DO NOT change any of the rest of the code -- you'll have to look at the rest of it to figure out how to properly complete the constructor (the __init__ method).

class Car(object):
    def __init__(self, color, make, miles_per_gallon):
        self.color = color
        self.make = make
        self.mpg = miles_per_gallon

    def __str__(self):
        return "{} {} car with {} MPG".format(self.color,self.make, self.mpg)

    def miles_can_go(self, gallons_in_tank):
        return float(gallons_in_tank)*self.mpg

## Uncomment the following to try it out (will generate error if you try to run it before doing Problem 5)
# c = Car("grey","SUV",20)
# print (c.miles_can_go(4)) # Should print: 80.0
# print (c) # Should print: grey SUV car with 20 MPG

# another_car = Car("rainbow","convertible", 28)
# print(another_car) # Should print: rainbow convertible car with 28 MPG
# print(another_car.miles_can_go(10)) # Should print: 280.0

## [PROBLEM 6]
print ("\n\n***** Problem 6 *****")

## We've provided a .json file with nested data that represents ONE tweet from Twitter: nested_data_tweet.json.

## Investigate that data a little bit, using Python code and/or jsoneditoronline.org.

## The following code, which we've provided here, extracts the data from that file into a Python dictionary, in a variable called tweet_diction1, which you can investigate:
f = open("nested_data_tweet.json",'r')
file_contents = f.read()
f.close()
tweet_diction1 = json.loads(file_contents)

## Define a class Tweet whose input to the constructor should always be 1 dictionary that represents 1 tweet, just like the dictionary assigned to tweet_diction1.

## The constructor of class Tweet should create 2 instance variables:
### text (which should contain the text of the tweet)
### user (which should contain the screen name of the person who posted the tweet)

## And the class Tweet should also have 1 additional method called num_words_text, which does not take any additional input, and returns the number of WORDS in the tweet's text.

## Write your class definition here:

class Tweet(object):
    def __init__(self, tweet_diction1):
        self.text = tweet_diction1['text']
        self.user = tweet_diction1['user']['screen_name']

    def num_words_text(self):
        num = 0
        for word in self.text.split():
            num += 1
        return num


##### TESTS BELOW THIS LINE; DO NOT CHANGE CODE BELOW THIS LINE #####
print ("\n\n**********") ### DO NOT CHANGE OR REMOVE THIS PRINT LINE! IT IS VERY IMPORTANT FOR GRADING

class Problem1(unittest.TestCase):
    def test_single_photo1(self):
        self.assertEqual(type(single_photo),type(Photo("Photo2","Photo Student",["multiple","tags"])))
    def test_single_photo2(self):
        self.assertEqual(single_photo.title, "Photo1")
    def test_single_photo3(self):
        self.assertEqual(single_photo.artist, "Ansel Adams")
    def test_single_photo4(self):
        self.assertEqual(single_photo.tags, ["river","yosemite"])

class Problem2(unittest.TestCase):
    def test_photo_insts1(self):
        self.assertEqual(type(photo_insts),type([]))
    def test_photo_insts2(self):
        self.assertEqual(type(photo_insts[0]),type(Photo("Photo2","Photo Student",["multiple","tags"])))
    def test_photo_insts3(self):
        self.assertEqual([x.title for x in photo_insts],["Portrait 2", "Children in School", "Airplanes"])
    def test_photo_insts4(self):
        self.assertEqual([x.artist for x in photo_insts],["Gordon Parks","Dorothea Lange","Margaret Bourke-White"])
    def test_photo_insts5(self):
        self.assertEqual([x.tags for x in photo_insts],[["chicago","society"],["children", "school","1930s"],["war","sky","landscape"]])

class Problem3(unittest.TestCase):
    def test_student1(self):
        student1 = Student("Lyra")
        self.assertEqual(student1.__str__(),"My name is Lyra. I've been at UMich for 1 years and I've written 0 programs.")
    def test_student2(self):
        student2 = Student("Aisha")
        student2.write_programs()
        self.assertEqual(student2.__str__(),"My name is Aisha. I've been at UMich for 1 years and I've written 1 programs.")
    def test_student3(self):
        student3 = Student("Ali",3)
        student3.write_programs(4)
        self.assertEqual(student3.__str__(),"My name is Ali. I've been at UMich for 3 years and I've written 4 programs.")
    def test_student4(self):
        student4 = Student("Aja")
        student4.write_programs(12)
        self.assertEqual(student4.programs_written, 12)
        student4.write_programs()
        self.assertEqual(student4.programs_written,13)

class Problem4(unittest.TestCase):
    def test_apple1(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.color,"green")
    def test_apple2(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.variety,"Granny Smith")
    def test_apple3(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.size, "large")
    def test_apple4(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.grown_in, "Sydney, Australia")
    def test_apple5(self):
        ap2 = Apple("green","Granny Smith","large","Sydney, Australia")
        self.assertEqual(ap2.for_pies(),True)
    def test_apple6(self):
        ap2 = Apple("red","Red Delicious","large","WA")
        self.assertEqual(ap2.for_pies(),False)
    def test_apple7(self):
        ap2 = Apple("red","Braeburn","large","WA")
        self.assertEqual(ap2.for_pies(),True)
    def test_apple8(self):
        ap2 = Apple("yellow","Golden Delicious","large","WA")
        self.assertEqual(ap2.for_pies(),True)
    def test_apple9(self):
        ap2 = Apple("yellow","Golden Delicious","large","the United States")
        self.assertEqual(ap2.__str__(), "A large yellow apple of the Golden Delicious variety, grown in the United States.")
    def test_apple10(self):
        ap2 = Apple("red","Braeburn","medium","WA")
        self.assertEqual(ap2.__str__(),"A medium red apple of the Braeburn variety, grown in WA.")

class Problem5(unittest.TestCase):
    def test_car1(self):
        c = Car("grey","SUV",20)
        self.assertEqual(c.__str__(),"grey SUV car with 20 MPG")
    def test_car2(self):
        c = Car("grey","SUV",20)
        self.assertEqual(c.miles_can_go(4), 80.0)
    def test_car3(self):
        c = Car("Blue!!!","convertible",2)
        self.assertEqual(c.__str__(),"Blue!!! convertible car with 2 MPG")
    def test_car4(self):
        c = Car("Blue!!!","convertible",2)
        self.assertEqual(c.miles_can_go(4),8.0)
    def test_car5(self):
        c = Car("Silver","Nissan",26)
        self.assertEqual(c.color, "Silver")
    def test_car6(self):
        c = Car("Silver","Nissan",26)
        self.assertEqual(c.make,"Nissan")
    def test_car7(self):
        c = Car("Silver","Nissan",26)
        self.assertEqual(c.mpg,26)

class Problem6(unittest.TestCase):
    def setUp(self):
        f = open("nested_data_tweet.json",'r')
        self.file_contents = f.read()
        f.close()
        self.tweet_diction = json.loads(self.file_contents)
        self.tweet = Tweet(self.tweet_diction)
    def test_class_tweet1(self):
        self.tweet2 = Tweet(self.tweet_diction)
        self.assertIsInstance(self.tweet2,Tweet)
    def test_class_tweet2(self):
        self.assertEqual(self.tweet.text, "U-M's oldest student group, @UMMGC organized in 1859 and launched a treasured campus tradition. #UMich200 https://t.co/q0koMuRwNo")
    def test_class_tweet3(self):
        self.assertEqual(self.tweet.user, "UMich")
    def test_class_tweet4(self):
        self.assertEqual(self.tweet.num_words_text(),16)


if __name__ == "__main__":
    unittest.main(verbosity=2)
