import tkinter as tk
import pandas as pd
from pandastable import Table
from re import error
import pdb
from bl3data import BL3Data
data = BL3Data()
"""
JSON classifacation
JSONInfo ends with a #, then it is a dict (or str depending on how far down it goes)
JSONInfo ends with a list, then it is a list
"""
NonUsedInfo = ["_apoc_data_ver", "_jwp_export_idx", "_jwp_is_asset", "_jwp_arr_idx", "_jwp_object_name", "export_type"]
List_1 = []
List_2 = []
List_3 = []
DataNeeded = []

#This will be used to grab all the other information about this particular layer
Extra_info = []

poollist_name = '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss'
JSONInfo = data.get_data(poollist_name)

df = pd.DataFrame(JSONInfo) 
print(df) 


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