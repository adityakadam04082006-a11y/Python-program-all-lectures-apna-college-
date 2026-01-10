#TUPLES
# in tuples it are immutables values similar to string 
# here we have to use ( ) instead of [] also add a , we written in () like ("aditya",) 
#if comma not used then system uses it as string not s tuple
#It's diff from list ad we cant add or replace as we done in list 
#ex -
tup = ("adi",)
print(tup)
print(type(tup))

#for multiple tuple ex- 
tup = (4,5,7,9)     #here in case of multiple comma is not necessary to apply after completion
print(tup)
print(type(tup))

#Tuples Method

# 1. tup.index() - returns index of first occurrence or we are searching index to that element
#ex -

tup1 = (5,8,3,1,4,7)
print(tup1.index(3))

#2. tup.count()  -- its like we are count the repeated no.

tup2= (3,4,1,3,4,3,3,8)
print(tup2.count(3))