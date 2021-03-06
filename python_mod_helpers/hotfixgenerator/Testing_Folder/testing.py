import tkinter as tk
from tkinter import *
from bl3data import BL3Data
from flatten_json import flatten
data = BL3Data()
"""

JSON classifacation
JSONInfo ends with a #, then it is a dict (or str depending on how far down it goes)
JSONInfo ends with a list, then it is a list
"""
# NonUsedInfo = ["_apoc_data_ver", "_jwp_export_idx", "_jwp_is_asset", "_jwp_arr_idx", "_jwp_object_name", "export_type"]
List_1 = []
# List_2 = []
# List_3 = []
# DataNeeded = []

#This will be used to grab all the other information about this particular layer
# Extra_info = []
poollist_name = '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss'

boss_loot = data.get_data(poollist_name)
# Loop through the pool list
for pool in boss_loot[0]['ItemPools']:
    print('Found item pool: {}'.format(pool['ItemPool'][1]))


JSONInfo = data.get_data(poollist_name)
root = tk.Tk()
test = flatten(JSONInfo[0], separator="/")
for key, value in test.items():
    if "/" in str(value):
        List_1.append(value)
List_1.sort()
lb4 = Listbox(root, width=110)
k = 1
for i in List_1:
    lb4.insert(k, i)
    k += 1
lb4.pack()

root.mainloop()


# patients_df = pd.read_json(r'F:\Users\Trevor\Desktop\extracted_new\Game\GameData\Loot\ItemPools\ItemPoolList_Boss.json')
# print(patients_df)

# Hold = type(JSONInfo)
# ############################################################################################################
# def JSON_Parsing_Data(Hold, Data):
#     i = 0
#     #I can change these variables types depending on my needs
#     Instance_1 = 0
#     Instance_2 = ""
#     Instance_3 = None
#     Instance_4 = None
#     Instance_5 = None
#     Instance_5 = None
    
#     if Hold == list:
        
#         while Instance_1 < len(Data):
            
#             for pool in Data[Instance_1]:
                
#                 if type(Data[Instance_1][pool]) == list:
                    
#                     if pool not in List_1: List_1.append(pool)
                
#                 else:
                    
#                     try:
#                         if List_1[i] not in Extra_info: 
#                             Extra_info.append(List_1[i] + "Layer")
#                             i+=1
#                         Extra_info.append(pool + " : " + str(Data[Instance_1][pool]))
                    
#                     except:
#                         Extra_info.append(pool + " : " + str(Data[Instance_1][pool]))
                    
        
#             for Instance_2 in List_1:

#                 while Instance_3 < len(JSONInfo[Instance_1][Instance_2]):
                    
#                     for pool in JSONInfo[Instance_1][Instance_2][Instance_3]:
                        
#                         if pool not in NonUsedInfo:
                            
#                             if pool not in List_2:
#                                 List_2.append(pool)
#             Instance_3 += 1
#     elif Hold == dict:
#         return None
    
#     else:
#         print(Hold)
#         return None

# Iter1 = JSON_Parsing_Data(Hold, JSONInfo)
# # if __name__ == "__main__":