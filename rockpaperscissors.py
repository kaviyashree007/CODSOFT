import random

#giving instructions to the user before the game

def instructions():
    print("=== Rock, Paper, Scissors ===")
    print("Instructions:")
    print("1. Choose 'rock', 'paper', or 'scissors'.")
    print("2. The computer will also make a choice.")
    print("3. The winner is determined by the following rules:")
    print("   - Rock beats scissors")
    print("   - Scissors beats paper")
    print("   - Paper beats rock")
    print("4. If both choices are the same, it's a tie.")
    print("5. You can play multiple rounds and keep track of the score.")
    print("6. After each round, you will be asked if you want to play again.")
    print("Enjoy the game!\n")

#Prompting the user to choose rock, paper, or scissors.

def userchoice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

#Generate a random choice (rock, paper, or scissors) for the computer.

def computerchoice():
    return random.choice(['rock', 'paper', 'scissors'])

#game logic

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
    

#displaying the result

def showresult(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def game():
    instructions()
    user_score = 0
    computer_score = 0
    while True:
        user_choice = userchoice()
        computer_choice = computerchoice()
        result = winner(user_choice, computer_choice)
        showresult(user_choice, computer_choice, result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"\nCurrent Score: You {user_score} - {computer_score} Computer")
        
        playagain = input("Do you wanna play another game with me? (yes/no): ").lower()
        if playagain != 'yes':
            break

    print("\nThank you for playing!. Come again :).")

game()
