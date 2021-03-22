################################################################################################################################################################
#Going to try to import only what I need to save on space and calculation time
from tkinter import Tk, Frame, Label, Entry, Button, Scrollbar, Text
from tkinter import LEFT, BOTH, RIGHT, TOP, Y, BOTTOM, END
# from bl3hotfixmod import LVL_TO_ENG
################################################################################################################################################################
# Functions I uses to get only what is needed if you are choosing a JSON file

# This is used to help format the file path, so we can input the correct format to search for
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names

# # Unused at this point. thought it would be more useful. Will keep for now but may get rid of later
# FuncNames = ["get_data", "find", "find_data", "glob", "glob_data", "get_export_idx",
#              "get_exports", "get_parts_category_name", "get_extra_anoints"]  # stores function names

Map_Locations = ['Anger_P', 'Archive_P', 'AtlasHQ_P', 'Bar_P', 'Beach_P', 'BloodyHarvest_P', 'COVSlaughter_P', 'Camp_P', 'Cartels_P', 'CasinoIntro_P', 'Chase_P', 'CityBoss_P', 'CityVault_P', 'City_P', 'Convoy_P', 'Core_P', 'CraterBoss_P', 'CreatureSlaughter_P', 'Crypt_P', 'DesertBoss_P', 'Desert_P', 'Desertvault_P', 'Desolate_P', 'Eldorado_P', 'Experiment_P', 'Facility_P', 'FinalBoss_P', 'Forest_P', 'Frontier_P', 'GuardianTakedown_P', 'Impound_P', 'Lake_P', 'Lodge_P', 'Mansion_P', 'MarshFields_P', 'Mine_P', 'Monastery_P',
                 'MotorcadeFestival_P', 'MotorcadeInterior_P', 'Motorcade_P', 'OrbitalPlatform_P', 'Outskirts_P', 'Prison_P', 'Prologue_P', 'ProvingGrounds_Trial1_P', 'ProvingGrounds_Trial4_P', 'ProvingGrounds_Trial5_P', 'ProvingGrounds_Trial6_P', 'ProvingGrounds_Trial7_P', 'ProvingGrounds_Trial8_P', 'Raid_P', 'Recruitment_P', 'Sacrifice_P', 'Sanctuary3_P', 'Sanctum_P', 'Strip_P', 'TechSlaughter_P', 'TowerLair_P', 'Towers_P', 'Town_P', 'Trashtown_P', 'Venue_P', 'Village_P', 'Watership_P', 'WetlandsBoss_P', 'WetlandsVault_P', 'Wetlands_P', 'Woods_P', 'MatchAll']


# Will be used for deciding what kind of hotfix to apply
Patch_Types = ['Mod.PATCH', 'Mod.LEVEL', 'Mod.EARLYLEVEL',
               'Mod.CHAR', 'Mod.PACKAGE', 'Mod.POST']
################################################################################################################################################################
# Lists I call to stroe things in.
# They are called globally so that they may not change.
Mod_Header = []
Reg_hotfix = []
Table_Hotfix = []
Mesh_Hotfix = []
Queue_Order = []

DataBase_Results = []
File_Results_List = []
Search_List = []

# These are for holding information to make comments
Comment_Queue = []
Header_Lines_Queue = []
Headers_Queue = []
################################################################################################################################################################
# All the fonts that you can use. may impliment this one day
# fonts=list(tkFont.families())
# fonts.sort()
Stan_Font = ("Times New Roman", 10)
# Stan_Font = ("Wingdings 2", 12)
# Stan_Font = ("Courier New", 10)
def ListBoxWindow(List):
    ListWindow = Tk()
    w, h = 500, 350
    ws, hs = ListWindow.winfo_screenwidth(), ListWindow.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    # Reference: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/

    Fram_Of_Reference = Frame(ListWindow)
    Fram_Of_Reference.pack(side=TOP)

    Label(Fram_Of_Reference, text='Text to find:',font=Stan_Font).pack(side=LEFT)

    Find_String = Entry(Fram_Of_Reference)
    Find_String.pack(side=LEFT, fill=BOTH, expand=1)
    Find_String.focus_set()

    Scroll_Bar = Scrollbar(ListWindow)
    Scroll_Bar.pack(side=RIGHT, fill=Y)

    Find_Text_Button = Button(Fram_Of_Reference, text='Find', font=Stan_Font)
    Find_Text_Button.pack(side=RIGHT)

    Info_Display_Text_Box = Text(ListWindow, yscrollcommand=Scroll_Bar, width=300, height=100, font=Stan_Font)
    Info_Display_Text_Box.delete('1.0', END)
################################################################################################################################################################
    if List == 1:  # Has all the results of the database search
        ListWindow.title("Data base results")
        ListWindow.geometry('+%d+%d' % ( x, y/3.5))
        DataBase_Results.sort()
        for x in DataBase_Results: Info_Display_Text_Box.insert('1.0', x + '\n')
        Info_Display_Text_Box.place(width=2000)

    elif List == 2:  # Displays the contents of when you looked through a file
        ListWindow.title("JSON File Information")
        ListWindow.geometry('+%d+%d' % (x/3.8, y/3.5))
        File_Results_List.sort()
        for x in File_Results_List: Info_Display_Text_Box.insert('1.0', x + '\n')
        Info_Display_Text_Box.place(width=2000)

    # exclusively used with the find function so that it makes it easier on my life
    elif List == 3:  # Displays Searched information
        ListWindow.title("JSON Filtered Information")
        ListWindow.geometry('+%d+%d' % (x/3.8, y/3.5))
        Search_List.sort()
        for x in Search_List: Info_Display_Text_Box.insert('1.0', x + '\n')
        Info_Display_Text_Box.place(width=2000)

    Scroll_Bar.config(command=Info_Display_Text_Box.yview)
    Info_Display_Text_Box.pack(side=BOTTOM)
    # based on: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
    def find():
        i = 0
        Content_List = []
        Info_Display_Text_Box.tag_remove('found', '1.0', END)
        s = Find_String.get()
        if len(Search_List) > 0: Search_List.clear()  # Clears out the list so we don't geta data contamination

        Text_Content_Hold = Info_Display_Text_Box.get("1.0", "end")
        Content_List = Text_Content_Hold.split("\n")

        while i < len(Content_List):
            if s in Content_List[i]: Search_List.append(Content_List[i])
            i += 1

        ListBoxWindow(5)
        Find_String.focus_set()

    Find_Text_Button.config(command=find)
################################################################################################################################################################
