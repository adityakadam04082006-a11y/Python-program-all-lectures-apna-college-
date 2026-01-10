# WAP to check if the list contains a palindrome of elements .(Hint use copy() method)
#palindrome means things like which are same from front and back  = 1,2,3,2,1


list = [2,1,2]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("not palindrome")

