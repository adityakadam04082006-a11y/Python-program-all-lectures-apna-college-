#  Range()

# Range function returne a sequence of numbers ,starting from 0 by default, and increments by 1(by default),
# and stops before a specified numbers.
# ex -- range(5) will be from 0 so it will be 0,1,2,3,4

seq = range(5)

for i in seq :
    print(i)
    
# or

for j in range(10) :    #range(stop)
    print(j)


#  Range can be written in three ways --(optional = ?)
# range(start?, stop ,step?)

for k in range(2,5) :    #range(start, stop)
    print(k)

for a in range(3,32,3) :    #range(start, stop ,step) (we can make tables from it if we want)
    print(a)

# in programming this way of writing code is called as linear search

# nums = [1,4,9,16,25,36,49,64,81,100]
# and linear search is=n simple way is this not then this means next like see here 1 not then 4 ,4 not then 9 like this.

