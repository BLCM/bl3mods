#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import csv
import sys
import enum
from bl3data.bl3data import BL3Data

# This script is what I'd used to construct my Enemy Equips mods.  I didn't
# directly plug that mod-generation script into data because it seemed like
# there was a fair bit of massaging that needed to be done.  This script has
# mutated across the development of that mod, so it would need some tweaking
# for anyone looking at it "blind," most likely.  The outputs are ill-defined
# and probably only really made sense to myself while constructing the mod.
# Ah well!

data = BL3Data()

bpchars_of_interest = set([
    'BPChar_MimicBasic',
    'BPChar_PunkArmored_LooterVIP',
    'BPChar_PunkBadass_Looter',
    'BPChar_CasinoBot_Basic',
    'BPChar_ServiceBot_Basic',
    'BPChar_ServiceBot_Mime',
    'BPChar_TherapyBot',
    'BPChar_Zealot',
    'BPChar_DoubleDown_DoubleDownDomina',
    'BPChar_RagingBot_Yvan',
    'BPChar_PunkArmored_LooterVIP',
    ])

known_multi = set([
    # Dunno what's up with this one, but whatever.
    '/Hibiscus/Enemies/Zealot/Clone/_Design/Character/BPChar_ZealotExplosiveTrailClone',
    ])

class PoolType(enum.Enum):
    SG = 1
    SM = 2
    AR = 3
    SR = 4
    HW = 5
    PS = 6
    SG_AR_SM_PS = 7

pool_blocklist = set([
    '/Alisma/Enemies/_Unique/SpongeBoss/_Design/ItemPools/ItemPool_SpongeBoss',
    '/Game/Enemies/Ape/_Unique/KingBobo/_Design/Weapon/ItemPool_ApeKingBobo_Club',
    '/Game/Enemies/DropShipTurret/_Shared/_Design/Weapon/ItemPool_DropshipTurret_Weapon',
    '/Game/Enemies/Enforcer/Anointed/_Design/Weapons/ItemPool_Enforcer_Anointed_Gun',
    '/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Weapon/ItemPool_KillaVolt_Ninevolt',
    '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Gun',
    '/Game/Enemies/Frontrunner/Badass/_Design/ItemPools/ItemPool_FrontrunerBadass',
    '/Game/Enemies/Frontrunner/Jammer/_Design/Weapons/Itempool_FrontJammer_Beam',
    '/Game/Enemies/Goliath/_Unique/CageArena/_Design/Weapons/ItemPool_GoliathCageArea_Gun',
    '/Game/Enemies/Goon/_Shared/_Design/Weapons/ItemPool_Goon_AirGun',
    '/Game/Enemies/Guardian/Sera/_Design/Weapon/ItemPool_GuardianSera_Pods',
    '/Game/Enemies/Guardian/Wraith/_Design/Weapon/ItemPool_GuardianStaff',
    '/Game/Enemies/Mech/_Unique/EvilAI/_Design/Weapon/ItemPool_MechEvilAI_Gun',
    '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/BallGun/Weapon/ItemPool_BallGun',
    '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Weapons/Gun/ItemPool_GiganticMech1_Gun',
    '/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Weapons/Launcher/ItemPool_GiganticMech_Launcher',
    '/Game/Enemies/Oversphere/_Shared/_Design/Weapon/ItemPool_Oversphere_Weapon_03',
    '/Game/Enemies/Oversphere/_Unique/OversphereVR/_Design/Weapon/ItemPool_OversphereVR_Weapon',
    '/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/ItemPool_PunkBounty02_Equipped',
    '/Game/Enemies/Saurian/_Unique/Laser/_Design/Character/ItemPool_SaurianLaser',
    '/Game/Enemies/ServiceBot/EMS/_Design/Weapon/ItemPool_ServiceBot_EMS',
    '/Game/Enemies/ServiceBot_Turret/_Shared/_Design/Weapon/ItemPool_ServiceBotTurret_Weapon',
    '/Game/Enemies/Tink_Turret/_Shared/_Design/Weapon/ItemPool_Tink_Turret_BasicGun',
    '/Game/Gear/Weapons/_Shared/NPC_Weapons/Typhon/ItemPool_SG_JAK_Typhon',
    '/Game/Missions/Side/Zone_2/Prison/FreeHugs/ItemPool_FreeHugs_Fingerbiter',
    '/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/ItemPool_Troy_Gun',
    '/Game/PatchDLC/Dandelion/Enemies/HyperionTurret/Cryo/_Design/Weapon/ItemPool_HyperionTurret_Cryo',
    '/Game/PatchDLC/Dandelion/Enemies/HyperionTurret/Fire/_Design/Weapon/ItemPool_HyperionTurret_Fire',
    '/Game/PatchDLC/Dandelion/Enemies/HyperionTurret/_Shared/_Design/Weapon/ItemPool_HyperionTurret_Basic',
    '/Game/PatchDLC/Event2/Enemies/Cyber/Behemoth/_Shared/_Design/Weapons/Gunner/ItemPool_CyberGunner_Cannon',
    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Weapons/BallGun/ItemPool_Behemoth_Ballgun',
    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Weapons/Cannon/ItemPool_Gunner_Cannon',
    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Weapons/RaidCannon/ItemPool_Gunner_RaidCannon',
    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/BrainBeams/Weapons/ItemPool_BrainBeam_Weapon',
    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/UpperHalf/Weapon/ItemPool_UpperHalf_Gun',
    '/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Weapons/ItemPool_MechRaidBossA_Gun',
    '/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Weapons/ItemPool_MechRaidBossB_Gun',
    '/Game/PatchDLC/Raid1/Enemies/Oversphere/_Unique/RaidBoss/_Design/Weapons/ItemPool_Oversphere_RaidBoss_Weapon',
    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/Miniboss/_Design/Weapon/ItemPool_GuardianMiniboss_BladeGun',
    '/Geranium/Enemies/LodgeBoss/_Design/Weapon/ItemPool_SploderBoss_Weapon',
    '/Geranium/NonPlayerCharacters/Rose/_TheBoss/Weapon/ItemPool_RoseBoss_Pistol',
    '/Geranium/NonPlayerCharacters/Rose/_TheBoss/Weapon/ItemPool_RoseBoss_Sword',
    '/Hibiscus/Enemies/DefenseCannon/_Shared/_Design/Weapons/ItemPool_Hib_DefenseCannon_Weapon',
    '/Hibiscus/Enemies/Wolf/Alpha/_Design/ItemPools/ItemPool_WolfAlpha',
    '/Hibiscus/Enemies/Zealot/PilferEye/_Design/Weapon/ItemPool_PilferEye_Main_Weapon',
    '/Hibiscus/Enemies/_Shared/_Design/ItemPools/ItemPool_Specter_PS_Use',
    '/Hibiscus/InteractiveObjects/MissionSpecific/Crew/Mancubus/_Shared/_Design/Weapon/ItemPool_Mancubus',
    '/Ixora2/Enemies/CotV/Golaith/Cyberpunk_Bouncer/_Design/Weapons/ItemPool_Golaith_CyberpunkBouncer_Gun',
    '/Ixora2/Enemies/CotV/Punk/BanditChief/_Design/Weapon/ItemPool_Punk_BanditChief_Weapon',

    # Drop pools, may need redirect instead
    #'/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Common',
    #'/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_VeryRare',
    #'/Game/GameData/Loot/ItemPools/Guns/ItemPool_AR_Shotgun_SMG_Legendary',
    #'/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All',
    #'/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_ETech_All',
    #'/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Rare',
    #'/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Rare',

    # Fire SM
    '/Game/PatchDLC/Event2/Enemies/Meat/Punk/RoasterLT/_Design/Character/ItemPool_Roaster_Equip',
    # Shock HW
    '/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Weapon/ItemPools/ItemPool_SkagLady_HeavyWeapons',
    # Corrosive AR
    '/Game/Enemies/Goliath/Corrosive/_Design/Weapons/ItemPool_Goliath_Corrosive_AR_VLA',
    # Corrosive SG
    '/Game/PatchDLC/Event2/Enemies/Meat/Tink/TenderizerLt/_Design/Weapon/ItemPool_Tenderizer_SG',
    # Corrosive SM
    '/Geranium/Enemies/GerSaurian/_Unique/Horsemen1/_Design/Rider/ItemPool_GerTinkHorsemen1',
    # Fire SM
    '/Geranium/Enemies/GerSaurian/_Unique/Horsemen2/_Design/Rider/ItemPool_GerEnforcerHorsemen2',
    # Rad SM
    '/Geranium/Enemies/GerSaurian/_Unique/Horsemen3/_Design/Rider/ItemPool_GerPunkHorsemen3',
    # Cryo SM
    '/Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Rider/ItemPool_GerPunkHorsemen4',
    # Etech SM
    '/Hibiscus/Enemies/Zealot/Ghost/_Design/Inventory/ItemPool_Hib_SMGs_ETech_InvisibleZealots',
    # Corrosive SM
    '/Hibiscus/Enemies/_Shared/_Design/ItemPools/ItemPool_Zealots_EnemyUse_SMG_E_Corr_Only',
    # Shock SM
    '/Hibiscus/Enemies/_Shared/_Design/ItemPools/ItemPool_Zealots_EnemyUse_SMG_E_Shock_Only',
    ])

pool_mapping = {
        PoolType.SG: {
            '/Dandelion/Enemies/TraitorEddie/_Shared/_Design/Weapon/ItemPool_TraitorEddie',
            '/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/ItemPool_ApeJungleMonarch_SG',
            '/Game/Enemies/Enforcer/Gun/_Design/Character/ItemPool_EnforcerGun_Shotguns',
            '/Game/Enemies/Enforcer/_Shared/_Design/Weapon/ItemPool_CoVEnforcers_Shotguns',
            '/Game/Enemies/Tink/Shotgun/_Design/ItemPools/ItemPool_TinkUse_Shotguns',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SG',
            '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Shotguns',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_Loader_SG',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPool_WeeLoader_LeftArm',
            '/Geranium/Enemies/Gyro/Bomber/_Design/Weapons/ItemPool_GerTinkBomber_Weapons',
            '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_Shotguns',
            '/Hibiscus/Enemies/Lunatic/_Shared/_Design/Weapon/ItemPool_Hib_EnemyUse_SG_Lunatics',
            '/Hibiscus/Enemies/Lunatic/_Shared/_Design/Weapon/ItemPool_Lunatics_Shotguns',
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
            '/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/ItemPool_SR_MAL_KatagawaJR',
            '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SR',
            '/Geranium/Enemies/_Shared/_Design/ItemPools/ItemPool_GerCoVEnemyUse_SniperRifles',
            '/Hibiscus/Enemies/Zealot/Pilfer/_Design/Weapon/ItemPool_Zealots_EnemyUse_SR_E_Pilfer',
            },
        PoolType.HW: {
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
pool_mapping_known = set()
for pools in pool_mapping.values():
    for pool in pools:
        pool_mapping_known.add(pool)

# Process!
# Valid attributes inside the PlayThroughs entries are:
#
#   bOverrideEquippedItems
#	EquippedItemPoolCollection 
#   EquippedItemPoolCollections
#   bEquipSingleItemFromCollection
#
# ... but the singular `EquippedItemPoolCollection` is literally never used, at least
# as of 2021-06-17, so we'll ignore that one.  The plural `EquippedItemPoolCollections`
# is an array of ItemPools, with the same attrs as an ItemPoolList.
bpchar_to_pool = {}
pool_to_bpchar = {}
for bpchar_name in data.find('', 'BPChar_'):

    # Hardcoded exclusions; not doing antyhing PC related
    if bpchar_name.startswith('/Game/PlayerCharacters/') or bpchar_name.startswith('/Game/OakTest/'):
        continue

    balancestates = data.get_exports(bpchar_name, 'AIBalanceStateComponent')
    if len(balancestates) == 0:
        # Eh, whatever, there's a lot of 'em
        #print('No AIBalanceStateComponent for {}'.format(bpchar_name))
        continue
    elif len(balancestates) > 1:
        if bpchar_name not in known_multi:
            print('{} AIBalanceStateComponents for {}'.format(len(balancestates), bpchar_name))
        continue

    bpchar_short = bpchar_name.split('/')[-1]

    bs = balancestates[0]
    if 'PlayThroughs' in bs:
        for idx, pt in enumerate(bs['PlayThroughs']):
            if ('bOverrideEquippedItems' in pt
                    and pt['bOverrideEquippedItems']
                    and 'EquippedItemPoolCollections' in pt
                    and len(pt['EquippedItemPoolCollections']) > 0):

                if bpchar_short in bpchars_of_interest or False:

                    if len(pt['EquippedItemPoolCollections']) > 1:
                        extra = ' *** {} choices'.format(
                                len(pt['EquippedItemPoolCollections']),
                                )
                    else:
                        extra = ''

                    print('{}: PT {}{}'.format(
                        bpchar_name,
                        idx,
                        extra,
                        ))

                for col_idx, collection in enumerate(pt['EquippedItemPoolCollections']):

                    if 'ItemPools' in collection:

                        for pool_idx, pool in enumerate(collection['ItemPools']):
                            if ('ItemPool' in pool
                                    and 'export' not in pool['ItemPool']
                                    and len(pool['ItemPool']) == 2):
                                pool_name = pool['ItemPool'][1]

                                # Don't show stuff we've already blocked
                                if pool_name in pool_blocklist:
                                    continue

                                # Also don't show pools we've already "mapped"
                                if pool_name in pool_mapping_known:
                                    continue

                                if bpchar_short not in bpchar_to_pool:
                                    bpchar_to_pool[bpchar_short] = set()
                                bpchar_to_pool[bpchar_short].add(pool_name)

                                if pool_name not in pool_to_bpchar:
                                    pool_to_bpchar[pool_name] = set()
                                pool_to_bpchar[pool_name].add(bpchar_short)

                                if bpchar_short in bpchars_of_interest:
                                    print(' - Col {}, Pool {}: {}'.format(
                                        col_idx,
                                        pool_idx,
                                        pool_name,
                                        ))

# We *could* process some SpawnOptions as well - the `SpawnFactory_OakAI` class does have
# the necessary vars available in it, namely: bOverrideEquippedItems, CustomItemCollectionsToEquip,
# and bEquipSingleItemFromCollection.  (also CustomItemCollectionToEquip, but that's not used
# by any of them, and the AIBalanceStateComponents objects don't use that onw either.
#
# As of 2021-06-17, though, there's only a single SpawnOption object which seems to actually
# do it "properly," specifically:
#
#    /Game/Enemies/_Spawning/CotV/Punks/_Unique/SpawnOptions_PunkSecretAgent02
#
# ... and that's for a friendly ally during that one Ambermire mission.  So, whatever,
# just ignore SpawnOptions for the purposes of this.  There's vanishingly few which
# reference *any* of the attributes above.  There's this one which has the
# bOverrideEquippedItems boolean but no actual pool data:
#
#    /Alisma/Enemies/_Spawning/SpongBoss/Individual/SpawnOptions_SpongeBoss
#
# ... and then there's these three with pool data but no bOverrideEquippedItems boolean:
#
#    /Dandelion/Enemies/Boss/PrettyBoy/_Design/Character/SpawnOptions_PitBoss1
#    /Dandelion/Enemies/JackBot/Spawning/SpawnOptions_JackBot
#    /Game/Missions/Side/Zone_1/City/BitterPillToSwallow/MedicalSupplyTechnical/SpawnOptions_Technical_BitterPillToSwallow
#
# So yeah, the only one that does it right is an ally, so whatever.  Ignore 'em.
#
# ----
# 
#for spawnoption_name in data.find('', 'SpawnOptions_'):
#    spawnfactories = data.get_exports(spawnoption_name, 'SpawnFactory_OakAI')
#    for sf in spawnfactories:
#        if 'bOverrideEquippedItems' in sf and 'CustomItemCollectionsToEquip' in sf:
#            print(spawnoption_name)

print('')
print('--')
print('')
for pool_name, bpchars in sorted(pool_to_bpchar.items()):
    print(pool_name)
    for bpchar in sorted(bpchars):
        print(' - {}'.format(bpchar))
