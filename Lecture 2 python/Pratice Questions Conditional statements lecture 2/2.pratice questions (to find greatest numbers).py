# WAP to find the greatest of 3 numbers entered by the user 

a = float(input("enter the first number :"))
b = float(input("enterthe second number :"))
c = float(input("enter the third number :"))

if(a >= b and a>=c ):
    print("first number id the largest",a)

elif(b >= c):
    print("second number is the largest",c)

else:
    print("third number is the largest",c)    