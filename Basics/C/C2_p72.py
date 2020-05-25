
from array import *

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
        print('Thank you,', new_array)
        for num in new_array:
            print(num)
        return new_array
    raise Exception('please enter an array of 5 integers')

