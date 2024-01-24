# To find the Body Mass Index
weight=int(input("Enter the weight (in Kgs):"))
height=float(input("Enter the height(in metres):"))
bmi=weight//height**2
print("The Body Mass Index (BMI) value is:",bmi)
if bmi<18.5:
    print(f"Your BMI is {bmi} and you are underweighted")
elif bmi<25:
    print(f"You BMI is {bmi} and you have normal weight")
elif bmi<30:
    print(f"Your BMI is {bmi} and you are overweighted")
elif bmi<35:
    print(f"Your bmi is {bmi} and you are obese")
else:
    print(f"your bmi is {bmi} and you are clinically obese")

'''
Sample Output:
Enter the weight (in Kgs):58
Enter the height(in metres):1.9
The Body Mass Index (BMI) value is: 16.0
Your BMI is 16.0 and you are underweighted

'''
