'''
Fizzbuzz puzzle
Print numbers between a range. 
If a number is divisible by 3, print Fizz.
If a number is divisible by 5,print Buzz.
If a number is divisible by both 3 and 5,print FizzBuzz.
If a number does not satisfy any of these conditions,simply print that number.
'''

number=int(input("Enter the number till which it prints:"))
for num in range(1,number+1):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)


'''
Enter the number till which it prints:15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''
