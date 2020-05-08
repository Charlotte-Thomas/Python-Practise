
import math

#  ------- Maths --------

# EXTRA:

# to round to a certain no. of decimal places:
print(round(12.3333, 2))  # rounds to 2 dps

# p.32 - 034 print "1) Square 2) Triangle", let user choose num.
# If 1: ask for one length of the square & display area, if 2: ask for base & height & display area else display error message.

print("1) Square \n2) Triangle")
choice = int(input("choose option 1 or 2: "))
if choice == 1:
    length = int(input("length of one side of the square: "))
    print("area of square = ", length**2)
elif choice == 2:
    base = int(input("base length of triangle: "))
    height = int(input("height of triangle: "))
    print("area of triangle = ", (base * height) / 2)
else:
    print("invalid choice")
