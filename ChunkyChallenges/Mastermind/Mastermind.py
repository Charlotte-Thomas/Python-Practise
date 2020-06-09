
import random

# | p.153 - 147 |

# create list of four colours in code & present to user
# function for selecting random colour sequence
# allow user to guess in while loop until they get sequence correct
# two for loops to check matches of the different criteria

colours = ['b', 'g', 'c', 'r', 'w', 'y', 'p']


def randomise():
    selection = []
    for i in range(0, 4):
        selection.append(random.choice(colours))
    print(selection)  # del
    return selection

def colours_correct(choice, selection): # pass in with both dashed
    print(selection)
    correct = 0
    for col in choice:
        if selection.__contains__(col):
            correct += 1
            selection[selection.index(col)] = '-'
    print(correct)
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
    # repeat = True
    # while repeat == True:
    choice = input('''enter four colours from this selection (doubles allowed) using the first letter of each:
    \n (b)lue \n (g)reen \n (c)yan \n (r)ed \n (w)hite \n (y)ellow \n (p)urple \n''')
    choice = choice.replace(' ', '').replace(',', '') # removes any spaces or commas
    choice_list = list(choice)
    if len(choice_list) == 4:
        print('you chose:', choice_list)
        positions_correct(choice_list, selection)
        # matches = colours_correct(choice_list, selection)
    else:
        print('please enter 4 colours')

start_game()
