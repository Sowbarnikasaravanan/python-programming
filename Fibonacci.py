# To display the fibonacci numbers 
term=int(input("Enter the no. of terms:"))
t1=0
t2=1
if(term==1):
    print (t1)
elif(term==2):
    print(t1,t2)
elif term>2:
    for i in range(0,term):
        print(t1)
        n=t1+t2
        t1=t2
        t2=n
