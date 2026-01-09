#  if- elif - else-

    # if( condition):
    # statement1

    # elif(condition):
    # statement2

    #else: 
    # statememtsN

#can write multilple if ,elif or else ,but to write multiple elif one starting if  condition is needed
#and elif will check the condition ,when the if condition is false
#and can write else statement only one time , we usually write it at last 

#1.Ex -

num = 2

if(num > 3):
    print("greater than 3")
elif(num < 3) :
    print("less then 3")  

#or
#2.Ex -

college = "closed on sunday"

if(college == open):
    print("college is open from monday to sunday no hoilday")

elif(college == "closed on monday"):
    print("college has declared holiday")

elif(college == "closed on sunday"):
    print("college is closed due to official holiday ")

else:
    print("college is opened due to Students request")

# or 
#3.Ex -

# marks = int(input("Enter your marks:"))

# if(marks >= 90):
#     grade = "A"
# elif(marks>= 80 and marks <90):
#     grade = "B"
# elif(marks>= 70 and marks <80):
#     grade = "c"
# else :
#     grade = "D"

# print("grade of the students are->", grade)



#Nesting - in one statement we can write other condition/statement

age = int(input("Enter your age :"))

if age >= 18 :
    if age >= 80:
        print("cannot drive")
    else:
         print("can drive")   
      
else:
    print("cannot drive")

