# To check whether the number os armstrong or not 
num=int(input("Enter the number:"))
temp=num
rem=0
rev=0
while(num>0):
    rem=num%10
    rev=rev+rem**3
    num=num//10
if(temp==rev):
    print(temp," is an armstrong number")
else:
    print(temp," is not an armstrong number")
    
