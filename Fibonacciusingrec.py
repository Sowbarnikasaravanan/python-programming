#To display the fibonacci sequence using recursion
def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
num=int(input("Enter the positive integer:"))
print("Fibonacci sequence:")
for i in range(0,num+1):
    print(fibonacci(i))
