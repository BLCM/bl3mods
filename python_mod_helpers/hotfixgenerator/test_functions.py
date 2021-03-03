import json
# #I needed to make a window in here because i would have cirular logic orther wise
# import tkinter as tk
# from tkinter import *
# # from _global_lists import List_1
# Testwindow = tk.Tk()
# Testwindow.geometry("500x500")
# Testwindow.title("Hot Fix Generator")
# Button(Testwindow,text="1. Mod Header")

# top = Tk()
# Lb1 = Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
# Lb1.pack()
# top.mainloop()
# Listbox(Testwindow)
# k = 0
# for i in List_1:
#     tk.Listbox.insert(k, i)
#     k += 1
# from bl3data import BL3Data

# DATA = BL3Data()


# poollist_name = '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss'

# # boss_loot will contain a serialized version of the poollist.
# # boss_loot[0] will contain the single export, of type `ItemPoolListData`
# boss_loot = DATA.get_data(poollist_name)

# # Loop through the pool list
# test = boss_loot[0]['ItemPools']
# for pool in test:
#     print('Found item pool: {}'.format(pool['ItemPool'][1]))

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)