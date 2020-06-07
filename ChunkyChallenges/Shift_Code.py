
# | p.150 - 146 |

# list alphabet
# while loop to start the process
# ignore/skip punctuation & spaces (list them)
# split code and use length as loop num for each character
# convert each char by the num entered by user
# join code at the end and present to user


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

skip = [' ', '\'', '.', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def convert_msg():
    msg = input('enter message to be coded: ')
    num = int(input('enter number (1 - 25) to shift message by: '))
    code = []
    for char in list(msg):
        if not skip.__contains__(char):
            new_position = alphabet.index(char) + num
            if new_position >= 26:
                new_position -= 26
            code.append(alphabet[new_position])
        else:
            code.append(char)
    print('your coded message is:', ('').join(code))


def present_options():
    print(' 1) Make a code \n 2) Decode a message \n 3) Quit')
    choice = input('choose an option: ')
    if choice == '1':
        convert_msg()


present_options()
