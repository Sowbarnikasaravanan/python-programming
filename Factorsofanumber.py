// To print the factors of a number
num=int(input("Enter the number:"))
print("The factors of",num,":")
for i in range(1,num+1):
    if(num%i==0):
        print(i)
print()

/*
Sample output:
Enter the number:20
The factors of 20 :
1
2
4
5
10
20
*/
