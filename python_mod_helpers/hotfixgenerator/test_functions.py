from __Generate_Hotfix import ModHeader, JSONInfo, Search, HotFix
from bl3data import BL3Data
from _global_lists import FileNames
import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename

#after gelizing my mistake, I now relize that I must combine two of these things in order to work
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="1. Mod Header", font=("Times New Roman", 18),
           command=lambda: NeWindow(ModHeader))
    Button(text="2. Choose File", font=("Times New Roman", 18),
           command=lambda: NeWindow(JSONInfo), state=DISABLED) #Will reenable later once i can get it working
    Button(text="3. Find All References", font=(
        "Times New Roman", 18), command=lambda: NeWindow(Search))
    # Button(text="4. Make Regular Hotfix", font=(
    #     "Times New Roman", 18), command=lambda: NeWindow(HotFix))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    window.mainloop()