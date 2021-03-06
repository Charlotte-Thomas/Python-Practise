
from array import *
import random

#  ------- Numeric Arrays --------

# EXTRA:
# Arrays are only used to store numbers
# must define the data type (i, l, f or d) which cannot be changed

array_nums = array('i', [12, 100, 5, 17])  # <------ example
array_nums.reverse()  # returns None so can't assign / directly print this
print(array_nums)


# | p.74 - 090 |

def create_array(nums):
    if isinstance(nums, list) and len(nums) == 5:
        new_array = array('i', [])
        for num in nums:
            if isinstance(num, int) and 10 <= num <= 20:
                new_array.append(num)
            else:
                print(f'{num} is outside the range (10-20), a float or a string')
        print('Thank you,')
        for num in new_array:
            print(num)
        return new_array
    raise Exception('please enter a list of 5 integers')


# | p.74 - 092 |

def conjoin_arrays(nums):
    if isinstance(nums, list) and len(nums) == 3:
        new_array = array('i', [])
        for num in nums:
            if isinstance(num, int):
                new_array.append(num)
            else:
                raise TypeError('Please provide a list of integers only')

        random_array = array('i', [])
        while len(random_array) < 5:
            random_array.append(random.randint(0, 100))
        random_array.extend(new_array)
        print(sorted(random_array))
        return sorted(random_array)

    raise Exception('please enter a list of 3 integers')



# | p.74 - 092 |

def divide_array():
    choices = array('f', [10.56, 20.43, 44.87, 63.45, 98.73])
    user_num = int(input('Input an integer between 2 & 5: '))
    if  2 <= user_num <= 5:
        new_array = [] # can't be numeric array because it won't accept rounded numbers
        for choice in choices:
            divided = round(choice / user_num, 2)
            print(divided)
            new_array.append(divided)
        print(new_array)
        return new_array
    raise Exception(f'Please enter a number between 2 & 5, you picked {user_num}')
