'''
Using functions:
1. play() is the main function
2. is_win() to be called when the user wins

'''

import random


def play():
    options = ["r", "p", "s", "q"]

    user = input("Your choice: 'r' for rock, 'p' for paper, 's' for scissors, 'q' for quit ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user not in options:
        print("ERROR! Your choice must be among 'r', 'p', 's' or 'q'.")
        quit()

    if user == "q":
        return 'You have quit the game.'
        # break

    elif user == computer:
        # elif is_draw(user, computer):
        #     game_draws = game_draws + 1
        return 'It\'s a tie.'

    # r>s, s>p, p>r
    elif is_win(user, computer):
        # player_wins += 1
        return 'You won'

    else:
        # opponent_wins += 1
        return 'You lost.'


def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
