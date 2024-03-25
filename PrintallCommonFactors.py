# To print all the common factors between two numbers 
a=int(input("Enter the first number:"))
b=int(input("Enter thr second number:"))
n=a if a<=b else b
for i in range(1,n+1):
    if (a%i==0 and b%i==0) :
        print(i)
  
