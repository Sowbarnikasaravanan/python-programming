#To perform basic calculator operations 
cont=1
while(cont==1):
    print("Enter the operation to perform:")
    print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
    choice=int(input("Enter your choice to perform:"))
    if(choice==1):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("The addition of ",a," and ",b," is ",a+b)
    elif(choice==2):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("The subtraction of ",a," and ",b," is ",a-b)
    elif(choice==3):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("The Multiplication of ",a," and ",b," is ",a*b)
    elif(choice==4):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("The division of ",a," and ",b," is ",a/b)
    else:
        print("Invalid operation")
    cont=int(input("Do you want to continue ,press 1:"))
