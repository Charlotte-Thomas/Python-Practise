# ------------- Tuples ----------------

# notes: tuples are more efficient because they are smaller bytes-wise
# also takes less time to create a tuple than a list

my_tuple = (1, 2, 3, 4, 4, 4, 5)

# count how many of something is in a tuple
num_fours = my_tuple.count(4)
print(num_fours)

# turn into a list:
to_list = list(my_tuple)
print(to_list)

# back to tuple:
to_tuple = tuple(to_list)
print(to_tuple)

# unpacking a tuple
person = ('name', 'age', 'height')
name, age, height = person # num of elements must match num in tuple
print(name)
print(age)
print(height)

# unpacking tuples differently 
item_1, *item_2, item_3 = my_tuple # *item_2 means it takes all the items inbetween as a list
print(item_1, item_2, item_3)

item_1, item_2, *item_3 = my_tuple # this time  *item_3 will take all but the first 2 items
print(item_3)