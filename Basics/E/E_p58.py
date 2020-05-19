

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


# | p.63 - 069 |

def get_country_index(match):
    if isinstance(match, str):
        countries = ('England', 'USA', 'Australia', 'France')
        for country in countries:
            if match.lower() == country.lower():
                print('index of this country is: ', countries.index(country))
                return countries.index(country)
        raise Exception('Not a country in the list')
    raise TypeError('Please provide a string argument')


# | p.63 - 078 |


def add_show():
    shows = ['GOT', 'West World', 'Vikings', 'Medici', 'Tiger King']
    print(('\n').join(shows))
    new_show = input('name of new show: ')
    position = int(input('position of show: '))

    shows.insert(position, new_show)
    print(('\n').join(shows))
