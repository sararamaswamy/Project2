import unittest
import re

## SI 206 - W17 - HW3
## COMMENT WITH: Sara Ramaswamy
## Your section day/time: Thursday 6-7 PM
## Any names of people you worked with on this assignment: 

#####################


## PART 1: 300 points

## Use regular expressions to define a function called parse_counted_words which should accept a string, find strings of the form: <count> <word>  e.g. 101 Dalmations, inside it, and should return either the LAST correctly matching number-word combo in the string as a tuple, e.g. ('13', "pineapples"), if there are any such sub-strings, or None, if there are not.
## The number in the <count> should be one or more digits only. The word should be made up of an optional at the beginning non-alphabetic character followed by any number (1 or more) of alphabetic characters, upper or lower case.
## HINT:  \b matches the beginning or end of a word
## HINT:  you can use the Python re .findall method to get multiple matches in a string
#parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') should return ('1', 'papaya')
# parse_counted_words('101 dalmations!') should return ('101', 'dalmations') ...

## Write code to define your parse_counted_words function here.

def parse_counted_words(lin):

    y = re.findall(r'(\d+) (\D?[a-zA-Z]+)\b', lin) ## r means raw data. if you don't have r, backslash means data corrector 
    ## look for 1 or more digits then space then look for 0 OR 1 non alphabetic characters then alphabetic characters of any length ONLY NOT alphanumeric!! then match the end of a word
    if len(y) == 0:
        return None
    ## if everything is normal, continues executing 
    desired_tuple = ""
    for each_tuple in y:
        desired_tuple = each_tuple
        
    return desired_tuple



    # y = re.findall('(\d*) (\D*)[^\w]', lin)
    # desired_tuple = {}
    # for each_tuple in y:
    #     desired_tuple = each_tuple
    # return desired_tuple


        # extraction_bit = re.findall([0-9], x)
        # return extraction_bit
        # x =

        # desired_value = ""
        # for match in re.search((\d) (\w*), lin):
        #     desired_value = match

        # return(desired_value)
        # extract = re.findall((.*), x)
        # print(extract)

##
# Testing print statement: print(parse_counted_words("5 watermelons, 13 pineapples, and 1 papaya."))


	#for loop to loop through string 
	 ## if (string of one or more digits) space( nonalphabetic character) + any number of alphabetic characters statement 
	 	## return the tuple
	 ## else 
	 ##return None

	 ##notes: consider reading the string backwards to look for first instance of the match (will this work?)
	 ## create accumulator outside for loop, look for these matches, and if it works, increment the accumulator, once there are no more, return the match (will be the last match)


## PART 2: 200 points

## We have provided a text file computer_paths.txt. It's not incredibly long -- you can scan through it, but do NOT hard code your answers! Each line contains 1 filesystem path.

## (a) Write Python code to determine how many of these paths identify FILES, not directories. Save that number in the variable file_paths_num.
## acumulator, return the count() value of that accumulator
##files  ends in a alphabetical character, also have slash followed by alphabetical 


file = open('computer_paths.txt') ## Done
file_paths_num = 0 
for line in file:
    line = line.rstrip()
    y = re.findall(r'[.](\w+)', line) ## This is a correct way to parse it
    if len(y) > 0:
        file_paths_num = file_paths_num +1

# file_paths_num = len(y) ## 16


## (b) Write Python code to determine how many of these paths are FULL paths, not relative paths. Save that number in the variable full_paths_num.
## full path accumulator count()
file2 = open('computer_paths.txt') ## Returns 0
full_paths_num = 0
for line in file2:
    line = line.rstrip()
    z = re.findall(r'(^~?/)', line)
    if len(z) > 0:
        full_paths_num = full_paths_num +1 ## 16

# [\W?][\W+].*)

## (c) Write Python code to determine how many of these paths describe a Python file saved inside a folder called SI206. Save that number in the variable python_course_paths.
##see if inside folder, accumualator, return count
## must be a file format AFTER SI206 APPEARS
## Two Capital letters then three numbers then slash then text then file name (ends in two lowercase letters because of .py at the end 
file3 = open('computer_paths.txt') ## Done
python_course_paths= 0
for line in file3:
    line = line.rstrip()
    w = re.findall(r'[A-Z][A-Z][\d][\d][\d]/.+[.][a-z][a-z]\b', line)
    if len(w) > 0:
        python_course_paths = python_course_paths + 1 ##3

## (d) Write Python code to determine how many of these paths describe a Microsoft file (a file that EITHER ends with .docx OR .xlsx, but nothing else counts) where the file name ends in a digit. Save that total in the variable microsoft_files_num.

## see if it ends in alphabetical characters with periods with number of letters followed by a number followed by a period followed by an x, accumulator, return count 
## microsoft file AND file name ends in a digit!
file4 = open('computer_paths.txt') ##Done
microsoft_files_num = 0 
for line in file4:
    line = line.rstrip()
    x = re.findall(r'([\d][.]\w+[x])', line)
    if len(x) > 0:
        microsoft_files_num = microsoft_files_num + 1 ##3 




## We have provided unit tests in this file. To earn the full 500 points, you'll need to pass all of the tests and will need to have followed the instructions.
## Each class of the tests represents one "part" of the homework, and the points for each part are divided approx. equally between each of the tests.

####### UNIT TESTING BELOW; DO NOT CHANGE ANY TESTING CODE #######

class Part1_HW3(unittest.TestCase):
    def test_pcw_1(self):
        self.assertEqual(parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.'),('1','papaya'))
    def test_pcw_2(self):
        self.assertEqual(parse_counted_words('101 dalmations!'),('101','dalmations'))
    def test_pcw_3(self):
        self.assertEqual(parse_counted_words('snow white and the 7 #littledwarves'),('7','#littledwarves'))
    def test_pcw_4(self):
        self.assertEqual(parse_counted_words('goldilocks and the 3 little pigs'),('3','little'))
    def test_pcw_5(self): 
        self.assertEqual(parse_counted_words('678 1234567 890  '),None)
    def test_pcw_6(self):
        self.assertEqual(parse_counted_words("hellllo 5000"), None)
    def test_pcw_7(self):
        self.assertEqual(parse_counted_words("!!!! 6"), None)
    def test_pcw_8(self):
        self.assertEqual(parse_counted_words("!!!!! 72 and 76 calendars"),('76',"calendars"))

class Part2_HW3(unittest.TestCase):
    def test_cpaths_1(self):
        self.assertEqual(file_paths_num,16)
    def test_cpaths_2(self):
        self.assertEqual(full_paths_num,16)
    def test_cpaths_3(self):
        self.assertEqual(python_course_paths,3)
    def test_cpaths_4(self):
        self.assertEqual(microsoft_files_num,3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

