#To display the multiplication table 
table=int(input("Enter the table:"))
limit=int(input("Enter the limit:"))
for i in range(1,limit+1):
    print(i,"*",table,"=",i*table)
    
