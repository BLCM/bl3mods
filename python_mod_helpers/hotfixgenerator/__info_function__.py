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
from bl3hotfixmod import Mod
from bl3data import BL3Data
from _global_lists import Mod_Header, Reg_hotfix, FileNames, File_Results_List
################################################################################################################################################################
from tkinter import *
from tkinter.filedialog import askopenfilename
from flatten_json import flatten
import os
#Global variables
DATA = BL3Data()
################################################################################################################################################################
# I have to put the program like this because in order to make hotfixes in the way 
# the bl3data/bl3hotfixmod work, it has to be executed in a row in order to work
def Create_HotFix_File():
    #this firat part puts the header inside a new file it creats
    if len(Mod_Header) < 6:
        # If you don't give it someting, this is what I will replace it with
        Mod_Header.extend(["Chadd", "Chadd", "Chadd", "Chadd", "Chadd", "Chadd"])
    
    File_Name = Mod_Header[0]
    Mod_Title = Mod_Header[1]
    Author_Name = Mod_Header[2]
    Description = Mod_Header[3]
    Version = Mod_Header[4]
    Catagory = Mod_Header[5]
    mod = Mod(File_Name + '.bl3hotfix', Mod_Title, Author_Name,[Description, ], lic=Mod.CC_BY_SA_40, v=Version, cats=Catagory,)
    
    
    i = 0
    if i > len(Reg_hotfix):
        None
    else:
        while i < len(Reg_hotfix):
            Package_Tuple = Reg_hotfix[i], Object_Name = Reg_hotfix[i+1], Attribute_Name = Reg_hotfix[i+2], From_Length = Reg_hotfix[i+3], From_Value = Reg_hotfix[i+4], To_Value = Reg_hotfix[i+5],
            if Package_Tuple == "patch":
                Package_Tuple = mod.PATCH
            elif Package_Tuple == "level":
                Package_Tuple = mod.LEVEL
            elif Package_Tuple == "earlylevel":
                Package_Tuple = mod.EARLYLEVEL
            elif Package_Tuple == "char":
                Package_Tuple = mod.CHAR
            mod.reg_hotfix(Package_Tuple, Object_Name, Attribute_Name, From_Length, From_Value, To_Value)
            i += 6
################################################################################################################################################################

################################################################################################################################################################
# The user is able to choose a json file and search through the contents
def FileChoice():
    Tk().withdraw()
    file = askopenfilename(filetypes=[("Choose file", ".json")])
    # Removes the files extention, as we dont need it
    raw_path = os.path.splitext(file)[0]
    i = 0
    index = 0
    if os.path.exists(file) == True:
        while index <= 0:
            Find = "/" + FileNames[i]
            i += 1
            if Find in raw_path:
                index = raw_path.find(Find)
        # this is the data we need to pass in information
        True_Path = raw_path[index::]
        File_Results_Window(True_Path)

#This is stremlinded process of what I already have, but even better than before
def File_Results_Window(True_Path):
    I = 0
    Raw_Data = DATA.get_data(True_Path)
    while I < len(Raw_Data):
        File_Results_List.append(True_Path + ": index " + str(I))
        Refined_Data = flatten(Raw_Data[I], separator="/")
        for key, value in Refined_Data.items():
            File_Results_List.append(str(key) + " : "+ str(value))
        File_Results_List.append("\n")
        I +=1
################################################################################################################################################################
#This was me messing around with how these things work. still learning though
# mod.reg_hotfix(
# mod.LEVEL,
# "Anger_P",
# "/Game/GameData/Regions/RegionManagerData.RegionManagerData",
# "PlayThroughs.PlayThroughs[0].bGameStageTracksPlayerLevelAboveMinimum",
# "True",
# "")

# mod.reg_hotfix(mod.EARLYLEVEL,
# "MatchALL",
# "/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers.DataTable_DamageAndHealthScalers",
# "AI_AdditionalDamagePerLevel,Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86",
# "0.065",
# "")