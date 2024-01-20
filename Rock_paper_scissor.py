# To play the rock,paper,scissor game
import random
print("Welcome to the Game! ")
print("Let's start the Game!!")
user_input=int(input("It's your turn ! Press 0 for Rock ,1 for paper ,2 for scissor :"))
print("Your choice :",user_input)
computer_input=random.randint(0,2)
print("Computer's choice is",computer_input)
if(user_input == computer_input):
    print("Match draw")
elif((user_input==0 and computer_input==2) or (user_input==2 and computer_input==1) or (user_input==0 and computer_input==1)):
    print("Hurray ! You Won")
elif((user_input==2 and computer_input==0) or (user_input==2 and computer_input==1) or (user_input==1 and computer_input==0)):
    print("Oh! You Lose")
else:
    print("Sorry! You entered an invalid input")

'''
sample output 1:
Welcome to the Game! 
Let's start the Game!!
It's your turn ! Press 0 for Rock ,1 for paper ,2 for scissor :2
Your choice : 2
Computer's choice is 1
Hurray ! You Won

sample output 2:
Welcome to the Game! 
Let's start the Game!!
It's your turn ! Press 0 for Rock ,1 for paper ,2 for scissor :2
Your choice : 2
Computer's choice is 0
Oh! You Lose

sample output 3:
Welcome to the Game! 
Let's start the Game!!
It's your turn ! Press 0 for Rock ,1 for paper ,2 for scissor :2
Your choice : 2
Computer's choice is 2
Match draw
'''


