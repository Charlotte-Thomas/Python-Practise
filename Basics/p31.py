
# import math

#  ------- Maths --------

# EXTRA:
# to round to a certain no. of decimal places:
print(round(12.3333, 2))  # rounds to 2 dps

# | p.32 - 034 |
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


#  ------- For Loops --------

# EXTRA:
# first arg is start num, 2nd is range, 3rd is how much is added (or subtracted) to i every loop
for i in range(1, 10, 2):
    print(i)
# you can also loop through strings

# | p.37 - 044 |
people = int(input("number of people invited: "))
if people < 10:
    for i in range(0, people):
        name = input("name of person: ")
        print(name, "has been invited: ")
else:
    print("too many people")


#  ------- While Loops --------

# EXTRA:
# while loop where input decides when it ends
carry_on = "yes"
while carry_on == "yes":
    print(":)")
    carry_on = input("carry on? yes / no: ")
