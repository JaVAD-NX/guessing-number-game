import random
print("this is a game of guessing a number the computer will chose a number and you have to guess it if you guess it right you win")
computer_choice=random.randrange(11,20)
while True:

    player_choice =int(input("enter a number between 10 and 20: "))
    if player_choice >= 20 or player_choice <=10 :
        print("you are out of range")
    elif computer_choice != player_choice:
        print("try again you were wrong") 
    elif computer_choice== player_choice:
        print("you win")   
        break 
while True:
    input()