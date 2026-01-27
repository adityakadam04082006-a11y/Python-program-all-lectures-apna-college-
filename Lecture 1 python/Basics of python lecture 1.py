print("hello world","i am aditya")

name = "aditya"
age = 19
price = 25.20
old = False
ak = None

print("my name is : ",name)

print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(ak))


a = 500
b = 200
sum = a+b
print(sum)

print("hello world")
# print("hello world")

# arithematic operators

a1 = 10
b1 = 4
print(a1 + b1)
print(a1 - b1)
print(a1 * b1)
print(a1 / b1)
print(a1 % b1) # remainder 
print(a1 ** b1) # power means a^b

#relational operators

a2 = 20
b2 = 30
print(a2 == b2) #False
print(a2 != b2) #True
print(a2 >= b2) # False
print(a2 > b2) # False
print(a2 <= b2) # True
print(a2 < b2) # True

#assignment operators (AOs)
num1 = 20
num2 = num1 + 30 # 20+30 => 50        , 1st method 
num1 *= 30  # we can use different AOs like += ,*= ,-=, /= , etc. 2nd method
print("num :", num1)
print(num2)

# Logical operators (not ,  and , or )
# Not operator is going on 

K = 20 
L = 30 
print(not False)
print(not( K < L))

# AND , OR operator is now going on

val1 = True
val2 = False
print("AND operator :",val1 and val2)

print("or operator :",val1 or val2)
#OR By special operations also we can do this 

print("OR operator:",K == L or (K > L))


# Type conversion
Q = 2
W = 3.25
sum = Q + W
print(sum)
 
#Type casting
E = int("2")
R = 4.55

print(type(E))
print(E + R)

#Input in python 

#1
name = input("enter your name : ")
print("welcome", name)

#2
name1 = input("enter your name :")
age = int(input("enter age"))
marks = float(input("enter marks"))


# If want to print two variables on one line so type
print("aditya kadam", end="")
print("zeal college")

print("welcome",name1)
print("age",age)
print("marks",marks)
