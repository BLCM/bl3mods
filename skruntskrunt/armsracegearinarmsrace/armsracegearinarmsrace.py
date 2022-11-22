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
version = '0.0.1'


def parse_args():
    parser = argparse.ArgumentParser(description=f'Arms Race Gear in Arms race v{version}')
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
          f'Arms Race Gear in Arms Race',
          'skruntskrunt',
          [f"Makes the Arms race gear available in Arms race. Thanks to apple1417 and apocalyptech. Note: do not use this mod if you do not own arm's race."],
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
armsracegear = [
    "/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Deathrattle/Balance/InvBalD_Artifact_Deathrattle",
    "/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/HolyGrail/Balance/InvBalD_Artifact_HolyGrail",
    "/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet",
    "/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Toboggan/Balance/InvBalD_Artifact_Toboggan",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/L01/InvBalD_CM_Ixora_BSM_L01",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_01_Common",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_02_Uncommon",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_03_Rare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_04_VeryRare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/L01/InvBalD_CM_Ixora_GUN_L01",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_01_Common",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_02_Uncommon",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_03_Rare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_04_VeryRare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L01/InvBalD_CM_Ixora_OPE_L01",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/InvBalD_CM_Ixora_OPE_L02",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_01_Common",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_02_Uncommon",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_03_Rare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_04_VeryRare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/L01/InvBalD_CM_Ixora_SRN_L01",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_01_Common",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_02_Uncommon",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_03_Rare",
    "/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_04_VeryRare",
    "/Game/PatchDLC/Ixora/Gear/GrenadeMods/HOTSpring/Balance/InvBalD_GM_HOTSpring",
    "/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Beskar/Balance/InvBalD_Shield_Beskar",
    "/Game/PatchDLC/Ixora/Gear/Shields/_Unique/InfernalWish/Balance/InvBalD_Shield_InfernalWish",
    "/Game/PatchDLC/Ixora/Gear/Shields/_Unique/MadCap/Balance/InvBalD_Shield_LGD_Madcap",
    "/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Ventilator/Balance/InvBalD_Shield_Ventilator",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/BinaryOperator/Balance/Balance_MAL_SR_BinaryOperator",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Boogeyman/Balance/Balance_VLA_SR_Boogeyman",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/CriticalThug/Balance/Balance_SG_Torgue_CriticalThug",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/DarkArmy/Balance/Balance_SM_TED_DarkArmy",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Firefly/Balance/Balance_PS_VLA_Firefly",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/HotfootTeddy/Balance/Balance_AR_TOR_Hotfoot",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Kickcharger/Balance/Balance_HW_VLA_ETech_Kickcharger",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/PlasmaCoil/Balance/Balance_SM_MAL_PlasmaCoil",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/SpiritOfMaya/Balance/Balance_PS_ATL_SpiritOfMaya",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Torrent/Balance/Balance_SM_DAL_Torrent",
    "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Trickshot/Balance/Balance_PS_JAK_Trickshot",
]

filename = 'armsracegearinarmsrace.bl3hotfix'
mod = mod_header(filename)
for gear in armsracegear:
    mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, gear, "DlcInventorySetData", "OakDownloadableInventorySetData'\"/Game/PatchDLC/Ixora2/GameData/DLCData/InventorySet_Ixora2\"'")
mod.close()
