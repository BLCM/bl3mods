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
from tkinter import Tk, Frame, Button, Text, Entry, Scrollbar
from tkinter import END, RAISED
from flatten_json import flatten
import os
#Global variables
DATA = BL3Data()
Stan_Font = ("Times New Roman", 10)
# Stan_Font = ("Wingdings 2", 10)
# Stan_Font = ("Courier New", 10)
patch_types = ['SparkPatchEntry','SparkLevelPatchEntry','SparkEarlyLevelPatchEntry','SparkCharacterLoadedEntry','SparkStreamedPackageEntry', 'SparkPostLoadedEntry'] # to make sure we get the different patch types highlighted
color_types = ["blue", "dark blue", "red" , "dark red", "green", "dark green", "dark gray"]
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

# Trying to stream line the process of using the 'get_data' functions
def File_Results_Window(True_Path):
    I = 0
    Raw_Data = DATA.get_data(True_Path)
    # I slightly modified the flatten libary to make my program format easier, 
    # it may not work for all users and I may need to copy over what i modified into my code so that it will work for all users
    Refined_Data = flatten(Raw_Data[I], separator="[", replace_separators="]") 
    _jwp_object_name = Refined_Data["_jwp_object_name"]

    """
    I commented these out beause these are important, but i have not yet found a proper use for them
    _jwp_object_name = Refined_Data["_jwp_object_name"]
    _jwp_arr_idx = Refined_Data["_jwp_arr_idx"]
    _jwp_is_asset = Refined_Data["_jwp_is_asset"]
    export_type = Refined_Data["export_type"]
    _jwp_export_idx = Refined_Data["_jwp_export_idx"]
    _apoc_data_ver = Refined_Data["_apoc_data_ver"]
    """
    obj_name = str(True_Path + "." + _jwp_object_name + ", ") # This will allow the users to copy the object path into the program so that they have an easier time moddign
    while I < len(Raw_Data):
        for key, value in Refined_Data.items():
            attr_name = str(key) + " : " + str(value)
            File_Results_List.append(obj_name + attr_name)
        File_Results_List.append("\n")
        I += 1
    ListBoxWindow(2)

################################################################################################################################################################
# Reference: https://www.studytonight.com/tkinter/text-editor-application-using-tkinter
def openBL3Hotfixfile():
    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(filetypes=[("BL3HotFix File", "*.bl3hotfix")])
        if not filepath: return
        txt_edit.delete(1.0, END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(END, text)
        
        # this is attempting to make certain text in the hotfix file a certain color so that it is easier to search through
        c = 0 # for colors
        for i in range(len(patch_types)):
            # reference: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
            idx = 1.0
            while True: # this loops forever untill an error appears
                idx = txt_edit.search(patch_types[i],idx,stopindex=END) # grabs the first instance of when the word is found
                if not idx: break # breaks if we are at the end
                lastidx = '%s+%dc' % (idx, len(patch_types[i])) # this pasically makes it so it grabs the start and end of the word we are seatching for
                txt_edit.tag_add(patch_types[i], idx, lastidx) # adds a tabg the we use to add color later         
                idx = lastidx # we start our search from the last index
            if c >= len(color_types): c = 0 # this is to insure that if we are highlighting a lot of words, they stay the same types of colors consistantly
            txt_edit.tag_config(patch_types[i], foreground=color_types[c]) # colors it
            c += 1
        # if i wanted to add more hilighting I would need to make another loop for another set of words
        c = 0
        for i in range(len(FileNames)):
            idx = 1.0
            while True: # this loops forever untill an error appears
                idx = txt_edit.search("/"+FileNames[i], idx, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(FileNames[i])+1) #compensate for the "/" I added
                txt_edit.tag_add(FileNames[i], idx, lastidx)    
                idx = lastidx
            if c >= len(color_types): c = 0
            txt_edit.tag_config(FileNames[i], foreground=color_types[c])
            c += 1
        
        window.title(f"Text Editor Application - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(defaultextension="txt", filetypes=[("BL3HotFix File", "*.bl3hotfix")])
        if not filepath: return
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

        if len(Search_List) > 0: Search_List.clear()  # Clears out the list so we don't geta data contamination
        while i < len(content_list):
            if s in content_list[i]: Search_List.append(content_list[i])
            i += 1
        ListBoxWindow(3)

    # this is used for creating the window users see when opening their hotfix file.
    # reason why i did not call my own was because I wanted to not mess with anything as icopied this over from a nother site
    window = Tk()
    window.title("Text Editor Application")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    fr_buttons = Frame(window, relief=RAISED, bd=2)
    Scroll_Bar = Scrollbar(window, orient="vertical")   
    txt_edit = Text(window, yscrollcommand=Scroll_Bar, font=Stan_Font)
    Scroll_Bar.config(command=txt_edit.yview)
    
    btn_open = Button(fr_buttons, text="Open", command=open_file)
    btn_save = Button(fr_buttons, text="Save As...", command=save_file)
    Find_Text_Button = Button(fr_buttons, text='Find', command=find)
    Find_String = Entry(fr_buttons)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    Find_String.grid(row=2, column=0, sticky="ew", padx=5)
    Find_Text_Button.grid(row=3, column=0, sticky="ew", padx=5)
    
    Scroll_Bar.grid(column=2, sticky="nsw")
    
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")
    
    window.mainloop()
################################################################################################################################################################
