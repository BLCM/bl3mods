# Going to try to import only what I need to save on space and calculation time
# My files
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from bl3data import BL3Data
from __info_function__ import Create_HotFix_File, FileChoice
from _global_lists import Mod_Header, Reg_hotfix, DataBase_Results, Queue_Order, Comment_str, Header_lines_str
from _global_lists import List_Info, ListBoxWindow
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import Entry, Button, Label, Tk, StringVar, Frame
from tkinter import DISABLED
################################################################################################################################################################
# Global variables
data = BL3Data()
Stan_Font = ("Times New Roman", 10)
# Stan_Font = ("Wingdings 2", 12)
# Stan_Font = ("Courier New", 12)

################################################################################################################################################################
#Creates a new window for the user to see and for the commands to be used
def SelectionWindow(Func):
    # Global/Window variables
    SelectionWindow = Tk()
    #These are for sotring the feilds of information
    Frame_Left = Frame(SelectionWindow,borderwidth = 2)
    Frame_Right = Frame(SelectionWindow,borderwidth = 2)
    Frame_Bottom = Frame(SelectionWindow,borderwidth = 2)

    # Default values for window sizes for all, can manipulate inside the functions
    w, h, ws, hs = 500, 350, SelectionWindow.winfo_screenwidth(), SelectionWindow.winfo_screenheight()
    x,y = (ws/2) - (w/2), (hs/2) - (h/2)
    # These variables will determine how many things to add to the window as i need them
    Lab, Ent, Butt, hotfixoptions = 0, 0, 0, 0
    # To be able to grab the entry feilds
    Entry_1, Entry_2, Entry_3, Entry_4 = StringVar(Frame_Right), StringVar(Frame_Right), StringVar(Frame_Right), StringVar(Frame_Right)
    Entry_5, Entry_6, Entry_7, Entry_8 = StringVar(Frame_Right), StringVar(Frame_Right), StringVar(Frame_Right), StringVar(Frame_Right)
    
    def Get_Val(Type): # Used to grab the values the then entry textvariables
        # Information about your mod
        if Type == "ModHeader":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Puts the Information to make the file into a queue to be called later
            Mod_Header.extend([A, B, C, D, E, F])
        
        # Adds to the regular hot fix queue
        elif Type == "HotFix":
            A, B, C, D, E, F, G, H = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get()
            # Info is put into a regular hotfix queue for later
            Reg_hotfix.extend([A, B, C, D, E, F, G, H])
            Queue_Order.append("Regular hotfix")
        
        # Gives a frame of reference to what the Mod looks like
        elif Type == "Update Display":
            B, C, D, E, F, G, H = Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get()
            HotFix_Label["text"] = '[(1,1,{} , {}) , {} , {} , {} , {} , {}]'.format(B, C, D, E, F, G, H)        
        
        # This will search the database for provided information
        elif Type == "Search":
            Search = Entry_1.get()
            Info = data.get_refs_from_data(Search)
            # This will clean out the previous entry so that it does not become cluttered
            if len(DataBase_Results) > 0: DataBase_Results.clear()
            for Details in Info:
                if Details[0] not in DataBase_Results: DataBase_Results.append(Details[0])
            DataBase_Results.sort()
            ListBoxWindow(3)
    
    # Mod header info
    if Func == "ModHeader":  # Creates a mod file of you to use
        SelectionWindow.title("Mod Header")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x/4, y))
        Lab, Ent, Butt = 6, 6, 1
        Label_1_Text = 'Name of the hotfix file: '
        Label_2_Text = 'The actual mod name: '
        Label_3_Text = 'Author(s) name: '
        Label_4_Text = 'Discription: '
        Label_5_Text = 'Version of this mod: '
        Label_6_Text = 'The catagory in which this mods fits to: '
        Button_1_Text = 'Create Mod Header'
        def Button_1_Command(): return Get_Val("ModHeader")
   
    #Regular Hotfix Queue
    elif Func == "HotFix":
        SelectionWindow.title("Creating Regular Hot Fix.")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w*2, h, x, y/10))
        Lab, Ent, Butt = 8, 8, 2
        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = 'Map Name: (package)'
        Label_4_Text = 'JSON Path + JWP Object: (obj_name)'
        Label_5_Text = 'Attribute: (attr_name)'
        Label_6_Text = 'Lenght of the previous value, (prev_val_len)'
        Label_7_Text = 'True, False, or Leave Blank: (prev_val)'
        Label_8_Text = 'True or New Value Type (new_val)'

        Button_1_Text = "Add This Regular Hotfix To The Queue"
        def Button_1_Command(): return Get_Val("HotFix")
        Button_2_Text = "Look at what your HotFix looks like"
        def Button_2_Command(): return Get_Val("Update Display") 
        HotFix_Label = Label(Frame_Bottom, text = '{hf_type},(1,1,{notification_flag},{package}),{obj_name},{attr_name},{prev_val_len},{prev_val},{new_val}')
        hotfixoptions = 1
    
    # The user will search for a word, and puncuation does not matter, but spelling does
    elif Func == "Search":
        SelectionWindow.title("Find All References")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x*1.8, y))
        Lab, Ent, Butt = 1, 1, 1
        Label_1_Text = 'Enter what you want to search for: \nMay freeze on you. Do not worry, its just loading.'
        Button_1_Text = "Search"
        def Button_1_Command(): return Get_Val("Search")
    
    # Labels
    if Lab >= 1: Label(Frame_Left, text=Label_1_Text)
    if Lab >= 2: Label(Frame_Left, text=Label_2_Text)
    if Lab >= 3: Label(Frame_Left, text=Label_3_Text)
    if Lab >= 4: Label(Frame_Left, text=Label_4_Text)
    if Lab >= 5: Label(Frame_Left, text=Label_5_Text)
    if Lab >= 6: Label(Frame_Left, text=Label_6_Text)
    if Lab >= 7: Label(Frame_Left, text=Label_7_Text)
    if Lab >= 8: Label(Frame_Left, text=Label_8_Text)
    
    for c in sorted(Frame_Left.children):
        Frame_Left.children[c]["font"] = Stan_Font
        Frame_Left.children[c].pack(fill="both")

    # Entries
    if Ent >= 1: Entry(Frame_Right, textvariable=Entry_1)
    if Ent >= 2: Entry(Frame_Right, textvariable=Entry_2)
    if Ent >= 3: Entry(Frame_Right, textvariable=Entry_3)
    if Ent >= 4: Entry(Frame_Right, textvariable=Entry_4)
    if Ent >= 5: Entry(Frame_Right, textvariable=Entry_5)
    if Ent >= 6: Entry(Frame_Right, textvariable=Entry_6)
    if Ent >= 7: Entry(Frame_Right, textvariable=Entry_7)
    if Ent >= 8: Entry(Frame_Right, textvariable=Entry_8)
    
    for c in sorted(Frame_Right.children):
        Frame_Right.children[c]["width"]= 80
        Frame_Right.children[c]["font"] = Stan_Font
        Frame_Right.children[c].pack(fill="both")

    # Buttons
    if Butt >= 1: Button(Frame_Bottom, text=Button_1_Text, command=Button_1_Command)
    if Butt >= 2: Button(Frame_Bottom, text=Button_2_Text, command=Button_2_Command)
    
    #These buttons are for the hotfix options, so that they can present more options to the users
    for c in sorted(Frame_Bottom.children):
        Frame_Bottom.children[c]["font"] = Stan_Font
        Frame_Bottom.children[c].pack(fill="both")
    
    if hotfixoptions == 1:
        Button(Frame_Bottom, text="Click to make a new line", command=lambda: Queue_Order.append("New line")).pack(fill="both")
        Entry(Frame_Bottom, textvariable = StringVar(Frame_Bottom)).pack(fill="both")
        Button(Frame_Bottom, text="Fill entry above, then click to add a comment", command=lambda: (Queue_Order.append("Comment"), Comment_str.append(StringVar(Frame_Bottom).get()))).pack(fill="both")
    
    Frame_Left.grid( row = 0, column = 0)
    Frame_Right.grid(row = 0, column = 1)
    Frame_Bottom.grid(row = 1)
    # Frame_Left.pack(side=LEFT, fill="both")
    # Frame_Right.pack(side=RIGHT, fill="both")
    # Frame_Bottom.pack(side=BOTTOM, fill="both")
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
    Button(text="Add To Mod Header Queue", command=lambda: SelectionWindow("ModHeader"))
    Button(text="Add To Regular HotFix Queue", command=lambda: SelectionWindow("HotFix"))
    Button(text="Add To Table HotFix Queue", state=DISABLED)
    
    Button(text="JSON Information Formatter", command=lambda: FileChoice())
    Button(text="Database Search", command=lambda: SelectionWindow("Search"))
    Button(text="Useful Information", command=lambda: List_Info())
    
    Button(text="Create Your HotFix File\nNOTE: Fill Out Queues Before Clicking", command=lambda: Create_HotFix_File())
    
    # Formats all my wigits the same way
    for c in sorted(MainWindow.children):
        MainWindow.children[c]["font"]=Stan_Font
        MainWindow.children[c].pack(expand=True, fill="both")
    MainWindow.mainloop()
################################################################################################################################################################