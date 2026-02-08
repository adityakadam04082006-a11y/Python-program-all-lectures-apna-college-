# Que. Create student class that takes names & marks of 3 subjects as arguments in constructor 
# Then create a method to print the average


class student:                                            #class create
    def __init__(self,name,marks):                        #this is constructor
        self.name = name
        self.marks = marks

    def get_avg(self):                                     #this is method
        sum =0                                             #this is normal method
        for val in  self.marks:
            sum += val
        print("Hi",self.name,"your avg score is:",sum/3)


s1 = student("aditya kadam,",[98,97,92])                    #this is object
s1.get_avg()       
        