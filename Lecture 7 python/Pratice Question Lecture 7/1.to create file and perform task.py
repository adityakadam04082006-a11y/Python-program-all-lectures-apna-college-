# create a new file "pratice.txt" using python .add the following data in it:
#  hi everyone 
# we are learning file I/o
# using java
# i like programming in java

# WAF that replace all occurence of java with python in above File 
# search if the word learning exists in the file or not 

with open("pratice.txt","w") as f:
 f.write("hi everyone \n we are learning file I/o")
 f.write("\n using java \n i like programming in java")


with open ("pratice.txt","r") as f:
    data = f.read()

new_data =data.replace("java","python") 
print(new_data)   

with open ("pratice.txt","w") as f:
    f.write(new_data)



def check_for_word():
   word = "learning"
   with open("pratice.txt","r") as f:
      data = f.read()
      if(data.find(word) != -1 ):
         print("found")
      else:
         print("not found")   