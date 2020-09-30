# ------------- Dictionaries ----------------

# pop last dict item:
dict_1 = {'name': 'Jerry', 'job': 'painter', 'married': True}
dict_1.popitem() 
print(dict_1)

# pop specific item
dict_1.pop('job')
print(dict_1)


# to make a copy:
copy = dict(dict_1)
print(copy)

# to merge two dicts / update a dict
dict_1 = {'name': 'Jerry', 'job': 'painter', 'married': True}
dict_2 = dict(name='Phil', job='painter', married=False, age=35) # this is just another way of making a dict

dict_1.update(dict_2)
print(dict_1)

# you can use tuples as a key (can't use lists)
tuple_dict = {(2,5): 10}