
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
