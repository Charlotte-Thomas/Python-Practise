
# use Control + Option + N : to run code
# use Control + Option + M : to stop running code

while True:

# 011 enter a num > 100 and then a num < 10 & tell user how many times the smaller num goes into the larger
    num1 = int(input('enter a number larger than 100 '))
    num2 = int(input('enter a number smaller than 10 '))
    division = num1 // num2
    print(num2, ' goes into', num1, '', division, ' times')


