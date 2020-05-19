

#  ------- Tuples, Lists & Dicts --------

# EXTRA:
# delete an item at a certain index with:
fruit = ['apple', 'orange', 'pear', 'pineapple', 'dragon fruit', 'lychee']
del fruit[0:6:2] # <-------------- works like splice [start:end(not inclusive):step] / can put one index
print(fruit)
fruit.remove('lychee') # deletes first match
# also pop(index)

# to insert item at specific index:
fruit.insert(1, 'star fruit')
print(fruit)


# | p.63 - 078 |

shows = ['GOT', 'West World', 'Vikings', 'Medici', 'Tiger King']
print(('\n').join(shows))
new_show = input('name of new show: ')
position = int(input('position of show: '))

shows.insert(position, new_show)
print(('\n').join(shows))
