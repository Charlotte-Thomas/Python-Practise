
import csv
# | p.156 - 148 |

# display options to user in while loop
# function for each option and subfunctions to use across each (get data, password creation, find user, write data)


def read_data():
    data = []
    file = open('ChunkyChallenges/Passwords/Passwords.csv', 'r')
    reader = list(csv.reader(file))
    for row in reader:
        data.append(row)
    return data

def create_user():
    name = input('enter a user ID: ')


def display_options():
    # repeat = True
    # while repeat:
    print(' 1) Create a new User ID \n 2) Change a password \n 3) Display all User IDs \n 4) Quit')
    choice = int(input('choose an option from above: '))
    if choice == 1:
        create_user()


# display_options()
