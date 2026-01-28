# Write a recursion function to calculate the sum of first n natural numbers.

def print_list(list, idx):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)

name = (input("enter list :")).split()

print_list(name, 0)
