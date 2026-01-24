# WAP to find the factorial of first n numbers
# note : always to initilize factorial we start with 1

n= int(input("enter the number:"))

fact = 1
i = 1
while i <= n :
    fact *= i
    i += 1

    print("factoraial :",fact)