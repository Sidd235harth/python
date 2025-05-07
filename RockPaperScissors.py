import random
import sys
print(" Siddarth TR \n USN:1AY24AI106 \n sec:o")
print('ROCK, PAPER, SCISSORS')

# Tracking wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n")

    if move == 'q':
        print("Thanks for playing!")
        sys.exit()
    if move not in ['r', 'p', 's']:
        print("Invalid input. Please choose r, p, s, or q.")
        continue

    # Player move to string
    if move == 'r':
        player_move = 'ROCK'
    elif move == 'p':
        player_move = 'PAPER'
    else:
        player_move = 'SCISSORS'
    print(f'{player_move} versus...')

    # Computer move
    computer_move = random.choice(['r', 'p', 's'])
    if computer_move == 'r':
        comp_move_str = 'ROCK'
    elif computer_move == 'p':
        comp_move_str = 'PAPER'
    else:
        comp_move_str = 'SCISSORS'
    print(comp_move_str)

    # Determine outcome
    if move == computer_move:
        print("It is a tie!")
        ties += 1
    elif (move == 'r' and computer_move == 's') or \
         (move == 'p' and computer_move == 'r') or \
         (move == 's' and computer_move == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
