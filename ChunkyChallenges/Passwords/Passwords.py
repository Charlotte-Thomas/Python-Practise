
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

def find_user(name):
    data = read_data()
    for user in data:
        if name == user[0]:
            return False
    return True

def create_password():
    repeat = True
    while repeat:
        points = 0
        password = input('please enter a password: ')
        listed = list(password)
        if len(listed) >= 8:
            points += 1 
        special = ['!', '£', '$', '%', '&', '<', '*', '@']
        has_upper = has_lower = has_nums = has_special = False # allows mutiple variable assignments (can be dangerous if mutating lists)
        for char in listed:
            if char.isupper():
                has_upper = True
            if char.islower:
                has_lower = True
            if char.isnumeric():
                has_nums = True
            if special.__contains__(char):
                has_special = True
        if has_upper:
            points += 1
        if has_lower:
            points += 1
        if has_nums:
            points += 1
        if has_special:
            points += 1

        if points <= 2:
            print('This is a weak password')
        elif points <= 4:
            choice = input('this password could be improved, do you want to try again? y/n: ')
            if choice == 'n':
                repeat = False
        elif points == 5:
            print('this is a strong password')
            repeat = False
    return password


def create_user():
    repeat = True
    while repeat:
        name = input('enter a user ID: ')
        if not find_user(name):
            print('ID taken, please enter a different ID')
        else:
            repeat = False
    create_password()

# create_user()

def display_options():
    # repeat = True
    # while repeat:
    print(' 1) Create a new User ID \n 2) Change a password \n 3) Display all User IDs \n 4) Quit')
    choice = int(input('choose an option from above: '))
    if choice == 1:
        create_user()


# display_options()
