"""
This program was heavly based on apocalyptech bl3mods/python_mod_help
Link to current reposatory: https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers
apocalyptech has written most all functions that I am using. All I am doing is making
a interface for people to use.

At the time of coding this there is nothing like a BLCMM or other tools to make the hotfix for you, 
so you have to manually enter all data in order for it to work, and even then my coding my be off in some way.

BL3 is still in its modding infancy so if this program becomes obsolete in the future, well I still found it a great experience
making this and I hope BL3 live as long as BL3 did, as they are tied for soem of my favorite games of all times
"""
from bl3hotfixmod import Mod
from bl3data import BL3Data
from _global_lists import NonUsedInfo, List_1, List_2, Mod_Header, Reg_hotfix, Search_Results
from tkinter import *
from re import error
#Global variables
DATA = BL3Data()
################################################################################################################################################################
def Create_HotFix_File():
    #this firat part puts the header inside a new file it creats
    if len(Mod_Header) == 0:
        Mod_Header.extend(["Chadd", "Chadd", "Chadd", "Chadd", "Chadd", "Chadd"]) #If you don't give it someting, this is what I will replace it with
    input1 = Mod_Header[0], input2 = Mod_Header[1], input3 = Mod_Header[2], input4 = Mod_Header[3], input5 = Mod_Header[4], input6 = Mod_Header[5],
    mod = Mod(input1 + '.bl3hotfix', input2, input3, [ input4, ], lic=Mod.CC_BY_SA_40, v = input5, cats=input6,)
    
    i = 0
    if i > len(Reg_hotfix):
        None
    else:
        while i < len(Reg_hotfix):
            input1 = Reg_hotfix[i], input2 = Reg_hotfix[i+1], input3 = Reg_hotfix[i+2], input4 = Reg_hotfix[i+3], input5 = Reg_hotfix[i+4], input6 = Reg_hotfix[i+5],
            if input1 == "patch":
                input1 = mod.PATCH
            elif input1 == "level":
                input1 = mod.LEVEL
            elif input1 == "earlylevel":
                input1 = mod.EARLYLEVEL
            elif input1 == "char":
                input1 = mod.CHAR
            mod.reg_hotfix( input1, input2, input3, input4, input5, input6)
            i += 6
################################################################################################################################################################
# #will work on making this is similar to interface, so that i can reuse things constantly
# def SearchResults(input):
#     Testwindow = Tk()
#     Testwindow.title("Results for: " + input)
#     Lb1 = Listbox(Testwindow, width = 150)
#     k = 1
#     for i in List_1:
#         Lb1.insert(k, i)
#         k += 1
#     Lb1.pack()
#     Testwindow.mainloop()

#now it will search for all items related to it regardless of capitalization or puncuation
def Search(input):
    info = DATA.get_refs_from_data(input.capitalize())
    for details in info:
        if details[0] not in List_1:
            Search_Results.append(details[0])
################################################################################################################################################################
#I needed to make a window in here because i would have cirular logic orther wise
def WindowSel(proper_path):
    Testwindow = Tk()
    Testwindow.title("JSON File Content Display")
    Lb1 = Listbox(Testwindow, width=30)
    k = 1
    for i in List_1:
        Lb1.insert(k, i)
        k += 1
    Lb1.pack()
    testing = Button(Testwindow, text="Select to see content", font=("Times New Roman", 18),
        command= lambda: JSONInfo2(proper_path, Lb1.get(ANCHOR)))
    testing.pack()
    Testwindow.mainloop()

#this SHOULD display the next Layer of content
def WindowSel2():
    Testwindow2 = Tk()
    Testwindow2.title("JSON File Content Display")
    Lb1 = Listbox(Testwindow2, width=30)
    k = 1
    for i in List_2:
        Lb1.insert(k, i)
        k += 1
    Lb1.pack()
    # testing = Button(Testwindow, text="test", font=("Times New Roman", 18),
    #     command= lambda: JSONInfo2(proper_path, Lb1.get(ANCHOR)))
    # testing.pack()
    Testwindow2.mainloop()

#come back to this later
#Had to split these two functions up so that user can choose what to select next
def JSONInfo(proper_path):
    # The way that this is set up know, it will now iterate through 
    # all cache items, and then the user will have the whole list to view
    i = 0
    Parent = DATA.get_data(proper_path)
    while i < len(Parent):
        for pool in Parent[i]:
            if pool not in NonUsedInfo:
                List_1.append(pool)
        i += 1
    WindowSel(proper_path)  

#Thisn will run after the user chooses one of the things found inside the file they have chosen
def JSONInfo2(proper_path, info): 
    k = 0
    Parent = DATA.get_data(proper_path)
    Child = Parent[k][info]
    try:
        for key, value in Child.items():
            print("{} : {}".format(key, value))
            List_2.append(key, value)
    except Child == error:
        while k < len(Parent):
            k += 1
            Child = Parent[k][info]
            for key, value in Child.items():
                print("{} : {}".format(key, value))
                List_2.append(key)
    except:
        print("something else went wrong, find out what")
    WindowSel2()    

    # else:
    #     Child = Parent[k+1][info]
    #     for key, value in Child.items():
    #         print("{} : {}".format(key, value))
    #         List_2.append(key)

        # for pool in Child[0]:
        #     if pool not in NonUsedInfo:
        #         FilePool = pool
        #         try:
        #             for pool in Child:
        #                 None
        #             List_2.append(FilePool)
        #             print(FilePool)
        #         except:
        #             None
        #     ans2 = input("Enter a name from above: ")
        #     for pool in Child:
        #         print('Info: {}'.format(pool[ans2][1]))
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