#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
from bl3hotfixmod.bl3hotfixmod import Mod

(AR, HV, PS, SG, SM, SR) = range(6)
(ATL, COV, DAL, HYP, JAK, MAL, TED, TOR, VLA) = range(9)

eng_types = {
        AR: 'Assault Rifles',
        HV: 'Heavy Weapons',
        PS: 'Pistols',
        SG: 'Shotguns',
        SM: 'SMGs',
        SR: 'Sniper Rifles',
        }
eng_manufacturers = {
        ATL: 'Atlas',
        COV: 'COV',
        DAL: 'Dahl',
        HYP: 'Hyperion',
        JAK: 'Jakobs',
        MAL: 'Maliwan',
        TED: 'Tediore',
        TOR: 'Torgue',
        VLA: 'Vladof',
        }

# Get custom manufacturers to lock, from the user (if provided)
arg_to_man = {
        'atl': ATL,
        'cov': COV,
        'dal': DAL,
        'hyp': HYP,
        'jak': JAK,
        'mal': MAL,
        'ted': TED,
        'tor': TOR,
        'vla': VLA,
        }
custom_to_lock = set()
processed_args = []
eng_args = []
for gun_type in sys.argv[1:]:
    gun_type = gun_type.lower()
    processed_args.append(gun_type)
    if gun_type in arg_to_man:
        custom_to_lock.add(arg_to_man[gun_type])
        eng_args.append(eng_manufacturers[arg_to_man[gun_type]])
    else:
        raise Exception('{} not known as a manufacturer.  Valid values: {}'.format(gun_type, ', '.join(sorted(arg_to_man.keys()))))
if len(custom_to_lock) == 1:
    print('Not generating single-manufacturer custom file')
    custom_to_lock = set()
    processed_args = []
    eng_args = []

###
### This script now duplicates practically all of gen_expanded_legendary_pools.py.
### Be sure to update both when gear changes!
###

def set_pool(mod, pool_to_set, balances):

    parts = []
    for (bal, weight) in balances:
        full_bal = Mod.get_full_cond(bal)
        part = '(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData\'"{}"\',Weight=(BaseValueConstant={}))'.format(
                full_bal, full_bal,
                round(weight, 6),
                )
        parts.append(part)
    mod.reg_hotfix(Mod.PATCH, '',
            pool_to_set,
            'BalancedItems',
            '({})'.format(','.join(parts)))

addition_scale = 0.6
type_pools = [
        (AR, [
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Common', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Uncommon', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Rare', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_VeryRare', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_ETech_Rare', False, [COV, VLA, DAL, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_ETech_VeryRare', False, [COV, VLA, DAL, TOR]),
            ],
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary', [
                ### Original Pool

                # Carrier
                ('/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier.Balance_ATL_AR_Carrier', ATL, 1),
                # Rebel Yell
                ('/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell.Balance_ATL_AR_RebelYell', ATL, 1),
                # Pain is Power / Embrace the Pain
                ('/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR', COV, 2),
                # Sawbar
                ('/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar.Balance_AR_COV_Sawbar', COV, 1),
                # Barrage
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage.Balance_DAL_AR_Barrage', DAL, 1),
                # Breath of the Dying
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD.Balance_DAL_AR_BOTD', DAL, 1),
                # Kaos
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos.Balance_DAL_AR_Kaos', DAL, 1),
                # Star Helix
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix.Balance_DAL_AR_StarHelix', DAL, 1),
                # Warlord
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord.Balance_DAL_AR_Warlord', DAL, 1),
                # Gatling Gun
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun.Balance_AR_JAK_04_GatlingGun', JAK, 1),
                # Lead Sprinkler
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler.Balance_AR_JAK_LeadSprinkler', JAK, 1),
                # Rowan's Call
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall.Balance_AR_JAK_RowansCall', JAK, 1),
                # Alchemist
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist.Balance_AR_TOR_Alchemist', TOR, 1),
                # Bearcat
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat.Balance_AR_TOR_Bearcat', TOR, 1),
                # Laser-Sploder
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder.Balance_AR_TOR_LaserSploder', TOR, 1),
                # Try-Bolt
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt.Balance_AR_TOR_TryBolt', TOR, 1),
                # Damned
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn', VLA, 1),
                # The Dictator
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator.Balance_AR_VLA_Dictator', VLA, 1),
                # Faisor
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor.Balance_AR_VLA_Faisor', VLA, 1),
                # Lucian's Call
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall.Balance_AR_VLA_LuciansCall', VLA, 1),
                # Ogre
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre.Balance_AR_VLA_Ogre', VLA, 1),
                # Super Shredifier
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier.Balance_AR_VLA_Sherdifier', VLA, 1),
                # Boom Sickle / Sickle
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle', VLA, 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Good Juju
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju', DAL, 1),
                # Juliet's Dazzle
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop', TOR, 1),
                # Zheitsev's Eruption
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev', COV, 1),

                ### DLC1 (Moxxi's Heist)

                # Digby's Smooth Tube
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby.Balance_DAL_AR_Digby', DAL, 1*addition_scale),
                # Brad Luck
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash.Balance_AR_COV_Trash', COV, 1*addition_scale),
                # La Varlope
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope.Balance_AR_TOR_Varlope', TOR, 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Clairvoyance
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance', JAK, 1),
                # Seeryul Killur
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal', COV, 1),
                # Mutant
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant', JAK, 1),
                # Soulrender
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender', DAL, 1),
                # Stauros' Burn
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom', COV, 1),

                ### Revenge of the Cartels

                # NoPewPew
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew', COV, 1),
                # O.P.Q. System
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ', ATL, 1),

                ### Mayhem 2.0

                # The Monarch
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch', VLA, 1),

                ### Guardian Takedown

                # Web Slinger
                ('/Game/PatchDLC/Takedown2/Gear/Weapons/WebSlinger/Balance/Balance_AR_VLA_WebSlinger', VLA, 1),

                ### Additions

                # Earworm
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm', DAL, 1*addition_scale),
                # Hail
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail.Balance_DAL_AR_Hail', DAL, 1*addition_scale),
                # Bekah
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah.Balance_AR_JAK_Bekah', JAK, 1*addition_scale),
                # Hand of Glory
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory.Balance_AR_JAK_HandOfGlory', JAK, 1*addition_scale),
                # Pa's Rifle
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle.Balance_AR_JAK_PasRifle', JAK, 1*addition_scale),
                # Traitor's Death
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath.Balance_AR_JAK_TraitorsDeath', JAK, 1*addition_scale),
                # Amber Management
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement.Balance_AR_TOR_AmberManagement', TOR, 1*addition_scale),
                # The Big Succ - ordinarily a mission item, pretty lame, but we'll add it in at a lower probability anyway
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc.Balance_AR_VLA_BigSucc', VLA, 0.2*addition_scale),
                ])),
        (HV, [
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Common', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Uncommon', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Rare', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_VeryRare', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_ETech_Rare', False, [TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_ETech_VeryRare', False, [TOR, VLA]),
            ],
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary', [
                ### Original pool

                # Ruby's Wrath
                ('/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath.Balance_HW_ATL_RubysWrath', ATL, 1),
                # Scourge
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm.Balance_HW_TOR_Swarm', TOR, 1),
                # Tunguska
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska.Balance_HW_TOR_Tunguska', TOR, 1),
                # Jericho
                ('/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst.Balance_HW_VLA_CloudBurst', VLA, 1),

                ### DLC1 (Moxxi's Heist)

                # Creamer
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer.Balance_HW_TOR_Creamer', TOR, 1),
                # ION CANNON
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon.Balance_HW_VLA_IonCannon', VLA, 1),
                # Nukem
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem.Balance_HW_TOR_Nukem', TOR, 1),

                ### Revenge of the Cartels

                # Yellowcake
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake', COV, 1),

                ### Mayhem 2.0

                # Backburner
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner', VLA, 1),
                # Plaguebearer
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague', TOR, 1),

                ### Guardian Takedown

                # Globetrottr
                ('/Game/PatchDLC/Takedown2/Gear/Weapons/Globetrotter/Balance/Balance_HW_COV_Globetrotter', COV, 1),

                ### Additions

                # Freeman
                ('/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman.Balance_HW_ATL_Freeman', ATL, 1*addition_scale),
                # Hot Drop
                ('/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop.Balance_HW_COV_HotDrop', COV, 1*addition_scale),
                # Porta-Pooper 5000
                ('/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper.Balance_HW_COV_PortaPooper', COV, 1*addition_scale),
                # Agonizer 1500
                ('/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror', COV, 1*addition_scale),
                # Gettleburger
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon.Balance_HW_TOR_BurgerCannon', TOR, 1*addition_scale),
                # Hive
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive.Balance_HW_TOR_Hive', TOR, 1*addition_scale),
                # Quadomizer
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager.Balance_HW_TOR_Rampager', TOR, 1*addition_scale),
                # R.Y.N.A.H.
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO.Balance_HW_TOR_RYNO', TOR, 1*addition_scale),
                # Mongol
                ('/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol', VLA, 1*addition_scale),
                ])),
        (PS, [
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Common', False, [JAK, DAL, TED, VLA, MAL, COV, TOR, ATL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Uncommon', False, [JAK, DAL, TED, VLA, MAL, COV, TOR, ATL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Rare', False, [JAK, DAL, TED, VLA, MAL, COV, TOR, ATL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_VeryRare', False, [JAK, DAL, TED, VLA, MAL, COV, TOR, ATL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_ETech_Rare', False, [DAL, COV, MAL, TED, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_ETech_VeryRare', False, [DAL, COV, MAL, TED, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_FirstGuns', False, [JAK, DAL, TED, VLA, MAL, COV, TOR, ATL]),

            # Manufacturer must exist to touch these pools
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Default', True, [DAL, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_SecondGunA', True, [JAK, DAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_SecondGunB', True, [JAK, DAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Test', True, [JAK, DAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_TestTwo', True, [JAK, DAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/Elemental/ItemPool_Pistols_Common_Fire', True, [DAL, TED, VLA, MAL, COV, TOR]),
            ],
            ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary', [
                ### Original pool

                # Linoge
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion.Balance_PS_COV_Legion', COV, 1),
                # AAA
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA.Balance_DAL_PS_AAA', DAL, 1),
                # Hornet
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet.Balance_DAL_PS_Hornet', DAL, 1),
                # Nemesis
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis.Balance_DAL_PS_Nemesis', DAL, 1),
                # The Flood
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc', JAK, 1),
                # Maggie
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie', JAK, 1),
                # The Companion
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion.Balance_PS_JAK_MelsCompanion', JAK, 1),
                # The Duc
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc.Balance_PS_JAK_TheDuc', JAK, 1),
                # Unforgiven
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven.Balance_PS_JAK_Unforgiven', JAK, 1),
                # Wagon Wheel
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel.Balance_PS_JAK_WagonWheel', JAK, 1),
                # Hellshock
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock', MAL, 1),
                # Superball
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber', MAL, 1),
                # Thunderball Fists
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists', MAL, 1),
                # Bangarang
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang.Balance_PS_TED_Bangerang', TED, 1),
                # Baby Maker ++
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker.Balance_PS_Tediore_BabyMaker', TED, 1),
                # Gunerang
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang.Balance_PS_TED_Gunerang', TED, 1),
                # Devastator
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator', TOR, 1),
                # Echo / Breeder
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo.Balance_PS_TOR_Echo', TOR, 2),
                # Devils Foursum
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM.Balance_PS_TOR_4SUM', TOR, 1),
                # Roisen's Thorns
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns.Balance_PS_TOR_RoisensThorns', TOR, 1),
                # Infinity
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti.Balance_PS_VLA_Infiniti', VLA, 1),
                # Magnificent
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent', VLA, 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Moonfire
                ('/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon', TOR, 1),
                # S3RV-80S-EXECUTE
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute', TED, 1),

                ### DLC1 (Moxxi's Heist)

                # Craps
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps.Balance_PS_TOR_Craps', TOR, 1),
                # Lucky 7
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7', JAK, 1),
                # Robo-Melter
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher.Balance_PS_JAK_RoboMasher', JAK, 1*addition_scale),
                # Scoville
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville.Balance_PS_TOR_Scoville', TOR, 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Bite Size
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize', JAK, 1),
                # Frozen Devil
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil', MAL, 1),
                # Hydrafrost
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost', COV, 1),
                # Kaleidoscope
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope', DAL, 1*addition_scale),
                # Little Yeeti
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti', JAK, 1),
                # Love Drill (legendary version)
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary', JAK, 1),
                # Seventh Sense (legendary version)
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense', JAK, 1),

                ### Revenge of the Cartels

                # Grease Trap
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap', MAL, 1),
                # Ice Pick - nothing special about it, just a regular Maliwan pistol
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IcePick/Balance/Balance_PS_MAL_IcePick', MAL, 0.2*addition_scale),

                ### Mayhem 2.0

                # Multi-tap
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap', ATL, 1),

                ### Additions

                # Linc
                ('/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill.Balance_PS_ATL_Drill', ATL, 1*addition_scale),
                # Peacemonger
                ('/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger.Balance_PS_ATL_Warmonger', ATL, 1*addition_scale),
                # Extreme Hangin' Chadd
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad.Balance_PS_COV_Chad', COV, 1*addition_scale),
                # Pestilence
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion', COV, 1*addition_scale),
                # The Killing Word
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece.Balance_PS_COV_Mouthpiece', COV, 1*addition_scale),
                # Psycho Stabber
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber.Balance_PS_COV_PsychoStabber', COV, 1*addition_scale),
                # SkekSil
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis.Balance_PS_COV_Skeksis', COV, 1*addition_scale),
                # Omniloader
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader.Balance_DAL_PS_Omniloader', DAL, 1*addition_scale),
                # Night Flyer
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman.Balance_DAL_PS_Rakkman', DAL, 1*addition_scale),
                # Amazing Grace
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace.Balance_PS_JAK_AmazingGrace', JAK, 1*addition_scale),
                # Buttplug
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug.Balance_PS_JAK_Buttplug', JAK, 1*addition_scale),
                # King's Call / Queen's Call
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother.Balance_PS_JAK_GodMother', JAK, 1.2*addition_scale),
                # Dead Chamber
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent.Balance_PS_JAK_Malevolent', JAK, 1*addition_scale),
                # Rogue-Sight (mission item, but somewhat unique thanks to the homing bullets)
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver.Balance_PS_JAK_SpyRevolver', JAK, 1*addition_scale),
                # Hyper-Hydrator
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator', MAL, 1*addition_scale),
                # Starkiller
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller', MAL, 1*addition_scale),
                # Sellout
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch', MAL, 1*addition_scale),
                # Scorpio
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre', TED, 1*addition_scale),
                # Heckle - quite uninteresting, has no unique effects.  Bump its weight down even more than the others.
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle', TOR, 0.5*addition_scale),
                # Hyde - quite uninteresting, has no unique effects.  Bump its weight down even more than the others.
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde', TOR, 0.5*addition_scale),
                # Girth Blaster Elite (joke weapon)
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf.Balance_PS_TOR_Nurf', TOR, 0.2*addition_scale),
                # Occultist
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy.Balance_PS_TOR_Troy', TOR, 1*addition_scale),
                # Bone Shredder
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder.Balance_PS_VLA_BoneShredder', VLA, 1*addition_scale),
                # The Leech
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech.Balance_PS_VLA_TheLeech', VLA, 1*addition_scale),
                ])),
        (SG, [
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Common', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Uncommon', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Rare', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_VeryRare', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_ETech_Rare', False, [HYP, MAL, TED, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_ETech_Rare', False, [HYP, MAL, TED, TOR]),

            # Manufacturer must exist to touch these pools
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Monastery', True, [HYP, JAK]),
            ],
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary', [
                ### Original pool

                # Face-puncher
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick.Balance_SG_HYP_Brick', HYP, 1),
                # Conference Call
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall.Balance_SG_HYP_ConferenceCall', HYP, 1),
                # Brainstormer
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor.Balance_SG_HYP_Redistributor', HYP, 1),
                # The Butcher
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher.Balance_SG_HYP_TheButcher', HYP, 1),
                # Hellwalker
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker.Balance_SG_JAK_Hellwalker', JAK, 1),
                # T.K.'s Wave / T.K's Heatwave / T.K's Shockwave / The Tidal Wave
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave.Balance_SG_JAK_Unique_Wave', JAK, 1),
                # Projectile Recursion
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion', MAL, 1),
                # Trevonator
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev', MAL, 1),
                # Kill-o'-the-Wisp
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp', MAL, 1),
                # Polybius
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius.Balance_SG_TED_Polybius', TED, 1),
                # Flakker
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker.Balance_SG_Torgue_Flakker', TOR, 1),
                # The Boring Gun
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring.Balance_SG_TOR_Boring', TOR, 1),
                # The Lob
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob', TOR, 1),

                ### Bloody Harvest Additions

                # Fearmonger
                ('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger.Balance_SG_HYP_ETech_Fearmonger', HYP, 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Tiggs' Boom
                ('/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom', TOR, 1),
                # Vosk's Deathgrip
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip', MAL, 1),

                ### DLC1 (Moxxi's Heist)

                # Heart Breaker
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker.Balance_SG_HYP_HeartBreaker', HYP, 1),
                # Melt Facer
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer.Balance_SG_HYP_MeltFacer', HYP, 1*addition_scale),
                # Slow Hand
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand.Balance_SG_HYP_SlowHand', HYP, 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Anarchy
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy', TED, 1),
                # Firecracker
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker', HYP, 1*addition_scale),
                # Insider
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider', MAL, 1),
                # Flama Diddle
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen', TED, 1),
                # Sacrificial Lamb
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb', TED, 1*addition_scale),
                # Shocker
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker', TOR, 1),
                # The Cure
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure', JAK, 1*addition_scale),
                # Nothingness
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing', MAL, 1),

                ### Broken Hearts Additions

                # Superstreamer (just a somewhat partlocked purple Tediore shotgun, only thing special is the material.  no red text, even!)
                ('/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/TwitchPrime/Balance/Balance_SG_TED_Twitch.Balance_SG_TED_Twitch', TED, 0.5*addition_scale),

                ### Revenge of the Cartels

                # Iceburger
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger', HYP, 1),

                ### Mayhem 2.0

                # Reflux
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux', HYP, 1),

                ### Additions

                # Phebert
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert.Balance_SG_HYP_Phebert', HYP, 1*addition_scale),
                # Fingerbiter
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter.Balance_SG_JAK_Fingerbiter', JAK, 1*addition_scale),
                # The Garcia
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia.Balance_SG_JAK_Garcia', JAK, 1*addition_scale),
                # Nimble Jack
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble.Balance_SG_JAK_Nimble', JAK, 1*addition_scale),
                # One Pump Chump
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch.Balance_SG_JAK_OnePunch', JAK, 1*addition_scale),
                # Sledge's Shotgun / Sledge's Super Shotgun
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge.Balance_SG_JAK_LGD_Sledge', JAK, 1*addition_scale),
                # Mind-Killer
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2.Balance_SG_MAL_Mouthpiece2', MAL, 1*addition_scale),
                # Shrieking Devil
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek', MAL, 1*addition_scale),
                # Manic Pixie Dream Gun
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Balance/Balance_SG_TED_FriendZone.Balance_SG_TED_FriendZone', TED, 1*addition_scale),
                # The Horizon
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon.Balance_SG_TED_Horizon', TED, 1*addition_scale),
                # Creeping Death
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge', TED, 1*addition_scale),
                # Chomper
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog.Balance_SG_Torgue_Balrog', TOR, 1*addition_scale),
                # Black Flame (mission item, somewhat unremarkable)
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha.Balance_SG_TOR_Brewha', TOR, 0.5*addition_scale),
                # Redline
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine.Balance_SG_Torgue_RedLine', TOR, 1*addition_scale),
                # Thumper
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper.Balance_SG_Torgue_Thumper', TOR, 1*addition_scale),
                ])),
        (SM, [
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Common', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Uncommon', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Rare', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_VeryRare', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_ETech_Rare', False, [DAL, HYP, MAL, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_ETech_VeryRare', False, [DAL, HYP, MAL, TED]),
            ],
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary', [
                ### Original pool

                # Night Hawkin
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag.Balance_SM_DAL_Demoskag', DAL, 1),
                # Ripper
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper.Balance_SM_DAL_Ripper', DAL, 1),
                # Sleeping Giant
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant.Balance_SM_DAL_SleepingGiant', DAL, 1),
                # Vanquisher
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher.Balance_SM_DAHL_Vanquisher', DAL, 1),
                # Bitch
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch.Balance_SM_HYP_Bitch', HYP, 1),
                # Crossroad
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad.Balance_SM_HYP_Crossroad', HYP, 1),
                # Handsome Jackhammer
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome.Balance_SM_HYP_Handsome', HYP, 1),
                # XZ41
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ.Balance_SM_HYP_XZ', HYP, 1),
                # Cutsman
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman', MAL, 1),
                # Destructo Spinner
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin', MAL, 1),
                # Devoted
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted', MAL, 1),
                # Long Musket
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower.Balance_SM_TED_NotAFlamethrower', TED, 1),
                # Ten Gallon
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon.Balance_SM_TED_TenGallon', TED, 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Redistributor
                ('/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2', HYP, 1),
                # Kyb's Worth
                ('/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth', MAL, 1),
                # P2P Networker
                ('/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link', MAL, 1),
                # Crader's EM-P5
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5', DAL, 1),

                ### DLC1 (Moxxi's Heist)

                # Boomer
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer.Balance_SM_DAL_Boomer', DAL, 1),
                # Cheap Tips
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips.Balance_SM_HYP_CheapTips', HYP, 1),
                # Ember's Purge
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge.Balance_SM_MAL_EmbersPurge', MAL, 1),
                # ION LASER
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser.Balance_SM_MAL_IonLaser', MAL, 1),
                # Just Kaus
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic.Balance_SM_HYP_JustCaustic', HYP, 1*addition_scale),

                ### DLC2 (Guns, Love, and Tentacles)

                # Oldridian
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian', HYP, 1),
                # SF Force
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce', MAL, 1),
                # Short Stick (legendary version)
                ('/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick_Legendary', HYP, 1),

                ### Broken Hearts additions

                # Terminal Polyaimorous
                ('/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim.Balance_SM_MAL_PolyAim', MAL, 1),

                ### Revenge of the Cartels

                # Needle Gun
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun', TED, 1),
                # Pricker
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker', HYP, 1*addition_scale),

                ### Mayhem 2.0

                # D.N.A.
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA', MAL, 1),
                # Kaoson
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson', DAL, 1),

                ### Guardian Takedown

                # Smog
                ('/Game/PatchDLC/Takedown2/Gear/Weapons/Smog/Balance/Balance_SM_HYP_Smog', HYP, 1),

                ### Additions

                # Hellfire
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire.Balance_SM_DAHL_HellFire', DAL, 1*addition_scale),
                # 9-Volt
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt.Balance_SM_DAHL_NineVolt', DAL, 1*addition_scale),
                # Redistributor
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork.Balance_SM_HYP_Fork', HYP, 1*addition_scale),
                # L0V3M4CH1N3
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3.Balance_SM_HYP_L0V3M4CH1N3', HYP, 1*addition_scale),
                # Predatory Lending
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending.Balance_SM_HYP_PredatoryLending', HYP, 1*addition_scale),
                # Cloud Kill
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill', MAL, 1*addition_scale),
                # Crit
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit', MAL, 1*addition_scale),
                # Vault Hero (VIP Reward gun, nothing special about it except for good stats)
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3.Balance_SM_MAL_E3', MAL, 0.7*addition_scale),
                # E-Gone
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon', MAL, 1*addition_scale),
                # The Emperor's Condiment
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer', MAL, 1*addition_scale),
                # Kevin's Chilly (mission item, and pretty unremarkable)
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins.Balance_SM_MAL_Kevins', MAL, 0.2*addition_scale),
                # Tsunami
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami', MAL, 1*addition_scale),
                # Miss Moxxi's Vibra-Pulse
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse', MAL, 1*addition_scale),
                # Westergun
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun', MAL, 1*addition_scale),
                # The Boo
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans.Balance_SM_TED_Beans', TED, 1*addition_scale),
                # Smart-Gun
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind.Balance_SM_TED_SpiderMind', TED, 1*addition_scale),
                ])),
        (SR, [
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Common', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Uncommon', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Rare', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_VeryRare', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_ETech_Rare', False, [DAL, HYP, MAL, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_ETech_VeryRare', False, [DAL, HYP, MAL, VLA]),
            ],
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary', [
                ### Original pool

                # Malak's Bane
                ('/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane.Balance_SR_DAL_ETech_MalaksBane', DAL, 1),
                # Woodblocker
                ('/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks.Balance_SR_HYP_Woodblocks', HYP, 1),
                # Monocle
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle.Balance_SR_JAK_Monocle', JAK, 1),
                # The Hunt(ed)
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted.Balance_SR_JAK_Hunted', JAK, 1),
                # ASMD
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD', MAL, 1),
                # Krakatoa
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa', MAL, 1),
                # Storm / Firestorm
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm', MAL, 1),
                # Lyuda
                ('/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda.Balance_VLA_SR_Lyuda', VLA, 1),

                ### Bloody Harvest Additions

                # Stalker
                ('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt', DAL, 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Tankman's Shield
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman', HYP, 1),

                ### DLC1 (Moxxi's Heist)

                # AutoAimè
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime.Balance_SR_DAL_AutoAime', DAL, 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Cocky Bastard
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard', JAK, 1),
                # Skullmasher
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher', JAK, 1),
                # Unseen Threat
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat', JAK, 1),

                ### Broken Hearts Additions

                # Wedding Invitation
                ('/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite.Balance_SR_JAK_WeddingInvite', JAK, 1),

                ### Mayhem 2.0

                # Sand Hawk
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk', DAL, 1),

                ### Additions

                # Brashi's Dedication
                ('/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication.Balance_SR_DAL_BrashisDedication', DAL, 1*addition_scale),
                # Kenulox
                ('/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer.Balance_SR_DAL_WorldDestroyer', DAL, 1*addition_scale),
                # Masterwork Crossbow
                ('/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork.Balance_SR_HYP_Masterwork', HYP, 1*addition_scale),
                # THE TWO TIME
                ('/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime.Balance_SR_HYP_TwoTime', HYP, 1*addition_scale),
                # Headsplosion
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion.Balance_SR_JAK_Headsplosion', JAK, 1*addition_scale),
                # The Ice Queen
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen.Balance_SR_JAK_IceQueen', JAK, 1*addition_scale),
                # The Hunt(er)
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter.Balance_SR_JAK_Hunter', JAK, 1*addition_scale),
                # The Hunt(ress)
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress.Balance_SR_JAK_Huntress', JAK, 1*addition_scale),
                # Soleki Protocol
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki', MAL, 1*addition_scale),
                # Cold Shoulder
                ('/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison.Balance_VLA_SR_Prison', VLA, 1*addition_scale),
                # Null Pointer
                ('/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer.Balance_SR_HYP_ZeroForPlayer', HYP, 1*addition_scale),
                ])),
        ]

# Make a struct to let us know easily which manufacturers make which types
type_to_manufacturer = {}
leg_to_manufacturer = {}
for (guntype, pools, (leg_pool, leg_balances)) in type_pools:
    type_to_manufacturer[guntype] = set()
    for (pool, must_exist, manufacturers) in pools:
        for manufacturer in manufacturers:
            type_to_manufacturer[guntype].add(manufacturer)
    leg_to_manufacturer[leg_pool] = set()
    for (balance, man, scale) in leg_balances:
        leg_to_manufacturer[leg_pool].add(man)

# Now loop through and make a mod for each manufacturer
for (man, man_label) in eng_manufacturers.items():

    man_file_label = man_label.lower()
    man_filename = 'manufacturer_lock_{}.txt'.format(man_file_label)

    mod = Mod(man_filename,
            'Manufacturer Lock: {}'.format(man_label),
            'Apocalyptech',
            [
                "Restricts drops for (mostly) all global (world-drop) weapon pools so that",
                "*only* {} weapons will drop from that pool, including the relevant world".format(man_label),
                "drop legendary pools.  This will *not* touch any pools in which that",
                "manufacturer doesn't show up.  There are various corner cases where you'll",
                "still see non-{} spawns, in situations where a drop pool is tightly".format(man_label),
                "restricted to a particular manufacturer.  Boss/Miniboss/Rare_Spawn drops",
                "have also not been touched.",
                "",
                "Note that this *only* touches weapon type pools which {} actually".format(man_label),
                "produces.  For other weapon types, you'll still see the full range of",
                "available manufacturers.",
                "",
                "To generate combinations of manufacturers, run the generation script with",
                "three-letter manufacturer codes as the arguments.  See sourcecode for",
                "details",
            ],
            lic=Mod.CC_BY_SA_40,
            )

    for (guntype, pools, (leg_pool, leg_balances)) in type_pools:
        if man in type_to_manufacturer[guntype]:
            mod.comment(eng_types[guntype])
            for (pool, must_exist, pool_manufacturers) in pools:
                if must_exist and man not in set(pool_manufacturers):
                    continue
                for idx, pool_man in enumerate(pool_manufacturers):
                    if pool_man == man:
                        weight = 1
                    else:
                        weight = 0
                    mod.reg_hotfix(Mod.PATCH, '',
                            pool,
                            'BalancedItems.BalancedItems[{}].Weight.BaseValueConstant'.format(idx),
                            weight)
            mod.newline()

        if man in leg_to_manufacturer[leg_pool]:
            balances = []
            for (balance, bal_man, scale) in leg_balances:
                if bal_man == man:
                    balances.append((balance, scale))
            mod.comment('{} Legendaries'.format(eng_types[guntype][:-1]))
            set_pool(mod, leg_pool, balances)
            mod.newline()

    mod.close()

# If we've had some manufacturers specified, do a "combined" mod as well
if len(custom_to_lock) >  0:

    man_filename = 'manufacturer_lock_custom_{}.txt'.format('_'.join(sorted(processed_args)))

    mod = Mod(man_filename,
            'Custom Manufacturer Lock: {}'.format(', '.join(sorted(eng_args))),
            'Apocalyptech',
            [
                "Restricts drops for (mostly) all global (world-drop) weapon pools so that",
                "*only* weapons from the following manufacturers will drop from that pool,",
                "including the relevant world drop legendary pools:",
                "",
                "    {}".format(', '.join(sorted(eng_args))),
                "",
                "This will *not* touch any pools in which these manufacturers dont't show up.",
                "There are various corner cases where you'll still see other manufacturers'",
                "weapons spawn, in situations where a drop pool is tightly restricted to a",
                "particular manufacturer.  Boss/Miniboss/Rare_Spawn drops have also not been",
                "touched.",
                "",
                "Note that this *only* touches weapon type pools which these manufacturers",
                "actually belong to.  For other weapon types, you'll still see the full range",
                "of available manufacturers.",
            ],
            lic=Mod.CC_BY_SA_40,
            )

    for (guntype, pools, (leg_pool, leg_balances)) in type_pools:
        if any([man in type_to_manufacturer[guntype] for man in custom_to_lock]):
            mod.comment(eng_types[guntype])
            for (pool, must_exist, pool_manufacturers) in pools:
                pool_manufacturers_set = set(pool_manufacturers)
                if must_exist and not any([man in pool_manufacturers_set for man in custom_to_lock]):
                    continue
                for idx, pool_man in enumerate(pool_manufacturers):
                    if pool_man in custom_to_lock:
                        weight = 1
                    else:
                        weight = 0
                    mod.reg_hotfix(Mod.PATCH, '',
                            pool,
                            'BalancedItems.BalancedItems[{}].Weight.BaseValueConstant'.format(idx),
                            weight)
            mod.newline()

        if any([man in leg_to_manufacturer[leg_pool] for man in custom_to_lock]):
            balances = []
            for (balance, bal_man, scale) in leg_balances:
                if bal_man in custom_to_lock:
                    balances.append((balance, scale))
            mod.comment('{} Legendaries'.format(eng_types[guntype][:-1]))
            set_pool(mod, leg_pool, balances)
            mod.newline()

    mod.close()
