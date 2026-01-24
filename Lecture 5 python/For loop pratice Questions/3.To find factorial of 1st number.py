# WAP to find the factorial of first n numbers
# note : always to initilize factorial we start with 1

n= int(input("enter the number:"))
fact = 1

for i in range(1,n+1):
    fact *= i

    print("factorial =",fact)