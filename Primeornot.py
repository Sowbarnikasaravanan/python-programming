#To check whether the number is prime or not
number=int(input("Enter the number:"))
prime=0
if number==1:
    prime=1
else :
    for i in range(2,number):
        if number%i==0:
            prime=1
            break
if(prime==0): 
     print(number," is a prime number")
else:
    print(number," is not a prime number")
 
