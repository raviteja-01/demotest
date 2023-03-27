import random 

print("Welcome to Rock Paper Scissors Game")

user_score = 0

computer_score = 0 

no_of_ties = 0

options = ["rock","paper","scissors"]

while True:
    computers_choice = random.choice(options)
    user_choice = input("Enter your choice(Rock/Paper/Scissors) or press q to to quit: ").lower()
    if user_choice == 'q':
        break
    if user_choice not in options:
        print("Please enter valid option")
    elif user_choice != computers_choice:
        if user_choice == "rock" and computers_choice=="scissors":
            user_score += 1 
            print("You WON!!!")
        elif user_choice == "paper" and computers_choice == "rock":
            user_score += 1
            print("You WON!!!")
        elif user_choice =="scissors" and computers_choice == "paper":
            user_score += 1
            print("You WON!!!")
        else:
            computer_score += 1 
            print("You LOST")
    else:
        no_of_ties += 1
        print("Game Tied")

print(f"You won in {user_score} times.")
print(f"Computer Won in {computer_score} times.")
print(f"No of Times Tied: {no_of_ties}")
print("See you again!!!")
    
    




