from __Generate_Hotfix import JSONInfo, Search, Create_HotFix_File, FileChoice
from bl3data import BL3Data
from _global_lists import Mod_Header, Reg_hotfix, List_Info
import tkinter as tk
from tkinter import *
data = BL3Data()


#Creates a new window for the user to see and for the commands to be used
def SelectionWindow(func):
    SelectionWindow = Tk()
    #these variables will determine how many things to add to the window as i need them
    l, e, b = 0, 0, 0
    #generics we can reuse for any task I have created
    entry1, entry2, entry3, entry4, entry5, entry6 = StringVar(SelectionWindow), StringVar(
        SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)

    # Used to grab the values the then entry textvariables,
    # So that for any function I can call them and reuse them
    def Get_Val(type):
        if type == "ModHeader":
            a, b, c, d, e, f = entry1.get(), entry2.get(
            ), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            # Puts the Information to make the file into a queue to be called later
            Mod_Header.extend([a, b, c, d, e, f])
        elif type == "HotFix":
            a, b, c, d, e, f = entry1.get(), entry2.get(
            ), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            # info is put into a regular hotfix queue for later
            Reg_hotfix.extend([a, b, c, d, e, f])
        elif type == Search:
            a = entry1.get()
            Search(a)

    #So now this works for the most part. the inner code still needs to work
    if func == "ModHeader":  # creates a mod file of you to use
        SelectionWindow.title("Mod Header")
        text1 = 'Name of the hotfix file: '
        text2 = 'The actual mod name: '
        text3 = 'Author(s) name: '
        text4 = 'Discription: '
        text5 = 'Version of this mod: '
        text6 = 'The catagory in which this mods fits to: '
        l = 6
        e = 6

        b1text = 'Create Mod Header'
        def b1command(): return Get_Val("ModHeader")
        b = 1

    #This will make the user put hotfix information into a queue to be executed later
    elif func == "HotFix":
        SelectionWindow.title(
            "Creating Regular Hot Fix. NOTE: Very much a WIP, so things will be buggy")
        text1 = 'Enter what type of hotfix you want to make: \n(Package Tuple)'
        text2 = 'What Map is this affecting, or type MatchALL: \n(Object Name)'
        text3 = 'File Path with JSON name and what \n__JWP__ Object you want to grab from that JSON file: \n(Attribute Name)'
        text4 = 'What you want to manipulate in the JSON file \n(WIP, will be better later on both discription and whatvalues to grab): \n("From" Length)'
        text5 = 'Type True for most things, or type new value: \n("From" Value)'
        text6 = 'For right now type "", will give better instructions later when I understand it more: \n("To" Value)'
        l = 6
        e = 6

        b1text = "Add This Regular Hotfix To The Queue"
        def b1command(): return Get_Val("HotFix")
        b = 1

    # The user will search for a word, and puncuation does not matter, but spelling does
    elif func == Search:
        SelectionWindow.title("Find All References")
        text1 = 'Enter what you want to search for: \n NOTE: To look at your search results, please click the 5th button and go from there. \nSometimes the program will take a while to load in all the data, so be patient with it.'
        l = 1
        e = 1

        b1text = "Search"
        def b1command(): return Get_Val(Search)
        b = 1

    # This is the best way for the program to reuse generics,
    # While being able to determine how many are needed for a paticular program
    #These are Labels
    if l >= 1:
        Label(SelectionWindow, text=text1).grid(row=0)
    if l >= 2:
        Label(SelectionWindow, text=text2).grid(row=1)
    if l >= 3:
        Label(SelectionWindow, text=text3).grid(row=2)
    if l >= 4:
        Label(SelectionWindow, text=text4).grid(row=3)
    if l >= 5:
        Label(SelectionWindow, text=text5).grid(row=4)
    if l >= 6:
        Label(SelectionWindow, text=text6).grid(row=5)

    #Entries
    if e >= 1:
        Entry(SelectionWindow, textvariable=entry1, width=100).grid(row=0, column=1)
    if e >= 2:
        Entry(SelectionWindow, textvariable=entry2, width=100).grid(row=1, column=1)
    if e >= 3:
        Entry(SelectionWindow, textvariable=entry3, width=100).grid(row=2, column=1)
    if e >= 4:
        Entry(SelectionWindow, textvariable=entry4, width=100).grid(row=3, column=1)
    if e >= 5:
        Entry(SelectionWindow, textvariable=entry5, width=100).grid(row=4, column=1)
    if e >= 6:
        Entry(SelectionWindow, textvariable=entry6, width=100).grid(row=5, column=1)

    #Buttons
    if b >= 1:
        Button(SelectionWindow, font=("Times New Roman", 18),
               text=b1text, command=b1command).grid(row=l)
    # if b >= 2:
        # Button(Nwindow, font=("Times New Roman", 18), text=b2text, command=b2command).grid(row=l, column=1)


# Main menu.
if __name__ == "__main__":
    MainWindow = tk.Tk()
    MainWindow.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="Add To Mod Header Queue", font=(
        "Times New Roman", 18), command=lambda: SelectionWindow("ModHeader"))

    Button(text="Add To The HotFix Queue", font=(
        "Times New Roman", 18), command=lambda: SelectionWindow("HotFix"))

    Button(text="Choose File To Search Through", font=("Times New Roman", 18),
           command=lambda: FileChoice())  # Will reenable later once i can get it working
    
    Button(text="Find All References To An Object", font=(
        "Times New Roman", 18), command=lambda: SelectionWindow(Search))
    
    Button(text="Click To Look At Stored information", font=(
        "Times New Roman", 18), command=lambda: List_Info())

    Button(text="Click This To Create Your HotFix File", font=(
        "Times New Roman", 18), command=lambda: Create_HotFix_File())
    
    #this will pack everything so that I do not have to do it every time
    for c in sorted(MainWindow.children):
        MainWindow.children[c].pack()
    MainWindow.mainloop()
