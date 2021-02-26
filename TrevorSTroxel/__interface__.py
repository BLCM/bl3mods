import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from __Generate_Hotfix import test1, test2, test3, test4
#reference: https://www.geeksforgeeks.org/python-gui-tkinter/

#This is used as a referencesto look and see what are the names of the game folders
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names

#the user is able to choose a json file


def filechoice():
    file = askopenfilename(filetypes=[("Choose file", ".json")])
    return file
#Creates a new window for the user to see and for the commands to be used


def NeWindow(func):

    #used to grab the values the then entry textvariables, so that for any function I can call them and reuse them
    def get_val(func):
        if func == test1:
            a, b, c, d, e, f = entry1.get(), entry2.get(
            ), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            test1(a, b, c, d, e, f)
        elif func == test2:
            None
        elif func == test3:
            None
        elif func == test4:
            None

    Nwindow = Tk()
    #generics we can reuse for any task I have created
    entry1 = StringVar(Nwindow)
    entry2 = StringVar(Nwindow)
    entry3 = StringVar(Nwindow)
    entry4 = StringVar(Nwindow)
    entry5 = StringVar(Nwindow)
    entry6 = StringVar(Nwindow)
    #attempting to use generics to make my life easier
    #this will change a lot later on, but for now i will try to get it to work
    l1 = Label(Nwindow, text="Name of the hotfix file: ").grid(row=0)
    l2 = Label(Nwindow, text="The actual mod name: ").grid(row=1)
    l3 = Label(Nwindow, text="Author(s) name: ").grid(row=2)
    l4 = Label(Nwindow, text="Discription: ").grid(row=3)
    l5 = Label(Nwindow, text="Version of this mod: ").grid(row=4)
    l6 = Label(
        Nwindow, text="The catagory in which this mods fits to: ").grid(row=5)

    e1 = Entry(Nwindow, textvariable=entry1).grid(row=0, column=1)
    e2 = Entry(Nwindow, textvariable=entry2).grid(row=1, column=1)
    e3 = Entry(Nwindow, textvariable=entry3).grid(row=2, column=1)
    e4 = Entry(Nwindow, textvariable=entry4).grid(row=3, column=1)
    e5 = Entry(Nwindow, textvariable=entry5).grid(row=4, column=1)
    e6 = Entry(Nwindow, textvariable=entry6).grid(row=5, column=1)

    b1 = Button(Nwindow, text="Create Mod Header",
                command=lambda: get_val(func)).grid(row=6)

    if func == test1:  # creates a mod file of you to use
        Nwindow.title("Mod Header")

    elif func == test2:  # this will be more fleshed out later, but for now it I am trying to get the interfce to work
        Nwindow.title("Look Through File information")
        path = Button(Nwindow, text="Select File", command=filechoice).grid(
            row=0)  # user sees a button they can click
        # Removes the files extention, as we dont need it
        raw_path = os.path.splitext(path)[0]
        i = 0
        index = 0
        while index <= 0:
            Find = "/" + FileNames[i]
            i += 1
            if Find in raw_path:
                index = raw_path.find(Find)
        # this is the data we need to pass in information
        True_Path = raw_path[index::]
        #will have new buttons added after the user clicks the file
    elif func == test3:
        None
    elif func == test4:
        None


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="1. Mod Header", font=("Times New Roman", 18),
           command=lambda: NeWindow(test1))
    Button(text="2. Choose File", font=("Times New Roman", 18),
           command=lambda: NeWindow(test2))
    Button(text="3. Find All References", font=(
        "Times New Roman", 18), command=lambda: NeWindow(test3))
    Button(text="4. Make Regular Hotfix", font=(
        "Times New Roman", 18), command=lambda: NeWindow(test4))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    window.mainloop()
