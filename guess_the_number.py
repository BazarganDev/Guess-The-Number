# Import necessary modules
import random

# Storing attempts in a list
game_scores = []

# Define functions
def ShowScore():
    """Showing every game scores and the highest score (which is the lowest attempt)
    """
    title = f"Number of times you attempted to guess: {game_scores}\n"
    title += f"\nHighest score: {min(game_scores)}"
    print(title)

def RestartGame():
    """Restart the game
    """
    GameLogic()

def GameLogic():
    """Defining the game logic
    """
    print("\n****** START ******\n")
    random_number = random.randint(1, 10)
    attempts = 0
    print("Enter your name")
    player_name = input("You > ")
    GameStatusActive = True
    while GameStatusActive:
        print("\nPick a number between 1 and 10")
        guessed_number = int(input(f"{player_name} > "))
        
        # The entered number must be between 1 and 10
        if guessed_number < 1 or guessed_number > 10:
            ERROR_MSG = "Please enter a number within the given range\n"
            print(ERROR_MSG)
            continue
        else:
            if guessed_number > random_number:
                attempts += 1
                print("Try lower\n")
            elif guessed_number < random_number:
                attempts += 1
                print("Try higher\n")
            else:
                attempts += 1
                print("Congrats!\nYou guessed it right.")
                game_scores.append(attempts)
                ShowScore()
                break
    # Replay the game without losing your game scores
    replay = input("Wanna play again? (yes/no) ")
        
    if replay.lower() == 'no':
        ShowScore()
        print("Ok\nHave a nice day")
        input("Press any key to quit...")
        quit()
    else:
        RestartGame()

def StartGame():
    """Game intro
    """
    welcome_message = '\nWelcome to the "Guess The Number" game'
    welcome_message += "\nShall we begin? (yes/no)"
    print(welcome_message)
    
    while True:
        lets_play = input("You > ")
        if lets_play.lower() == 'no':
            print("Bye")
            input("Press any key to quit...")
            quit()
        elif lets_play.lower() == 'yes':
            print("Cool")
            GameLogic()
        else:
            print("Invalid command\n")

def main():
    StartGame()

main()