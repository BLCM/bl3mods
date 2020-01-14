#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

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

type_pools = [
        (AR, [
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Common', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Uncommon', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Rare', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_VeryRare', False, [VLA, ATL, COV, DAL, JAK, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_ETech_Rare', False, [COV, VLA, DAL, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_ETech_VeryRare', False, [COV, VLA, DAL, TOR]),
            ]),
        (HV, [
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Common', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Uncommon', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Rare', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_VeryRare', False, [ATL, COV, TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_ETech_Rare', False, [TOR, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_ETech_VeryRare', False, [TOR, VLA]),
            ]),
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
            ]),
        (SG, [
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Common', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Uncommon', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Rare', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_VeryRare', False, [HYP, MAL, TOR, JAK, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_ETech_Rare', False, [HYP, MAL, TED, TOR]),
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_ETech_Rare', False, [HYP, MAL, TED, TOR]),

            # Manufacturer must exist to touch these pools
            ('/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Monastery', True, [HYP, JAK]),
            ]),
        (SM, [
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Common', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Uncommon', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Rare', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_VeryRare', False, [DAL, HYP, TED, MAL]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_ETech_Rare', False, [DAL, HYP, MAL, TED]),
            ('/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_ETech_VeryRare', False, [DAL, HYP, MAL, TED]),
            ]),
        (SR, [
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Common', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Uncommon', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Rare', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_VeryRare', False, [MAL, DAL, HYP, JAK, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_ETech_Rare', False, [DAL, HYP, MAL, VLA]),
            ('/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_ETech_VeryRare', False, [DAL, HYP, MAL, VLA]),
            ]),
        ]

# Make a struct to let us know easily which manufacturers make which types
type_to_manufacturer = {}
for (guntype, pools) in type_pools:
    type_to_manufacturer[guntype] = set()
    for (pool, must_exist, manufacturers) in pools:
        for manufacturer in manufacturers:
            type_to_manufacturer[guntype].add(manufacturer)

# Now loop through and make a mod for each manufacturer
for (man, man_label) in eng_manufacturers.items():

    man_file_label = man_label.lower()
    man_filename = 'manufacturer_lock_{}.txt'.format(man_file_label)

    mod = Mod(man_filename,
            'Manufacturer Lock: {}'.format(man_label),
            [
                "Restricts drops for (mostly) all relevant non-legendary/unique weapon pools so",
                "that *only* {} weapons will drop from that pool.  Will not touch any pools".format(man_label),
                "in which that manufacturer doesn't show up.  There are various corner cases",
                "where you'll still see non-{} spawns, in situations where a drop pool is".format(man_label),
                "tightly restricted to a particular manufacturer.",
                "",
                "Note that this *only* touches weapon type pools which {} actually".format(man_label),
                "produces.  For other weapon types, you'll still see the full range of",
                "available manufacturers.",
            ],
            'Lock{}'.format(man_label),
            )

    for (guntype, pools) in type_pools:
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

    mod.close()
    print('Generated {}'.format(man_filename))
