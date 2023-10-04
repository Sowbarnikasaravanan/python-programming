#To display all the armstrong numbers between two intervals  
start=int(input("Enter the starting point:"))
end=int(input("Enter the ending point:"))
print("The armstrong between ",start," and ",end,": ")
for num in range(start,end):
    rem=0
    sum=0
    temp=num
    while(num>0):
        rem=num%10
        sum=sum+rem**3
        num=num//10
    if temp==sum:
        print(temp," ")
        
