from __Generate_Hotfix import JSONInfo, Search, Create_HotFix_File
from bl3data import BL3Data
from _global_lists import FileNames, Mod_Header, Reg_hotfix, Information
import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
data = BL3Data()

#This is used as a referencesto look and see what are the names of the game folders
#the user is able to choose a json file
def FileChoice():
    file = askopenfilename(filetypes=[("Choose file", ".json")])
    # Removes the files extention, as we dont need it
    raw_path = os.path.splitext(file)[0]
    i = 0
    index = 0
    while index <= 0:
        Find = "/" + FileNames[i]
        i += 1
        if Find in raw_path:
            index = raw_path.find(Find)
    # this is the data we need to pass in information
    True_Path = raw_path[index::]
    JSONInfo(True_Path)

#Creates a new window for the user to see and for the commands to be used
def NeWindow(func):
    Nwindow = Tk()    
    #these variables will determine how many things to add to the window as i need them
    l, e, b = 0, 0, 0
    #generics we can reuse for any task I have created
    entry1 = StringVar(Nwindow)
    entry2 = StringVar(Nwindow)
    entry3 = StringVar(Nwindow)
    entry4 = StringVar(Nwindow)
    entry5 = StringVar(Nwindow)
    entry6 = StringVar(Nwindow)
    
    # Used to grab the values the then entry textvariables, 
    # So that for any function I can call them and reuse them
    def get_val(type):
        if type == "ModHeader":
            a, b, c, d, e, f = entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            Mod_Header.extend([a, b, c, d, e, f])
        elif type == Search:
            a = entry1.get()
            Search(a)
        elif type == "HotFix":
            a, b, c, d, e, f = entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            Reg_hotfix.extend([a, b, c, d, e, f])

    #So now this works for the most part. the inner code still needs to work
    if func == "ModHeader":  # creates a mod file of you to use
        Nwindow.title("Mod Header")
        text1 = 'Name of the hotfix file: '
        text2 = 'The actual mod name: '
        text3 = 'Author(s) name: '
        text4 = 'Discription: '
        text5 = 'Version of this mod: '
        text6 = 'The catagory in which this mods fits to: '
        b1text = 'Create Mod Header'
        l = 6
        e = 6
        def b1command(): return get_val("ModHeader")
        b = 1
    
    elif func == "HotFix":
        Nwindow.title("Creating Regular Hot Fix. NOTE: Very much a WIP, so things will be buggy")
        text1 = 'Enter what type of hotfix you want to make: '
        text2 = 'What Map is this affecting, or type MatchALL'
        text3 = 'File Path with JSON name and what \n__JWP__ Object you want to grab from that JSON file: '
        text4 = 'What you want to manipulate in the JSON file \n(WIP, will be better later on both discription and whatvalues to grab):'
        text5 = 'Type True for most things, else hit enter: '
        text6 = 'For right now type "", will give better instructions later when I understand it more'
        l = 6
        e = 6
        b1text = "Add This Regular Hotfix To The Queue"
        def b1command(): return get_val("HotFix")
        b2text = "Click To See List Of Patch Types and Map Areas"
        def b2command(): return Information()
        b = 2

    # Come back to this function later, as it is giving me to much grief right now
    elif func == JSONInfo:  # this will be more fleshed out later, but for now it I am trying to get the interfce to work
        Nwindow.title("Look Through File information")
        l = 0
        e = 0   

        b1text = "Choose file"
        def b1command(): return FileChoice()
        b = 1

    elif func == Search:
        Nwindow.title("Find All References")
        text1 = 'Enter what you want to search for: '
        l = 1
        e = 1 

        b1text = "Search"
        def b1command(): return get_val(Search)
        b = 1


    # This is the best way for the program to reuse generics, 
    # While being able to determine how many are needed for a paticular program
    #These are Labels
    if l >= 1:
        Label(Nwindow, text=text1).grid(row=0)
    if l >= 2:
        Label(Nwindow, text=text2).grid(row=1)
    if l >= 3:
        Label(Nwindow, text=text3).grid(row=2)
    if l >= 4:
        Label(Nwindow, text=text4).grid(row=3)
    if l >= 5:
        Label(Nwindow, text=text5).grid(row=4)
    if l >= 6:
        Label(Nwindow, text=text6).grid(row=5)
    
    #Entries
    if e >= 1:
        Entry(Nwindow, textvariable=entry1, width=100).grid(row=0, column=1)
    if e >= 2:
        Entry(Nwindow, textvariable=entry2, width=100).grid(row=1, column=1)
    if e >= 3:
        Entry(Nwindow, textvariable=entry3, width=100).grid(row=2, column=1)
    if e >= 4:
        Entry(Nwindow, textvariable=entry4, width=100).grid(row=3, column=1)
    if e >= 5:
        Entry(Nwindow, textvariable=entry5, width=100).grid(row=4, column=1)
    if e >= 6:
        Entry(Nwindow, textvariable=entry6, width=100).grid(row=5, column=1)
    
    #Buttons
    if b >= 1:
        Button(Nwindow, font=("Times New Roman", 18), text=b1text, command=b1command).grid(row=l)
    if b >= 2:
        Button(Nwindow, font=("Times New Roman", 18), text=b2text, command=b2command).grid(row=l, column=1)

#after gelizing my mistake, I now relize that I must combine two of these things in order to work
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="1. Add To Mod Header Queue", font=("Times New Roman", 18), command=lambda: NeWindow("ModHeader"))
    Button(text="2. Choose File To Search Through", font=("Times New Roman", 18), command=lambda: NeWindow(JSONInfo), state=DISABLED) #Will reenable later once i can get it working
    Button(text="3. Find All References To An Object", font=( "Times New Roman", 18), command=lambda: NeWindow(Search))
    Button(text="4. Add To The HotFix", font=( "Times New Roman", 18), command=lambda: NeWindow("HotFix"))
    Button(text="Click This To Create Your HotFix File", font=( "Times New Roman", 18), command=lambda: Create_HotFix_File())
    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    window.mainloop()