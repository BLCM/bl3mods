#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
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
import enum
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, ItemPool

# The data which drives this mod was collected basically all using my `get_char_equips.py`
# script, in my `dataprocessing` dir.  I didn't hook this generation script up directly
# to the data-gathering routines, though, since it seemed like more work to do so than
# just do some copy-and-pasting.

class PoolType(enum.Enum):
    SG = 'Shotguns'
    SG_ONLY = 'Shotguns (restricted)'
    SM = 'SMGs'
    AR = 'Assault Rifles'
    SR = 'Sniper Rifles'
    SR_ONLY = 'Sniper Rifles (restricted)'
    HW = 'Heavy Weapons'
    HW_ONLY = 'Heavy Weapons (restricted)'
    PS = 'Pistols'
    SG_AR_SM_PS = 'Various Types'

    def __lt__(self, other):
        return str(self) < str(other)

    def __str__(self):
        return self.value

# The pools which enemies use for their equips; we'll be resetting the contents of these
# pools.
equip_pools = {
        PoolType.SG: {
            '/Game/Enemies/Enforcer/Gun/_Design/Character/ItemPool_EnforcerGun_Shotguns',
            '/Game/Enemies/Enforcer/_Shared/_Design/Weapon/ItemPool_CoVEnforcers_Shotguns',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SG',
            '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Shotguns',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_Loader_SG',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_WeeLoader_LeftArm',
            '/Geranium/Enemies/Gyro/Bomber/_Design/Weapons/ItemPool_GerTinkBomber_Weapons',
            '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_Shotguns',
            '/Hibiscus/Enemies/Lunatic/_Shared/_Design/Weapon/ItemPool_Hib_EnemyUse_SG_Lunatics',
            '/Hibiscus/Enemies/Lunatic/_Shared/_Design/Weapon/ItemPool_Lunatics_Shotguns',
            },
        PoolType.SG_ONLY: {
            '/Dandelion/Enemies/TraitorEddie/_Shared/_Design/Weapon/ItemPool_TraitorEddie',
            '/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/ItemPool_ApeJungleMonarch_SG',
            '/Game/Enemies/Tink/Shotgun/_Design/ItemPools/ItemPool_TinkUse_Shotguns',
            },
        PoolType.SM: {
            '/Game/Enemies/Frontrunner/Striker/_Design/ItemPools/ItemPool_FrontStriker_SMG',
            '/Game/Enemies/Mech/MG/_Design/Weapons/ItemPool_MechMG_Gun',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_MAL_SM_NoBeams',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_TrooperBasic_SM',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SM',
            '/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/ItemPool_Trooper_Bounty01_Equipped',
            '/Game/Enemies/Trooper/_Unique/JavaFlasher/_Design/Character/ItemPool_TrooperJavaFlasher_SM',
            '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_SMGs',
            '/Game/NonPlayerCharacters/CrimsonAlliance/_Design/ItemPoolLists/ItemPool_CrimsonAlliance_SMGs',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_Loader_SM',
            '/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/ItemPool_Enforcer_Reaper',
            },
        PoolType.AR: {
            '/Game/Enemies/Tink/Anointed/_Design/ItemPool/ItemPool_TinkAnointed_AssaultRifles',
            '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_AssaultRifles',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_Loader_AR',
            '/Geranium/Enemies/Quartermaster/Mech/_Design/Weapons/ItemPool_Quartermaster_Mech_AssaultRifles',
            '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_AssaultRifles',
            '/Hibiscus/NonPlayerCharacters/_Generic/Gideon/_Design/Character/ItemPool_EnemyUse_AS_Guideon',
            '/Ixora/Enemies/CotV/Punk/Badass/_Design/Character/ItemPool_BadassPunk_AssaultRifles',
            '/Ixora/Enemies/Maliwan/Frontrunner/GearUp/_Design/ItemPools/ItemPool_CoVFrontrunner_GearUp_Equip',
            },
        PoolType.SR: {
            # I actually feel like basically anything that's set to use Snipers should continue to do so.
            },
        PoolType.SR_ONLY: {
            '/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/ItemPool_SR_MAL_KatagawaJR',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SR',
            '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_SniperRifles',
            '/Hibiscus/Enemies/Zealot/Pilfer/_Design/Weapon/ItemPool_Zealots_EnemyUse_SR_E_Pilfer',
            },
        PoolType.HW: {
            # I actually feel like basically anything that's set to use Heavies should continue to do so.
            },
        PoolType.HW_ONLY: {
            '/Game/Enemies/Mech/Grenadier/_Design/Weapons/ItemPool_MechGrenadier_Launcher',
            '/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Weapon/ItemPool_Mech_TrialBoss_Launcher',
            '/Game/Enemies/Punk_Female/Badass/_Design/Weapon/ItemPools/ItemPool_BadassPunk_HeavyWeapons',
            '/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Weapon/ItemPool_PunkBrewHag_Weapon',
            '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_COVEnemyUse_HeavyWeapons',
            '/Hibiscus/Enemies/FrostBiters/_Unique/_Design/Character/ItemPool_Spimmouth_EnemyUse_HW',
            },
        PoolType.PS: {
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_TrooperBadass',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_PS',
            '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Pistols',
            '/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Weapons/ItemPool_AureliaBoss_Equipped',
            '/Geranium/Enemies/Gyro/_Unique/Painless/_Design/ItemPools/ItemPool_GyroPainless_EquippedGun',
            '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_Pistols',
            },
        PoolType.SG_AR_SM_PS: {
            '/Geranium/NonPlayerCharacters/GerNPC/_Shared/_Design/Character/ItemPool_GerNPC_Weapon',
            },
        }

# There are some bpchars whose Equip pools point right to the world-drop pools already, but
# we're going to want to modify those too.  So we're just taking the first pool in each of
# our categories and reassigning to those.  The UE4 dynamic object loading stuff should
# do the rest.
bpchar_inject_pools = {}
for weap_type, pools in equip_pools.items():
    if len(pools) > 0:
        bpchar_inject_pools[weap_type] = Mod.get_full_cond(sorted(pools)[0], 'ItemPoolData')

# ... aaand here's those bpchars.  The tuple numbers here refer to, in order:
#    1) PlayThroughs index
#    2) EquippedItemPoolCollections index
#    3) ItemPools index
bpchar_injections = [
        ('/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan', [
            (0, 0, 0, PoolType.SM),
            (1, 0, 0, PoolType.SM),
            ]),
        ('/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina', [
            (0, 0, 0, PoolType.SM),
            ]),
        ('/Dandelion/Enemies/Looters/Punk/ArmoredVIP/_Design/Character/BPChar_PunkArmored_LooterVIP', [
            (0, 0, 1, PoolType.AR),
            (0, 0, 2, PoolType.SG),
            ]),
        ('/Dandelion/Enemies/Looters/Punk/Badass/_Design/Character/BPChar_PunkBadass_Looter', [
            (0, 0, 1, PoolType.SG_AR_SM_PS),
            ]),
        ('/Dandelion/Enemies/ServiceBot/MimeBot/BPChar_ServiceBot_Mime', [
            (0, 0, 0, PoolType.PS),
            (1, 0, 0, PoolType.PS),
            ]),
        ('/Dandelion/Enemies/Mimic/Basic/_Design/Character/BPChar_MimicBasic', [
            (0, 0, 0, PoolType.AR),
            (0, 0, 1, PoolType.AR),
            ]),
        # TODO: This should really just be *etech* SRs
        #('/Hibiscus/Enemies/Zealot/_Shared/_Design/Character/BPChar_Zealot', [
        #    (0, 0, 0, PoolType.SM),
        #    ]),
        ('/Game/PatchDLC/Dandelion/Enemies/ServiceBot/Basic/_Design/character/BPChar_CasinoBot_Basic', [
            (0, 0, 0, PoolType.PS),
            (1, 0, 0, PoolType.PS),
            ]),
        ('/Game/NonPlayerCharacters/_Nekrotafeyo/Therapybot/_Design/Character/BPChar_TherapyBot', [
            (0, 0, 0, PoolType.PS),
            ]),
        ('/Game/Enemies/ServiceBot/Basic/_Design/Character/BPChar_ServiceBot_Basic', [
            (0, 0, 0, PoolType.PS),
            (1, 0, 0, PoolType.PS),
            ]),
        ]

# Pools that we're going to actually use for the equips
reg_sg = ItemPool('foo', pools=[
    ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Common', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common')),
    ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Uncommon', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon')),
    ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Rare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare')),
    ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_VeryRare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare')),
    ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary')),
    ])
reg_sm = ItemPool('foo', pools=[
    ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Common', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common')),
    ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Uncommon', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon')),
    ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Rare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare')),
    ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_VeryRare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare')),
    ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary')),
    ])
reg_ar = ItemPool('foo', pools=[
    ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Common', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common')),
    ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Uncommon', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon')),
    ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Rare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare')),
    ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_VeryRare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare')),
    ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary')),
    ])
reg_sr = ItemPool('foo', pools=[
    ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Common', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common')),
    ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Uncommon', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon')),
    ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Rare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare')),
    ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_VeryRare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare')),
    ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary')),
    ])
reg_hw = ItemPool('foo', pools=[
    ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Common', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common')),
    ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Uncommon', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon')),
    ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Rare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare')),
    ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_VeryRare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare')),
    ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary')),
    ])
reg_ps = ItemPool('foo', pools=[
    ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Common', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common')),
    ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Uncommon', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon')),
    ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Rare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare')),
    ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_VeryRare', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare')),
    ('/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary', BVC(bva='/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary')),
    ])
reg_all = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All'])
leg_sg = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary'])
leg_sm = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary'])
leg_ar = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary'])
leg_sr = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary'])
leg_hw = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary'])
leg_ps = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary'])
leg_all = ItemPool('foo', pools=['/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary'])
fakobs = ItemPool('foo', balances=['/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs'])

# Now loop through and generate some mods!
for filename, label, extra_cats, desc, pool_mapping in [
        ('all', 'All World Drops', None, [
            "Sets nearly all enemies to use the world drop pools to define the",
            "weapons they equip.  Mods which increase drop quality will result",
            "in more powerful enemies, and enemies using sniper rifles and",
            "heavy weapons will become more frequent.  It's recommended to use",
            "my Early Bloomer mod if using this in the early game.",
            ], {
                PoolType.SG: reg_all,
                PoolType.SG_ONLY: reg_sg,
                PoolType.SM: reg_all,
                PoolType.AR: reg_all,
                PoolType.SR: reg_all,
                PoolType.SR_ONLY: reg_sr,
                PoolType.HW: reg_all,
                PoolType.HW_ONLY: reg_hw,
                PoolType.PS: reg_all,
                PoolType.SG_AR_SM_PS: reg_all,
                }),
        ('typelocked', 'Typelocked World Drops', None, [
            "Sets nearly all enemies to use the world drop pools to define the",
            "weapons they equip.  Mods which increase drop quality will result",
            "in more powerful enemies.  Enemies will still equip the same type",
            "of weapon they ordinarily would.  It's recommended to use",
            "my Early Bloomer mod if using this in the early game.",
            ], {
                PoolType.SG: reg_sg,
                PoolType.SG_ONLY: reg_sg,
                PoolType.SM: reg_sm,
                PoolType.AR: reg_ar,
                PoolType.SR: reg_sr,
                PoolType.SR_ONLY: reg_sr,
                PoolType.HW: reg_hw,
                PoolType.HW_ONLY: reg_hw,
                PoolType.PS: reg_ps,
                PoolType.SG_AR_SM_PS: reg_all,
                }),
        ('legendaries_all', 'Legendaries (all)', ['joke'], [
            "Sets nearly all enemies to use the world drop legendary pools to",
            "define the weapons they equip.  This will almost certainly result",
            "in a more difficult game, and there will be more enemies using",
            "sniper rifles and heavy weapons, too.  It's recommended to use",
            "my Expanded Legendary Pools mod along with this one.",
            ], {
                PoolType.SG: leg_all,
                PoolType.SG_ONLY: leg_sg,
                PoolType.SM: leg_all,
                PoolType.AR: leg_all,
                PoolType.SR: leg_all,
                PoolType.SR_ONLY: leg_sr,
                PoolType.HW: leg_all,
                PoolType.HW_ONLY: leg_hw,
                PoolType.PS: leg_all,
                PoolType.SG_AR_SM_PS: leg_all,
                }),
        ('legendaries_typelocked', 'Legendaries (typelocked)', ['joke'], [
            "Sets nearly all enemies to use the world drop legendary pools to",
            "define the weapons they equip.  This will almost certainly result",
            "in a more difficult game.  Enemies will still equip the same type",
            "of weapon they ordinarily would.  It's recommended to use my",
            "my Expanded Legendary Pools mod along with this one.",
            ], {
                PoolType.SG: leg_sg,
                PoolType.SG_ONLY: leg_sg,
                PoolType.SM: leg_sm,
                PoolType.AR: leg_ar,
                PoolType.SR: leg_sr,
                PoolType.SR_ONLY: leg_sr,
                PoolType.HW: leg_hw,
                PoolType.HW_ONLY: leg_hw,
                PoolType.PS: leg_ps,
                }),
        ('shoddy', 'All The Shoddy', ['joke'], [
            "Sets nearly all enemies to use The Shoddy as their equipped",
            "weapon.  Someone might want to have a talk with the CoV about",
            "the effectiveness of this otherwise-majestic weapon...",
            ], {
                PoolType.SG: fakobs,
                PoolType.SG_ONLY: fakobs,
                PoolType.SM: fakobs,
                PoolType.AR: fakobs,
                PoolType.SR: fakobs,
                PoolType.SR_ONLY: fakobs,
                PoolType.HW: fakobs,
                PoolType.HW_ONLY: fakobs,
                PoolType.PS: fakobs,
                PoolType.SG_AR_SM_PS: fakobs,
                }),
        ]:

    # Mod categories
    cats = ['enemy', 'gameplay']
    if extra_cats:
        cats.extend(extra_cats)

    # In-mod description
    desc.extend([
        "",
        "Does not affect unique-gear-using enemies, elemental-gear-locked",
        "enemies, melee-only enemies, or enemies with extremely customized",
        "weapons (such as Eridians, etc).",
        ])

    # Start the mod
    mod = Mod('enemy_equips_{}.bl3hotfix'.format(filename),
            'Enemy Equips: {}'.format(label),
            'Apocalyptech',
            desc,
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.0.0',
            cats=', '.join(sorted(cats)),
            )

    # First up, do our BPChar pool injections, for enemies which reference
    # the main world drop pools already.
    mod.header('BPChar Pool Injections (for the few BPChars which need it)')
    for bpchar, injections in bpchar_injections:
        bpchar_short = bpchar.split('/')[-1]
        mod.comment(bpchar)
        for pt, col, pool, weap_type in injections:
            mod.reg_hotfix(Mod.CHAR, bpchar_short,
                    '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar, bpchar_short),
                    'PlayThroughs.PlayThroughs[{}].EquippedItemPoolCollections.EquippedItemPoolCollections[{}].ItemPools.ItemPools[{}].ItemPool'.format(
                        pt,
                        col,
                        pool,
                        ),
                    bpchar_inject_pools[weap_type])
        mod.newline()

    # Now do our pool overrides.
    for weap_type, pools in sorted(equip_pools.items()):
        if len(pools) > 0:
            if weap_type in pool_mapping:
                new_pool = pool_mapping[weap_type]

                mod.header(str(weap_type))
                for pool_name in sorted(pools):
                    mod.reg_hotfix(Mod.CHAR, 'MatchAll',
                            pool_name,
                            'BalancedItems',
                            str(new_pool))
                mod.newline()

    mod.close()

