import tkinter as tk 
from tkinter import *
from __Generate_Hotfix import test1, test2, test3, test4
#reference: https://www.geeksforgeeks.org/python-gui-tkinter/

#Creates a new window for the user to see and for the commands to be used
def NeWindow(func):
    Nwindow = Tk()
    #generics we can reuse for any task I have created
    entry1=StringVar(Nwindow)
    entry2=StringVar(Nwindow)
    entry3=StringVar(Nwindow)
    entry4=StringVar(Nwindow)
    entry5=StringVar(Nwindow)
    entry6=StringVar(Nwindow)

    #used to grab the values the then entry textvariables, so that for any function I can call them and reuse them
    def get_val(func):
        if func == test1:
            a,b,c,d,e,f = entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            test1(a,b,c,d,e,f)
            #this will be used to display what is going to put in the hotfix file
        elif func == test2:
            None
        elif func == test3:
            None
        elif func == test4:
            None
        
    
    if func == test1: #creates a mod file of you to use
        Nwindow.title("Mod header")
        Label(Nwindow, text= "Name of the hotfix file: ").grid(row=0)
        Entry(Nwindow, textvariable = entry1).grid(row = 0, column = 1)
        Label(Nwindow, text= "The actual mod name: ").grid(row=1)
        Entry(Nwindow, textvariable = entry2).grid(row = 1, column = 1)
        Label(Nwindow, text= "Author(s) name: ").grid(row=2)
        Entry(Nwindow, textvariable = entry3).grid(row = 2, column = 1)
        Label(Nwindow, text= "Discription: ").grid(row=3)
        Entry(Nwindow, textvariable = entry4).grid(row = 3, column = 1)
        Label(Nwindow, text= "Version of this mod: ").grid(row=4)
        Entry(Nwindow, textvariable = entry5).grid(row = 4, column = 1)
        Label(Nwindow, text= "The catagory in which this mods fits to: ").grid(row=5)
        Entry(Nwindow, textvariable = entry6).grid(row = 5, column = 1)
        Button(Nwindow, text="Create Mod Header", command = lambda: get_val(func)).grid(row = 6)
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
    Button(text="1. Mod Header", font=("Times New Roman", 18), command = lambda: NeWindow(test1))
    Button(text="2. Choose File", font=("Times New Roman", 18), command = lambda: NeWindow(test2))
    Button(text="3. Find All References", font=("Times New Roman", 18), command = lambda: NeWindow(test3))
    Button(text="4. Make Regular Hotfix", font=("Times New Roman", 18), command = lambda: NeWindow(test4))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    window.mainloop()