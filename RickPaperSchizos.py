import random

def determine_winner(player_choice, computer_choice):
    outcome = ""
    player_score = 0

    if player_choice == computer_choice:
        if player_choice == "Rick":
            outcome = "Rickrolled!"
        elif player_choice == "Paper":
            outcome = "No points awarded."
        else:
            outcome = "Your brains are eaten by a zombie!"
    else:
        if player_choice == "Rick":
            if computer_choice == "Paper":
                player_score -= 5
                outcome = "Computer wins with Paper. You lose 5 points."
            else:
                player_score += 10
                outcome = "You win with Rick! You gain 10 points."
        elif player_choice == "Paper":
            if computer_choice == "Schizos":
                outcome = "Your brains are eaten by the computer!"
            else:
                player_score += 5
                outcome = "You win with Paper! You gain 5 points."
        else:
            if computer_choice == "Rick":
                player_score -= 10
                outcome = "Computer wins with Rick. You lose 10 points."
            else:
                player_score += 20
                outcome = "You win with Schizos! You gain 20 points."

    return player_score, outcome

def play_game():
    total_score = 0
    
    print("Welcome to Rick Paper Schizos!")
    print("Choose 'Rick', 'Paper', or 'Schizos'. Type 'exit' to end the game.\n")
    
    while True:
        player_choice = input("Your choice: ").capitalize()

        if player_choice == "Exit":
            break
        
        if player_choice not in ["Rick", "Paper", "Schizos"]:
            print("Invalid choice. Please choose 'Rick', 'Paper', or 'Schizos'.\n")
            continue

        computer_choice = random.choice(["Rick", "Paper", "Schizos"])
        print(f"Computer chose: {computer_choice}")

        score, outcome = determine_winner(player_choice, computer_choice)
        total_score += score

        print(outcome)
        print(f"Your total score: {total_score}\n")

    print("Thanks for playing!")

play_game()
