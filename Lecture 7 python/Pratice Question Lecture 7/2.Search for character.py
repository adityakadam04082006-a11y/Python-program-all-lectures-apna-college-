
word = "learning"
with open("pratice.txt","r") as f:
    data = f.read()
if(data.find(word) != -1 ):
    print("found")
else:
   print("not found")   