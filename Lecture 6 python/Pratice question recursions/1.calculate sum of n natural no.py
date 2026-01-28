# Write a recursion function to calculate the sum of first n natural numbers.

def cal_num(n):
    if (n == 0):
        return 0
    return cal_num(n-1) + n
    cal_num(n-1)

n = int(input("enter number:"))
print(cal_num(n))

    