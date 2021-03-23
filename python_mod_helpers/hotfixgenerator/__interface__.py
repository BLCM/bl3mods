# Going to try to import only what I need to save on space and calculation time
# My files
from bl3data import BL3Data
from __info_function__ import FileChoice, openBL3Hotfixfile
from __hotfix_control import Create_HotFix_File
from _global_lists import Mod_Header, Reg_hotfix, Table_Hotfix, Mesh_Hotfix, DataBase_Results, Queue_Order, Comment_Queue, Headers_Queue, Map_Locations, Patch_Types
from _global_lists import ListBoxWindow
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import Entry, Button, Label, OptionMenu, Tk, StringVar
from tkinter import DISABLED
import subprocess
import sys
import os
################################################################################################################################################################
# Global variables
data = BL3Data()
# Lists I need for later
noti_flag = [0,1] # Something to hold the true or false flags 
List_Holder = [Patch_Types, noti_flag, Map_Locations] # A list that holds list so that I can assign them easially
Stan_Font = ("Times New Roman", 10)
# Stan_Font = ("Wingdings 2", 10)
# Stan_Font = ("Courier New", 10)
################################################################################################################################################################
def SelectionWindow(Func):
    SelectionWindow = Tk()
    Hotfix_Label_Display = Label(SelectionWindow) # Had to put this up here as it would not work any other way
    # Default values for window sizes for all, can manipulate inside the functions
    w, h, ws, hs = 500, 350, SelectionWindow.winfo_screenwidth(), SelectionWindow.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    # These variables will determine how many things to add to the window as I need them
    Lab_Ent, Butt, HotFix_Options, dropBox = 0, 0, 0, 0 # Theses are used for defining how many lables, entries, buttons, and if they need hotfix options applied to them
    # generic names assigned to entry fields. Maybe there is a better way of assigning them, but i don't want to mess around with this to much
    Entry_1, Entry_2, Entry_3, Entry_4 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    Entry_5, Entry_6, Entry_7, Entry_8 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    Entry_9, Entry_10, Entry_11 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)

    # This is actually what is used to put your inputs inside a queue to be executed later
    def Get_Val(Type):
        # Puts the Information to make the file into a queue to be called later
        A, B, C, D, E, F, G, H, I = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get(), Entry_9.get()        
        # Information about your mod
        if Type == "Mod Info": Mod_Header.extend([A, B, C, D, E, F])
        # Adds to the regular hot fix queue
        elif Type == "Regular Hotfix":
            Reg_hotfix.extend([A, B, C, D, E, F, G, H])
            Queue_Order.append("Regular hotfix")
        # Adds to the table hot fix queue
        elif Type == "Table Hotfix":
            Table_Hotfix.extend([A, B, C, D, E, F, G, H, I])
            Queue_Order.append("Table hotfixes")
        # Adds to the mesh hot fix queue
        elif Type == "Mesh Hotfix":
            Mesh_Hotfix.extend([A, B, C, D, E, F, G, H, I])
            Queue_Order.append("Mesh hotfixes")
        # This will search the database for provided information
        elif Type == "Search":
            Info = data.get_refs_from_data(A)
            # This will clean out the previous entry so that it does not become cluttered
            if len(DataBase_Results) > 0: DataBase_Results.clear()
            # puts the database results into a tkinter Text window so that the user can look at this information
            for Details in Info: #the reason this looks weird is because of how python gets data from databases, it adds extra characters to the return result, so this helps make it cleaner
                if Details[0] not in DataBase_Results: DataBase_Results.append(Details[0])
            DataBase_Results.sort() # sorts the results because it produces a cleaner result
            ListBoxWindow(1) # Calls the function to display the 

    # This is used for displaying what the hotfix will look like. use this to preview your creation before interting it
    def Display_Hotfix(hotfix_type):
        B, C, D, E, F, G, H, I = Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get(), Entry_9.get()
        if hotfix_type == 1: Hotfix_Label_Display.config(text='(1,1,{} , {}), {}, \n{}, {}, {}, {}'.format(B, C, D, E, F, G, H))
        elif hotfix_type == 2: Hotfix_Label_Display.config(text='(1,2,{} , {}), {}, \n{}, {}, {}, {}, {}'.format(B, C, D, E, F, G, H, I))
        # This one is more complicated than the others because it has lets inputs than what is technically needed, 
        # but due to the way the code works is that it divides up the other answers and puts them in where they need to be 
        elif hotfix_type == 3:
            # This was all grabbed from the bl3hotfix file, as i wanted a way for users to see their hotfixes they are creating, and there was no easy way of doing it
            map_first, map_last = C.rsplit('/', 1)
            mesh_first, mesh_last = D.rsplit('/', 1)
            location = E.split(",")
            rotation = F.split(",")
            scale = G.split(",")
            coord_parts = []
            for coords in [location, rotation, scale]: coord_parts.append(','.join(['{:.6f}'.format(int(n)) for n in coords]))
            coord_field = '|'.join(coord_parts)
            Hotfix_Label_Display.config(text='(1,6,{}, {}), {}, \n{}, {}, {}, "{}", {})'.format(B, map_last, map_first, mesh_first, mesh_last, len(coord_field), coord_field, H))

    # Mod header info
    if Func == "Mod Info":  # Creates a mod file of you to use
        SelectionWindow.title("Mod Info")
        SelectionWindow.geometry('+%d+%d' % ( x/4, y)) # this makes it so it only grows to the size it needs to, while still appearing in a specified location
        Lab_Ent, Butt = 6, 2 # ,since it starts at zero, the range function will only do 0, 1, so if we specify that it is 2 then it will do 0, than one, thenstop
        # Though these are not assigned to anything, they are in the system local dictionary, 
        # Meaning that I can grab them for use later without having them assigned to anything
        Label_1_Text = 'Name of the hotfix file: '
        Label_2_Text = 'The actual mod name: '
        Label_3_Text = 'Author(s) name: '
        Label_4_Text = 'Discription: '
        Label_5_Text = 'Version of this mod: '
        Label_6_Text = 'The catagory in which this mods fits to: '
        
        Button_1_Text = 'Create Mod Header'
        def Button_1_Command(): return Get_Val("Mod Info")
    
    # The user will search for a word, and puncuation does not matter, but spelling does
    elif Func == "Search":
        SelectionWindow.title("Find All References")
        SelectionWindow.geometry('+%d+%d' % (x*1.8, y))
        Lab_Ent, Butt = 2, 2 # same deal here, I only need one but I need to clarify that i need two
        Label_1_Text = 'Enter what you want to search for: \nNOTE: May pause on you.'
        
        Button_1_Text = "Search"
        def Button_1_Command(): return Get_Val("Search")
    
    # Regular Hotfix
    elif Func == "Regular Hotfix":
        SelectionWindow.title("Creating Regular HotFix.")
        SelectionWindow.geometry('+%d+%d' % (x, y/10))
        Lab_Ent, Butt, HotFix_Options, dropBox = 8, 2, 1, 3
        
        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = 'Map Name: (package)'
        Label_4_Text = 'JSON Path + JWP Object: (obj_name)'
        Label_5_Text = 'Attribute: (attr_name)'
        Label_6_Text = 'Lenght of the previous value, (prev_val_len)'
        Label_7_Text = 'True, False, or Leave Blank: (prev_val)'
        Label_8_Text = 'True, New Value, or Other (new_val)'
        
        Button_1_Text = "Add To Regular Hotfix Queue"
        def Button_1_Command(): return Get_Val("Regular Hotfix")
        Button_2_Text = "Preview Your Hotfix"
        def Button_2_Command(): Display_Hotfix(1)
        HotFix_Label_Text = '(1,1,{notification_flag},{package}),{obj_name},\n{attr_name},{prev_val_len},{prev_val},{new_val}'

    # Table Hotfix
    elif Func == "Table Hotfix":
        SelectionWindow.title("Creating Table HotFix.")
        SelectionWindow.geometry('+%d+%d' % (x, y/7))
        Lab_Ent, Butt, HotFix_Options, dropBox = 9, 2, 1, 3
        
        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = 'Map Name: (package)'
        Label_4_Text = 'JSON Path + JWP Object: (obj_name)'
        Label_5_Text = 'Row: (row_name)'
        Label_6_Text = 'Attribute: (attr_name)'
        Label_7_Text = 'Lenght of the previous value, (prev_val_len)'
        Label_8_Text = 'True, False, or Leave Blank: (prev_val)'
        Label_9_Text = 'True, New Value, or Other (new_val)'
        
        Button_1_Text = "Add To Table Hotfix Queue"
        def Button_1_Command(): return Get_Val("Table Hotfix")
        Button_2_Text = "Preview Your Hotfix"
        def Button_2_Command(): Display_Hotfix(2)
        HotFix_Label_Text = '(1,2,{notification_flag},{package}),{obj_name},{row_name},\n{attr_name},{prev_val_len},{prev_val},{new_val}'

    # Mesh Hotfix
    elif Func == "Mesh Hotfix":
        SelectionWindow.title("Creating Mesh HotFix.")
        SelectionWindow.geometry('+%d+%d' % ( x, y/5))
        Lab_Ent, Butt, HotFix_Options, dropBox = 8, 2, 1, 2
        
        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = '(map_path)'
        Label_4_Text = '(mesh_path)'
        Label_5_Text = 'Enter Numbers Like So: n,n,n (location)'
        Label_6_Text = 'Enter Numbers Like So: n,n,n (rotation)'
        Label_7_Text = 'Enter Numbers Like So: n,n,n (scale)'
        Label_8_Text = 'Transparent: True or False'
        
        Button_1_Text = "Add To Mesh Hotfix Queue"
        def Button_1_Command(): return Get_Val("Mesh Hotfix")
        Button_2_Text = "Preview Your Hotfix"
        def Button_2_Command(): Display_Hotfix(3)
        HotFix_Label_Text = '(1,6,{notification_flag},{map_last}),{map_first},{mesh_first},\n{mesh_last},{coord_len},"{coord_field}",{transparent_flag}'

    # Labels, Entries/DropBox
    # The reason I do it like this is so that I only create what I need for each different window, saving resources and code space
    # What this should do now is give the user a list of all locations, patch types and notification flags, so that users have an easier time with creating their mod
    # I have mergen labels and entries into one thing because I relised that they were always the same amount, so whay not just make them one variable
    for i in range(1, Lab_Ent):
        k = 0 # This insures that both label and entry/droplist have been stisfied before breaking to start the next variable
        Label_Text = "Label_" + str(i) + "_Text" # This checks for my genericly named functions to grab and put inside the buttons
        Entry_Var = "Entry_" + str(i)
        for key, value in locals().items():
            if key == Label_Text:
                Label(SelectionWindow, text=value).grid(row=i, column=0, sticky="W")  # Lables are set to the west side of the window
                k += 1
            if key == Entry_Var:
                if i <= dropBox: # this way I do not have to specify which hitfix it is, I can just say how may times I want it to have a drop box
                    lst = List_Holder[i-1] # grabes the index in order from my list of lists. we have to start at zero so that  is why I have  it as  i-1
                    value.set(lst[0]) # sets the dropbox to display the first entry in the list so that the user can see
                    OptionMenu(SelectionWindow, value, *lst).grid(row=i, column = 1, sticky="E") # this creates a dropbox for us to use
                    k += 1 # we only break here because we want to make sure we get the labels first, then we go on to grab the next set.
                else: 
                    Entry(SelectionWindow, textvariable=value, width=50).grid(row = i, column=1, sticky="E") # normal entries to enter your data
                    k += 1

            # this is to insure that both label and optionmenu/entry are created before moving on to the next set that needs to be created
            if  k == 2:
                break

    # Buttons
    # This one works a bit different, since I need two different commands here;
    # I have their values stored in temporary var so that I can put them into the button later once I have both of them
    for i in range(Butt):
        Text = "Button_" + str(i) + "_Text"
        Command = "Button_" + str(i) + "_Command"
        k = 0 # K is for my special command that I have to assign the button two things at the same time
        for key, value in locals().items():
            if key == Text:
                text_hold = value
                k += 1
            if key == Command:
                command_hold = value
                k += 1
            if k == 2:
                Button(SelectionWindow, text=text_hold, command=command_hold).grid(row = Lab_Ent + i, column=0, sticky="W")

    # Exclusive to Hotfixes
    # I had to hard code a bit of these buttons in because I could not find a better way of doing it, but I still tried to make it as modular as possible
    if HotFix_Options == 1:
        # functionality for the Label, users see the preview of their hotfix
        Hotfix_Label_Display.config(text = HotFix_Label_Text)
        Hotfix_Label_Display.grid(row = Lab_Ent+Butt+1, column=0)
        
        Button(SelectionWindow, text="Insert New Line Into Hotfix", font=Stan_Font,command=lambda: Queue_Order.append("New line")).grid(row = Lab_Ent+Butt+2, column = 0, sticky="W") # Calls the new line function
        
        Entry(SelectionWindow, textvariable=Entry_10, width=50).grid(row=Lab_Ent+Butt+3, column=1, sticky="E") #Fill this with a comment
        Button(SelectionWindow, text="Fill Entry, Then Click To Add A Comment", command=lambda: (Queue_Order.append("Comment"), Comment_Queue.append(Entry_10.get()))).grid(row = Lab_Ent+Butt+3, column = 0, sticky="W",) # Grabs the comment
        
        Entry(SelectionWindow, textvariable=Entry_11, width=50).grid(row=Lab_Ent+Butt+4, column=1, sticky="E") # Fill for header
        Button(SelectionWindow, text="Fill Entry, Then Click To Add A Header", command=lambda: (Queue_Order.append("Header"), Headers_Queue.append(Entry_11.get())), state=DISABLED).grid(row = Lab_Ent+Butt+4, column = 0, sticky="W") # Works but not in the way i intend, will work on it a bit later

    # formats the widgiest all the same way so I do not have to do it every time
    for c in sorted(SelectionWindow.children):
        SelectionWindow.children[c]["font"] = Stan_Font # This mkakes anything with SelectionWindow as their root format the same way
    SelectionWindow.mainloop()


################################################################################################################################################################
# Main menu.
if __name__ == "__main__":
    MainWindow = tk.Tk()
    MainWindow.title("Hotfix Generator")
    # variables to help  center the window
    w, h = 270, 300
    ws, hs = MainWindow.winfo_screenwidth(), MainWindow.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y)) # What this does is it centers the window while not taking up asny more space than it needs to
    
    # All main menu buttons
    Button(MainWindow,text="Add Mod Header", command=lambda: SelectionWindow("Mod Info"))
    Button(MainWindow,text="Add Regular HotFix",command=lambda: SelectionWindow("Regular Hotfix"))
    Button(MainWindow,text="Add Table HotFix",command=lambda: SelectionWindow("Table Hotfix"))
    Button(MainWindow,text="Add Mesh HotFix", command=lambda: SelectionWindow("Mesh Hotfix"))
    Button(MainWindow,text="Database Search", command=lambda: SelectionWindow("Search"))
    # Functions that are out of not inside this file
    Button(MainWindow,text="Look Through A JSON File Contents", command=lambda: FileChoice())
    Button(MainWindow,text="Open A .bl3hotfix File", command=lambda: openBL3Hotfixfile())
    Button(MainWindow,text="Create Your Hotfix File", command=lambda: Create_HotFix_File())

    # Formats all my wigits the same way
    for c in MainWindow.children:
        MainWindow.children[c]["font"] = Stan_Font
        MainWindow.children[c].pack(expand=True, fill="both")
    MainWindow.mainloop()
################################################################################################################################################################