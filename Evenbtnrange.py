# To print all the even numbers between a range 
s=int(input("Enter the starting number:"))
e=int(input("Enter the ending number:"))
if(s>e):
    t=s
    s=e
    e=t
even=[]
for i in range(s,e+1):
    if(i%2==0):
        even.append(i)
print(even)
        
'''
Sample output:
Enter the starting number:5
Enter the ending number:10
[6, 8, 10]

''' 
