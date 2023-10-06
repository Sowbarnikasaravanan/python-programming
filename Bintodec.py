#To convert the binary number to decimal number
binary=int(input("Enter the binary number:"))
temp=binary
decimal=0
i=0
while(binary>0):
    rem=binary%10
    decimal=decimal+rem*2**i
    binary//=10
    i=i+1
print("The decimal number of ", temp," is ",decimal)
