#  For loops 

# are used for sequential traversal.for traversing list,string,tuples ,etc.

# FOR loop Ex -- (ex for list ,tuples,string)

nums = [1,2,3,4,5,6,7]
tup = (8,9,6)
str = "adityakadam"

for val in nums :
    print(val)
for no in tup :
    print(no)
for char in str :
    print(char)


#  for loop with else (optional if want to use they use rather leave)
# see else is used in case of break means we complete loops occurs then else works otherwise not 
# see by two ex --

# Ex 1
string = "aditya"

for chara in string :
    print(chara)

else:
    print("end")

# Ex 2.
string1= "aditya"

for chr in string1 :
    if( chr == 'y') :
        print("y found")
        break

    print(chr)

else:
    print("end")
    # so here the loop was broken and so end was not printed so its diff fro regulear print function
    
