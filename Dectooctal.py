#To convert the decimal value to octal
num=int(input("Enter the decimal to convert :"))
octal=0
rem=0
i=1
temp=num
while num>0:
    rem=num%8
    octal=octal+rem*i
    i=i*10
    num=num//8
print("The equivalent octal value for ",temp," is ",octal)
    
    
