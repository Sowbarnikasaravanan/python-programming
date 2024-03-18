#TO print # before vowels in a string
name=input("Enter the string:")
vowels=['a','e','i','o','u','A','E','I','O','U']
last=""
for i in name:
    if i in vowels:
        last=last+'#'
    last=last+i
print(last)

/*
Sample Output:
Enter the string:sowbarnika
s#owb#arn#ik#a
*/
