# Going to try to import only what I need to save on space and calculation time
# My files
# from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from bl3data import BL3Data
from bl3hotfixmod import LVL_TO_ENG
from __info_function__ import FileChoice, openBL3Hotfixfile
from __hotfix_control import Create_HotFix_File
from _global_lists import Mod_Header, Reg_hotfix, Table_Hotfix, Mesh_Hotfix, DataBase_Results, Queue_Order, Comment_Queue, Headers_Queue, Patch_Types
from _global_lists import List_Info, ListBoxWindow
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import Entry, Button, Label, Tk, StringVar
from tkinter import DISABLED
################################################################################################################################################################
# Global variables
data = BL3Data()
Stan_Font = ("Times New Roman", 10)
# Stan_Font = ("Wingdings 2", 12)
# Stan_Font = ("Courier New", 12)
################################################################################################################################################################
# for info in test:
#     print(info)


def SelectionWindow(Func):
    # Global/Window variables
    SelectionWindow = Tk()
    Hotfix_Label_Display = Label(SelectionWindow)
    #These are for sotring the feilds of information
    # SelectionWindow = Frame(SelectionWindow,borderwidth = 2)
    # SelectionWindow = Frame(SelectionWindow,borderwidth = 2)
    # SelectionWindow = Frame(SelectionWindow,borderwidth = 2)

    # Default values for window sizes for all, can manipulate inside the functions
    w, h, ws, hs = 500, 350, SelectionWindow.winfo_screenwidth(
    ), SelectionWindow.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    # These variables will determine how many things to add to the window as I need them
    Lab, Ent, Butt, HotFix_Options = 0, 0, 0, 0
    # To be able to grab the entry feilds
    Entry_1, Entry_2, Entry_3, Entry_4 = StringVar(SelectionWindow), StringVar(
        SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    Entry_5, Entry_6, Entry_7, Entry_8 = StringVar(SelectionWindow), StringVar(
        SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    Entry_9, Entry_10, Entry_11 = StringVar(SelectionWindow), StringVar(
        SelectionWindow), StringVar(SelectionWindow)

    # Used to grab the values the then entry textvariables
    def Get_Val(Type):
        # Information about your mod
        if Type == "Mod Info":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(
            ), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Puts the Information to make the file into a queue to be called later
            Mod_Header.extend([A, B, C, D, E, F])

        # Adds to the regular hot fix queue
        elif Type == "Regular HotFix":
            A, B, C, D, E, F, G, H = Entry_1.get(), Entry_2.get(), Entry_3.get(
            ), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get()
            Reg_hotfix.extend([A, B, C, D, E, F, G, H])
            Queue_Order.append("Regular hotfix")

        elif Type == "Table HotFix":
            A, B, C, D, E, F, G, H, I = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(
            ), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get(), Entry_9.get()
            Table_Hotfix.extend([A, B, C, D, E, F, G, H, I])
            Queue_Order.append("Table hotfixes")

        elif Type == "Mesh HotFix":
            A, B, C, D, E, F, G, H, I = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(
            ), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get(), Entry_9.get()
            Mesh_Hotfix.extend([A, B, C, D, E, F, G, H, I])
            Queue_Order.append("Mesh hotfixes")

        # This will search the database for provided information
        elif Type == "Search":
            Search = Entry_1.get()
            Info = data.get_refs_from_data(Search)
            # This will clean out the previous entry so that it does not become cluttered
            if len(DataBase_Results) > 0:
                DataBase_Results.clear()
            for Details in Info:
                if Details[0] not in DataBase_Results:
                    DataBase_Results.append(Details[0])
            DataBase_Results.sort()
            ListBoxWindow(3)

    # This is used for displaying what the hotfix will look like. use this to preview your creation before interting it
    def Dis_Hotfix(ints):
        B, C, D, E, F, G, H, I = Entry_2.get(), Entry_3.get(), Entry_4.get(
        ), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get(), Entry_9.get()
        if ints == 1:
            Hotfix_Label_Display.config(
                text='(1,1,{} , {}), {}, {}, \n{}, {}, {}'.format(B, C, D, E, F, G, H))
        elif ints == 2:
            Hotfix_Label_Display.config(
                text='(1,2,{} , {}), {}, {}, \n{}, {}, {}, {}'.format(B, C, D, E, F, G, H, I))
        # Does nothing at the current moment
        elif ints == 3:
            notification_flag = B
            
            map_first, map_last = C.rsplit('/', 1)
            mesh_first, mesh_last = D.rsplit('/', 1)
            location = E.split(",")
            rotation = F.split(",")
            scale = G.split(",")
            coord_parts = []
            for coords in [location, rotation, scale]:
                coord_parts.append(','.join([
                    '{:.6f}'.format(int(n)) for n in coords
                ]))
            coord_field = '|'.join(coord_parts)
            Hotfix_Label_Display.config(
                text='(1,6,{}, {}), {}, {}, \n{}, {}, "{}", {})'.format(notification_flag, map_last, map_first, mesh_first, mesh_last, len(coord_field), coord_field, H))

    # Mod header info
    if Func == "Mod Info":  # Creates a mod file of you to use
        SelectionWindow.title("Mod Info")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x/4, y))
        Lab, Ent, Butt = 6, 6, 1
        Label_1_Text = 'Name of the hotfix file: '
        Label_2_Text = 'The actual mod name: '
        Label_3_Text = 'Author(s) name: '
        Label_4_Text = 'Discription: '
        Label_5_Text = 'Version of this mod: '
        Label_6_Text = 'The catagory in which this mods fits to: '
        Button_1_Text = 'Create Mod Header'
        def Button_1_Command(): return Get_Val("Mod Info")

    # Regular Hotfix
    elif Func == "Regular HotFix":
        SelectionWindow.title("Creating Regular HotFix.")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w*1.2, h, x, y/10))

        Lab, Ent, Butt = 8, 8, 2
        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = 'Map Name: (package)'
        Label_4_Text = 'JSON Path + JWP Object: (obj_name)'
        Label_5_Text = 'Attribute: (attr_name)'
        Label_6_Text = 'Lenght of the previous value, (prev_val_len)'
        Label_7_Text = 'True, False, or Leave Blank: (prev_val)'
        Label_8_Text = 'True, New Value, or Other (new_val)'

        Button_1_Text = "Add To Regular Hotfix Queue"
        def Button_1_Command(): return Get_Val("Regular HotFix")
        Button_2_Text = "Preview Your Hotfix"
        def Button_2_Command(): Dis_Hotfix(1)

        HotFix_Label_Text = '(1,1,{notification_flag},{package}),{obj_name},\n{attr_name},{prev_val_len},{prev_val},{new_val}'
        HotFix_Options = 1

    # Table Hotfix
    elif Func == "Table HotFix":
        SelectionWindow.title("Creating Table HotFix.")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w*1.2, h, x, y/7))

        Lab, Ent, Butt = 9, 9, 2
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
        def Button_1_Command(): return Get_Val("Table HotFix")
        Button_2_Text = "Preview Your Hotfix"
        def Button_2_Command(): Dis_Hotfix(2)

        HotFix_Label_Text = '(1,2,{notification_flag},{package}),{obj_name},{row_name},\n{attr_name},{prev_val_len},{prev_val},{new_val}'
        HotFix_Options = 1

    # Mesh Hotfix
    elif Func == "Mesh HotFix":
        SelectionWindow.title("Creating Mesh HotFix.")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w*1.2, h, x, y/5))
        # I need to figure out how to display it proporly, so right no i will disable this feature
        Lab, Ent, Butt = 8, 8, 2

        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = '(map_path)'
        Label_4_Text = '(mesh_path)'
        Label_5_Text = 'Enter Numbers Like So: n,n,n (location)'
        Label_6_Text = 'Enter Numbers Like So: n,n,n (rotation)'
        Label_7_Text = 'Enter Numbers Like So: n,n,n (scale)'
        Label_8_Text = 'Transparent: True or False'

        Button_1_Text = "Add To Mesh Hotfix Queue"
        def Button_1_Command(): return Get_Val("Mesh HotFix")
        Button_2_Text = "Preview Your Hotfix"
        def Button_2_Command(): Dis_Hotfix(3)

        HotFix_Label_Text = '(1,6,{notification_flag},{map_last}),{map_first},{mesh_first},\n{mesh_last},{coord_len},"{coord_field}",{transparent_flag}'
        HotFix_Options = 1

    # The user will search for a word, and puncuation does not matter, but spelling does
    elif Func == "Search":
        SelectionWindow.title("Find All References")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x*1.8, y))
        Lab, Ent, Butt = 1, 1, 1
        Label_1_Text = 'Enter what you want to search for: \nMay freeze on you. Do not worry, its just loading.'
        Button_1_Text = "Search"
        def Button_1_Command(): return Get_Val("Search")

    # Labels
    i = 1
    while i <= Lab:
        Label_Text = "Label_" + str(i) + "_Text"
        for key, value in locals().items():
            if key == Label_Text:
                Label(SelectionWindow, text=value).grid(
                    row=i, column=0, sticky="W")
                break
        i += 1

    # Entries
    i = 1
    while i <= Ent:
        Entry_Var = "Entry_" + str(i)
        for key, value in locals().items():
            if key == Entry_Var:
                Entry(SelectionWindow, textvariable=value, width=50).grid(
                    row=i, column=1, sticky="E")
                break
        i += 1

    # Buttons
    i, k = 1, 0
    while i <= Butt:
        # This is used to check my generic variable names that I have, and grab the value to put inside the things i need
        Text = "Button_" + str(i) + "_Text"
        Command = "Button_" + str(i) + "_Command"
        k = 0
        for key, value in locals().items():
            if key == Text:
                text_hold = value
                k += 1
            if key == Command:
                command_hold = value
                k += 1
            if k == 2:
                Button(SelectionWindow, text=text_hold, command=command_hold).grid(
                    row=Lab + i, column=0, sticky="W")
                break
        i += 1

    # Exclusive to hotfixes
    if HotFix_Options == 1:
        Hotfix_Label_Display.config(text=HotFix_Label_Text)
        Hotfix_Label_Display.grid(row=Lab+Butt+1, column=0)

        Button(SelectionWindow, text="Insert New Line Into Hotfix", font=Stan_Font,
               command=lambda: Queue_Order.append("New line")).grid(row=Lab+Butt+2, column=0, sticky="W")

        Entry(SelectionWindow, textvariable=Entry_10, width=50).grid(
            row=Lab+Butt+3, column=1, sticky="E")
        Button(SelectionWindow, text="Fill Entry, Then Click To Add A Comment", command=lambda: (Queue_Order.append(
            "Comment"), Comment_Queue.append(Entry_10.get()))).grid(row=Lab+Butt+3, column=0, sticky="W")

        Entry(SelectionWindow, textvariable=Entry_11, width=50).grid(
            row=Lab+Butt+4, column=1, sticky="E")
        Button(SelectionWindow, text="Fill Entry, Then Click To Add A Header", command=lambda: (Queue_Order.append(
            "Header"), Headers_Queue.append(Entry_11.get())), state=DISABLED).grid(row=Lab+Butt+4, column=0, sticky="W")

    for c in sorted(SelectionWindow.children):
        SelectionWindow.children[c]["font"] = Stan_Font
        # SelectionWindow.children[c].pack(expand=True, fill="both")
    SelectionWindow.mainloop()


################################################################################################################################################################
# Main menu.
if __name__ == "__main__":
    MainWindow = tk.Tk()
    MainWindow.title("Hot Fix Generator")
    w, h = 500, 350
    ws, hs = MainWindow.winfo_screenwidth(), MainWindow.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Button(text="Add Mod Header", command=lambda: SelectionWindow("Mod Info"))
    Button(text="Add Regular HotFix",
           command=lambda: SelectionWindow("Regular HotFix"))
    Button(text="Add Table HotFix",
           command=lambda: SelectionWindow("Table HotFix"))
    Button(text="Add Mesh HotFix", command=lambda: SelectionWindow("Mesh HotFix"))
    Button(text="Database Search", command=lambda: SelectionWindow("Search"))

    Button(text="JSON Information Formatter", command=lambda: FileChoice())
    Button(text="Open A .bl3hotfix File", command=lambda: openBL3Hotfixfile())
    Button(text="Useful Information", command=lambda: List_Info())
    Button(text="Create Your HotFix File\nNOTE: Fill Out Queues Before Clicking",
           command=lambda: Create_HotFix_File())

    # Formats all my wigits the same way
    for c in sorted(MainWindow.children):
        MainWindow.children[c]["font"] = Stan_Font
        MainWindow.children[c].pack(expand=True, fill="both")
    MainWindow.mainloop()
################################################################################################################################################################