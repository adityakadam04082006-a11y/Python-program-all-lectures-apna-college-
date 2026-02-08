# OOPS -- Objects Oriented programming

# To map with real world scenarios, we started using objects in code. 
# This is called Objects Oriented programming.

# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
# CLASS & OBJECTS in python

# class is a blueprint for creating objects.

# -----------------this is an overview-------------------
# creating class **

class students:
     name = "Aditya kadam"

# creating object(instance) **

s1 = students()
print(s1.name)

# ________________________________________________________________________________________________
# ________________________________________________________________________________________________
# _ _inti_ _ Function

# constructor **

# All classes have a function called _inti_(), which is always executrd when the class
# is being initiated.
# means this function works when its time for object creation.
# even ifyou have not created one init function the computer will always make it for you
# and execute .

# -----------------this is an overview-------------------
# This is a parameterized constructor--
# creating class **

class student:
     def __init__ (self,fullname):  #see here self means that object is calling itself 
          self.name = fullname   


# creating object(instance) **

s2 = student("aditya")  #--() see this parentheses are use for constructor
print(s2.name)

# __________________________________________________________________________________________________
# Note :-
# see here the argument self or instead of it you can write abcd anything ,but its compulsary
# to write that argumentotherwise you will have a error

# The self parameter is a reference to the current instance of the class, and is used to access
# variables that belongs to the class.
# see here the self.name means, inside object it is going to create new
# and like wise fullname here is the parameter in it.

# see this type of constructor is called ---default constructor---
# class student
#      def __init__ (self)
#       print("add database")
# 
# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
#   this is a overview--       class
#                               /\
#                              /  \
#                             /    \
#                          data     Methods
#                   (Attributes)    (functions)
#     means properies in a way       means a function written in class


# Class & Instance Attributes

#  Class Attribute (SHARED)
#  Meaning-----
# A class attribute is shared by ALL objects of the class
# Think: one common notice board 

# class Student:
#     college = "Zeal College"   # class attribute

#     def __init__(self, name):
#         self.name = name       # instance attribute

# Here:
# college belongs to the class
# Every student has the same college

# _______________________________________________________________________________________
# ________________________________________________________________________________________
# Instance Attribute (UNIQUE)
#  Meaning --
# Instance attributes belong to ONE object only
# Think: personal ID card 
# Example

# self.name = name

# name is different for every student
# Stored inside each object


# print(s1.name)   # Adi
# print(s2.name)   # Rahul

# -------------------------use------------------------------
# Why we NEED both--

# Use class attributes when:
# -value is same for all
# -constants
# -settings
# -shared data

# Use instance attributes when:
# -value differs per object
# -user data
# -state
# -identity

# class attr < object attr -- usuallyobject atr has more prefrence
# this is in case if you named the variable same 
    
# ______________________________________________________________________________________________________
# ______________________________________________________________________________________________________
# Methods --
# 
# methods are the function that belongs to the objects.
class Student1:              # class
    college_name= "zeal"     #class attribute
     
    def __init__(self,name):     #constructor
     self.name = name            #instance attributes
    def bye(self):
     print("bye friend,",self.name)

s3 = Student1("karan")
s3.bye()  

# _______________________________________________________________________________________________________
# _______________________________________________________________________________________________________
# Static Methods --

# methods  that don't uses the self parameter (works at class level)

class Student2:
    
    @staticmethod           # --Decorators
    def college():  
        print("ZCOER")

Student2.college()       

# Decorators allow us to wrap another function in order to extend the behaviour of 
# the wrapped function, without permanently modifying it



# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# ----------------IMPORTANT CONCEPTS----------------

# --------1 .Abstraction --------------

# Hiding theimplementation details of a class and showing the essential 
# feactures to the user.
# meaning of this is like in  aa class you had hidden unnecessary thing and shown 
# essential only ,in this way you can understand this defination.
# see this example--

class car:
    def __init__(self):
       self.acc= False
       self.brk = False
       self.clutch = False

    def start(self) :
          self.acc= True
          self.clutch= True
          print("car starting..")

car1 = car()
car1.start()  

# so here you can see self.acc= True
          # self.clutch= True
# this was not used in front it was hidden in function and not shown so in this way
# it shows necessary and rest is hidden.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ------------------2. Encapsulation---------------------

# Define:-- Wrapping data and function into a single unit(object).
# means see whenever we make a class we so attribution,has methods,function everything
# in that its said to be a capsulation.
