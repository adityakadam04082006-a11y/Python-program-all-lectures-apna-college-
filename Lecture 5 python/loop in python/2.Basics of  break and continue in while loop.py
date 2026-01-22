# Break and Continue

# Break : Used to terminate the loop when encountered.
# Continue : terminates execution in the current iteration and continues execution of the loop with the next ,
# iteration.


# Ex -- (Break -)
i = 0
while i <= 5 :
    print(i)
    if(i == 3):
        break

    i += 1
print("The end")



#  Ex -- (continue -)
j = 0
while (j <= 5):
    if (j == 3):
        j += 1
        continue

    print(j)
    j += 1

# Ex --( if wants to skip even numbers :)

print("ONLY ODD NUMS :")
k = 0
while (k <= 10):
    if (k%2 == 0):
        k += 1
        continue

    print(k)
    k += 1


#  Ex -- 

print("ONLY EVEN NUMS :")
l = 0
while (l <= 10):
    if (l%2 != 0):
        l += 1
        continue

    print(l)
    l += 1