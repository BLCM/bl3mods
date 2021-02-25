import tkinter as tk 
from tkinter import Button, Label, Entry
from __Generate_Hotfix import test1, test2, test3, test4
#reference: https://www.geeksforgeeks.org/python-gui-tkinter/

#Creates a new window for the user to see and for the commands to be used
def newwindow(func):
    Nwindow = tk.Tk()
    # Nwindow.geometry("500x500")
    filename=tk.StringVar()
    modname=tk.StringVar()
    authorname=tk.StringVar()
    discname=tk.StringVar()
    vername=tk.StringVar()
    catname=tk.StringVar()

    if func == test1:
        Nwindow.title("Mod header")
        Label(Nwindow, text= "Name of the hotfix file: ").grid(row=0)
        Entry(Nwindow, textvariable = filename).grid(row = 0, column = 1)
        Label(Nwindow, text= "The actual mod name: ").grid(row=1)
        Entry(Nwindow, textvariable = modname).grid(row = 1, column = 1)
        Label(Nwindow, text= "Author(s) name: ").grid(row=2)
        Entry(Nwindow, textvariable = authorname).grid(row = 2, column = 1)
        Label(Nwindow, text= "Discription: ").grid(row=3)
        Entry(Nwindow, textvariable = discname).grid(row = 3, column = 1)
        Label(Nwindow, text= "Version of this mod: ").grid(row=4)
        Entry(Nwindow, textvariable = vername).grid(row = 4, column = 1)
        Label(Nwindow, text= "The catagory in which this mods fits to: ").grid(row=5)
        Entry(Nwindow, textvariable = catname).grid(row = 5, column = 1)
        Button(Nwindow, text="Create Mod Header", command = lambda: test1(filename.get(), modname.get(), authorname.get(), discname.get(), vername.get(), catname.get())).grid(row = 6)
    elif func == test2:
        None
    elif func == test3:
        None
    elif func == test4:
        None

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="1. Mod Header", font=("Times New Roman", 18), command = lambda: newwindow(test1))
    Button(text="2. Choose File", font=("Times New Roman", 18), command = lambda: newwindow(test2))
    Button(text="3. Find All References", font=("Times New Roman", 18), command = lambda: newwindow(test3))
    Button(text="4. Make Regular Hotfix", font=("Times New Roman", 18), command = lambda: newwindow(test4))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack(side="top")
    #add all widgets before
    window.mainloop()