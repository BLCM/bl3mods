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
from _global_lists import NonUsedInfo, List_1, List_2
from tkinter import *
from re import error
#Global variables
DATA = BL3Data()

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

#this SHOULD display the next
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

#Puts in the title of the mod, and also creates the file
def ModHeader(input1, input2, input3, input4, input5, input6):
    Mod(input1 + '.bl3hotfix', input2, input3, [ input4 ], lic = Mod.CC_BY_SA_40, v = input5, cats = input6 )

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

def Search():
    list = []
    input1 = input("What do you want to search for? ")
    info = DATA.get_refs_from_data(input1)
    for details in info:
        if details[0] not in list:
            list.append(details[0])
    list.sort()
    with open("<name>/search_results.txt", "a+") as a_file:
        for items in list:
            a_file.write(str(items) + "\n")
    a_file.close()
    print("Look inside the search results text file")

#This one has a lot of cleaning up to do
def HotFix():
    print("NOTE: As of right now, this will be vauge because I am still learning how all the hotfixes work, so keep in mind that not all input requests won't make a lot of since")
    # print("I will work to improve on this later, but for now keep in mind that it will be confusing for what I am asking for")
    # input1 = input("Hot Fix Type: Mod.PATCH - Will create a SparkPatchEntry hotfix\n"
    # "mod.LEVEL- Will create a SparkLevelPatchEntry hotfix\n"
    # "mod.EARLYLEVEL- Will create a SparkEarlyLevelPatchEntry hotfix\n"
    # "mod.CHAR - Will create a SparkCharacterLoadedEntry hotfix\n"
    # # "Bottom onees are currently not used, do not use them"
    # # "Mod.PACKAGE - Will create a SparkStreamedPackageEntry hotfix\n"
    # # "Mod.POST - Will create a SparkPostLoadedEntry hotfix\n"
    # )
    # input2 = input("Map Location: ")

    # input3 = input("File Path with JSON name and what __JWP__ Object you want to grab from that JSON file: ")

    # input4 = input("What you want to manipulate in the JSON file (WIP, will be better later on both discription and whatvalues to grab):")
    # input4a = input("Value you want to change: ")

    # input5 = input("Type True for most things, else hit enter: ")
    # input5a = input("If you are changing a value, insert new value: ")

    # input6 = "" #is ment to be blank. may change in the future

    # if input1 == "patch":
    #     input1 = mod.PATCH
    # elif input1 == "level":
    #     input1 = mod.LEVEL
    # elif input1 == "earlylevel":
    #     input1 = mod.EARLYLEVEL
    # elif input1 == "char":
    #     input1 = mod.CHAR

    # mod.reg_hotfix(input1, input2, input3, input4, input5, input6)


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