

#  ------- Tuples, Lists & Dicts --------

# EXTRA:
# delete an item at a certain index with:
fruit = ['apple', 'orange', 'pear', 'pineapple', 'dragon fruit', 'lychee']
# <-------------- works like splice [start:end(not inclusive):step] / can put one index
del fruit[0:6:2]
print(fruit)
fruit.remove('lychee')  # deletes first match
# also pop(index)

# to insert item at specific index:
fruit.insert(1, 'star fruit')
print(fruit)


# | p.62 - 069 |

def get_country_index(match):
    if isinstance(match, str):
        countries = ('England', 'USA', 'Australia', 'France')
        for country in countries:
            if match.lower() == country.lower():
                print('index of this country is: ', countries.index(country))
                return countries.index(country)
        raise Exception('Not a country in the list')
    raise TypeError('Please provide a string argument')


# | p.62 - 0.74 |

def colour_range(start, end):
    if isinstance(start, int) and isinstance(end, int):
        if 4 >= start >= 0 and 5 <= end <= 9:
            colours = ['blue', 'yellow', 'red', 'green', 'black', 'pink', 'purple', 'grey', 'white', 'orange']
            new_colours = colours[start:end]
            print(new_colours)
            return new_colours
        raise Exception('Please provide a number between 0-4 [0] and 5-9 [1]')
    raise TypeError('Please provide an int argument')
colour_range(0, 9)

# | p.63 - 078 |


def add_show():
    shows = ['GOT', 'West World', 'Vikings', 'Medici', 'Tiger King']
    print(('\n').join(shows))
    new_show = input('name of new show: ')
    position = int(input('position of show: '))

    shows.insert(position, new_show)
    print(('\n').join(shows))


def add_show_test_version(new_show, position):
    shows = ['GOT', 'West World', 'Vikings', 'Medici', 'Tiger King']
    if isinstance(new_show, str) and isinstance(position, int):
        shows.insert(position, new_show)
        print((shows))
        return shows
    raise TypeError(
        'Please provide a string argument [0] and an int argument [1]')

