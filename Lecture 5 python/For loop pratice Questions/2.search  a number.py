# Search for a number x in this tuple using loop:


nums = (1,4,9,16,25,36,49,64,81,100,49,36)
x = int(input("enter the value of 1 to 10 squares:"))

idx = 0
for el in nums :
    if (el ==  x):
        print("number found at idx",idx)
    idx += 1


