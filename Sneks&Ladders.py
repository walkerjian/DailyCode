import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from ipywidgets import interact_manual, fixed
import random

# Snakes and Ladders dictionary
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to plot the board
def plot_board(snakes, ladders):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw grid
    for i in range(10):
        for j in range(10):
            ax.add_patch(Rectangle((i, j), 1, 1, fill=None, edgecolor='black'))

    # Draw snakes
    for start, end in snakes.items():
        ax.annotate("", xy=((start-1)%10+0.5, (start-1)//10+0.5), xytext=((end-1)%10+0.5, (end-1)//10+0.5), arrowprops=dict(arrowstyle="->", lw=1.5))

    # Draw ladders
    for start, end in ladders.items():
        ax.annotate("", xy=((start-1)%10+0.5, (start-1)//10+0.5), xytext=((end-1)%10+0.5, (end-1)//10+0.5), arrowprops=dict(arrowstyle="->", color='red', lw=1.5))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.grid(True)
    plt.gca().invert_yaxis()
    plt.show()

# Function to play the game
def play_game(snakes, ladders):
    plot_board(snakes, ladders)
    position = 1
    turns = 0
    while position < 100:
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")
        if position + roll > 100:
            print("You need to roll a smaller number to win. Try again.")
        else:
            position += roll
            print(f"You moved to position {position}.")
            if position in snakes:
                print("Oh no, you landed on a snake!")
                position = snakes[position]
                print(f"You are now on position {position}.")
            elif position in ladders:
                print("Yay, you landed on a ladder!")
                position = ladders[position]
                print(f"You climbed up to position {position}.")
        turns += 1
    print(f"Congratulations, you won the game in {turns} turns!")

# Interactive widget
interact_manual(play_game, snakes=fixed(snakes), ladders=fixed(ladders));
