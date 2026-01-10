# WAP to ask the user to enter names of their 3 favorite movies and store them in a list
movies = []
name1 = input("enter first movie name :")
name2 = input("enter second movie name :")
name3 = input("enter third movie name :")

movies.append(name1)
movies.append(name2)
movies.append(name3)

print(movies)

#or

movies = []
movies.append(input("enter first movie name :"))
movies.append( input("enter second movie name :"))
movies.append(input("enter third movie name :"))
