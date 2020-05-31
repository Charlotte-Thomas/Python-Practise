

#  ------- Text Files --------

# EXTRA:
# text files are a way of storing data
# you can read, write and append to a text file
# not easy to alter so often better to use SQL db


# | p.88 - 106 |

def write_file():
    file = open('Names.txt', 'w')
    file.write('Rebecca\n')
    file.write('Bob\n')
    file.write('Jerry\n')
    file.write('Tash\n')
    file.write('Natalie\n')
    file.close()


# | p.88 - 107 |

def open_file():
    file = open('Names.txt', 'r')
    print(file.read())
    file.close()


# | p.88 - 108 |

def append_file():
    file = open('Names.txt', 'a')
    new_name = input('enter a new name: ').capitalize()
    file.write(new_name + '\n')
    file.close()
    file = open('Names.txt', 'r')
    print(file.read())
    file.close()


# | p.88 - 110 |

def alter_file():
    file = open('Names.txt', 'r')
    print(file.read())
    file.close()

    file = open('Names.txt', 'r')
    new_name = input('pick a name from the list: ').capitalize() + '\n'
    for name in file:
        if name != new_name:
            file = open('Names2.txt', 'a')
            file.write(name)
            file.close()
    file.close()
