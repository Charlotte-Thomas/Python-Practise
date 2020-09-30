# ------------- Sets ----------------
# skipped the rest of this section (look back if you use sets in future)

# sets are unordered, mutable lists with NO DUPLICATES
my_set = {1, 2, 3, 4, 4, 4}
print(my_set)  # ----> {1, 2, 3, 4}

# they have no order:
new_set = set('hello')
print(new_set)

# mutable
my_set.add(6)
my_set.remove(2)
my_set.discard(3)
print(my_set)
my_set.pop() 
my_set.clear() # completely clears the set

