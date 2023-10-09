#To find the sum of first n natural numbers using recursion 
def sumofn(num):
    if num==1:
        return 1;
    else:
        return num+sumofn(num-1)
num=int(input("Enter the positive integer:"))
print(sumofn(num))
