# WAF to find whether the number is odd or even

def check_odd_even(num):
    if (num %2 == 0) :
        print(num,"is even")

    else:
        print(num,"is odd")    

n = int(input("enter the number :"))

check_odd_even(n)


# or  -- its simple way using condition 

m = int(input("enter the number here :"))
if ( m %2 == 0) :
   print(m,"number even")

else:
    print(m,"number odd ")    

# or without condition and function     

a = int(input("enter no. :"))
print(a,"is",["even","odd"][n % 2])

# here 0 = even and 1 = odd so % =reminder
# ex -- n = 7 and , 7/2 is 3 with reminder 1 so answer is odd




