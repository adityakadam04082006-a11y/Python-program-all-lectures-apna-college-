# we can make our own dictionary and can save any word , list, tuples
# we can make key string, floating value ,boolean ,tuples means such a value like assigned one at a time so can't be changed
#generally string is only used in dictionary
# They are unordered ,mutable(changeable) and  don't allow duplicate keys


info = {
    "name" : "zeal college",
    "subjects": ["ptyhon","c","java"] ,
    "topics": ("maths","english"),
    "age" : 25,
    "is adult" : True ,
    13.55 : 98.6
} 
print(info)

#ex -
print(info["name"])

# ex it want to replace

dict = {
    "name" : "zeal college",
    "subjects": ["ptyhon","c","java"] ,
    "topics": ("maths","english"),
    "age" : 25,
    "is adult" : True ,
    13.55 : 98.6
} 

dict["name"] = "Aditya kadam"
print(dict)
 
 # can also add new key valve pair
 #ex -

dict["name"] = "Aditya"
dict["surnamename"] = "kadam"
print(dict)

#can also create null dictionary or empty dict and write in it -

null_dict = {}
null_dict ["name"] = "aditya kadam"
print(null_dict)

#nested dictionaries 

student = {
      "name" : "adi kadam",
      "subjects" : {
          "phy" : 55,
          "chem" : 65,
          "maths": 73,


      }
}

print(student["subjects"])            #can select for branches or nested --
print(student["subjects"]["chem"])    #can also write selected only      --  this all there are ex of how to write
print(student)                        #can write for whole               --
 
# Dictionary Methods

#1.mydict.key()  -- we can get all the keys by this
print(student.keys()) #we can also make it into list
print(list(student.keys()))



#2 .mydict.values()  -- returns all the values
print(student.values()) #we can also make it into list
print(list(student.values()))


#note we can store one type of datatype in other data types ,can store it in dictionary or dictionary 
#can be stored in list

#3 .mydict.items()  returns all(key,val) pairs as tuples
print(student.items()) 
print(list(student.items()))

pair = list(student.items())
print(pair[0])


#4 .mydict.get("key")  -- returnsthe key accordingto values
print(student.get("name"))
print(student["name"])

# print(student.get("name2"))  -- if this written then error will be printed
# print(student["name2"])      -- if this written then no error it will print none 

#5. mydict.update(newDict)   -- inserts the specified items to the dictionary

new_dict = {"name": "raj", }
student.update(new_dict)

print(student)


