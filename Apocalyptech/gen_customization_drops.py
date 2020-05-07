#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod, BVC, BVCF, Pool

for (label, filename, rate, desc) in [
        ('None', 'none', 0, [
            "This removes the customization drops entirely from the standard enemy drop pools.",
            "It doesn't tough badass/miniboss/boss drops at all, or any specific customization",
            "drop that might exist for a particular enemy.  It's mostly just for if you've",
            "already got all the customizations and don't want them cluttering up your Lost",
            "Loot machine.",
            ]),
        ('Improved', 'improved', 0.03, [
            "This improves the customization drop rate from 0.5% to 3%, on 'standard' enemy",
            "drops only.  Basdass/miniboss/boss drops haven't been touched, nor have any",
            "specific customization drop that a particular enemy might have.",
            ]),
        ('Frequent', 'frequent', 0.06, [
            "This improves the customization drop rate from 0.5% to 6%, on 'standard' enemy",
            "drops only.  Basdass/miniboss/boss drops haven't been touched, nor have any",
            "specific customization drop that a particular enemy might have.",
            ]),
        ('Constant', 'constant', 0.12, [
            "This improves the customization drop rate from 0.5% to 12%, on 'standard' enemy",
            "drops only.  Basdass/miniboss/boss drops haven't been touched, nor have any",
            "specific customization drop that a particular enemy might have.",
            "",
            "This will seriously interfere with your Lost Loot machine, so only really",
            "recommended if you're chasing down those last few customizations.",
            ]),
        ]:

    full_filename = 'customization_drops_{}.txt'.format(filename)

    mod = Mod(full_filename,
            'Standard Enemy Customization Drop Rate: {}'.format(label),
            desc,
            )

    mod.header('Set cosmetics chance to {}'.format(rate))
    for (pool, chars) in [
            ('/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear', [
                'BPChar_Ape',
                'BPChar_EnforcerShared',
                'BPChar_Frontrunner',
                'BPChar_Goon',
                'BPChar_GuardianShared',
                'BPChar_Heavy_Shared',
                'BPChar_Nekrobug_Shared',
                'BPChar_Nog',
                'BPChar_OversphereShared',
                'BPChar_PsychoShared',
                'BPChar_PunkShared',
                'BPChar_Rakk',
                'BPChar_Ratch',
                'BPChar_Saurian_Shared',
                'BPChar_ServiceBot',
                'BPChar_SkagShared',
                'BPChar_Spiderant',
                'BPChar_Tink',
                'BPChar_Tink_Turret',
                'BPChar_Trooper',
                'BPChar_VarkidShared',
                'BPChar_LootTracker',

                # Maliwan Takedown
                'BPChar_MechBasicMini',
                'BPChar_MechMeleeMini',

                # Moxxi's Heist
                'BPChar_EnforcerShared_Stripped',
                'BPChar_Goon_Stripped',
                'BPChar_PsychoShared_Stripped',
                'BPChar_PunkShared_Stripped',
                'BPChar_TinkStripped',
                ]),

            # Dandelion standard-enemy drop list
            ('/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Dandelion', [
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

            # Dandelion standard-loader drop list
            ('/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_StandardEnemyGunsandGearLoader', [
                # Moxxi's Heist
                'BPChar_HyperionTurretBasic',
                'BPChar_LoaderShared',
                'BPChar_WeeLoaderBasic',
                ]),
            ]:

        for char in chars:

            # Default is 0.5%.
            mod.reg_hotfix(Mod.CHAR, char,
                    pool,
                    'ItemPools[9].PoolProbability',
                    BVCF(bvc=rate))

    mod.newline()

    mod.close()
    print('Wrote {}'.format(full_filename))
