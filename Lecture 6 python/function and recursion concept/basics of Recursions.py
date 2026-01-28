# Recursion

# when a function call itself repeatedly.
# its same as loop 
# measn it call of himself like see if we print
# n = 5
#  show(5) then it will print it and go to n-1 so it wee be 4 sand so..on and 
# when we use (return ) then it will be in control systemto stop

# Recursive function --ex--

def show (n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    

n = int(input("enter number :"))   
show(n) 

# Note : in recursion we can't go to infinite loop we need to give condition 
# which is called [ base case ] --{ if(n == 0):
#                                       return } see this is said as basecase.
# smiliarly and if we have printed -1 instead of 0 so it will also print 0

# call stack is like a layer and layer calling to complete the task
# see like [n! = (n-1)! x n] , in such case we can come to know that we can use recursion
# its like if we want to find factorial of n! then 1st we need to find (n-1)! factorial

#  return n! --- see here how to do
# ex--

def fact (k):
    if(k == 0 or k == 1):
        return 1
    else:
        return k*fact(k-1)
    
k = int(input("enter number :"))    
print("factorial is :",fact (k))
