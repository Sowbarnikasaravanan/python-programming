#To convert the decimal number into binary number
num=float(input("Enter the decimal number:"))
print("The binary value of ",num," is ",bin(num))


#Without using a built in function
num=int(input("Enter the decimal to convert :"))
binary=0
rem=0
i=1
while num>0:
    rem=num%2
    binary=binary+rem*i
    i=i*10
    num=num//2
print("The equivalent binary value for ",num," is ",binary)
