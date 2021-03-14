"""
This program was heavly based on apocalyptech bl3mods/python_mod_help
Link to current reposatory: https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers
apocalyptech has written most all functions that I am using. All I am doing is making
a interface for people to use.

At the time of coding this there is nothing like a BLCMM or other tools to make the hotfix for you, 
so you have to manually enter all data in order for it to work, and even then my coding my be off in some way.

BL3 is still in its modding infancy so if this program becomes obsolete in the future, well I still found it a great experience
making this and I hope BL3 live as long as BL2 did, as they are tied for some of my favorite games of all times
"""
from bl3data import BL3Data
from _global_lists import FileNames, File_Results_List, Search_List
from _global_lists import ListBoxWindow
################################################################################################################################################################
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk, Frame, Button, Text, Entry
from tkinter import END, RAISED
from flatten_json import flatten
import os
#Global variables
DATA = BL3Data()
################################################################################################################################################################
# The user is able to choose a json file and search through the contents


def FileChoice():
    Tk().withdraw()
    File_Path = askopenfilename(filetypes=[("Choose file", ".json")])
    # Removes the files extention, as we dont need it
    Raw_Path = os.path.splitext(File_Path)[0]
    i = 0
    index = 0
    if os.path.exists(File_Path) == True:
        while index <= 0:
            # We search for a Key word from that corralates to an apporiate path
            Find = "/" + FileNames[i]
            i += 1
            if Find in Raw_Path:
                index = Raw_Path.find(Find)
        # This is used for the BL3Data.get_data function
        True_Path = Raw_Path[index::]
        File_Results_Window(True_Path)

# Trying to stream line the


def File_Results_Window(True_Path):
    I = 0
    Raw_Data = DATA.get_data(True_Path)
    Refined_Data = flatten(Raw_Data[I], separator="[", replace_separators="]")
    _jwp_object_name = Refined_Data["_jwp_object_name"]

    """
    _jwp_object_name = Refined_Data["_jwp_object_name"]
    _jwp_arr_idx = Refined_Data["_jwp_arr_idx"]
    _jwp_is_asset = Refined_Data["_jwp_is_asset"]
    export_type = Refined_Data["export_type"]
    _jwp_export_idx = Refined_Data["_jwp_export_idx"]
    _apoc_data_ver = Refined_Data["_apoc_data_ver"]
    """
    obj_name = str(True_Path + "." + _jwp_object_name + ", ")
    while I < len(Raw_Data):
        for key, value in Refined_Data.items():
            attr_name = str(key) + " : " + str(value)
            File_Results_List.append(obj_name + attr_name)
        File_Results_List.append("\n")
        I += 1
    ListBoxWindow(4)

################################################################################################################################################################
# Reference: https://www.studytonight.com/tkinter/text-editor-application-using-tkinter


def openBL3Hotfixfile():

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Hot Fix File", "*.bl3hotfix")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, END)
        hold_path = filepath
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(END, text)
        window.title(f"Text Editor Application - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Hot Fix File", "*.bl3hotfix")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, END)
            output_file.write(text)
        window.title(f"Text Editor Application - {filepath}")

    def find():
        i = 0
        content_list = []
        txt_edit.tag_remove('found', '1.0', END)
        s = Find_String.get()
        hold = txt_edit.get("1.0", "end")
        content_list = hold.split("\n")

        if len(Search_List) > 0:
            Search_List.clear()  # Clears out the list so we don't geta data contamination
        while i < len(content_list):
            if s in content_list[i]:
                Search_List.append(content_list[i])
            i += 1
        ListBoxWindow(5)

    window = Tk()
    window.title("Text Editor Application")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    fr_buttons = Frame(window, relief=RAISED, bd=2)
    txt_edit = Text(window)

    btn_open = Button(fr_buttons, text="Open", command=open_file)
    btn_save = Button(fr_buttons, text="Save As...", command=save_file)
    Find_Text_Button = Button(fr_buttons, text='Find', command=find)
    Find_String = Entry(fr_buttons)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    Find_String.grid(row=2, column=0, sticky="ew", padx=5)
    Find_Text_Button.grid(row=3, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()
################################################################################################################################################################
