################################################################################################################################################################
from tkinter import *
################################################################################################################################################################
# Functions I uses to get only what is needed if you are choosing a JSON file

# This is used to help format the file path, so we can input the correct format to search for
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names

# Unused at this point. thought it would be more useful. Will keep for now but may get rid of later
FuncNames = ["get_data", "find", "find_data", "glob", "glob_data", "get_export_idx",
             "get_exports", "get_parts_category_name", "get_extra_anoints"]  # stores function names

#Will be used for deciding what kind of hotfix to apply
Patch_Types = ['This is the list of patch types',
               'patch', 'level', 'earlylevel', 'char']

# Used to display all map names/
# May change later, but for now i think this is a good idea
Map_Locations = ['The names of all the maps, type one', 'Anger_P', 'Archive_P', 'AtlasHQ_P', 'Bar_P', 'Beach_P', 'BloodyHarvest_P', 'COVSlaughter_P', 'Camp_P', 'Cartels_P', 'CasinoIntro_P', 'Chase_P', 'CityBoss_P', 'CityVault_P', 'City_P', 'Convoy_P', 'Core_P', 'CraterBoss_P', 'CreatureSlaughter_P', 'Crypt_P', 'DesertBoss_P', 'Desert_P', 'Desertvault_P', 'Desolate_P', 'Eldorado_P', 'Experiment_P', 'Facility_P', 'FinalBoss_P', 'Forest_P', 'Frontier_P', 'GuardianTakedown_P', 'Impound_P', 'Lake_P', 'Lodge_P', 'Mansion_P', 'MarshFields_P', 'Mine_P', 'Monastery_P',
                 'MotorcadeFestival_P', 'MotorcadeInterior_P', 'Motorcade_P', 'OrbitalPlatform_P', 'Outskirts_P', 'Prison_P', 'Prologue_P', 'ProvingGrounds_Trial1_P', 'ProvingGrounds_Trial4_P', 'ProvingGrounds_Trial5_P', 'ProvingGrounds_Trial6_P', 'ProvingGrounds_Trial7_P', 'ProvingGrounds_Trial8_P', 'Raid_P', 'Recruitment_P', 'Sacrifice_P', 'Sanctuary3_P', 'Sanctum_P', 'Strip_P', 'TechSlaughter_P', 'TowerLair_P', 'Towers_P', 'Town_P', 'Trashtown_P', 'Venue_P', 'Village_P', 'Watership_P', 'WetlandsBoss_P', 'WetlandsVault_P', 'Wetlands_P', 'Woods_P', 'MatchAll']

################################################################################################################################################################
# Lists I call to stroe things in. 
# They are called globally so that they may not change.
Mod_Header = []
Reg_hotfix = []
Search_Results = []
File_Results_List = []
################################################################################################################################################################
def ListBoxWindow(List):
    ListWindow = Tk()
    ListWindow.title("Data Table Look Up")
    w = 500
    h = 200 
    ws = ListWindow.winfo_screenwidth()
    hs = ListWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # Reference: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
    # This should add a search bar to help find all text, 
    # also replacing all listboxes with text to see how well that will go
    Fram_Of_Reference = Frame(ListWindow) 
    Label(Fram_Of_Reference,text='Text to find:').pack(side=LEFT)
    
    Find_String = Entry(Fram_Of_Reference)
    Find_String.pack(side=LEFT, fill=BOTH, expand=1)
    Find_String.focus_set()
    
    Find_Text_Button = Button(Fram_Of_Reference, text='Find')   
    Find_Text_Button.pack(side=RIGHT)  
    Fram_Of_Reference.pack(side=TOP)

    Scroll_Bar = Scrollbar(ListWindow)
    Scroll_Bar.pack( side = RIGHT, fill = Y )

    Info_Display_Text_Box = Text(ListWindow, yscrollcommand=Scroll_Bar, width= 120, height=100)

    # Similar to my __interface__ file, depending on what is needed they will add different things
    if List == 1: # Displayes what you should type inside the first section of the hotfix section
        ListWindow.geometry('%dx%d+%d+%d' % (w/1.5, h/1.2, x/2, y*1.5))
        for x in Patch_Types:
            Info_Display_Text_Box.insert('1.0', x + '\n')

    elif List == 2: # Displays a list of the map areas, or you can type MatchAll
        ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x*1.8, y*1.5))
        for x in Map_Locations:
            Info_Display_Text_Box.insert('1.0', x + '\n')

    elif List == 3: # Has all the results of the database search
        ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x*1.8, y/3.5))
        for x in Search_Results:
            Info_Display_Text_Box.insert('1.0', x + '\n')

    elif List == 4: # Displays the contents of when you looked through a file
        ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x/3.8, y/3.5))
        for x in File_Results_List:
            Info_Display_Text_Box.insert('1.0', x + '\n')

    Scroll_Bar.config( command = Info_Display_Text_Box.yview )
    Info_Display_Text_Box.pack(side=BOTTOM)
    
    # Reference: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
    # The function we need to find and highlight text
    def find():
        Info_Display_Text_Box.tag_remove('found', '1.0', END)
        s = Find_String.get()
        if s:
            idx = '1.0'
            while 1:
                idx = Info_Display_Text_Box.search(s, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                Info_Display_Text_Box.tag_add('found', idx, lastidx)
                idx = lastidx
            Info_Display_Text_Box.tag_config('found', foreground='red')
        Find_String.focus_set()
    Find_Text_Button.config(command=find)
################################################################################################################################################################
#This creates a new window that the user can use to look through information
def List_Info():
    ListWindow = Tk()
    ListWindow.title("Data Table Look Up")
    
    # This code sets up the positioning of the first window in the middle of the screen
    w = 500
    h = 200 
    ws = ListWindow.winfo_screenwidth()
    hs = ListWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x, y*1.5))
    
    Button(ListWindow, text="'Patch' section reference ",font=("Times New Roman", 14), command=lambda: ListBoxWindow(1))
    Button(ListWindow, text="Map Names", font=("Times New Roman", 14), command=lambda: ListBoxWindow(2))
    Button(ListWindow, text="Reference Search Results", font=("Times New Roman", 14), command=lambda: ListBoxWindow(3))
    Button(ListWindow, text="Selected File Results", font=("Times New Roman", 14), command=lambda: ListBoxWindow(4))
    # Button(text="5. Click to look at the Stored information that might be helpful to you", font=( "Times New Roman", 18), command=lambda: List_Info())
    
    # This Is so that I do not have to pack everysingle time I create something
    for c in sorted(ListWindow.children):
        ListWindow.children[c].pack()
    ListWindow.mainloop()