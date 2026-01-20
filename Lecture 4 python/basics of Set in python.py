# Set in python
#set is the collectionof the unordered iteams. Each element in the set must be unique and immutable.
# it ignores duplicate values 
#can't add list in set or we can't add hashable values
#and see this carefully set is mutable but th elements in it are immutable

collection = {5,1,5,5,5,7,"world","hello","world"}


print(collection)
print(len(collection))  #total no of iteams

#empty set
collection = set()
print(type(collection))

# Set Method

# 1. set.add(el)   -- adds an elements

collection.add(1)
collection.add(1)
collection.add(2)
collection.add("adi")
collection.add(('Tuple'))  # can add tuple but not list
print(collection)

# 2. set.remove(el)   -- remove the element

s = {1,2,3,4,5,5}
s.remove(2)
print(s)

# 3. set.clear(el)   -- its to remove everything

s = {1,2,3,4,5,5}
s.clear()
print(s)

# 4.set.pop(el)    -- removes random values

collection = {5,1,5,5,5,7,"adi","world","hello","world"}

print(collection.pop())
print(collection.pop())


# 5. set.union (set2)    -- combines both set values and returns new

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))

# 6. set.intersection(el)     -- combines common values annd returns new 

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.intersection(set2))
