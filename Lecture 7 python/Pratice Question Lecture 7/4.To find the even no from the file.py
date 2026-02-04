# From a file in whiich line of the file does the word "learning" occurs first.


with open("Q4 problem.txt","w") as f:
    f.close()

with open("Q4 problem.txt","w") as f:
    f.write("1,22,4,5,6,7,8,98,65,78,4,49,58,67,21,32,76,66")

count = 0
even_number = []
with open("Q4 problem.txt","r") as f:
     data = f.read()
     

     num = data.split(",")
     for val in num:
         if (int(val) %2 == 0):
             count += 1
             even_number.append(int(val))
          

print("this is count of even numbers in in file :",count)
print("Thoses even numbers are:",even_number)
                 

            
             
     
      
