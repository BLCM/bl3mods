#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Arm's Race Gear in Arm's Race
# Copyright (C) 2021 abram/skruntksrunt, Christopher J. Kucera
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
version = '0.0.2'

OUTPUT = 'armsracegearinarmsrace.bl3hotfix'

def parse_args():
    parser = argparse.ArgumentParser(description=f'Arms Race Gear in Arms race v{version}')
    parser.add_argument('--output', type=str, default=OUTPUT, help='Hotfix output file')
    parser.add_argument('--gear', action='store_true',help='Generate hotfix to manipulate specific gear')
    return parser.parse_args()

args = parse_args()
filename = args.output

DFL_LEVEL=Mod.EARLYLEVEL
LEVEL=Mod.LEVEL



def mod_header(output_filename,colour="green"):
    mod = Mod(output_filename,
          f'Arms Race Gear in Arms Race',
          'skruntskrunt, apocalyptech',
          [
              f"Makes the Arms race gear available in Arms race. Thanks to apple1417 and apocalyptech.",
              f"In COOP, COOP players without the mod can equip arms race gear by unequipping a slot",
              f"and picking up an arm's race item. To pickup a torrent, unequip gun slot 1, then",
              f"pickup the torrent. To equip a gas mask, unequip your shield, then pick up the gas mask.",
              f"Note: do not use this mod if you do not own arm's race.",
          ],
          lic=Mod.CC_BY_SA_40,
          v=version,
          cats=['gameplay','armsrace'],
    )
    return mod

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

mod = mod_header(filename)

if args.gear:
    for gear in armsracegear:
        mod.reg_hotfix(DFL_LEVEL, IXORA_MAP, gear, "DlcInventorySetData", "OakDownloadableInventorySetData'\"/Game/PatchDLC/Ixora2/GameData/DLCData/InventorySet_Ixora2\"'")
        mod.reg_hotfix(    LEVEL, IXORA_MAP, gear, "DlcInventorySetData", "OakDownloadableInventorySetData'\"/Game/PatchDLC/Ixora2/GameData/DLCData/InventorySet_Ixora2\"'")

mod.reg_hotfix(LEVEL, 
    IXORA_MAP,
    '/Game/PatchDLC/Ixora/GameData/Mode/FrostSiteGearUpData',
    'DlcPackageData',
    None
)

mod.close()
