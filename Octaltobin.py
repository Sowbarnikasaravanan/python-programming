#To convert an octal number to decimal number
octal=int(input("Enter an octal number:"))
temp=octal
decimal=0
i=0
while(octal>0):
    rem=octal%10
    decimal=decimal+rem*8**i
    octal//=10
    i=i+1
print("The decimal number of ", temp," is ",decimal)
