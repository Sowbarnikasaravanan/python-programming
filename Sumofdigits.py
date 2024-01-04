#To find the sum of digits of a number
number=input("Enter the number:")
sum=0
for i in range(0,len(number)):
    sum=sum+int(number[i])
print("The sum of the digits of",number,"is",sum)
