#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2022 Christopher J. Kucera
# <cj@apocalyptech.com>
# <https://apocalyptech.com/contact.php>
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
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVCF, DataTableValue

###
### A lot of this mod is duplicated in gen_manufacturer_lock.py now.
### Be sure to update both when gear changes!
###

def get_full_object(obj_name):
    if obj_name is None:
        return None
    endpart = obj_name.rsplit('/', 1)[-1]
    if '.' in endpart:
        return obj_name
    else:
        return '{}.{}'.format(obj_name, endpart)

def set_pool(mod, pool_to_set, balances):

    parts = []
    for (bal, weight) in balances:
        full_bal = get_full_object(bal)
        part = '(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData\'"{}"\',Weight=(BaseValueConstant={}))'.format(
                full_bal, full_bal,
                round(weight, 6),
                )
        parts.append(part)
    mod.reg_hotfix(Mod.PATCH, '',
            pool_to_set,
            'BalancedItems',
            '({})'.format(','.join(parts)))

mod = Mod('expanded_legendary_pools.bl3hotfix',
        'Expanded Legendary Pools',
        'Apocalyptech',
        [
            'Adds all uniques and stuff (minus a few exceptions) into the legendary drop pools,',
            'at a reduced rate compared to the legendaries already in there.',
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.6.1',
        cats='loot-system, enemy-drops',
        )

# Items Omitted:
#
# Portals and Shite - /Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Balance/Balance_ATL_AR_Portals.Balance_ATL_AR_Portals
#   Unremarkable, shares red text with Boring Gun, is almost certainly totally unimplemented
#
# Eridian Fabricator - /Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Balance/Balance_Eridian_Fabricator.Balance_Eridian_Fabricator
#   No need
#
# Fixed-part Baby Maker - /Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Salvage/Balance_PS_Tediore_BabyMaker_Salvage.Balance_PS_Tediore_BabyMaker_Salvage
#   Reward for Claptrap salvages, perhaps?  Anyway, no need since the actual non-partlocked Baby Maker is already in there
#
# Mission version of Love Drill - /Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill
#   Legendary version's better, would be a bit silly to have both.
#
# Email-reward version of Short Stick - /Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick
#   The MinGameStage and MaxGameStage for this are both set to 57, so it will refuse to spawn unless
#   the game's exactly there.  You can add it to pools, etc, but if you're not exactly 57 it just won't
#   spawn.  Easy enough to fix, but you might as well just use the legendary version anyway.
#
# Seventh Sense guns.  There's four total variants, and we're only adding one of them.  The others:
#   This one is referenced by a mission, presumably only available during that
#   '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense_MissionWeapon',
#
#   This one is referenced by an enemy; I suspect it might be enemy-use-only
#   '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SS_L',
#
#   This one doesn't seem to really be referenced by anything at all (or rather, it's in a pool, but
#   the pool isn't referenced by anything)
#   '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SeventhSense',
#
# The Shoddy - /Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs
#   Literally does no damage, just a "joke" gun for a DLC3 mission.
#
# Marshal - /Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Sheriff/Balance/Balance_PS_JAK_Sheriff
#   It's just a green Jakobs pistol.  I haven't gone through DLC3 yet, but I assume that it's just
#   mission-related, or maybe an enemy-use gun.  Or something that's just Not Finished.
#
# Purple-rarity versions of all the DLC4 legendaries.  They have either the exact same effects (or worse),
# and worse weapon stats, so despite the unique name and red text, they're just not worth having.
#    Guilty Spark - /Game/PatchDLC/Alisma/Gear/Shields/_Uniques/FaultyStar/Balance/InvBalD_Shield_Legendary_FaultyStar_Epic
#    Limit Break - /Game/PatchDLC/Alisma/Gear/Shields/_Uniques/PlusUltra/Balance/InvBalD_Shield_Legendary_PlusUltra_Epic
#    Ashen Beast - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast_Epic
#    Minor Kong - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher_Epic
#    Blind Bandit - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit_Epic
#    Reunion - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence_Epic
#    Likable Rascal - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue_Epic
#    P.A.T. Mk. I - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3_Parent
#    P.A.T. Mk. II - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3_Epic
#    Sawpenny - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse_Epic
#    Septimator - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator_Epic
#    Critical Mass - /Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice_Epic
#
# Unfinished Operative COM from DLC5 (Designer's Cut).  At least says that it's got a unique ability,
# but shares its red text with the other DLC5 Operative COM and doesn't have a title (so all you get
# on the card is prefixes) -- had not tested to see if it actually does what it says it does.
#     /Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/InvBalD_CM_Ixora_OPE_L02
#
# Mysterious Amulet from DLC5 -- no actual drop source, I'm not sure if it actually has an effect
# on anything, and it appears to be a *legit* drop from DLC6, though as "Mysterious Artifact" instead.
# They're visually identical, so we're not gonna bother having this one in here.
#    '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet'
#
# There's a `_FixedParts` variant for all Vault Card items, which I think is just the version that's shown when
# you inspect it on the card.  Not bothering with those.

addition_scale = 0.6
pools = [
        ('ARs', 0, '/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary.ItemPool_AssaultRifles_Legendary',
            [
                ### Original Pool

                # Carrier
                ('/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier.Balance_ATL_AR_Carrier', 1),
                # Rebel Yell
                ('/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell.Balance_ATL_AR_RebelYell', 1),
                # Pain is Power / Embrace the Pain
                ('/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR', 2),
                # Sawbar
                ('/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar.Balance_AR_COV_Sawbar', 1),
                # Barrage
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage.Balance_DAL_AR_Barrage', 1),
                # Breath of the Dying
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD.Balance_DAL_AR_BOTD', 1),
                # Kaos
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos.Balance_DAL_AR_Kaos', 1),
                # Star Helix
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix.Balance_DAL_AR_StarHelix', 1),
                # Warlord
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord.Balance_DAL_AR_Warlord', 1),
                # Gatling Gun
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun.Balance_AR_JAK_04_GatlingGun', 1),
                # Lead Sprinkler
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler.Balance_AR_JAK_LeadSprinkler', 1),
                # Rowan's Call
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall.Balance_AR_JAK_RowansCall', 1),
                # Alchemist
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist.Balance_AR_TOR_Alchemist', 1),
                # Bearcat
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat.Balance_AR_TOR_Bearcat', 1),
                # Laser-Sploder
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder.Balance_AR_TOR_LaserSploder', 1),
                # Try-Bolt
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt.Balance_AR_TOR_TryBolt', 1),
                # Damned
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn', 1),
                # The Dictator
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator.Balance_AR_VLA_Dictator', 1),
                # Faisor
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor.Balance_AR_VLA_Faisor', 1),
                # Lucian's Call
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall.Balance_AR_VLA_LuciansCall', 1),
                # Ogre
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre.Balance_AR_VLA_Ogre', 1),
                # Super Shredifier
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier.Balance_AR_VLA_Sherdifier', 1),
                # Boom Sickle / Sickle
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle', 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Good Juju
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju', 1),
                # Juliet's Dazzle
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop', 1),
                # Zheitsev's Eruption
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev', 1),

                ### DLC1 (Moxxi's Heist)

                # Digby's Smooth Tube
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby.Balance_DAL_AR_Digby', 1*addition_scale),
                # Brad Luck
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash.Balance_AR_COV_Trash', 1*addition_scale),
                # La Varlope
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope.Balance_AR_TOR_Varlope', 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Clairvoyance
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance', 1),
                # Seeryul Killur
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal', 1),
                # Mutant
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant', 1),
                # Soulrender
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender', 1),
                # Stauros' Burn
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom', 1),

                ### Revenge of the Cartels

                # NoPewPew
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew', 1),
                # O.P.Q. System
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ', 1),

                ### Mayhem 2.0

                # The Monarch
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch', 1),

                ### Guardian Takedown

                # Web Slinger
                ('/Game/PatchDLC/Takedown2/Gear/Weapons/WebSlinger/Balance/Balance_AR_VLA_WebSlinger', 1),

                ### DLC3 (Bounty of Blood)

                # The Beast (rad)
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Rad', 1*addition_scale/2),
                # The Beast (shock)
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Shock', 1*addition_scale/2),
                # Contained Blast
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ContainedExplosion/Balance/Balance_AR_TOR_Contained', 1),
                # Icebreaker
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/CoolBeans/Balance/Balance_AR_JAK_CoolBeans', 1*addition_scale),
                # Dowsing Rod
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/DowsingRod/Balance/Balance_AR_VLA_Dowsing', 1),
                # The Chalice
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/McSmugger/Balance/Balance_AR_JAK_McSmugger', 1*addition_scale),
                # Stonethrower
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/StoneThrow/Balance/Balance_AR_JAK_Stonethrow', 1),

                ### DLC4 (Psycho Krieg)

                # Lovable Rogue
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue', 1),
                # Rebound
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse', 1),

                ### DLC5 (Designer's Cut)

                # Hotfoot Teddy
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/HotfootTeddy/Balance/Balance_AR_TOR_Hotfoot', 1),

                ### Vault Card 3

                # Blade Fury
                ('/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/BladeFury/Balance/Balance_AR_JAK_BladeFury', 1),

                # Creeping Corruption
                ('/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/Corruption/Balance/Balance_DAL_AR_Corruption', 1),

                ### Additions

                # Earworm
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm', 1*addition_scale),
                # Hail
                ('/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail.Balance_DAL_AR_Hail', 1*addition_scale),
                # Bekah
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah.Balance_AR_JAK_Bekah', 1*addition_scale),
                # Hand of Glory
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory.Balance_AR_JAK_HandOfGlory', 1*addition_scale),
                # Pa's Rifle
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle.Balance_AR_JAK_PasRifle', 1*addition_scale),
                # Traitor's Death
                ('/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath.Balance_AR_JAK_TraitorsDeath', 1*addition_scale),
                # Amber Management
                ('/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement.Balance_AR_TOR_AmberManagement', 1*addition_scale),
                # The Big Succ - ordinarily a mission item, pretty lame, but we'll add it in at a lower probability anyway
                ('/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc.Balance_AR_VLA_BigSucc', 0.2*addition_scale),
                ]),

        ('Heavy Weapons', 1, '/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary.ItemPool_Heavy_Legendary',
            [
                ### Original pool

                # Ruby's Wrath
                ('/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath.Balance_HW_ATL_RubysWrath', 1),
                # Scourge
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm.Balance_HW_TOR_Swarm', 1),
                # Tunguska
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska.Balance_HW_TOR_Tunguska', 1),
                # Jericho
                ('/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst.Balance_HW_VLA_CloudBurst', 1),

                ### DLC1 (Moxxi's Heist)

                # Creamer
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer.Balance_HW_TOR_Creamer', 1),
                # ION CANNON
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon.Balance_HW_VLA_IonCannon', 1),
                # Nukem
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem.Balance_HW_TOR_Nukem', 1),

                ### Revenge of the Cartels

                # Yellowcake
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake', 1),

                ### Mayhem 2.0

                # Backburner
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner', 1),
                # Plaguebearer
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague', 1),

                ### Guardian Takedown

                # Globetrottr
                ('/Game/PatchDLC/Takedown2/Gear/Weapons/Globetrotter/Balance/Balance_HW_COV_Globetrotter', 1),

                ### DLC3 (Bounty of Blood)

                # Plumage
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Plumage/Balance/Balance_HW_ATL_Plumage', 1),
                # Satisfaction
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Satisfaction/Balance/Balance_HW_TOR_Satisfaction', 1),

                ### DLC4 (Psycho Krieg)

                # Major Kong
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher', 1),

                ### DLC5 (Designer's Cut)

                # Ice Age
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/IceAge/Balance/Balance_HW_TOR_IceAge', 1),

                ### DLC6 (Director's Cut) + associated

                # Redeye Rocket Pod
                ('/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Redeye/Balance/Balance_HW_VLA_Redeye', 1),
                # Mechanic
                ('/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/Mechanic/Balance/Balance_HW_COV_Mechanic', 1),
                # Kickcharger
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Kickcharger/Balance/Balance_HW_VLA_ETech_Kickcharger', 1),

                ### Additions

                # Freeman
                ('/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman.Balance_HW_ATL_Freeman', 1*addition_scale),
                # Hot Drop
                ('/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop.Balance_HW_COV_HotDrop', 1*addition_scale),
                # Porta-Pooper 5000
                ('/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper.Balance_HW_COV_PortaPooper', 1*addition_scale),
                # Agonizer 1500
                ('/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror', 1*addition_scale),
                # Gettleburger
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon.Balance_HW_TOR_BurgerCannon', 1*addition_scale),
                # Hive
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive.Balance_HW_TOR_Hive', 1*addition_scale),
                # Quadomizer
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager.Balance_HW_TOR_Rampager', 1*addition_scale),
                # R.Y.N.A.H.
                ('/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO.Balance_HW_TOR_RYNO', 1*addition_scale),
                # Mongol
                ('/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol', 1*addition_scale),
                ]),

        ('Pistols', 3, '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary.ItemPool_Pistols_Legendary',
            [
                ### Original pool

                # Linoge
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion.Balance_PS_COV_Legion', 1),
                # AAA
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA.Balance_DAL_PS_AAA', 1),
                # Hornet
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet.Balance_DAL_PS_Hornet', 1),
                # Nemesis
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis.Balance_DAL_PS_Nemesis', 1),
                # The Flood
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc', 1),
                # Maggie
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie', 1),
                # The Companion
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion.Balance_PS_JAK_MelsCompanion', 1),
                # The Duc
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc.Balance_PS_JAK_TheDuc', 1),
                # Unforgiven
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven.Balance_PS_JAK_Unforgiven', 1),
                # Wagon Wheel
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel.Balance_PS_JAK_WagonWheel', 1),
                # Hellshock
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock', 1),
                # Superball
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber', 1),
                # Thunderball Fists
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists', 1),
                # Bangarang
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang.Balance_PS_TED_Bangerang', 1),
                # Baby Maker ++
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker.Balance_PS_Tediore_BabyMaker', 1),
                # Gunerang
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang.Balance_PS_TED_Gunerang', 1),
                # Devastator
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator', 1),
                # Echo / Breeder
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo.Balance_PS_TOR_Echo', 2),
                # Devils Foursum
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM.Balance_PS_TOR_4SUM', 1),
                # Roisen's Thorns
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns.Balance_PS_TOR_RoisensThorns', 1),
                # Infinity
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti.Balance_PS_VLA_Infiniti', 1),
                # Magnificent
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent', 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Moonfire
                ('/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon', 1),
                # S3RV-80S-EXECUTE
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute', 1),

                ### DLC1 (Moxxi's Heist)

                # Craps
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps.Balance_PS_TOR_Craps', 1),
                # Lucky 7
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7', 1),
                # Robo-Melter
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher.Balance_PS_JAK_RoboMasher', 1*addition_scale),
                # Scoville
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville.Balance_PS_TOR_Scoville', 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Bite Size - Basically just a WIP that started with the Duc; don't drop it much.  The initial nova looks
                # nice but it's entirely for show
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize', 0.2*addition_scale),
                # Frozen Devil
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil', 1),
                # Hydrafrost
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost', 1),
                # Kaleidoscope
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope', 1*addition_scale),
                # Little Yeeti
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti', 1),
                # Love Drill (legendary version)
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary', 1),
                # Seventh Sense (legendary version)
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense', 1),

                ### Revenge of the Cartels

                # Grease Trap
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap', 1),
                # Ice Pick - nothing special about it, just a regular Maliwan pistol
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IcePick/Balance/Balance_PS_MAL_IcePick', 0.2*addition_scale),

                ### Mayhem 2.0

                # Multi-tap
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap', 1),

                ### DLC3 (Bounty of Blood)

                # Bubble Blaster
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Balance/Balance_PS_MAL_BubbleBlaster', 1*addition_scale),
                # Beacon
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Balance/Balance_PS_MAL_Decoupler', 1),
                # Gargoyle
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Gargoyle/Balance/Balance_PS_COV_Gargoyle', 1),
                # Light Show
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Lasocannon/Balance/Balance_PS_VLA_Lasocannon', 1),
                # Miscreant
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Miscreant/Balance/Balance_PS_VLA_Miscreant', 1),
                # Peashooter
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Peashooter/Balance/Balance_PS_JAK_Peashooter', 1*addition_scale),
                # The Blanc
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/PrivateInvestigator/Balance/Balance_DAL_PS_PrivateInvestigator', 1),
                # Quickdraw
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/QuickDraw/Balance/Balance_PS_JAK_QuickDraw', 1*addition_scale),
                # Bloom
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Rose/Balance/Balance_PS_JAK_Rose', 1),
                # Unkempt Harold
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/Balance/Balance_PS_TOR_UnkemptHarold', 1),

                ### DLC4 (Psycho Krieg)

                # Prompt Critical
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice', 1),

                ### DLC5 (Designer's Cut)

                # Firefly
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Firefly/Balance/Balance_PS_VLA_Firefly', 1),
                # Res
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/SpiritOfMaya/Balance/Balance_PS_ATL_SpiritOfMaya', 1),
                # Fasterfied Tizzy
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy', 1),
                # Snide Trickshot
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Trickshot/Balance/Balance_PS_JAK_Trickshot', 1),

                ### DLC6 (Director's Cut) + associated

                # Free Radical
                ('/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Deatomizer/Balance/Balance_PS_MAL_Deatomizer', 1),
                # Atlas Replay
                ('/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Replay/Balance/Balance_PS_ATL_Replay', 1),

                ### Vault Card 3

                # TNTina
                ('/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/TinyTinaGun/Balance/Balance_PS_TOR_TinyTinaGun', 1),

                ### Additions

                # Linc
                ('/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill.Balance_PS_ATL_Drill', 1*addition_scale),
                # Peacemonger
                ('/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger.Balance_PS_ATL_Warmonger', 1*addition_scale),
                # Extreme Hangin' Chadd
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad.Balance_PS_COV_Chad', 1*addition_scale),
                # Pestilence
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion', 1*addition_scale),
                # The Killing Word
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece.Balance_PS_COV_Mouthpiece', 1*addition_scale),
                # Psycho Stabber
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber.Balance_PS_COV_PsychoStabber', 1*addition_scale),
                # SkekSil
                ('/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis.Balance_PS_COV_Skeksis', 1*addition_scale),
                # Omniloader
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader.Balance_DAL_PS_Omniloader', 1*addition_scale),
                # Night Flyer
                ('/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman.Balance_DAL_PS_Rakkman', 1*addition_scale),
                # Amazing Grace
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace.Balance_PS_JAK_AmazingGrace', 1*addition_scale),
                # Buttplug
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug.Balance_PS_JAK_Buttplug', 1*addition_scale),
                # King's Call / Queen's Call
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother.Balance_PS_JAK_GodMother', 1.2*addition_scale),
                # Dead Chamber
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent.Balance_PS_JAK_Malevolent', 1*addition_scale),
                # Rogue-Sight (mission item, but somewhat unique thanks to the homing bullets)
                ('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver.Balance_PS_JAK_SpyRevolver', 1*addition_scale),
                # Hyper-Hydrator
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator', 1*addition_scale),
                # Starkiller
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller', 1*addition_scale),
                # Sellout
                ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch', 1*addition_scale),
                # Scorpio
                ('/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre', 1*addition_scale),
                # Heckle - quite uninteresting, has no unique effects.  Bump its weight down even more than the others.
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle', 0.5*addition_scale),
                # Hyde - quite uninteresting, has no unique effects.  Bump its weight down even more than the others.
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde', 0.5*addition_scale),
                # Girth Blaster Elite (joke weapon)
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf.Balance_PS_TOR_Nurf', 0.2*addition_scale),
                # Occultist
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy.Balance_PS_TOR_Troy', 1*addition_scale),
                # Bone Shredder
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder.Balance_PS_VLA_BoneShredder', 1*addition_scale),
                # The Leech
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech.Balance_PS_VLA_TheLeech', 1*addition_scale),
                ]),

        ('Shotguns', 4, '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary.ItemPool_Shotguns_Legendary',
            [
                ### Original pool

                # Face-puncher
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick.Balance_SG_HYP_Brick', 1),
                # Conference Call
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall.Balance_SG_HYP_ConferenceCall', 1),
                # Brainstormer
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor.Balance_SG_HYP_Redistributor', 1),
                # The Butcher
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher.Balance_SG_HYP_TheButcher', 1),
                # Hellwalker
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker.Balance_SG_JAK_Hellwalker', 1),
                # T.K.'s Wave / T.K's Heatwave / T.K's Shockwave / The Tidal Wave
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave.Balance_SG_JAK_Unique_Wave', 1),
                # Projectile Recursion
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion', 1),
                # Trevonator
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev', 1),
                # Kill-o'-the-Wisp
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp', 1),
                # Polybius
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius.Balance_SG_TED_Polybius', 1),
                # Flakker
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker.Balance_SG_Torgue_Flakker', 1),
                # The Boring Gun
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring.Balance_SG_TOR_Boring', 1),
                # The Lob
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob', 1),

                ### Bloody Harvest Additions

                # Fearmonger
                ('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger.Balance_SG_HYP_ETech_Fearmonger', 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Tiggs' Boom
                ('/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom', 1),
                # Vosk's Deathgrip
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip', 1),

                ### DLC1 (Moxxi's Heist)

                # Heart Breaker
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker.Balance_SG_HYP_HeartBreaker', 1),
                # Melt Facer
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer.Balance_SG_HYP_MeltFacer', 1*addition_scale),
                # Slow Hand
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand.Balance_SG_HYP_SlowHand', 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Anarchy
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy', 1),
                # Firecracker
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker', 1*addition_scale),
                # Insider
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider', 1),
                # Flama Diddle
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen', 1),
                # Sacrificial Lamb
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb', 1*addition_scale),
                # Shocker
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker', 1),
                # The Cure
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure', 1*addition_scale),
                # Nothingness
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing', 1),

                ### Broken Hearts Additions

                # Superstreamer (just a somewhat partlocked purple Tediore shotgun, only thing special is the material.  no red text, even!)
                ('/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/TwitchPrime/Balance/Balance_SG_TED_Twitch.Balance_SG_TED_Twitch', 0.5*addition_scale),

                ### Revenge of the Cartels

                # Iceburger
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger', 1),

                ### Mayhem 2.0

                # Reflux
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux', 1),

                ### DLC3 (Bounty of Blood)

                # Chandelier
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Balance/Balance_SG_MAL_ETech_Antler', 1),
                # Brightside
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Brightside/Balance/Balance_SG_TED_Brightside', 1),
                # Dakota
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Dakota/Balance/Balance_SG_JAK_Dakota', 1*addition_scale),
                # Frequency
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Balance/Balance_SG_MAL_Frequency', 1),
                # Spade
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Shoveler/Balance/Balance_SG_Torgue_Shoveler', 1),
                # Robin's Call
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/SpeakEasy/Balance/Balance_SG_JAK_SpeakEasy', 1),
                # Splinter
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Splinter/Balance/Balance_SG_JAK_Splinter', 1*addition_scale),

                ### DLC4 (Psycho Krieg)

                # Blind Sage
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit', 1),
                # Convergence
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence', 1),

                ### DLC5 (Designer's Cut)

                # Critical Thug / Critical Thug x2
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/CriticalThug/Balance/Balance_SG_Torgue_CriticalThug', 1),

                ### DLC6 (Director's Cut) + associated

                # Guardian 4N631
                ('/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/Guardian/Balance/Balance_SG_HYP_Guardian', 1),

                ### Additions

                # Phebert
                ('/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert.Balance_SG_HYP_Phebert', 1*addition_scale),
                # Fingerbiter
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter.Balance_SG_JAK_Fingerbiter', 1*addition_scale),
                # The Garcia
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia.Balance_SG_JAK_Garcia', 1*addition_scale),
                # Nimble Jack
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble.Balance_SG_JAK_Nimble', 1*addition_scale),
                # One Pump Chump
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch.Balance_SG_JAK_OnePunch', 1*addition_scale),
                # Sledge's Shotgun / Sledge's Super Shotgun
                ('/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge.Balance_SG_JAK_LGD_Sledge', 1*addition_scale),
                # Mind-Killer
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2.Balance_SG_MAL_Mouthpiece2', 1*addition_scale),
                # Shrieking Devil
                ('/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek', 1*addition_scale),
                # Manic Pixie Dream Gun
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Balance/Balance_SG_TED_FriendZone.Balance_SG_TED_FriendZone', 1*addition_scale),
                # The Horizon
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon.Balance_SG_TED_Horizon', 1*addition_scale),
                # Creeping Death
                ('/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge', 1*addition_scale),
                # Chomper
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog.Balance_SG_Torgue_Balrog', 1*addition_scale),
                # Black Flame (mission item, somewhat unremarkable)
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha.Balance_SG_TOR_Brewha', 0.5*addition_scale),
                # Redline
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine.Balance_SG_Torgue_RedLine', 1*addition_scale),
                # Thumper
                ('/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper.Balance_SG_Torgue_Thumper', 1*addition_scale),
                ]),

        ('SMGs', 5, '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary.ItemPool_SMGs_Legendary',
            [
                ### Original pool

                # Night Hawkin
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag.Balance_SM_DAL_Demoskag', 1),
                # Ripper
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper.Balance_SM_DAL_Ripper', 1),
                # Sleeping Giant
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant.Balance_SM_DAL_SleepingGiant', 1),
                # Vanquisher
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher.Balance_SM_DAHL_Vanquisher', 1),
                # Bitch
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch.Balance_SM_HYP_Bitch', 1),
                # Crossroad
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad.Balance_SM_HYP_Crossroad', 1),
                # Handsome Jackhammer
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome.Balance_SM_HYP_Handsome', 1),
                # XZ41
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ.Balance_SM_HYP_XZ', 1),
                # Cutsman
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman', 1),
                # Destructo Spinner
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin', 1),
                # Devoted
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted', 1),
                # Long Musket
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower.Balance_SM_TED_NotAFlamethrower', 1),
                # Ten Gallon
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon.Balance_SM_TED_TenGallon', 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Redistributor (legendary rarity)
                ('/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2', 1),
                # Kyb's Worth
                ('/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth', 1),
                # P2P Networker
                ('/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link', 1),
                # Crader's EM-P5
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5', 1),

                ### DLC1 (Moxxi's Heist)

                # Boomer
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer.Balance_SM_DAL_Boomer', 1),
                # Cheap Tips
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips.Balance_SM_HYP_CheapTips', 1),
                # Ember's Purge
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge.Balance_SM_MAL_EmbersPurge', 1),
                # ION LASER
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser.Balance_SM_MAL_IonLaser', 1),
                # Just Kaus
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic.Balance_SM_HYP_JustCaustic', 1*addition_scale),

                ### DLC2 (Guns, Love, and Tentacles)

                # Oldridian
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian', 1),
                # SF Force
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce', 1),
                # Short Stick
                ('/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick_Legendary', 1),

                ### Broken Hearts additions

                # Terminal Polyaimorous
                ('/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim.Balance_SM_MAL_PolyAim', 1),

                ### Revenge of the Cartels

                # Needle Gun
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun', 1),
                # Pricker
                ('/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker', 1*addition_scale),

                ### Mayhem 2.0

                # D.N.A.
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA', 1),
                # Kaoson
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson', 1),

                ### Guardian Takedown

                # Smog
                ('/Game/PatchDLC/Takedown2/Gear/Weapons/Smog/Balance/Balance_SM_HYP_Smog', 1),

                ### DLC3 (Bounty of Blood)

                # Proprietary License
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Copybeast/Balance/Balance_SM_HYP_Copybeast', 1),
                # Mother Too
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Earthbound/Balance/Balance_SM_TED_Earthbound', 1),
                # Flipper
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper', 1),

                ### DLC4 (Psycho Krieg)

                # Blood-Starved Beast
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast', 1),
                # P.A.T. Mk. III
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3', 1),

                ### DLC5 (Designer's Cut)

                # Dark Army +
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/DarkArmy/Balance/Balance_SM_TED_DarkArmy', 1),
                # Superconducting Plasma Coil
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/PlasmaCoil/Balance/Balance_SM_MAL_PlasmaCoil', 1),

                ### DLC6 (Director's Cut) + associated

                # Torrent
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Torrent/Balance/Balance_SM_DAL_Torrent', 1),

                ### Vault Card 2

                # Gold Rush
                ('/Game/PatchDLC/VaultCard2/Gear/Weapons/Unique/GoldRush/Balance/Balance_SM_HYP_GoldRush', 1),

                # Troubleshooter
                ('/Game/PatchDLC/VaultCard2/Gear/Weapons/Unique/Troubleshooter/Balance/Balance_SM_HYP_ETech_Troubleshooter', 1),

                ### Additions

                # Hellfire
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire.Balance_SM_DAHL_HellFire', 1*addition_scale),
                # 9-Volt
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt.Balance_SM_DAHL_NineVolt', 1*addition_scale),
                # Redistributor (blue rarity, mission reward) - the Legendary version is better in just about every way
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork.Balance_SM_HYP_Fork', 0.2*addition_scale),
                # L0V3M4CH1N3
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3.Balance_SM_HYP_L0V3M4CH1N3', 1*addition_scale),
                # Predatory Lending
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending.Balance_SM_HYP_PredatoryLending', 1*addition_scale),
                # Cloud Kill
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill', 1*addition_scale),
                # Crit
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit', 1*addition_scale),
                # Vault Hero (VIP Reward gun, nothing special about it except for good stats)
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3.Balance_SM_MAL_E3', 0.7*addition_scale),
                # E-Gone
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon', 1*addition_scale),
                # The Emperor's Condiment
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer', 1*addition_scale),
                # Kevin's Chilly (mission item, and pretty unremarkable)
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins.Balance_SM_MAL_Kevins', 0.2*addition_scale),
                # Tsunami
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami', 1*addition_scale),
                # Miss Moxxi's Vibra-Pulse
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse', 1*addition_scale),
                # Westergun
                ('/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun', 1*addition_scale),
                # The Boo
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans.Balance_SM_TED_Beans', 1*addition_scale),
                # Smart-Gun
                ('/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind.Balance_SM_TED_SpiderMind', 1*addition_scale),
                ]),

        ('Snipers', 2, '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary',
            [
                ### Original pool

                # Malak's Bane
                ('/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane.Balance_SR_DAL_ETech_MalaksBane', 1),
                # Woodblocker
                ('/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks.Balance_SR_HYP_Woodblocks', 1),
                # Monocle
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle.Balance_SR_JAK_Monocle', 1),
                # The Hunt(ed)
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted.Balance_SR_JAK_Hunted', 1),
                # ASMD
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD', 1),
                # Krakatoa
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa', 1),
                # Storm / Firestorm
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm', 1),
                # Lyuda
                ('/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda.Balance_VLA_SR_Lyuda', 1),

                ### Bloody Harvest Additions

                # Stalker
                ('/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt', 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Tankman's Shield
                ('/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman', 1),

                ### DLC1 (Moxxi's Heist)

                # AutoAimè
                ('/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime.Balance_SR_DAL_AutoAime', 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Cocky Bastard
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard', 1),
                # Skullmasher
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher', 1),
                # Unseen Threat
                ('/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat', 1),

                ### Broken Hearts Additions

                # Wedding Invitation
                ('/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite.Balance_SR_JAK_WeddingInvite', 1),

                ### Mayhem 2.0

                # Sand Hawk
                ('/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk', 1),

                ### DLC3 (Bounty of Blood)

                # Complex Root
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber', 1),
                # Narp
                ('/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Narp/Balance/Balance_SR_HYP_Narp', 1),

                ### DLC4 (Psycho Krieg)

                # Septimator Prime
                ('/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator', 1),

                ### DLC5 (Designer's Cut)

                # Binary Operator
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/BinaryOperator/Balance/Balance_MAL_SR_BinaryOperator', 1),
                # Boogeyman
                ('/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Boogeyman/Balance/Balance_VLA_SR_Boogeyman', 1),

                ### DLC6 (Director's Cut) + associated

                # Ionic Disruptor
                ('/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Disruptor/Balance/Balance_SR_JAK_Disruptor', 1),
                # Bird of Prey
                ('/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/BirdofPrey/Balance/Balance_SR_JAK_BirdofPrey', 1),

                ### Additions

                # Brashi's Dedication
                ('/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication.Balance_SR_DAL_BrashisDedication', 1*addition_scale),
                # Kenulox
                ('/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer.Balance_SR_DAL_WorldDestroyer', 1*addition_scale),
                # Masterwork Crossbow
                ('/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork.Balance_SR_HYP_Masterwork', 1*addition_scale),
                # THE TWO TIME
                ('/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime.Balance_SR_HYP_TwoTime', 1*addition_scale),
                # Headsplosion
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion.Balance_SR_JAK_Headsplosion', 1*addition_scale),
                # The Ice Queen
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen.Balance_SR_JAK_IceQueen', 1*addition_scale),
                # The Hunt(er)
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter.Balance_SR_JAK_Hunter', 1*addition_scale),
                # The Hunt(ress)
                ('/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress.Balance_SR_JAK_Huntress', 1*addition_scale),
                # Soleki Protocol
                ('/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki', 1*addition_scale),
                # Cold Shoulder
                ('/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison.Balance_VLA_SR_Prison', 1*addition_scale),
                # Null Pointer
                ('/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer.Balance_SR_HYP_ZeroForPlayer', 1*addition_scale),
                ]),

        ('Shields', None, '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary.ItemPool_Shields_05_Legendary',
            [
                ### Original pool

                # Back Ham
                ('/Game/Gear/Shields/_Design/_Uniques/BackHam/Balance/InvBalD_Shield_BackHam.InvBalD_Shield_BackHam', 1),
                # Big Boom Blaster
                ('/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/Balance/InvBalD_Shield_LGD_BigBoomBlaster.InvBalD_Shield_LGD_BigBoomBlaster', 1),
                # Black Hole
                ('/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole.InvBalD_Shield_LGD_BlackHole', 1),
                # Front Loader
                ('/Game/Gear/Shields/_Design/_Uniques/FrontLoader/Balance/InvBalD_Shield_LGD_FrontLoader.InvBalD_Shield_LGD_FrontLoader', 1),
                # Impaler
                ('/Game/Gear/Shields/_Design/_Uniques/Impaler/Balance/InvBalD_Shield_LGD_Impaler.InvBalD_Shield_LGD_Impaler', 1),
                # Nova Berner
                ('/Game/Gear/Shields/_Design/_Uniques/NovaBurner/Balance/InvBalD_Shield_LGD_NovaBurner.InvBalD_Shield_LGD_NovaBurner', 1),
                # Re-Charger
                ('/Game/Gear/Shields/_Design/_Uniques/Re-Charger/Balance/InvBalD_Shield_LGD_ReCharger.InvBalD_Shield_LGD_ReCharger', 1),
                # Rectifier
                ('/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier.InvBalD_Shield_LGD_Rectifier', 1),
                # Revengenader
                ('/Game/Gear/Shields/_Design/_Uniques/Revengenader/Balance/InvBalD_Shield_LGD_Revengenader.InvBalD_Shield_LGD_Revengenader', 1),
                # Rough Rider
                ('/Game/Gear/Shields/_Design/_Uniques/RoughRider/Balance/InvBalD_Shield_LGD_RoughRider.InvBalD_Shield_LGD_RoughRider', 1),
                # Red Card
                ('/Game/Gear/Shields/_Design/_Uniques/SlideKick/Balance/InvBalD_Shield_LGD_SlideKick.InvBalD_Shield_LGD_SlideKick', 1),
                # Stop-Gap
                ('/Game/Gear/Shields/_Design/_Uniques/StopGap/Balance/InvBalD_Shield_LGD_StopGap.InvBalD_Shield_LGD_StopGap', 1),
                # The Transformer
                ('/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer.InvBalD_Shield_LGD_Transformer', 1),
                # Re-Router
                ('/Game/Gear/Shields/_Design/_Uniques/Vamp/Balance/InvBalD_Shield_Legendary_Vamp.InvBalD_Shield_Legendary_Vamp', 1),
                # Whiskey Tango Foxtrot
                ('/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot.InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot', 1),

                ### Bloody Harvest Additions

                # Scream of Terror
                ('/Game/PatchDLC/BloodyHarvest/Gear/Shields/_Design/_Unique/ScreamOfPain/Balance/InvBalD_Shield_ScreamOfTerror.InvBalD_Shield_ScreamOfTerror', 1),

                ### Maliwan Takedown / Mayhem 4 Legendaries

                # Version 0.m
                ('/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom', 1),
                # Re-Charger Berner
                ('/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner', 1),
                # Frozen Snowshoe
                ('/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart', 1),
                # Red Card Re-Charger
                ('/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger', 1),

                ### DLC1 (Moxxi's Heist)
                
                # All-in
                ('/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Balance/InvBalD_Shield_Clover.InvBalD_Shield_Clover', 1*addition_scale),
                # Double Downer
                ('/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner.InvBalD_Shield_DoubleDowner', 1*addition_scale),
                # Ember's Blaze
                ('/Game/PatchDLC/Dandelion/Gear/Shield/Ember/Balance/InvBalD_Shield_Ember.InvBalD_Shield_Ember', 1*addition_scale),
                # Rico
                ('/Game/PatchDLC/Dandelion/Gear/Shield/Rico/Balance/InvBalD_Shield_Rico.InvBalD_Shield_Rico', 1),

                ### DLC2 (Guns, Love, and Tentacles)

                # Initiative
                ('/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Initiative/Balance/InvBalD_Shield_Initiative', 1*addition_scale),
                # Old God
                ('/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod', 1),
                # Torch
                ('/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch', 1),
                # Void Rift
                ('/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/VoidRift/Balance/InvBalD_Shield_LGD_VoidRift', 1),

                ### Revenge of the Cartels

                # Firewall
                ('/Game/PatchDLC/Event2/Gear/Shield/_Unique/Firewall/Balance/InvBalD_Shield_Legendary_Firewall', 1),
                # M.E.A.T. Shield
                ('/Game/PatchDLC/Event2/Gear/Shield/_Unique/MEAT/Balance/InvBalD_Shield_Legendary_MEAT', 1),
                # Wattson
                ('/Game/PatchDLC/Event2/Gear/Shield/_Unique/Wattson/Balance/InvBalD_Shield_Legendary_Wattson', 1),

                ### Guardian Takedown

                # Asclepius
                ('/Game/PatchDLC/Takedown2/Gear/Shields/Aesclepius/Balance/InvBalD_Shield_LGD_Aesclepius', 1),
                # Stinger
                ('/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Balance/InvBalD_Shield_LGD_Stinger', 1),

                ### DLC4 (Psycho Krieg)

                # Faulty Star
                ('/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/FaultyStar/Balance/InvBalD_Shield_Legendary_FaultyStar', 1),
                # Plus Ultra
                ('/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/PlusUltra/Balance/InvBalD_Shield_Legendary_PlusUltra', 1),

                ### DLC5 (Designer's Cut)

                # Beskar
                ('/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Beskar/Balance/InvBalD_Shield_Beskar', 1),
                # Madcap
                ('/Game/PatchDLC/Ixora/Gear/Shields/_Unique/MadCap/Balance/InvBalD_Shield_LGD_Madcap', 1),
                # Gas Mask
                ('/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Ventilator/Balance/InvBalD_Shield_Ventilator', 1),

                ### DLC6 (Director's Cut) + associated

                # Re-Volter
                ('/Game/PatchDLC/Ixora2/Gear/Shields/_Unique/Re-Volter/Balance/InvBalD_Shield_Revolter', 1),
                # Super Soldier
                ('/Game/PatchDLC/VaultCard/Gear/Shields/Unique/SuperSoldier/Balance/InvBalD_Shield_SuperSoldier', 1),
                # Infernal Wish
                ('/Game/PatchDLC/Ixora/Gear/Shields/_Unique/InfernalWish/Balance/InvBalD_Shield_InfernalWish', 1),

                ### Vault Card 3

                # Mana Well
                ('/Game/PatchDLC/VaultCard3/Gear/Shields/Unique/Manawell/Balance/InvBalD_Shield_Pangolin_Manawell', 1),

                ### Additions

                # Frozen Heart
                ('/Game/Gear/Shields/_Design/_Uniques/Aurelia/Balance/InvBalD_Shield_LGD_Aurelia.InvBalD_Shield_LGD_Aurelia', 1*addition_scale),
                # Mendel's Multivitamin Shield
                ('/Game/Gear/Shields/_Design/_Uniques/BuriedAlive/Balance/InvBalD_Shield_BuriedAlive.InvBalD_Shield_BuriedAlive', 1*addition_scale),
                # Band of Sitorak
                ('/Game/Gear/Shields/_Design/_Uniques/Cyttorak/bALANCE/InvBalD_Shield_Cyttorak.InvBalD_Shield_Cyttorak', 1*addition_scale),
                # MSRC AUto-Dispensary
                ('/Game/Gear/Shields/_Design/_Uniques/Dispensary/Balance/InvBalD_Shield_LGD_Dispensary.InvBalD_Shield_LGD_Dispensary', 1*addition_scale),
                # Golden Touch
                ('/Game/Gear/Shields/_Design/_Uniques/GoldenTouch/Balance/InvBalD_Shield_GoldenTouch.InvBalD_Shield_GoldenTouch', 1*addition_scale),
                # Loop of 4N631
                ('/Game/Gear/Shields/_Design/_Uniques/LoopOf4N631/Balance/InvBalD_Shield_HYP_LoopOf4N631.InvBalD_Shield_HYP_LoopOf4N631', 1*addition_scale),
                # Messy Breakup
                ('/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup.InvBalD_Shield_MessyBreakup', 1*addition_scale),
                # Moxxi's Embrace
                ('/Game/Gear/Shields/_Design/_Uniques/MoxxisEmbrace/Balance/InvBalD_Shield_MoxxisEmbrace.InvBalD_Shield_MoxxisEmbrace', 1*addition_scale),
                # Mr Caffeine
                ('/Game/Gear/Shields/_Design/_Uniques/MrCaffeine/Balance/InvBalD_Shield_PAN_MrCaffeine.InvBalD_Shield_PAN_MrCaffeine', 1*addition_scale),
                # Red Suit
                ('/Game/Gear/Shields/_Design/_Uniques/Radiate/Balance/InvBalD_Shield_LGD_Radiate.InvBalD_Shield_LGD_Radiate', 1*addition_scale),
                # Shooting Star
                ('/Game/Gear/Shields/_Design/_Uniques/ShootingStar/Balance/InvBalD_Shield_LGD_ShootingStar.InvBalD_Shield_LGD_ShootingStar', 1*addition_scale),
                # Unpaler
                ('/Game/Gear/Shields/_Design/_Uniques/Unpaler/Balance/InvBalD_Shield_LGD_Unpaler.InvBalD_Shield_LGD_Unpaler', 1*addition_scale),
                # Ward
                ('/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward.InvBalD_Shield_Ward', 1*addition_scale),
                # Deluxe Badass Combustor
                ('/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Balance/InvBalD_Shield_XPLootBooster.InvBalD_Shield_XPLootBooster', 1*addition_scale),
                ]),

        ('Grenades', None, '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary.ItemPool_GrenadeMods_05_Legendary',
            [
                ### Original pool

                # ECHO-2
                ('/Game/Gear/GrenadeMods/_Design/_Unique/EchoV2/Balance/InvBalD_GM_EchoV2.InvBalD_GM_EchoV2', 1),
                # Epicenter
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Epicenter/Balance/InvBalD_GM_Epicenter.InvBalD_GM_Epicenter', 1),
                # Fastball
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball.InvBalD_GM_TED_Fastball', 1),
                # Firestorm
                ('/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm', 1),
                # Tina's Hippity Hopper
                ('/Game/Gear/GrenadeMods/_Design/_Unique/HipHop/Balance/InvBalD_GM_TOR_HipHop.InvBalD_GM_TOR_HipHop', 1),
                # Hunter-Seeker
                ('/Game/Gear/GrenadeMods/_Design/_Unique/HunterSeeker/Balance/InvBalD_GM_HunterSeeker.InvBalD_GM_HunterSeeker', 1),
                # Moxxi's Bouncing Pair
                ('/Game/Gear/GrenadeMods/_Design/_Unique/MoxiesBosom/Balance/InvBalD_GM_PAN_MoxiesBosom.InvBalD_GM_PAN_MoxiesBosom', 1),
                # Nagata
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Nagate/Balance/InvBalD_GM_Nagate.InvBalD_GM_Nagate', 1),
                # Quasar
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Quasar/Balance/InvBalD_GM_Quasar.InvBalD_GM_Quasar', 1),
                # Red Queen
                ('/Game/Gear/GrenadeMods/_Design/_Unique/RedQueen/Balance/InvBalD_GM_RedQueen.InvBalD_GM_RedQueen', 1),
                # Hex
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Seeker/Balance/InvBalD_GM_Seeker.InvBalD_GM_Seeker', 1),
                # Storm Front
                ('/Game/Gear/GrenadeMods/_Design/_Unique/StormFront/Balance/InvBalD_GM_StormFront.InvBalD_GM_StormFront', 1),
                # Surge
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Surge/Balance/InvBalD_GM_Surge.InvBalD_GM_Surge', 1),
                # Tran-fusion
                ('/Game/Gear/GrenadeMods/_Design/_Unique/TranFusion/Balance/InvBalD_GM_TranFusion.InvBalD_GM_TranFusion', 1),
                # Widowmaker
                ('/Game/Gear/GrenadeMods/_Design/_Unique/WidowMaker/Balance/InvBalD_GM_WidowMaker.InvBalD_GM_WidowMaker', 1),

                ### Bloody Harvest Additions

                # Ghast Call
                ('/Game/PatchDLC/BloodyHarvest/Gear/GrenadeMods/_Design/_Unique/FontOfDarkness/Balance/InvBalD_GM_TOR_FontOfDarkness.InvBalD_GM_TOR_FontOfDarkness', 1),

                ### DLC1 (Moxxi's Heist)

                # Acid Burn
                ('/Game/PatchDLC/Dandelion/Gear/Grenade/AcidBurn/Balance/InvBalD_GM_AcidBurn.InvBalD_GM_AcidBurn', 1*addition_scale),
                # Slider
                ('/Game/PatchDLC/Dandelion/Gear/Grenade/Slider/Balance/InvBalD_GM_TED_Slider.InvBalD_GM_TED_Slider', 1*addition_scale),

                ### Revenge of the Cartels

                # Fish Slap
                ('/Game/PatchDLC/Event2/Gear/GrenadeMods/FishSlap/Balance/InvBalD_GM_FishSlap', 1),

                ### Guardian Takedown

                # Lightspeed
                ('/Game/PatchDLC/Takedown2/Gear/GrenadeMods/Lightspeed/Balance/InvBalD_GM_HYP_Lightspeed', 1),

                ### DLC3 (Bounty of Blood)

                # Core Buster
                ('/Game/PatchDLC/Geranium/Gear/Grenade/CoreBurst/Balance/InvBalD_GM_CoreBurst', 1*addition_scale),
                # Doc Hina's Miracle Bomb
                ('/Game/PatchDLC/Geranium/Gear/Grenade/SkagOil/Balance/InvBalD_GM_SkagOil', 1*addition_scale),

                ### DLC5 (Designer's Cut)

                # HOT Spring
                ('/Game/PatchDLC/Ixora/Gear/GrenadeMods/HOTSpring/Balance/InvBalD_GM_HOTSpring', 1),

                ### DLC6 (Director's Cut) + associated

                # Mesmer
                ('/Game/PatchDLC/Ixora2/Gear/GrenadeMods/_Unique/Mesmer/Balance/InvBalD_GM_Mesmer', 1),
                # Ringer / The Big Ringer / Dead Ringer
                ('/Game/PatchDLC/Ixora2/Gear/GrenadeMods/_Unique/Ringer/Balance/InvBalD_GM_Ringer', 1),

                ### Vault Card 2

                # Pyroburst
                ('/Game/PatchDLC/VaultCard2/Gear/GrenadeMods/Unique/Pyroburst/Balance/InvBalD_GM_Pyroburst', 1),

                ### Vault Card 3

                # Bloodsucker
                ('/Game/PatchDLC/VaultCard3/Gear/GrenadeMods/Unique/Bloodsucker/Balance/InvBalD_GM_Bloodsucker', 1),
                # Sidewinder
                ('/Game/PatchDLC/VaultCard3/Gear/GrenadeMods/Unique/Sidewinder/Balance/InvBalD_GM_Sidewinder', 1),

                ### Additions

                # Exterminator
                ('/Game/Gear/GrenadeMods/_Design/_Unique/BirthdaySuprise/Balance/InvBalD_GM_BirthdaySuprise.InvBalD_GM_BirthdaySuprise', 1*addition_scale),
                # Diamond Butt Bomb
                ('/Game/Gear/GrenadeMods/_Design/_Unique/ButtStallion/Balance/InvBalD_GM_ButtStallion.InvBalD_GM_ButtStallion', 1*addition_scale),
                # Rubber Cheddar Shredder
                ('/Game/Gear/GrenadeMods/_Design/_Unique/CashMoneyPreorder/Balance/InvBalD_GM_CashMoneyPreorder.InvBalD_GM_CashMoneyPreorder', 1*addition_scale),
                # Chupa's Organ
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Chupa/Balance/InvBalD_GM_Chupa.InvBalD_GM_Chupa', 1*addition_scale),
                # EMP
                ('/Game/Gear/GrenadeMods/_Design/_Unique/EMP/Balance/InvBalD_GM_EMP.InvBalD_GM_EMP', 1*addition_scale),
                # Chocolate Thunder
                ('/Game/Gear/GrenadeMods/_Design/_Unique/JustDeserts/Balance/InvBalD_GM_JustDeserts.InvBalD_GM_JustDeserts', 1*addition_scale),
                # Kryll
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Kryll/Balance/InvBalD_GM_Kryll.InvBalD_GM_Kryll', 1*addition_scale),
                # Elemental Persistent Contact Grenade (not a unique/leg?  Dropped by Jabbermogwai.  I guess we'll keep it, but eh?)
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Mogwai/Balance/InvBalD_GM_Mogwai.InvBalD_GM_Mogwai', 0.1*addition_scale),
                # Fungus Among Us
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Mushroom/Balance/InvBalD_GM_Shroom.InvBalD_GM_Shroom', 1*addition_scale),
                # Whispering Ice
                ('/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap', 1*addition_scale),
                # It's Piss
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss.InvBalD_GM_Piss', 1*addition_scale),
                # Burning Summit
                ('/Game/Gear/GrenadeMods/_Design/_Unique/Summit/Balance/InvBalD_GM_Summit.InvBalD_GM_Summit', 1*addition_scale),
                # Porcelain Pipe Bomb
                ('/Game/Gear/GrenadeMods/_Design/_Unique/ToiletBombs/Balance/InvBalD_GM_TOR_ToiletBombs.InvBalD_GM_TOR_ToiletBombs', 1*addition_scale),
                # Ultraball
                ('/Game/Gear/GrenadeMods/_Design/_Unique/ToyGrenade/Balance/InvBalD_GM_ToyGrenade.InvBalD_GM_ToyGrenade', 1*addition_scale),
                # NOG Potion #9
                ('/Game/Gear/GrenadeMods/_Design/_Unique/WizardOfNOG/Balance/InvBalD_GM_WizardOfNOG.InvBalD_GM_WizardOfNOG', 1*addition_scale),
                ]),

        ('Beastmaster COMs', None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster_05_Legendary.ItemPool_ClassMods_Beastmaster_05_Legendary',
            [
                # Stock COMs
                ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_05_Legendary', 6),

                # Mayhem 4 / Maliwan Takedown - R4kk P4k
                ('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1', 1),

                # DLC1 - St4ckbot
                ('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1', 1),

                # DLC2 - Tr4iner
                ('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib', 1),

                # DLC4 - Peregrine
                ('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Alisma', 1),

                # DLC5 - Cmdl3t
                ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/L01/InvBalD_CM_Ixora_BSM_L01', 1),

                # DLC6 - Roll Reversal
                ('/Game/PatchDLC/Ixora2/Gear/ClassMods/_Design/BSM/L01/InvBalD_CM_Ixora2_BSM_L01', 1),

                ]),

        ('Gunner COMs', None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner_05_Legendary.ItemPool_ClassMods_Gunner_05_Legendary',
            [
                # Stock COMs
                ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner_05_Legendary', 5),

                # Mayhem 4 / Maliwan Takedown - Raging Bear
                ('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_Raid1', 1),

                # DLC1 - Green Monster
                ('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1', 1),

                # DLC2 - Sapper
                ('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Hib', 1),

                # DLC4 - Flare
                ('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Alisma', 1),

                # DLC5 - Eternal Flame
                ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/L01/InvBalD_CM_Ixora_GUN_L01', 1),

                # DLC6 - Primary Heat Exchanger
                ('/Game/PatchDLC/Ixora2/Gear/ClassMods/_Design/GUN/L01/InvBalD_CM_Ixora2_GUN_L01', 1),

                ]),

        ('Operative COMs', None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative_05_Legendary.ItemPool_ClassMods_Operative_05_Legendary',
            [
                # Stock COMs
                ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative_05_Legendary', 5),

                # Mayhem 4 / Maliwan Takedown - Antifreeze
                ('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1', 1),

                # DLC1 - Seein' Dead
                ('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_DLC1', 1),

                # DLC2 - Conductor
                ('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Hib', 1),

                # DLC4 - Hustler
                ('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Alisma', 1),

                # DLC5 - Spy
                ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L01/InvBalD_CM_Ixora_OPE_L01', 1),

                # DLC5 - Provocateur (requires the Provocateur COM mod to work, so weight is set to
                # zero.  The Provocateur COM mod will set it to 1)
                ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/InvBalD_CM_Ixora_OPE_L02', 0),

                # DLC6 - Critical Mass
                ('/Game/PatchDLC/Ixora2/Gear/ClassMods/_Design/OPE/L01/InvBalD_CM_Ixora2_OPE_L01', 1),

                ]),

        ('Siren COMs', None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren_05_Legendary.ItemPool_ClassMods_Siren_05_Legendary',
            [
                # Stock COMs
                ('/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_05_Legendary', 5),

                # Mayhem 4 / Maliwan Takedown - Spiritual Driver
                ('/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1', 1),

                # DLC1 - Golden Rule
                ('/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_DLC1', 1),

                # DLC2 - Stone
                ('/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib', 1),

                # DLC4 - Muse
                ('/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Alisma', 1),

                # DLC5 - Kensei
                ('/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/L01/InvBalD_CM_Ixora_SRN_L01', 1),

                # DLC6 - Death's Blessings
                ('/Game/PatchDLC/Ixora2/Gear/ClassMods/_Design/SRN/L01/InvBalD_CM_Ixora2_SRN_L01', 1),

                ]),

        ('Artifacts', None, '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts_05_Legendary.ItemPool_Artifacts_05_Legendary',
            [
                ### Original Pool

                ('/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_05_Legendary', 14),

                ### DLC2 (Guns, Love, and Tentacles)

                # Lunacy
                ('/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy', 1),
                # Pearl of Ineffable Knowledge
                ('/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK', 1),

                ### DLC3 (Bounty of Blood)

                # Vendetta
                ('/Game/PatchDLC/Geranium/Gear/Artifacts/_Design/_Unique/Vengeance/Balance/InvBalD_Artifact_Vengeance', 1*addition_scale),

                ### DLC5 (Designer's Cut)

                # Deathrattle
                ('/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Deathrattle/Balance/InvBalD_Artifact_Deathrattle', 1),
                # Holy Grail / Perceval's Holy Grail / King Arthur's Holy Grail
                ('/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/HolyGrail/Balance/InvBalD_Artifact_HolyGrail', 1),

                ### DLC6 (Director's Cut) + associated

                # Mysterious Artifact
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet', 1*addition_scale),
                # Company Man (various) - gonna give this a 2x chance of spawning but spread out over the 9 variants.
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Atlas/Balance/InvBalD_Artifact_CompanyMan_Atlas', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/CoV/Balance/InvBalD_Artifact_CompanyMan_CoV', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Dahl/Balance/InvBalD_Artifact_CompanyMan_Dahl', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Hyperion/Balance/InvBalD_Artifact_CompanyMan_Hyperion', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Jakobs/Balance/InvBalD_Artifact_CompanyMan_Jakobs', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Maliwan/Balance/InvBalD_Artifact_CompanyMan_Maliwan', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Tediore/Balance/InvBalD_Artifact_CompanyMan_Tediore', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Torgue/Balance/InvBalD_Artifact_CompanyMan_Torgue', (1/9)*2),
                ('/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Vladof/Balance/InvBalD_Artifact_CompanyMan_Vladof', (1/9)*2),
                # Toboggan
                ('/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Toboggan/Balance/InvBalD_Artifact_Toboggan', 1),

                ### Vault Card 2

                # Shlooter
                ('/Game/PatchDLC/VaultCard2/Gear/Artifacts/Unique/Shlooter/Balance/InvBalD_Artifact_Shlooter', 1),

                ### Additions

                # Unleash the Dragon
                ('/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElDragonJr/Balance/InvBalD_Artifact_ElDragonJr', 1),
                # Electric Banjo
                ('/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElectricBanjo/Balance/InvBalD_Artifact_ElectricBanjo', 1),
                # Grave
                ('/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave', 1),
                # Phoenix Tears
                ('/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/PhoenixTears/Balance/InvBalD_Artifact_PhoenixTears', 1),
                # Road Warrior
                ('/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/RoadWarrior/Balance/InvBalD_Artifact_RoadWarrior', 1*addition_scale),
                # Vault Hunter's Relic
                ('/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/VaultHunterRelic/Balance/InvBalD_Artifact_Relic', 1*addition_scale),

                ]),

    ]

mod.header('Expand Legendary Pools')
legendary_weight_params = []
total_weight = 0
for (label, leg_gun_idx, pool, balances) in pools:
    mod.comment(label)
    set_pool(mod, pool, balances)
    mod.newline()

    # Collect info about the total weights contained in each gun category
    if leg_gun_idx is not None:
        legendary_weight_params.append((
            leg_gun_idx,
            label,
            sum([b[1] for b in balances]),
            ))
        total_weight += legendary_weight_params[-1][2]

mod.newline()

mod.header('Redistribute legendary gun drops evenly')
for idx, label, weight in sorted(legendary_weight_params):
    mod.comment('{}: {}%'.format(
        label,
        int(round(weight/total_weight, 6)*100),
        ))
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary',
            f'BalancedItems.BalancedItems[{idx}].Weight.BaseValueConstant',
            round(weight, 6))
mod.newline()

# A handful of DLC artifacts don't have a MinGameStage defined (or rather, it's set to 1),
# as opposed to most gear's 27.  This can cause problems for someone using this mod in
# Normal mode *without* my Early Bloomer mod -- prior to gamestage 27, the Artifact pools
# become valid drops, but the only available artifacts would be these.  So, those users
# would start seeing mysterious legendary artifacts pop up with surprising frequency.
# So, this hooks those artifacts up to the main-game DataTable, so that they play nicely
# with or without Early Bloomer.
#
# The Mysterious Amulet here will never spawn ordinarily -- it's the unreleased DLC5 version
# of the Mysterious Artifact which was properly released with DLC6.  But, we may as well do
# it here, too, since we're doing the others.
mod.header('Fix various artifact MinGameStage entries')
mingamestage = BVCF(dtv=DataTableValue(
    table='/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
    row='Artifacts',
    value='MinGameStage_17_2500317646FAD2F4916D158835B29E83',
    ))
for name, balance in [
        ('Lunacy', '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy'),
        ('Mysterious Amulet', '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet'),
        ('Mysterious Artifact', '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet'),
        ('Pearl of Ineffable Knowledge', '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK'),
        ('Vendetta', '/Game/PatchDLC/Geranium/Gear/Artifacts/_Design/_Unique/Vengeance/Balance/InvBalD_Artifact_Vengeance'),
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            balance,
            'Manufacturers.Manufacturers[0].GameStageWeight.MinGameStage',
            mingamestage)
mod.newline()

mod.close()


