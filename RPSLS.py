import random
import sys

score = 0

while True:
    win_lose_pairs = [('Scissors' , 'Paper'),
                ('Paper'      , 'Rock'),
                ('Rock'       , 'Lizard'),
                ('Lizard'     , 'Spock'),
                ('Spock'      , 'Scissors'),
                ('Scissors'   , 'Lizard'),
                ('Lizard'     , 'Paper'),
                ('Paper'      , 'Spock'),
                ('Spock'      , 'Rock'), 
                ('Rock'       , 'Scissors')]

    moves = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    cpu_action = random.choice(moves)

    print('Choose your fighter: ')
    print('-> Rock (1)\n-> Paper (2)\n-> Scissors (3)\n-> Lizard (4)\n-> Spock (5)')
    
    while True:
        try:
            user_input = (input('Your pick (1 - 5): '))
            if user_input == "SHELDON":
                score += 100
                print(' > You win the game, hackerman.')
                print(' > Score: ', score)
                sys.exit() 
            if int(user_input) not in range (1,6):
                print("Rock, Gun, Lightning, Devil, Dragon, Water, Air, Paper, Sponge, Wolf, Tree, Human, Snake, Scissors, Fire, Rock will be released at a later date, please input values from 1 through 5 for now.")
                continue
            break
        except ValueError:
             print("Cheat codes are not allowed (and definitely don't exist), pick a number from 1 through 5.")

    user_action = moves[int(user_input)-1]

    if cpu_action == user_action:
        result = 'Draw! :|'

    elif (user_action, cpu_action) in win_lose_pairs:
        result = 'You win! :)'
        score += 1

    else: 
        result = 'You lost! ):'

    print('---------------------------------------')
    print(' > You chose: ', user_action)
    print(' > Computer chose: ', cpu_action)
    print(' > Result: ', result)
    print(' > Wins: ', score)
    print('---------------------------------------')

    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        break
