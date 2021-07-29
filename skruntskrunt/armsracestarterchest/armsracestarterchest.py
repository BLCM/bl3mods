#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Arm's Race Start Chest Generator
# Copyright (C) 2021 abram/skruntksrunt, altef-4, Christopher J. Kucera
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import json
import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod
import random
import argparse

IXORA_MAP = 'FrostSite_P'
version = '0.2.0'


def parse_args():
    parser = argparse.ArgumentParser(description=f'Arm\'s Race Starter Chest Generator v{version}')
    # parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    return parser.parse_args()

args = parse_args()

DFL_LEVEL=Mod.EARLYLEVEL

WHITE  = "Common"
GREEN  =  "Uncommon"
BLUE   = "Rare"
PURPLE = "VeryRare"
ORANGE = "Legendary"

colours = ["white","green","blue","purple","orange"]
colours_rarity = [WHITE,GREEN,BLUE,PURPLE,ORANGE]



pools = {
    "white": {
        "uc_pistols": f"/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_{WHITE}",
        "uc_smg"    : f"/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_{WHITE}",
        "uc_shield" : f"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_01_{WHITE}",
    },
    "green": {
        "uc_pistols": f"/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_{GREEN}",
        "uc_smg"    : f"/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_{GREEN}",
        "uc_shield" : f"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_02_{GREEN}",
    },
    "blue": {
        "uc_pistols": f"/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_{BLUE}",
        "uc_smg"    : f"/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_{BLUE}",
        "uc_shield" : f"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_03_{BLUE}",
    },
    "purple": {
        "uc_pistols": f"/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_{PURPLE}",
        "uc_smg"    : f"/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_{PURPLE}",
        "uc_shield" : f"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_04_{PURPLE}",
    },
    "orange": {
        "uc_pistols": f"/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_{ORANGE}",
        "uc_smg"    : f"/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_{ORANGE}",
        "uc_shield" : f"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_{ORANGE}",
    }
}

def mod_header(output_filename,colour="green"):
    mod = Mod(output_filename,
          f'Arm\'s Race Starter Chest: {colour}',
          'skruntskrunt',
          [f"Makes the Arm's Race Starter Chest items of {colour} colour"],
          lic=Mod.CC_BY_SA_40,
          v=version,
          cats=['gameplay','armsrace'], # fix this
    )
    return mod

def bias_item_rarity(mod):
    # we can't guarantee initial chest but we can bias against it
    GEARUP = "/Game/PatchDLC/Ixora/GameData/Balance/Table_GearUp_ItemRarity_Standard"
    WHITE  = "Common"
    GREEN  =  "Uncommon"
    BLUE   = "Rare"
    PURPLE = "VeryRare"
    ORANGE = "Legendary"
    BASEWEIGHT = "BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191"
    mod.comment("This is stolen from Poïpoï's Legendary Arm's race CC-BY-SA 4.0 ")
    mod.comment("at https://github.com/BLCM/bl3mods/blob/master/Po%C3%AFpo%C3%AF/Legendary%20Arms%20Race.bl3hotfix")
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, WHITE ,BASEWEIGHT,   1)   # 30
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, GREEN ,BASEWEIGHT, 749)   # 50
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, BLUE  ,BASEWEIGHT, 200)   # 15
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, PURPLE,BASEWEIGHT,  40)   #  4
    mod.table_hotfix(DFL_LEVEL, IXORA_MAP, GEARUP, ORANGE,BASEWEIGHT,  10)   #  1
    
def change_chest_rarity(mod, colour="green",change_key=False):
    # Ok now we manipulate the itempools instead
    valuename = "BaseWeight_7_F9F7E65D4BC13F8CB481169592B2D191"
    # 1% chance here
    valuevalue = "Legendary"
    pistol_equippable = "/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/ItemPool_GearUp_Chest_PS_Equippable"
    pistol_key =  "BalancedItems.BalancedItems[0].ItemPoolData"
    pistol_key2 = "BalancedItems.BalancedItems[0].Weight.DataTableValue"
    pistol_v2 = "None"
    # uc_pistols = "/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Uncommon"
    uc_pistols = pools[colour]["uc_pistols"]
    itempool_pistols = f"ItemPoolData'\"{uc_pistols}\"'"
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, pistol_equippable, pistol_key, itempool_pistols)
    smg_equippable = "/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/ItemPool_GearUp_Chest_AR_SG_SMG_Equippable"
    smg_key = pistol_key
    smg_key2 = pistol_key2
    smg_v2 = "None"
    # uc_smg = "/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_Uncommon"
    uc_smg = pools[colour]["uc_smg"]        
    itempool_smg = f"ItemPoolData'\"{uc_smg}\"'"
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, smg_equippable, smg_key, itempool_smg)
    shield_equippable = "/Game/PatchDLC/Ixora/GameData/Loot/ItemPools/Chest/ItemPool_GearUp_Chest_Shields_Equippable"
    shield_key = pistol_key
    shield_key2 = smg_key2
    shield_v2 = smg_v2
    # uc_shield = "/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_02_Uncommon"
    uc_shield = pools[colour]["uc_shield"]        
    itempool_shield = f"ItemPoolData'\"{uc_shield}\"'"    
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, shield_equippable, shield_key, itempool_shield)
    if change_key:
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, smg_equippable, smg_key2, smg_v2)
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, pistol_equippable, pistol_key2, pistol_v2)
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, shield_equippable, shield_key2, shield_v2)
    

def gen_mod_for_colour(filename, colour):
    mod = mod_header(filename, colour=colour)
    bias_item_rarity(mod)
    change_chest_rarity(mod, colour=colour,change_key=False)
    mod.close()

for colour in colours:
    if colour == "white":
        continue
    filename = f'armsracestarter-{colour}.bl3hotfix'
    gen_mod_for_colour(filename, colour)

