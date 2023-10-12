#To display the numbers in triangle pattern 
rows=int(input("Enter the numner of rows :"))
for i in range(0,rows+1):
    for j in range(0,i):
        print(i,end=" ")
    print("\n")


#Expected output 
# 1
# 2 2
# 3 3 3
# 4 4 4 4 
