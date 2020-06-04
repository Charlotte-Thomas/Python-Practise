from tkinter import *
from tkinter import ttk # needed to add for mac

#  ------- Tkinter GUI --------

# Tkinter does not work properly on Macs 
# I believe it is due to using homebrew to install python

def Call():
    print("hi")
    button["bg"] = "pink"
    button["fg"] = "pink"


window = Tk()
window.title("title")
window.geometry("400x150")
button = ttk.Button(text="Say Hello", command="Call")
button.place(x=30, y=30, width=130, height=25)
window.mainloop()


# | p.114 - 124 |


# def greet(window, name):
#     message = Label(window, text=f"Hello {name}")
#     message.place(x=25, y=55)


# def create_window():
#     window = Tk()
#     window.title("title")
#     window.geometry("400x150")
#     entry = Entry(text=0)
#     entry["justify"] = "center"
#     entry.place(x=20, y=10, width=100, height=25)

#     button = Button(text="Say Hello", command=greet(window, entry["text"]))
#     button.place(x=20, y=50, width=100, height=25)
#     window.mainloop()

# create_window()


