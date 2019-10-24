#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

def set_pool(mod, pool_to_set, balances):

    parts = []
    for (bal, weight) in balances:
        part = '(InventoryBalanceData={},ResolvedInventoryBalanceData=InventoryBalanceData\'"{}"\',Weight=(BaseValueConstant={}))'.format(
                bal, bal,
                round(weight, 6),
                )
        parts.append(part)
    mod.reg_hotfix(Mod.PATCH, '',
            pool_to_set,
            'BalancedItems',
            '({})'.format(','.join(parts)))

mod = Mod('expanded_legendary_pools.txt',
        'Expanded Legendary Pools',
        [
            'Adds all uniques and stuff (minus a few exceptions) into the legendary drop pools,',
            'at a reduced rate compared to the legendaries already in there.',
            ],
        'Pools',
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

addition_scale = 0.6
pools = [
        ('ARs', '/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary.ItemPool_AssaultRifles_Legendary',
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

        ('Heavy Weapons', '/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary.ItemPool_Heavy_Legendary',
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

        ('Pistols', '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary.ItemPool_Pistols_Legendary',
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
                # Echo
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo.Balance_PS_TOR_Echo', 1),
                # Devils Foursum
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM.Balance_PS_TOR_4SUM', 1),
                # Roisen's Thorns
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns.Balance_PS_TOR_RoisensThorns', 1),
                # Infinity
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti.Balance_PS_VLA_Infiniti', 1),
                # Magnificent
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent', 1),

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
                # Heckle
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle', 1*addition_scale),
                # Hyde
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde', 1*addition_scale),
                # Girth Blaster Elite (joke weapon)
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf.Balance_PS_TOR_Nurf', 0.2*addition_scale),
                # Occultist
                ('/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy.Balance_PS_TOR_Troy', 1*addition_scale),
                # Bone Shredder
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder.Balance_PS_VLA_BoneShredder', 1*addition_scale),
                # The Leech
                ('/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech.Balance_PS_VLA_TheLeech', 1*addition_scale),
                ]),

        ('Shotguns', '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary.ItemPool_Shotguns_Legendary',
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

        ('SMGs', '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary.ItemPool_SMGs_Legendary',
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

                ### Additions

                # Hellfire
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire.Balance_SM_DAHL_HellFire', 1*addition_scale),
                # 9-Volt
                ('/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt.Balance_SM_DAHL_NineVolt', 1*addition_scale),
                # Redistributor
                ('/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork.Balance_SM_HYP_Fork', 1*addition_scale),
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

        ('Snipers', '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary.ItemPool_SnipeRifles_Legendary',
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

        ('Shields', '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary.ItemPool_Shields_05_Legendary',
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

        ('Grenades', '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary.ItemPool_GrenadeMods_05_Legendary',
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
    ]

for (label, pool, balances) in pools:
    mod.comment(label)
    set_pool(mod, pool, balances)
    mod.newline()

mod.close()


