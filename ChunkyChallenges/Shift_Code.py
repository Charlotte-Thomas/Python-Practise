
# | p.150 - 146 |

# list alphabet
# while loop to start the process
# ignore/skip punctuation & spaces (list them)
# split code and use length as loop num for each character
# convert each char by the num entered by user
# join code at the end and present to user


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def convert_msg():
    msg = input('enter message to be coded: ')
    print(list(msg))


def present_options():
    print(' 1) Make a code \n 2) Decode a message \n 3) Quit')
    choice = input('choose an option: ')
    if choice == '1':
        convert_msg()


present_options()
