from tkinter import *
##Function i uses to get only what is needed if you are choosing a JSON file
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names
FuncNames = ["get_data", "find", "find_data", "glob", "glob_data", "get_export_idx",
             "get_exports", "get_parts_category_name", "get_extra_anoints"]  # stores function names
#this is used to remove any data when searching files. may add or remove depending on what I learn later
NonUsedInfo = ["_apoc_data_ver", "_jwp_export_idx", "_jwp_is_asset",
               "_jwp_object_name", "export_type", "_jwp_arr_idx"]

#will be used for deciding what kind of hotfix to apply
Patch_Types = ['This is the list of patch types, type one', 'patch', 'level', 'earlylevel', 'char']
#This will be used to select the map name when creating a hotfix, may change later, but for now i think this is a good idea 
Map_Locations = ['The names of all the maps, type one', 'Anger_P','Archive_P','AtlasHQ_P','Bar_P','Beach_P','BloodyHarvest_P','COVSlaughter_P','Camp_P','Cartels_P','CasinoIntro_P','Chase_P','CityBoss_P','CityVault_P','City_P','Convoy_P','Core_P','CraterBoss_P','CreatureSlaughter_P','Crypt_P','DesertBoss_P','Desert_P','Desertvault_P','Desolate_P','Eldorado_P','Experiment_P','Facility_P','FinalBoss_P','Forest_P','Frontier_P','GuardianTakedown_P','Impound_P','Lake_P','Lodge_P','Mansion_P','MarshFields_P','Mine_P','Monastery_P','MotorcadeFestival_P','MotorcadeInterior_P','Motorcade_P','OrbitalPlatform_P','Outskirts_P','Prison_P','Prologue_P','ProvingGrounds_Trial1_P','ProvingGrounds_Trial4_P','ProvingGrounds_Trial5_P','ProvingGrounds_Trial6_P','ProvingGrounds_Trial7_P','ProvingGrounds_Trial8_P','Raid_P','Recruitment_P','Sacrifice_P','Sanctuary3_P','Sanctum_P','Strip_P','TechSlaughter_P','TowerLair_P','Towers_P','Town_P','Trashtown_P','Venue_P','Village_P','Watership_P','WetlandsBoss_P','WetlandsVault_P','Wetlands_P','Woods_P', 'MatchAll']


#used for storing info and grabbing it later
List_1 = []
List_2 = []
List_3 = []

#I will be attempting to store the users input in a list, so that later I can call them later qand execute it all at once
Mod_Header = []
Reg_hotfix = []

#now this is used as a reference point for users
def Information():
    Nwindow = Tk()
    Nwindow.title("test")
    lb1 = Listbox(Nwindow, width = 35)
    k = 1
    for i in Patch_Types:
        lb1.insert(k, i)
        k += 1
    lb1.pack()
    lb2 = Listbox(Nwindow, width = 35)
    k = 1
    for i in Map_Locations:
        lb2.insert(k, i)
        k += 1
    lb2.pack()
    Nwindow.mainloop()