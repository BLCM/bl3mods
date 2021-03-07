# Going to try to import only what I need to save on space and calculation time
# My files
from bl3data import BL3Data
from __info_function__ import Create_HotFix_File, FileChoice
from _global_lists import Mod_Header, Reg_hotfix, Search_Results
from _global_lists import List_Info
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import Entry, Button, Label, Tk, StringVar, Frame
from tkinter import DISABLED
################################################################################################################################################################
# Global variables
data = BL3Data()
################################################################################################################################################################
#Creates a new window for the user to see and for the commands to be used
def SelectionWindow(Func):
    # Global/Window variables
    SelectionWindow = Tk()
    Frame_Left = Frame(SelectionWindow, relief='ridge',borderwidth = 2)
    Frame_Right = Frame(SelectionWindow, relief='ridge',borderwidth = 2)
    Frame_Bottom = Frame(SelectionWindow, relief='ridge',borderwidth = 2)
    # Default values for window sizes, can manipulate inside the functions
    w = 500
    h = 350 
    ws = SelectionWindow.winfo_screenwidth()
    hs = SelectionWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # These variables will determine how many things to add to the window as i need them
    Lab, Ent, Butt = 0, 0, 0
    # Generics we can reuse for any task I have created
    Entry_1, Entry_2, Entry_3, Entry_4, Entry_5, Entry_6 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    
    # Used to grab the values the then entry textvariables,
    def Get_Val(Type):
        # Puts information into a queue to be executed later
        if Type == "ModHeader":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Puts the Information to make the file into a queue to be called later
            Mod_Header.extend([A, B, C, D, E, F])
        # Allows for the creation of multiple regular hotixes
        elif Type == "HotFix":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Info is put into a regular hotfix queue for later
            Reg_hotfix.extend([A, B, C, D, E, F])
        # This will search the database for provided information
        elif Type == "Search":
            Search = Entry_1.get()
            Info = data.get_refs_from_data(Search)
            for Details in Info:
                if Details[0] not in Search_Results:
                    Search_Results.append(Details[0])
    
    if Func == "ModHeader":  # Creates a mod file of you to use
        SelectionWindow.title("Mod Header")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x/4, y))

        Lab = 6
        Ent = 6
        Label_1_Text = 'Name of the hotfix file: '
        Label_2_Text = 'The actual mod name: '
        Label_3_Text = 'Author(s) name: '
        Label_4_Text = 'Discription: '
        Label_5_Text = 'Version of this mod: '
        Label_6_Text = 'The catagory in which this mods fits to: '

        Button_1_Text = 'Create Mod Header'
        def Button_1_Command(): return Get_Val("ModHeader")
        Butt = 1

    #This will make the user put hotfix information into a queue to be executed later
    elif Func == "HotFix":
        SelectionWindow.title("Creating Regular Hot Fix.")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x, y/10))

        Lab = 6
        Ent = 6
        Label_1_Text = 'Hotfix Type: (Package Tuple)'
        Label_2_Text = 'Map Name: (Object Name)'
        Label_3_Text = 'JSON Path + _JWP_ Object: (Attribute Name)'
        Label_4_Text = 'JSON Attribute: ("From" Length)'
        Label_5_Text = 'True or type new value: ("From" Value)'
        Label_6_Text = 'For right now type "", ("To" Value)'

        Button_1_Text = "Add This Regular Hotfix To The Queue"
        def Button_1_Command(): return Get_Val("HotFix")
        Butt = 1
    
    # The user will search for a word, and puncuation does not matter, but spelling does
    elif Func == "Search":
        SelectionWindow.title("Find All References")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x*1.8, y))

        Lab = 1
        Ent = 1
        Label_1_Text = 'Enter what you want to search for: \nSometimes the program will take a \nwhile to load in all the data, so be patient with it.'

        Button_1_Text = "Search"
        def Button_1_Command(): return Get_Val("Search")
        Butt = 1
    
    # Reuseable variables, saves on code space and looks nicer
    # Labels
    if Lab >= 1:
        Label(Frame_Left, text=Label_1_Text)
    if Lab >= 2:
        Label(Frame_Left, text=Label_2_Text)
    if Lab >= 3:
        Label(Frame_Left, text=Label_3_Text)
    if Lab >= 4:
        Label(Frame_Left, text=Label_4_Text)
    if Lab >= 5:
        Label(Frame_Left, text=Label_5_Text)
    if Lab >= 6:
        Label(Frame_Left, text=Label_6_Text)

    for c in sorted(Frame_Left.children):
        Frame_Left.children[c].pack(expand=True, fill="both")

    # Entries
    if Ent >= 1:
        Entry(Frame_Right, textvariable=Entry_1, width=100)
    if Ent >= 2:
        Entry(Frame_Right, textvariable=Entry_2, width=100).pack(expand=True, fill="both")
    if Ent >= 3:
        Entry(Frame_Right, textvariable=Entry_3, width=100).pack(expand=True, fill="both")
    if Ent >= 4:
        Entry(Frame_Right, textvariable=Entry_4, width=100).pack(expand=True, fill="both")
    if Ent >= 5:
        Entry(Frame_Right, textvariable=Entry_5, width=100).pack(expand=True, fill="both")
    if Ent >= 6:
        Entry(Frame_Right, textvariable=Entry_6, width=100).pack(expand=True, fill="both")

    for c in sorted(Frame_Right.children):
        Frame_Right.children[c].pack(expand=True, fill="both")

    # Buttons
    if Butt >= 1:
        Button(Frame_Bottom, font=("Times New Roman", 14), text=Button_1_Text, command=Button_1_Command)
    # if b >= 2:
        # Button(Nwindow, font=("Times New Roman", 14), text=b2text, command=b2command).grid(row=l, column=1)
    for c in sorted(Frame_Bottom.children):
        Frame_Bottom.children[c].pack(expand=True, fill="both")
    
    
    Frame_Left.grid(column=0, row=0)
    Frame_Right.grid(column=1, row=0)
    Frame_Bottom.grid(column=0, row=1)
################################################################################################################################################################
# Main menu.
if __name__ == "__main__":
    MainWindow = tk.Tk()
    MainWindow.title("Hot Fix Generator")
    w = 500
    h = 350 
    ws = MainWindow.winfo_screenwidth()
    hs = MainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    Button(text="Add To Mod Header Queue",font=("Times New Roman", 14), command=lambda: SelectionWindow("ModHeader"))
    Button(text="Add To Regular HotFix Queue", font=("Times New Roman", 14), command=lambda: SelectionWindow("HotFix"))
    Button(text="Add To Table HotFix Queue", font=("Times New Roman", 14), state=DISABLED)
    Button(text="Choose JSON File To Look Through", font=("Times New Roman", 14), command=lambda: FileChoice())
    Button(text="Database Search", font=("Times New Roman", 14), command=lambda: SelectionWindow("Search"))
    Button(text="Stored Information", font=("Times New Roman", 14), command=lambda: List_Info())
    Button(text="Create Your HotFix File\nNOTE: Fill Out Queues Before Clicking", font=("Times New Roman", 14), command=lambda: Create_HotFix_File())
    
    # Formats all my wigits the same way
    for c in sorted(MainWindow.children):
        MainWindow.children[c].pack(expand=True, fill="both")
    MainWindow.mainloop()
################################################################################################################################################################