#To display the fibonacci sequence using recursion
def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)
num=int(input("Enter the positive integer:"))
print("Fibonacci sequence:")
for i in range(0,num+1):
    print(fibo(i))
