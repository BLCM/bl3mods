import tkinter as tk 
from tkinter import *

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    window.geometry("500x500")
    text1 = Button(text="1. Mod Header", font=("Times New Roman", 18))
    text2 = Button(text="2. Choose File", font=("Times New Roman", 18))
    text3 = Button(text="3. Find All References", font=("Times New Roman", 18))
    text4 = Button(text="4. Make Regular Hotfix", font=("Times New Roman", 18))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    #add all widgets before
    window.mainloop()