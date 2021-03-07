################################################################################################################################################################
from tkinter import *
################################################################################################################################################################
##Function i uses to get only what is needed if you are choosing a JSON file
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names
FuncNames = ["get_data", "find", "find_data", "glob", "glob_data", "get_export_idx",
             "get_exports", "get_parts_category_name", "get_extra_anoints"]  # stores function names
# #this is used to remove any data when searching files. may add or remove depending on what I learn later
# NonUsedInfo = ["_apoc_data_ver", "_jwp_export_idx", "_jwp_is_asset", "_jwp_arr_idx", "_jwp_object_name", "export_type"]

#will be used for deciding what kind of hotfix to apply
Patch_Types = ['This is the list of patch types',
               'patch', 'level', 'earlylevel', 'char']
#This will be used to select the map name when creating a hotfix, may change later, but for now i think this is a good idea
Map_Locations = ['The names of all the maps, type one', 'Anger_P', 'Archive_P', 'AtlasHQ_P', 'Bar_P', 'Beach_P', 'BloodyHarvest_P', 'COVSlaughter_P', 'Camp_P', 'Cartels_P', 'CasinoIntro_P', 'Chase_P', 'CityBoss_P', 'CityVault_P', 'City_P', 'Convoy_P', 'Core_P', 'CraterBoss_P', 'CreatureSlaughter_P', 'Crypt_P', 'DesertBoss_P', 'Desert_P', 'Desertvault_P', 'Desolate_P', 'Eldorado_P', 'Experiment_P', 'Facility_P', 'FinalBoss_P', 'Forest_P', 'Frontier_P', 'GuardianTakedown_P', 'Impound_P', 'Lake_P', 'Lodge_P', 'Mansion_P', 'MarshFields_P', 'Mine_P', 'Monastery_P',
                 'MotorcadeFestival_P', 'MotorcadeInterior_P', 'Motorcade_P', 'OrbitalPlatform_P', 'Outskirts_P', 'Prison_P', 'Prologue_P', 'ProvingGrounds_Trial1_P', 'ProvingGrounds_Trial4_P', 'ProvingGrounds_Trial5_P', 'ProvingGrounds_Trial6_P', 'ProvingGrounds_Trial7_P', 'ProvingGrounds_Trial8_P', 'Raid_P', 'Recruitment_P', 'Sacrifice_P', 'Sanctuary3_P', 'Sanctum_P', 'Strip_P', 'TechSlaughter_P', 'TowerLair_P', 'Towers_P', 'Town_P', 'Trashtown_P', 'Venue_P', 'Village_P', 'Watership_P', 'WetlandsBoss_P', 'WetlandsVault_P', 'Wetlands_P', 'Woods_P', 'MatchAll']

################################################################################################################################################################
#used for storing info and grabbing it later
List_1 = []
List_2 = []
List_3 = []
# I will be attempting to store the users input in a list, 
# so that later I can call them later qand execute it all at once
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
    # get screen width and height
    ws = ListWindow.winfo_screenwidth() # width of the screen #width 1920
    hs = ListWindow.winfo_screenheight() # height of the screen #height 1080
    # Middle of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    #Reference: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
    #This should add a search bar to the top of the menu to look for things
    fram = Frame(ListWindow) 
    Label(fram,text='Text to find:').pack(side=LEFT)
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text='Find')   
    butt.pack(side=RIGHT)  
    fram.pack(side=TOP)
    text = Text(ListWindow)  

    if List == 1: #Displayes what you should type inside the first section of the hotfix section
        ListWindow.geometry('%dx%d+%d+%d' % (w/1.5, h/1.2, x/2, y*1.5))
        for x in Patch_Types:
            text.insert(END, x + '\n')
        text.pack(side=BOTTOM) 

    elif List == 2: #Displays a list of the map areas, or you can type MatchAll
        ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x*1.8, y*1.5))
        for x in Map_Locations:
            text.insert(END, x + '\n')
        text.pack(side=BOTTOM) 

    elif List == 3: #Has all the results of the database search
        ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x*1.8, y/3.5))
        ListWindow.title("Data Table Look Up")
        for x in Search_Results:
            text.insert(END, x + '\n')
        text.pack(side=BOTTOM) 

    elif List == 4: #Displays the contents of when you looked through a file
        ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x/3.8, y/3.5))
        for x in File_Results_List:
            text.insert(END, x + '\n')
        text.pack(side=BOTTOM)

    # Reference: https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
    # The function we need to find and highlight text
    def find():
        text.tag_remove('found', '1.0', END)
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                idx = text.search(s, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                text.tag_add('found', idx, lastidx)
                idx = lastidx
            text.tag_config('found', foreground='red')
        edit.focus_set()
    butt.config(command=find)
################################################################################################################################################################
#This creates a new window that the user can use to look through information
def List_Info():
    ListWindow = Tk()
    ListWindow.title("Data Table Look Up")
    w = 500
    h = 200 
    # get screen width and height
    ws = ListWindow.winfo_screenwidth() # width of the screen #width 1920
    hs = ListWindow.winfo_screenheight() # height of the screen #height 1080
    # Middle of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ListWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x, y*1.5))
    Button(ListWindow, text="1. Look At What To Put In the 'Patch' section ",font=("Times New Roman", 14), command=lambda: ListBoxWindow(1))
    Button(ListWindow, text="2. Look At All The Map Names", font=("Times New Roman", 14), command=lambda: ListBoxWindow(2))
    Button(ListWindow, text="3. Look At Your Search Results", font=("Times New Roman", 14), command=lambda: ListBoxWindow(3))
    Button(ListWindow, text="4. File Results", font=("Times New Roman", 14), command=lambda: ListBoxWindow(4))
    # Button(text="5. Click to look at the Stored information that might be helpful to you", font=( "Times New Roman", 18), command=lambda: List_Info())
    for c in sorted(ListWindow.children):
        ListWindow.children[c].pack()
    ListWindow.mainloop()