
import random

# ------- Random --------

# EXTRA:
# random gives a random num between 0-1
# it can return 0 but it WON'T return 1 - the largest num it can return is: 0.99999999999999988897769753748434595763683319091796875
print(round(random.random(), 3))

# selects random whole num between a set range (inclusive):
print(random.randint(0, 6))

# selects a random whole num between a range at set intervals (3rd arg) (inclusive)
print(random.randrange(0, 10, 2))

# selects ranodm val from a list
print(random.choice(['apple', 'banana', 'pear']))

# ___________________________

# | p.47 - 059 |
colour_game = True
colours = ['white', 'grey', 'yellow', 'red', 'cyan']
while colour_game:
    print(str(colours).strip('[]'))
    picked = input('choose colour from above: ').lower()
    random_colour = random.choice(colours)
    print(random_colour)
    if picked == random_colour:
        print('well done!')
        colour_game = False
    elif random_colour == 'white':
        print('oops you\'re looking as WHITE as a ghost')
    elif random_colour == 'grey':
        print('oops things are looking GREY for you')
    elif random_colour == 'yellow':
        print('oops don\'t be a YELLOW belly, try again')
    elif random_colour == 'red':
        print('oops I bet you\'ve gone RED in the face')
    elif random_colour == 'cyan':
        print('oops CYA-N on the next try')
