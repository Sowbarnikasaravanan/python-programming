#To find the sum of first n natural numbers 
num=int(input("Enter the number :"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("The sum of first ",num," number is ",sum)
