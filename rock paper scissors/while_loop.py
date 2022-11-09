#this is the main loop for a rock paper scissors game
# Randomly select an object for the computer's choice
import random

def play_game():
    while True:
        user_action=input("Enter a choice [rock, paper, or scissors]:")
        possible_actions=["rock","paper","scissors"]
        computer_actions = random.choice(possible_actions)
        print(f"You chose {user_action}, the computer chose {computer_actions}.")
        if user_action==computer_actions:
            print("It's a tie.")
        elif user_action=="rock":
            if computer_actions=="scissors":
                print("You win!")
            else:
                print("You lose.")
        elif user_action=="paper":
            if computer_action=="rock":
                print("You win!")
            else:
                print("You lose.")
        elif user_action=="scissors":
            if computer_action=="paper":
                print("You win!")
            else:
                print("You lose.")
        else:
            print("Invalid input. Try again.", user_action)
        play_again=input("Play again? (y/n):")
        if play_again.lower()!="y":
            break

def main():
    play_game()

if __name__=='__main__':
    main()