# 1.Functions in python ----
# _____________________________________________________________

# Define-- Blocks of statements thatperforms a specific task.

# step1 :--
# def func_name(parameter1, parameter2): -- called as [ function definition ]
# some work
# returns value -- for last return

# step2 :--
# func_name(arg1, arg2..):  -(its called function call)-argument

# step3:--ex
# def sum(a, b):
#     s = a+ b
#     return s
# print(sum(2, 3))

# means simple a function takes input like parameters and gives some output its used
# to reduce redudant or repeatiblity in code and make code better

# Actual ex--

#function definition
def calc_sum(a, b):   #parameters
    sum = a + b
    print(sum)
    return sum


calc_sum(2, 3)    #function call; arguments

# more line of code

calc_sum(12, 31)

calc_sum(21, 13)

# you can make function who does't has parameter means no input so in this ay
# we can not use return as return is output means it completely depends


# ex-- make function which calculate average of 3 numbers--

def cal_avg(a, b, c):
    avg = (a + b + c)/ 3
    print(avg)
    return avg


cal_avg(1,2,3)

# If want to print two variables on one line so type
print("aditya kadam", end="")
print(" zeal college")

# ____________________________________________________________________
# 2.Tyes of Function in python ----

# 1.Built -in Functions

# I.   print()
# II.  len()
# III. type()
# IV.  range()
# etc their are more

# 2. User defined Functions 
# means we make made it like it where not in python ,we have defined it--

# _____________________________________________________________________
# 3.Default Parameters---
# define -- Assigning a default value to parameter ,which is used when no arguments 
# is passed.
# also if we are givinfg default values so we can give it from last not like 
# a=2,b so we will get error 

def cal_prod(a, b=1):
    print(a*b)
    return a *b

cal_prod(1)

# or

def cal1_prod(a=1, b=1):
    print(a*b)
    return a *b

cal1_prod()


