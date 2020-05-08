
# use Control + Option + N : to run code
# use Control + Option + M : to stop running code

# while True:

# ------- Inputs --------

# | p.14 - 011 |
num1 = int(input('enter a number larger than 100: '))
num2 = int(input('enter a number smaller than 10: '))
division = num1 // num2
print(num2, ' goes into ', num1, '', division, ' times')

# ------- If Statements --------

# | p.21 - 0.19 |
num = int(input("Enter 1, 2 or 3: "))
if num == 1:
    print("thank you")
elif num == 2:
    print("well done")
elif num == 3:
    print("correct")
else:
    print("error message")

#  ------- Strings --------

# EXTRA :
# to strip certain letter / spaces from  string:
string = "hello world"
print(string.strip("h"))

# only includes specified letter indexes in string (spaces counted as indexes):
print(string[7:10])  # inlcudes 7, 8 & 9 only

# | p.28 - 026 |
string = input("enter a word: ").lower()
if string.startswith("a" or "e" or "i" or "o" or "u"):
    print(string + "way")
else:
    print(string[1:len(string)] + string[0] + "ay")
