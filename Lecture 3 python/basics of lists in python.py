# list and Tuples 

#list is made to make the varibles least by keep dta of same pattern in one variable
# like marks = [25,45,26.2,55.3]

marks = [55.2,88,77,64]
print(marks)

#see now in python string are - inmutable
#             and  lists are  - mutable 
# means indexing can do access but cant change it 
# but in list we can both access and change it.
# for ex -
student=["aditya" ,55.5,"ram"] 
print(student[0])
student[0] = "adi" 
print(student)  

# list slicing
# its smiliar to the string slicing 
# ending idx is not includes
# for ex-

marks = [85.5,44,78,99]
print(marks[1:3])
#negative index can also be done - see below
print(marks[-4:-1])

# List Method 
# 1.list.append  -- means to add one element at the end

list = [2,1,3]
list.append(5)
print(list)    #this thing which we done is also called as mutating 

#2. list.sort() --sorts in ascending order
#and see if this print(list) is not given then it given none output as for return there is nothing 

#ex -
list1 = [5,2,3]
print(list1.append(6))

#ex sort
list2 = [5,3,7,8]
list2.sort()
print(list2)

#3. list.sort(reverse-=True) - its for descending order

list3 = [8,6,1,7,]
list3.sort(reverse=True)
print(list3)

#4. list.reverse - it reverse orignal list comletely

list4 = ['a','f','g','u','z']
list4.reverse()
print(list4)

#5.list.index(idx ,el) --its like replacement on index 0,1,2,3..means adding element or inserts elements at index

list5 = [8,6,4,3,7,4]
list5.insert(2,7)
print(list5)

#6.list.remove -- it removes the first occurrence of element
list6 = [7,4,5,1,5,1]
list6.remove(1)
print(list6)

#7. list.pop(idx)   -- removes elements at index
list7 = [7,4,5,1,5,1]
list7.pop(3)
print(list7)

#and there are many other list too to see it on vscode type list. so you can find option

#8. list._add__   --this is like a + b means to list merge or add together

list8 = [8,6,4,3,7,4]
list91 = [2,9]
result = list8.__add__(list91)
print(result)

#9 .list.extend  --its like add other list to different list
# its diff from append as we are add element from other list not one element
list9 = [5,6,1,4,7,9]
list9.extend([8,9])
print(list9)

#10. list.clear  -- its used to clear the list means in short empty list
list10 = [5,6,1,4,7,9]
list10.clear()
print(list10)

#11. list.count -- its used the repetated no. or values or character in the list

list11 = [5,6,1,4,7,1,9,2,1]
count = list11.count(1)
print(count)