#To find the factorial of a number using recursion
def fact(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter the positive integer:"))
print("The factorial of ",num," is ",fact(num))
