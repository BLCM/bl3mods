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
#used to select what file you want to get info out of
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import json
from re import error, search
#Global variables
data = BL3Data()


##Function i uses to get only what is needed if you are choosing a JSON file
filenames = [] #stores folder names
with open('TrevorSTroxel/File_Names.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        filenames.append(currentPlace)

funcnames = [] #stores function names
with open('TrevorSTroxel/Function_Names.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        filenames.append(currentPlace)

#locates where the needed file position is in the string to we can grab everythin afterwards
def filestart(string):
    i = 0
    index = 0
    while index <= 0:
        finding = "/" + filenames[i] 
        i+=1   
        if finding in string:
            index = take1.find(finding) 
    return index

while True:
    print("1. mod header")
    print("2. choose file")
    print("3. find all references")
    print("4. make reg hotfix")
    intake = input("Enter command: ")

    if intake == "1":
        input1 = input("Name of the hotfix file: ")
        input2 = input("The actual mod name: ")
        input3 = input("Author's name (You or who ever worked on it): ")
        input4 = input("Discription (NOTE: IT will be stored on one line for right now, will work to improve it later): ")
        input5 = input("Version of this mod: ")
        input6 = input("The catagory in which this mods fits to: ")
        mod = Mod(input1 + '.bl3hotfix',
                input2,
                input3,
                [
                    input4,
                ],
                lic = Mod.CC_BY_SA_40,
                v = input5,
                cats = input6,
                )

    elif intake == "2":
        #i=4 #Whant to start tring to see if the file has a imbedded list, like 'ItemPools, then it will print it out, hen the use can select which one to choose from and loop through that data again'
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        take1 = os.path.splitext(filename)[0] #Removes the files extention, as we dont need it
        proper_path = take1[filestart(take1)::] #this is the data we need to pass in information

        #used to loop through a list, top make sure that the user picks what they want to iterate through
        # A more complicated, but more user friendly version of the .get_data from bl3data, look into later how to make this patter

        Parent = data.get_data(proper_path)

        for pool in Parent[0]:
            #Best way I could figure this out. Will come back to improve on later
            if pool == "_apoc_data_ver":
                no = "pe"
            elif pool == "_jwp_export_idx":
                no = "pe"
            elif pool == "_jwp_is_asset":
                no = "pe"
            elif pool == "_jwp_object_name":
                no = "pe"
            elif pool == "export_type":
                no = "pe"
            else:
                print(pool)
        #Improve on this as this does not cover all cases, will improve on it later
        ans = input("Enter a name from above ")
        Child = Parent[0][ans]
        for pool in Child[0]:
            if pool == "_jwp_arr_idx":
                no = "pe"
            else:
                #This now checks to see if there is anythin worth seeing, other wise it wont display it
                #As I learn more I might have to come pack and change this, but for now it should be fine
                test = pool
                try:
                    for pool in Child:
                        Chadd = ('Information you may like to know: {}'.format(pool[test][1]))
                    print(test)
                except:
                    no = "pe"

        ans2 = input("Enter a name from above ")
        for pool in Child:
            print('Info: {}'.format(pool[ans2][1]))


    elif intake == "3":
        list = []
        input1 = input("What do you want to search for? ")
        info = data.get_refs_from_data(input1)
        for details in info:
            if details[0] not in list:
                list.append(details[0])
        
        list.sort()
        with open("TrevorSTroxel/search_results.txt", "a+") as a_file:
            for items in list:
                a_file.write(str(items) + "\n")
        a_file.close()
        print("Look inside the search results text file")


    elif intake == "4":
        print("NOTE: As of right now, this will be vauge because I am still learning how all the hotfixes work, so keep in mind that not all input requests won't make a lot of since")
        print("I will work to improve on this later, but for now keep in mind that it will be confusing for what I am asking for")
        input1 = input("Hot Fix Type: Mod.PATCH - Will create a SparkPatchEntry hotfix\n"
        "mod.LEVEL- Will create a SparkLevelPatchEntry hotfix\n"
        "mod.EARLYLEVEL- Will create a SparkEarlyLevelPatchEntry hotfix\n"
        "mod.CHAR - Will create a SparkCharacterLoadedEntry hotfix\n"
        # "Bottom onees are currently not used, do not use them"
        # "Mod.PACKAGE - Will create a SparkStreamedPackageEntry hotfix\n"
        # "Mod.POST - Will create a SparkPostLoadedEntry hotfix\n"
        )
        input2 = input("Map Location: ")

        input3 = input("File Path with JSON name and what __JWP__ Object you want to grab from that JSON file: ")

        input4 = input("What you want to manipulate in the JSON file (WIP, will be better later on both discription and whatvalues to grab):")
        input4a = input("Value you want to change: ")

        input5 = input("Type True for most things, else hit enter: ")
        input5a = input("If you are changing a value, insert new value: ")

        input6 = "" #is ment to be blank. may change in the future 

        if input1 == "patch":
            input1 = mod.PATCHlevel
        elif input1 == "level":
            input1 = mod.LEVEL
        elif input1 == "earlylevel":
            input1 = mod.EARLYLEVEL
        elif input1 == "char":
            input1 = mod.CHAR

        mod.reg_hotfix(input1, input2, input3, input4, input5, input6)

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

