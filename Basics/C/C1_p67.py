
#  ------- More string Manipulation --------

# EXTRA:
# Every letter & space has an index number in a string


# | p.69 - 085 |

def num_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num = 0
    if isinstance(name, str):
        for letter in name.lower():
            if letter in vowels:
                num += 1
        print(f'there are {num} vowels in your name')
        return num
    raise TypeError('Please provide a string argument')

