

#  ------- 2D Lists and Dicts --------

# EXTRA:

# Lists within a List
# e.g. [[4,5,6], [2,7,8], [3,1,8]]
# OR as dicts within a list:
# e.g. [{Month: May, Day: 5th}, {Month: June, Day: 10th}]
# OR dicts within a dict



# | p.82 - 096 & 097 |

def choose_value():
    grid = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    for row in grid:
        print(row)
    row = int(input('choose a row (0-3): '))
    column = int(input('choose a column (0-2): '))
    print(f'value = {grid[row][column]}')
    return grid[row][column]


# | p.82 - 102 |

def get_info(people):
    if isinstance(people, list) and len(people) == 3:
        for person in people:
            if not isinstance(person, dict) or not person.__contains__('name') or not person.__contains__('age') or not person.__contains__('shoe_size'):
                raise Exception('incorrect argument formatting')
        print('\n' + people[0]['name'], '\n' + people[1]['name'], '\n' + people[2]['name'])
        user_choice = str(input('Pick a name to see their age and shoe size: ')).lower()
        for person in people:
            if person['name'].lower() == user_choice:
                print(f'{person["name"]} is {person["age"]} years old and has a shoe size of {person["shoe_size"]}') # have to use double quotes in f string
                return [person['age'], person['shoe_size']]
        raise Exception('this person does not exist within the list')
    raise TypeError('Please provide a list with a length of 3')
            

# get_info([
#     {'name': 'Jess', 'age': 30, 'shoe_size': 5},
#     {'name': 'George', 'age': 45, 'shoe_size': 6},
#     {'name': 'Mary', 'age': 25, 'shoe_size': 7}
# ])


