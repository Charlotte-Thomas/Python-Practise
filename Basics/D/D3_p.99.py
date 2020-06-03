import csv

#  ------- Subprograms --------

# | p.102 - 118 |

def get_num():
    num = int(input('enter a number: '))
    return num


def count():
    num = get_num()
    for number in range(1, num + 1):
        print(number)

