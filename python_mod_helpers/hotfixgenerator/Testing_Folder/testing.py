import tkinter as tk
import pandas as pd
from pandastable import Table
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

poollist_name = '/Game/GameData/Loot/ItemPools/ItemPoolList_Boss'
JSONInfo = data.get_data(poollist_name)
Index_1 = 0
while Index_1 < len(JSONInfo):
  for pool in JSONInfo[Index_1]:
      if pool not in NonUsedInfo:
        List_1.append(pool)
  Index_1 += 1

Index_2 = 0
Index_1 = 0
for Object_1 in List_1:
    while Index_2 < len(JSONInfo[Index_1][Object_1]):
        for pool in JSONInfo[Index_1][Object_1][Index_2]:
            if pool not in NonUsedInfo:
                if pool not in List_2:
                    List_2.append(pool)
        Index_2 += 1

Index_2 = 0
Index_1 = 0
for Object_1 in List_1:
    while Index_2 < len(JSONInfo[Index_1][Object_1]):
        for Object_2 in List_2:
            if type(JSONInfo[Index_1][Object_1][Index_2][Object_2]) == list:
                print(JSONInfo[Index_1][Object_1][Index_2][Object_2])
        # for pool in JSONInfo[Index_1][Object_1][Index_2]: