#To find the GCD or HCF of two numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if(num1<num2):
    temp=num1
    num1=num2
    num2=temp
gcd=1
for i in range(2,num2+1):
    if(num1%i==0 and num2%i==0):
        gcd=i
print("The GCD of ",num1," and ",num2," is ",gcd)
        
