#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

mod = Mod('dlc_loot_de-emphasizer.txt',
        'DLC Loot De-Emphasizer',
        [
            "So far, both story DLCs for BL3 have included specific legendary loot",
            "pools which world-drop pretty frequently throughout the DLC, so you get",
            "the same relatively-small set of drops often while playing.  This is",
            "great for the first playthrough or two, but after that, I'd typically",
            "prefer just getting the 'usual' world drops instead.  So, this mod aims",
            "to replace those specific drops with our ordinary legendary pool drops",
            "instead.",
            "",
            "This doesn't touch *specific* enemy drops, such as Gideon and The",
            "Procurer from DLC2, who drop from the same pool ordinarily used for DLC2",
            "legendary world drops.",
            "",
            "This is intended to be used alongside my Expanded Legendary Pools mod,",
            "so you've got interesting stuff dropping most of the time.",
        ],
        'NoDLCLoot',
        )

# Pools that we're redirecting stuff to
leg_pool_guns = Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary', 'ItemPoolData')
leg_pool_shields = Mod.get_full_cond('/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary', 'ItemPoolData')
leg_pool_coms = Mod.get_full_cond('/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_05_Legendary', 'ItemPoolData')

# Support functions
def do_hotfix(char_name, object_name, attr_name, index, to_pool):
    global mod
    mod.reg_hotfix(Mod.CHAR, char_name,
            object_name,
            attr_name.format(index),
            to_pool)

def do_itempoollist(char_name, list_name, index, to_pool):
    do_hotfix(char_name, list_name, 'ItemPools.ItemPools[{}].ItemPool', index, to_pool)

def do_itempool(char_name, pool_name, index, to_pool):
    do_hotfix(char_name, pool_name, 'BalancedItems.BalancedItems[{}].ItemPoolData', index, to_pool)

def legendary_guns_itempoollist(char_name, list_name, index):
    global leg_pool_guns
    do_itempoollist(char_name, list_name, index, leg_pool_guns)

def legendary_guns_itempool(char_name, pool_name, index):
    global leg_pool_guns
    do_itempool(char_name, pool_name, index, leg_pool_guns)

def legendary_shields_itempoollist(char_name, list_name, index):
    global leg_pool_shields
    do_itempoollist(char_name, list_name, index, leg_pool_shields)

def legendary_shields_itempool(char_name, pool_name, index):
    global leg_pool_shields
    do_itempool(char_name, pool_name, index, leg_pool_shields)

def legendary_coms_itempoollist(char_name, list_name, index):
    global leg_pool_coms
    do_itempoollist(char_name, list_name, index, leg_pool_coms)

def legendary_coms_itempool(char_name, pool_name, index):
    global leg_pool_coms
    do_itempool(char_name, pool_name, index, leg_pool_coms)

def zero_pool(hf_mode, hf_target, pool_name, index):
    global mod
    mod.reg_hotfix(hf_mode, hf_target,
            pool_name,
            'BalancedItems.BalancedItems[{}].Weight'.format(index),
            BVCF(bvc=0))

###
### DLC1 - Moxxi's Heist of the Handsome Jackpot
###

mod.header("DLC1 - Moxxi's Heist of the Handsome Jackpot")

# Main weapon pool
# The main guns pool actually already points to the global legendary pool, in addition to
# the custom one, so we're just zeroing out the probability of the DLC-specific one.
mod.comment('Main Weapon Pool')
for char_name in [
        # Via ItemPoolList_BadassEnemyGunsGearLoader1
        'BPChar_HyperionTurretBadass',
        'BPChar_LoaderBadass',
        # Via ItemPoolList_StandardEnemyGunsandGearLoader
        'BPChar_HyperionTurretBasic',
        'BPChar_LoaderShared',
        'BPChar_WeeLoaderBasic',
        'BPChar_DefenseCannonSuperBadass',
        'BPChar_DefenseCannonBasic',
        # Via ItemPoolList_BadassEnemyGunsGear_Dandelion
        'BPChar_SisterlyLove_DebtCollectorLoader',
        'BPChar_GreatEscape_Rudy',
        'BPChar_RagingBot_MachineGunMikey',
        'BPChar_EnforcerBadass_Looter',
        'BPChar_Enforcer_PrettyBoy',
        'BPChar_GoliathBadass_Looter',
        'BPChar_GoonBadass_Looter',
        'BPChar_PsychoBadass_Looter',
        'BPChar_PunkArmored_LooterVIP',
        'BPChar_PunkBadass_Looter',
        'BPChar_TinkBadass_Looter',
        'BPChar_TinkBadassArmored_Looter',
        'BPChar_ThePlan_TricksyNick',
        # Via ItemPoolList_Boss_Dandelion
        'BPChar_JackBot',
        # Via ItemPoolList_MiniBoss_Dandelion
        'BPChar_EnforcerBadass_Lawrence',
        'BPChar_GoonBadass_Coco',
        'BPChar_PunkBadass_Gaudy',
        'BPChar_TinkBadass_Giorgio',
        'BPChar_TraitorEddie',
        'BPChar_ClaptrapQueen',
        'BPChar_LoaderBadass_Venchy',
        # Via ItemPoolList_StandardEnemyGunsandGear_Dandelion
        'BPChar_AcidTrip_EarlyPrototype',
        'BPChar_EnforcerBruiser_Looter',
        'BPChar_GoliathBasic_Looter',
        'BPChar_GoliathMidget_Looter',
        'BPChar_GoonBasic_looter',
        'BPChar_GoonVortex_Looter',
        'BPChar_PsychoBasic_Looter',
        'BPChar_PsychoFirebrand_Looter',
        'BPChar_PsychoSlugger_Looter',
        'BPChar_PsychoSuicide_Looter',
        'BPChar_PunkAssaulter_Looter',
        'BPChar_PunkBasic_Looter',
        'BPChar_PunkShotgunner_Looter',
        'BPChar_PunkSniper_Looter',
        'BPChar_TinkBasic_Looter',
        'BPChar_TinkPsycho_Looter',
        'BPChar_TinkShotgun_Looter',
        'BPChar_TinkSuicide_Looter',
        'BPChar_CasinoBot_BigJanitor',
        ]:
    zero_pool(Mod.CHAR, char_name, '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion', 4)
mod.newline()

# Boss Weapon Pool
# Same story re: zeroing out
# ... though, in the end, this is really a dedicated drop type thing, so I'm leaving it.
#mod.comment('Boss Weapon Pool')
#for char_name in [
#        # Via ItemPoolList_Boss_Dandelion
#        'BPChar_JackBot',
#        ]:
#    zero_pool(Mod.CHAR, char_name, '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion_Boss', 4)
#mod.newline()

# COMs
# This also shows up in ItemPool_EquippablesNotGuns_Dandelion but I'm not sure
# what to make of that one
mod.comment('COM Pools')
for (pool_name, pool_idx, char_names) in [
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Dandelion', 5, [
                'BPChar_SisterlyLove_DebtCollectorLoader',
                'BPChar_GreatEscape_Rudy',
                'BPChar_RagingBot_MachineGunMikey',
                'BPChar_EnforcerBadass_Looter',
                'BPChar_Enforcer_PrettyBoy',
                'BPChar_GoliathBadass_Looter',
                'BPChar_GoonBadass_Looter',
                'BPChar_PsychoBadass_Looter',
                'BPChar_PunkArmored_LooterVIP',
                'BPChar_PunkBadass_Looter',
                'BPChar_TinkBadass_Looter',
                'BPChar_TinkBadassArmored_Looter',
                'BPChar_ThePlan_TricksyNick',
                ]),
        # The boss drop here really seems like it should stay; omitting this one.
        #('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_Boss_Dandelion', 5, [
        #        'BPChar_JackBot',
        #        ]),
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_MiniBoss_Dandelion', 5, [
                'BPChar_EnforcerBadass_Lawrence',
                'BPChar_GoonBadass_Coco',
                'BPChar_PunkBadass_Gaudy',
                'BPChar_TinkBadass_Giorgio',
                'BPChar_TraitorEddie',
                'BPChar_ClaptrapQueen',
                'BPChar_LoaderBadass_Venchy',
                ]),
        ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Dandelion', 5, [
                'BPChar_AcidTrip_EarlyPrototype',
                'BPChar_EnforcerBruiser_Looter',
                'BPChar_GoliathBasic_Looter',
                'BPChar_GoliathMidget_Looter',
                'BPChar_GoonBasic_looter',
                'BPChar_GoonVortex_Looter',
                'BPChar_PsychoBasic_Looter',
                'BPChar_PsychoFirebrand_Looter',
                'BPChar_PsychoSlugger_Looter',
                'BPChar_PsychoSuicide_Looter',
                'BPChar_PunkAssaulter_Looter',
                'BPChar_PunkBasic_Looter',
                'BPChar_PunkShotgunner_Looter',
                'BPChar_PunkSniper_Looter',
                'BPChar_TinkBasic_Looter',
                'BPChar_TinkPsycho_Looter',
                'BPChar_TinkShotgun_Looter',
                'BPChar_TinkSuicide_Looter',
                'BPChar_CasinoBot_BigJanitor',
                ]),
        ]:
    for char_name in char_names:
        legendary_coms_itempoollist(char_name, pool_name, pool_idx)

mod.newline()

###
### DLC2 - Guns, Love, and Tentacles
### Grenade pool doesn't need to be touched because it's empty
###

mod.header('DLC2 - Guns, Love, and Tentacles')

# Main weapon pool
mod.comment('Main Weapon Pool')
for char_name in [
        # References via ItemPoolList_Boss_Hibiscus
        'BPChar_HeartBoss',
        'BPChar_LostTwo_BigBro',
        'BPChar_LostTwo_ToughBro',
        'BPChar_Vincent',
        # References via ItemPoolList_Eista
        'BPChar_Hib_EistaChild_Radiation',
        # References via ItemPoolList_MiniBoss_Hibiscus
        'BPChar_ZealotNightmareShocker_Rare',
        'BPChar_ZealotPilfer_Child_Rare',
        'BPChar_LunaticPossessed',
        # References via ItemPoolList_StandardEnemyGunsandGear_Hibiscus
        'BPChar_FlyingSlugBasic',
        'BPChar_LostOneBadass',
        'BPChar_LostOneFlailing',
        'BPChar_Lunatic',
        'BPChar_Minion',
        'BPChar_Slug',
        'BPChar_Wolven_Shared',
        'BPChar_Zealot',
        # References via SpawnOptions that reference ItemPoolList_StandardEnemyGunsandGear_Hibiscus
        'BPChar_FrostEnforcerBruiser',
        'BPChar_FrostEnforcerMelee',
        'BPChar_FrostPsychoFirebrand',
        'BPChar_FrostPsychoSlugger',
        'BPChar_FrostPsychoSuicide',
        'BPChar_FrostPunk_Assaulter',
        'BPChar_FrostPunk_Badass',
        'BPChar_FrostPunk_Basic',
        'BPChar_FrostPunk_Shotgunner',
        'BPChar_FrostPunk_Sniper',
        'BPChar_FrostTinkBadass',
        'BPChar_FrostTinkBasic',
        'BPChar_FrostTinkShotgun',
        'BPChar_Spinsmouth',
        # References via SpawnOptions_Hib_Badass_Empowered_Spirit_WithLoot
        'BPChar_Hib_Nekro_Spirit',
        # Direct references from char
        'BPChar_Hib_Mancubite',
        ]:
    legendary_guns_itempool(char_name,
            '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Guns_All_Hibiscus', 4)
mod.newline()

# Loot Skritaari
mod.comment('Loot Skritaari Weapons')
legendary_guns_itempoollist('BPChar_MinionLoot',
        '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_Hib_MinionLoot', 12)
mod.newline()

# Sniper/Heavy Pool
# I assume the level hotfixes here are good enough?
mod.comment('Sniper/Heavy Pool (for chests)')
for level_name in [
        'Archive_P',
        'Camp_P',
        'Lake_P',
        'Venue_P',
        'Village_P',
        'Woods_P',
        ]:
    zero_pool(Mod.LEVEL, level_name, '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool__Hib_Sniper_Heavy_Legendary', 2)
mod.newline()

# Shield Pool
mod.comment('Shield Pool')
for char_name in [
        # References via ItemPoolList_StandardEnemyGunsandGear_Hibiscus
        'BPChar_FlyingSlugBasic',
        'BPChar_LostOneBadass',
        'BPChar_LostOneFlailing',
        'BPChar_Lunatic',
        'BPChar_Minion',
        'BPChar_Slug',
        'BPChar_Wolven_Shared',
        'BPChar_Zealot',
        # References via SpawnOptions that reference ItemPoolList_StandardEnemyGunsandGear_Hibiscus
        'BPChar_FrostEnforcerBruiser',
        'BPChar_FrostEnforcerMelee',
        'BPChar_FrostPsychoFirebrand',
        'BPChar_FrostPsychoSlugger',
        'BPChar_FrostPsychoSuicide',
        'BPChar_FrostPunk_Assaulter',
        'BPChar_FrostPunk_Badass',
        'BPChar_FrostPunk_Basic',
        'BPChar_FrostPunk_Shotgunner',
        'BPChar_FrostPunk_Sniper',
        'BPChar_FrostTinkBadass',
        'BPChar_FrostTinkBasic',
        'BPChar_FrostTinkShotgun',
        'BPChar_Spinsmouth',
        # There's also ItemPool_EquippablesNotGuns_Hibiscus, but that sounds like equippables?
        ]:
    legendary_shields_itempool(char_name,
            '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Shields_All_Hibiscus', 4)
mod.newline()

# COMs
# They're also mentioned in ItemPool_EquippablesNotGuns_Hibiscus but that sounds like equippables?
mod.comment('COM Pool - Badass Enemies')
for char_name in [
        # Direct char references
        'BPChar_Hib_Hunt_Hampton',
        'BPChar_SlugBadass_Kratch',
        'BPChar_Hib_Nekro_Spirit_Invisible',
        'BPChar_Hib_Nekro_SpiritBadass',
        'BPChar_Lost_Mush_Child',
        'BPChar_FlyingSlugBadass',
        'BPChar_Wolven_Badass',
        'BPChar_Zealot_Badass',
        'BPChar_Zealot_Badass_Procurer',
        ]:
    legendary_coms_itempoollist(char_name,
            '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Hibiscus', 5)
mod.newline()
mod.comment('COM Pool - Standard Enemies')
for char_name in [
        # References via ItemPoolList_StandardEnemyGunsandGear_Hibiscus
        'BPChar_FlyingSlugBasic',
        'BPChar_LostOneBadass',
        'BPChar_LostOneFlailing',
        'BPChar_Lunatic',
        'BPChar_Minion',
        'BPChar_Slug',
        'BPChar_Wolven_Shared',
        'BPChar_Zealot',
        # References via SpawnOptions that reference ItemPoolList_StandardEnemyGunsandGear_Hibiscus
        'BPChar_FrostEnforcerBruiser',
        'BPChar_FrostEnforcerMelee',
        'BPChar_FrostPsychoFirebrand',
        'BPChar_FrostPsychoSlugger',
        'BPChar_FrostPsychoSuicide',
        'BPChar_FrostPunk_Assaulter',
        'BPChar_FrostPunk_Badass',
        'BPChar_FrostPunk_Basic',
        'BPChar_FrostPunk_Shotgunner',
        'BPChar_FrostPunk_Sniper',
        'BPChar_FrostTinkBadass',
        'BPChar_FrostTinkBasic',
        'BPChar_FrostTinkShotgun',
        'BPChar_Spinsmouth',
        ]:
    legendary_coms_itempoollist(char_name,
            '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Hibiscus', 5)
mod.newline()

# Finish
mod.close()
