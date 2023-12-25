#To remove duplicate letters of a string 
str=input("Enter the string:")
remdup=""
for i in str:
    if i not in remdup:
        remdup=remdup+i
print(remdup)
