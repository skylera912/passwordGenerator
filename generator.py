        ### Password Generator by Skyler Anderson (Ver. 1.0) ###

import random
import string
import tkinter as tk

        ### Configures the Window, Icon, and Background Color
root = tk.Tk()
root.geometry("500x200")
root.title("Password Generator! - v1.0 (Skyler Anderson)")
icon_photo = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, icon_photo)
root.configure(background = '#E7E595')

        ### Creates a list of adjectives from a file to help make a stronger password.
lines_list = open('words.txt').read().splitlines()

        ### Creates a combined string from user input and writes to a file
def createPassword():
    passwordUse = e1.get()
    specialWord = e2.get()
    random_word_int = random.randint(0,71)
    randomNumbers = string.digits
    randomNumbers = (''.join(random.choice(randomNumbers) for i in range(2)))
    randomSymbol = string.punctuation
    randomSymbol = (''.join(random.choice(randomSymbol) for i in range(1)))
    password = lines_list[random_word_int] + specialWord + randomNumbers + randomSymbol
    text_file = open("library.txt", "a")
    text_file.write("%s = %s\n" %(passwordUse, password))
    text_file.close()

        ### All Tkinter GUI Objects Grouped Here
e1 = tk.Entry(root)
e2 = tk.Entry(root)
tk.Label(root, text="What is this password being used for?: ", bg = '#E7E595').grid(row=2)
tk.Label(root, text="Enter a word you want included in your password: ", bg = '#E7E595').grid(row=3)
tk.Button(root, command = createPassword, text = "Create Password", bg = 'white').grid(row=4, column = 1)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

        ### This was a test method to debug my input issues
# def checkEntry():
#     passwordUse = e1.get()
#     specialWord = e2.get()
#     print(passwordUse)
#     print(specialWord)

        ### Loops the GUI to keep it running
root.mainloop()