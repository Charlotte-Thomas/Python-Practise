
# ------------- Lists ----------------

# will create a list with six 2's in it
myList = [2] * 6
print(myList)  # ----> [2, 2, 2, 2, 2, 2]

# if you don't specify when to stop (2nd arg) it will go through whole list
# if you don't specify start index it also starts from 1st item
new_list = myList[3:]
new_list.append(1)
print(new_list)

# reverses the list
print(new_list[::-1])

# three ways to copy lists:
copy_1 = new_list[:]
copy_2 = new_list.copy()
copy_3 = list(new_list)
print(copy_1, copy_2, copy_3)

# list comprehension - advanced way to copy 
# this example gives squared items 
orig_list = [1, 2, 3, 4, 5, 6]
copied_list = [i*i for i in orig_list]
print(copied_list)


