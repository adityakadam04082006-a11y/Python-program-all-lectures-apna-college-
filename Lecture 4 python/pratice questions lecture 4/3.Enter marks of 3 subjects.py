# Q3. 
# WAP to enter marks of 3 subjects from the user and store them in a dctionary. start with an empty
# dictionary & add one by one .Use subject names as key  & marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter maths : "))
marks.update({"maths" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)