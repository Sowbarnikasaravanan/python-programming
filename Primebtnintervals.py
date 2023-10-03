# To display all the primes between the two intervals 
start=int(input("Enter the starting point:"))
end=int(input("Enter the Ending point:"))
print("The prime numbers between ",start," and ",end,": ")
for j in range(start,end+1):
    if j>1:
        for i in range (2,start):
            if j%i==0:
                break
        else:
            print(j)
            
    
