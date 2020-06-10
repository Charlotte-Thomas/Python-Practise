
import csv
# | p.156 - 148 |

# display options to user in while loop
# function for each option and subfunctions to use across each (get data, password creation, find user)

def read_data():
    data = []
    file = open('ChunkyChallenges/Passwords/Passwords.csv', 'r')
    reader = list(csv.reader(file))
    for row in reader:
        data.append(row)
    file.close()
    return data

def find_user(name):
    data = read_data()
    for user in data:
        if name == user[0]:
            return [True, data.index(user)]
    return [False, None]

def create_password():
    repeat = True
    while repeat:
        points = 0
        password = input('please enter a password: ')
        listed = list(password)
        if len(listed) >= 8:
            points += 1 
        special = ['!', '£', '$', '%', '&', '<', '*', '@']
        has_upper = has_lower = has_nums = has_special = False # allows multiple variable assignments (can be dangerous if mutating lists)
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
        if find_user(name)[0]:
            print('ID taken, please enter a different ID')
        else:
            repeat = False
    return name

def change_password():
    data = read_data()
    user = input('enter ID of user: ')
    match = find_user(user)
    if match[0]:
        new_pass = create_password()
        data[match[1]][1] = new_pass
        print(data)
        file = open('ChunkyChallenges/Passwords/Passwords.csv', 'w')
        for row in data:
            file.write(f'{row[0]},{row[1]}\n')
        file.close()

def display_ids():
    data = read_data()
    for row in data:
        print(row[0])

def display_options():
    # repeat = True
    # while repeat:
    print(' 1) Create a new User ID \n 2) Change a password \n 3) Display all User IDs \n 4) Quit')
    choice = int(input('choose an option from above: '))
    if choice == 1:
        name = create_user()
        password = create_password()
        file = open('ChunkyChallenges/Passwords/Passwords.csv', 'a')
        file.write(f'{name},{password}\n')
        file.close()
    elif choice == 2:
        change_password()
    elif choice == 3:
        display_ids()

display_options()
