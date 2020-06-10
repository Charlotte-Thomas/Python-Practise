
import random

# | p.153 - 147 |

# create list of four colours in code & present to user
# function for selecting random colour sequence
# allow user to guess in while loop until they get sequence correct
# two for loops to check matches of the different criteria

colours = ['b', 'g', 'c', 'r', 'w', 'y', 'p']


def randomise():
    selection = []
    i = 0
    while i < 4:
        selection.append(random.choice(colours))
        i += 1
    return selection


def colours_correct(choice, selection):
    correct = 0
    for col in choice:
        if selection.__contains__(col) and col != '-':
            correct += 1
            selection[selection.index(col)] = '-'
    return correct


def positions_correct(choice, selection):
    correct = 0
    for col in enumerate(choice):
        if col[1] == selection[col[0]]:
            correct += 1
            selection[col[0]] = '-'
            choice[col[0]] = '-'
    return [correct, choice, selection]


def start_game():
    selection = randomise()
    repeat = True

    while repeat:
        choice = input('''enter four colours from this selection (doubles allowed) using the first letter of each:
        \n (b)lue  (g)reen  (c)yan  (r)ed \n (w)hite (y)ellow (p)urple \n''')
        choice = choice.replace(' ', '').replace(',', '') # removes any spaces or commas
        choice_list = list(choice)
        selection_reset = selection[:]

        if len(choice_list) == 4:
            print('\n you chose:', choice_list)
            [positions, choice_list, selection_reset] = positions_correct(choice_list, selection_reset)
            matches = colours_correct(choice_list, selection_reset)
            print(f' correct colours in correct positions: {positions} \n correct colours in wrong positions: {matches} \n')
            if positions == 4:
                print(f'you win! all positions correct')
                repeat = False
            else:
                continue
        else:
            print('IMPORTANT! : please enter 4 colours \n')

# start_game()
