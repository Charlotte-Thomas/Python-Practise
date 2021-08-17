def minion_game(string):
    # split string
    # check for single letters
    # go through whole word cutting short by 1 letter
    # move to next lettter and loop through the rest etc.
    kevin = 0
    stuart = 0
    vowels = ["A", "E", "I", "O", "U"]
    split = [s for s in string]
    print(split)
    for letter in enumerate(split):
        if letter[1] not in vowels:
            stuart += len(split) - letter[0]
        else:
            kevin += len(split) - letter[0]
    if kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Stuart', stuart)
minion_game('BANANA')