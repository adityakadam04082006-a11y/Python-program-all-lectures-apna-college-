#1 ways to write string 
" "             #empty character means space isalso valid
"aditya"
'aditya'
'''aditya'''    #used in this ways because sometime sentence has the Apostrophe marks like "aditya's"


#2. string concatenations
str1 = "aditya"
str2 = "kadam"
final_str = str1 + str2

print(final_str)

#3.length of string (magic words ) like len(str)

str1 = "aditya"
len1 = len(str1)
print(len1)

str2 = "kadam"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(len(final_str))
print(final_str)


# 4.Indexing
#  ------(Each number is arranged in form of numbers from o to infinity )------
#  --In this it help to access the characters which we want but we can't modify means str[2] = 'A' not allowed--

str = "aditya kadam"
len = len(str)   # wrote just to overview characters length ,not necessary
print(str[2])

#or ,can write it in any way

str = "aditya kadam"
ch = str[3]
print(ch)


#5. Slicing
#--Accessing parts of string--

str = "aditya kadam"
print(str[2:6])

#or ,can write it in any way

str = "aditya kadam"
ch = str[3:6]
print(ch)

#or

str = "aditya kadam"
print(str[6:]) #we can use space when we want to go at last index

#.Negative index    -- this isused in slicing only 
str = 'aditya'
print(str[-6:-3])


#7. String FUNCTIONS ---

#I point
str = "I am student"
print(str.endswith("nt"))       # --str.endswith("__") - output will be true or false--

#II point
str = "i am student"
print(str.capitalize())         # -- str.capitalize() capitizes 1st char ---

#III Point
str = "I am student of zeal"
print(str.replace("zeal","COEP"))        # --str.replace("k","a") -- for character replacement

#IV Point
str = "I am student of zeal"
print(str.find("z"))                     #  -- str.find("z") -- used to finf character

#V Point 
str = "I am student of zeal"
print(str.count("a"))                    #  --str.count("a") -- used for counting 

#And there are many string functions to find write -- str.  by this you cant get many functions to view

