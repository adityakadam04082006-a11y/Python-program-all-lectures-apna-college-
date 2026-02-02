# File Input / Output

# python can be used to perform operations ona file.(read & Write data)

# Types of all files
# 1. Text Files: txt, docx, log etc
# 2. Binary Files: mp4, mov, png, jpeg etc


# Open,Read & Close File
# we have to open a file before reading or writing

# f = open("file_name","mode")
#            |             |
#            |             | 
#            |             |
#       sample.txt        r: read mode
#        demo.docx        w: write mode

# data = f.read()
# f.close()

f = open("demo.txt","r")
data = f. read(3)
print(data)
print(type(data))
f.close

# File Open Modes (Python)

# Character          Meaning
# 'r' =      open for reading (default)
# 'w' =      open for writing, truncating the file first
# 'x' =      create a new file and open it for writing
# 'a' =      open for writing, appending to the end of the file if it exists
# 'b' =      binary mode
# 't' =      text mode (default)
# '+' =      open a disk file for updating (reading and writing)

# Reading a file

# data = f.read()
# data = f.readline()

line1 = f. readline()
print(line1)

line2 = f. readline()
print(line2)

f.close

# Writing to a file 

# f = open("demo.txt","w")
# f.write("this  is a new line ")   -- overwrites the entire file 

# f =open("demo.txt","a")
# f.write("this is a new line") -- adds to the files

f = open("demo.txt","a")
f.write("this  is a new line ") 
f.close()


# --------------------------------------------------------------------------
# f = open("demo.txt","w")
# f.write("this  is a new line ") 
# f.close()                        by this we can overwrite
#---------------------------------------------------------------------------
# f = open("sample.txt","w")
# f.close() ---- in this way we can make a file

# r+ by this we can overwrite from start
# means we can read and overwrite (pointer is from start)-has notruncate
f = open("demo.txt","r+")
f.write("abcd ") 
f.close()

# w+ -- has truncate it can reads and overwrites 
# a+  -- (the pointer is at end) it appends and has notruncate

# _____________________________________________________________________________________
# _____________________________________________________________________________________
# with syntax ~ 

# so till now we have done the work of opening and closing file ,so now in pyhon this
# is also a better way to do that

# so process is like -- with open ("demo.txt","a") as f:
#                       data = f.read

with open("demo.txt","r") as f:
    data = f.read()
    print(data)


# with open("demo.txt","w") as f:
#     f.write("new data")               --by this we can also write new data

# ______________________________________________________________________________________
# ______________________________________________________________________________________
# Deleting a file


