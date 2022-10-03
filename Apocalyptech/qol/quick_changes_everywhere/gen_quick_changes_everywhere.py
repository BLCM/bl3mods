#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021-2022 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('quick_changes_everywhere.bl3hotfix',
        'Quick Changes Everywhere',
        'Apocalyptech and CZ47',
        [
            "Introduces a Quick Change station to every level in the game which",
            "which didn't already have one.",
            "",
            "Requires either OpenHotfixLoader or B3HM v1.0.2 (or higher), and is",
            "incompatible with any other mod which adds Quick Change stations to",
            "the same levels!",
            "",
            "Slaughter / Trials Quick Change locations graciously donated by CZ47.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol, maps',
        quiet_streaming=True,
        ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/qol/quick_changes_everywhere/trashlantis.png',
        )

mod.header('Injecting Quick Change stations')

# Coordinates specified here were taken from apple1417's BL3TP unaltered, and are at
# Siren model height, wherever that is.  They need to be lowered a little bit to
# touch the ground, so there's some automatic adjustment being done below.
for label, map_path, coords, rotation in sorted([
        ("Ascension Bluff",
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_P',
            (51353, -34110, 13371), (0, 95, 0)),
        ("Devil's Razor (Boomtown)",
            '/Game/Maps/Zone_3/Desert/Desert_P',
            (27212, 19244, 5168), (0, -70, 0)),
        ("Devil's Razor (Roland's Rest)",
            '/Game/Maps/Zone_3/Desert/Desert_P',
            (-10083, -33141, 5496), (0, 150, 0)),
        ("Splinterlands (Homestead)",
            '/Game/Maps/Zone_3/Motorcade/Motorcade_P',
            (52962, 53868, -1146), (0, 160, 0)),
        ("Splinterlands (Chop Shop)",
            '/Game/Maps/Zone_3/Motorcade/Motorcade_P',
            (-59342, 81929, -2834), (0, 35, 0)),
        ("Carnivora",
            '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_P',
            (-26671, 63246, 221), (0, -30, 0)),
        ("Guts of Carnivora",
            '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_P',
            (-1240, -16422, 1099), (0, 89, 0)),
        ("Konrad's Hold",
            '/Game/Maps/Zone_3/Mine/Mine_P',
            (-6326, 10626, 1648), (0, -45, 0)),
        # Lying in a heap off to the side; I actually really like this placement,
        # but the quickchange model doesn't have a bottom, so you can see "into"
        # it from this angle.
        #("Sandblast Scar",
        #    '/Game/Maps/Zone_3/Convoy/Convoy_P',
        #    (-84007, 19458, -2324), (60, -20, 10)),
        ("Sandblast Scar",
            '/Game/Maps/Zone_3/Convoy/Convoy_P',
            (-87518, 12799, -1738), (0, 45, 0)),
        ("Cathedral of the Twin Gods",
            '/Game/Maps/Zone_3/DesertVault/Desertvault_P',
            (26162, 8369, 7975), (0, 45, 0)),
        ("The Great Vault",
            '/Game/Maps/Zone_3/DesertBoss/DesertBoss_P',
            (-40885, -56377, 1175), (0, 90, 0)),
        ("Destroyer's Rift",
            '/Game/Maps/Zone_0/FinalBoss/FinalBoss_P',
            (14009, -4606, 6366), (0, 90, 0)),
        ("Karass Canyon",
            '/Ixora2/Maps/Mystery/Pandora/PandoraMystery_p',
            (-14380, -20705, 195), (0, 120, 0)),
        ("Athenas",
            '/Game/Maps/Zone_1/Monastery/Monastery_P',
            (-45435, -88078, 7245), (0, -40, 0)),
        ("Meridian Outskirts",
            '/Game/Maps/Zone_1/Outskirts/Outskirts_P',
            (-71692, -49249, 1491), (0, 20, 0)),
        ("Meridian Metroplex",
            '/Game/Maps/Zone_1/City/City_P',
            (-32527, -28797, 5089), (0, 0, 0)),
        ("Lectra City (entrance)",
            '/Game/Maps/Zone_1/Towers/Towers_P',
            (17768, 12164, 2243), (0, 45, 0)),
        ("Lectra City (Moxxi's Bar)",
            '/Game/Maps/Zone_1/Towers/Towers_P',
            (-9872, -15397, 2770), (0, -135, 0)),
        ("Skywell-27 (entrance)",
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P',
            (-29257, 50791, -50279), (0, 90, 0)),
        ("Skywell-27 (lower level)",
            '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P',
            (-5514, 22316, -70720), (0, 80, 0)),
        ("Atlas HQ (Rhys's Office)",
            '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_P',
            (-10190, 2136, 31791), (0, -90, 0)),
        ("Neon Arterial (Transit Station)",
            '/Game/Maps/Zone_1/CityVault/CityVault_P',
            (70257, 23414, 1064), (0, 180, 0)),
        ("The Forgotten Basilica",
            '/Game/Maps/Zone_1/CityBoss/CityBoss_P',
            (-11026, -60891, 3515), (0, 150, 0)),
        ("Eschaton Row",
            '/Ixora2/Maps/Noir/Noir_P',
            (-4872, 1247, -10), (0, 0, 0)),
        ("Floodmoor Basin (Knotty Peak)",
            '/Game/Maps/Zone_2/Wetlands/Wetlands_P',
            (18390, 17251, 14188), (0, -90, 0)),
        ("Floodmoor Basin (Reliance)",
            '/Game/Maps/Zone_2/Wetlands/Wetlands_P',
            (-30707, -9715, 7217), (0, -150, 0)),
        ("The Anvil",
            '/Game/Maps/Zone_2/Prison/Prison_P',
            (-42336, 14983, 8040), (0, 145, 0)),
        ("Jakobs Estate",
            '/Game/Maps/Zone_2/Mansion/Mansion_P',
            (-35567, 8914, -140), (0, -70, 0)),
        ("Voracious Canopy",
            '/Game/Maps/Zone_2/Watership/Watership_P',
            (-38600, -49562, 2228), (0, 40, 0)),
        ("Ambermire (entrance)",
            '/Game/Maps/Zone_2/MarshFields/MarshFields_P',
            (33166, 34369, 2806), (0, -10, 0)),
        ("Ambermire (Rogue's Hollow)",
            '/Game/Maps/Zone_2/MarshFields/MarshFields_P',
            (6505, -3832, 2841), (0, -60, 0)),
        ("Blackbarrel Cellars",
            '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_P',
            (-66499, -35265, 3207), (0, -90, 0)),
        ("The Floating Tomb",
            '/Game/Maps/Zone_2/WetlandsBoss/WetlandsBoss_P',
            (-3277, -5840, 7044), (0, 90, 0)),
        ("Enoch's Grove",
            '/Ixora2/Maps/Cabin/Cabin_P',
            (9143, 22183, 44), (0, -5, 0)),
        ("Desolation's Edge (Typhon's Hideout)",
            '/Game/Maps/Zone_4/Desolate/Desolate_P',
            (15172, 12133, -1394), (0, -10, 0)),
        ("Tazendeer Ruins",
            '/Game/Maps/Zone_4/Beach/Beach_P',
            (89117, -37811, 4401), (0, 180, 0)),
        ("Pyre of Stars",
            '/Game/Maps/Zone_4/Crypt/Crypt_P',
            (-18154, 663, 549), (0, -90, 0)),
        ("Scryer's Crypt",
            '/Ixora2/Maps/Mystery/Nekro/NekroMystery_p',
            (39905, 20839, -2748), (0, -150, 0)),
        ("Villa Ultraviolet",
            '/Game/PatchDLC/Event2/Maps/Cartels_P',
            (-31176, -1295, 1058), (0, 90, 0)),
        ("The Heck Hole",
            '/Game/PatchDLC/BloodyHarvest/Maps/Seasons/BloodyHarvest/BloodyHarvest_P',
            (19106, 12244, 1215), (0, 0, 0)),
        ("Grand Opening",
            '/Dandelion/Maps/CasinoIntro/CasinoIntro_P',
            (-1498, 2034, 391), (0, 0, 0)),
        ("The Spendopticon (Casa de Timothy)",
            '/Dandelion/Maps/Strip/Strip_P',
            (2385, -21365, 3891), (0, 180, 0)),
        ("Impound Deluxe (entrance)",
            '/Dandelion/Maps/Impound/Impound_P',
            (1794, 4854, 391), (0, 180, 0)),
        ("Impound Deluxe (Beggar's Berth)",
            '/Dandelion/Maps/Impound/Impound_P',
            (41034, -11670, -4909), (0, -90, 0)),
        ("The Compactor",
            '/Dandelion/Maps/Trashtown/Trashtown_P',
            (22567, -4416, 2170), (-30, 130, -10)),
        ("Jack's Secret",
            '/Dandelion/Maps/Core/Core_P',
            (9534, 55993, 27391), (0, 135, 0)),
        ("VIP Tower",
            '/Dandelion/Maps/TowerLair/TowerLair_P',
            (1697, -35313, -3878), (0, 135, 0)),
        ("Skittermaw Basin (Gondola)",
            '/Hibiscus/Maps/Lake/Lake_P',
            (-3133, -5080, 8962), (0, 180, 0)),
        ("Skittermaw Basin (Clan Amourette)",
            '/Hibiscus/Maps/Lake/Lake_P',
            (7019, 87582, 6763), (0, 150, 0)),
        ("Cursehaven (Lantern's Hook)",
            '/Hibiscus/Maps/Village/Village_P',
            (118166, 22225, 735), (0, -15, 0)),
        ("Dustbound Archives",
            '/Hibiscus/Maps/Archive/Archive_P',
            (-10130, -13088, 190), (0, 180, 0)),
        ("Cankerwood",
            '/Hibiscus/Maps/Woods/Woods_P',
            (-19591, 29431, -1070), (0, 15, 0)),
        ("Negul Neshai",
            '/Hibiscus/Maps/Camp/Camp_P',
            (6100, 47040, 5555), (0, -30, 0)),
        ("Heart's Desire (What Beats Beneath)",
            '/Hibiscus/Maps/Venue/Venue_P',
            (1428, 24707, 792), (0, 120, 0)),
        ("Ashfall Peaks (entrance)",
            '/Geranium/Maps/Lodge/Lodge_P',
            (31855, -36277, 2688), (0, -150, 0)),
        ("Ashfall Peaks (Caldera Stronghold)",
            '/Geranium/Maps/Lodge/Lodge_P',
            (-15370, 4685, 9315), (0, -90, 0)),
        ("The Blastplains (Pump & Charge)",
            '/Geranium/Maps/Frontier/Frontier_P',
            (-27980, 18329, 8841), (0, 90, 0)),
        ("Obsidian Forest (Crone's Contentment)",
            '/Geranium/Maps/Forest/Forest_P',
            (-12074, -1358, 1501), (0, 150, 0)),
        ("Bloodsun Canyon (entrance)",
            '/Geranium/Maps/Facility/Facility_P',
            (-64573, 8454, 9372), (0, 40, 0)),
        ("Bloodsun Canyon (Presentation Room)",
            '/Geranium/Maps/Facility/Facility_P',
            (11231, -186, -585), (0, 110, 0)),
        ("Crater's Edge",
            '/Geranium/Maps/CraterBoss/CraterBoss_P',
            (12395, -15398, 3625), (0, -170, -5)),
        ("Castle Crimson",
            '/Alisma/Maps/Anger/Anger_P',
            (-967, -2313, 540), (0, -90, 0)),
        ("Sapphire's Run",
            '/Alisma/Maps/Chase/Chase_P',
            (-1500, -2583, 290), (0, 90, 0)),
        ("Benediction of Pain",
            '/Alisma/Maps/Experiment/Experiment_P',
            (6247, 31444, -488), (0, 60, 0)),
        ("Vaulthalla",
            '/Alisma/Maps/Eldorado/Eldorado_P',
            (-3760, -817, 4326), (-15, 140, 3)),

        # Trials/Slaughters, courtesy CZ47
        ("Slaughterstar 3000",
            '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_P',
            (-6080, -7570, 490), (0, 82, 0)),
        ("The Slaughter Shaft",
            '/Game/Maps/Slaughters/COVSlaughter/COVSlaughter_P',
            (-2270, -5420, 900), (0, 90, 0)),
        ("Cistern of Slaughter",
            '/Game/Maps/Slaughters/CreatureSlaughter/CreatureSlaughter_P',
            (-5400, 1032, 1473), (0, 180, 0)),
        ("Wayward Tether (Instinct)",
            '/Game/Maps/ProvingGrounds/Trial8/ProvingGrounds_Trial8_P',
            (130225, -9200, -12297), (0, 0, 0)),
        ("The Skydrowned Pulpit (Fervor)",
            '/Game/Maps/ProvingGrounds/Trial4/ProvingGrounds_Trial4_P',
            (-11100, 17000, 6089), (0, -135, 0)),
        ("Precipice Anchor (Discipline)",
            '/Game/Maps/ProvingGrounds/Trial7/ProvingGrounds_Trial7_P',
            (1169, 10970, 8360), (0, 0, 0)),
        ("The Hall Obsidian (Supremacy)",
            '/Game/Maps/ProvingGrounds/Trial6/ProvingGrounds_Trial6_P',
            (1100, 15707, 190), (0, 0, 0)),
        ("Gradient of Dawn (Survival)",
            '/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_P',
            (74516, -49259, -8084), (0, 155, 0)),
        ("Ghostlight Beacon (Cunning)",
            '/Game/Maps/ProvingGrounds/Trial5/ProvingGrounds_Trial5_P',
            (-1465, -1523, 1233), (0, 186, 0)),

        # I suppose we may as well do Stormblind Complex too, then,
        # since we've pulled in CZ47's data.  Otherwise I'll have to list
        # the *single* exception, and that would be lame.
        ("Stormblind Complex",
            '/Ixora/Maps/FrostSite/FrostSite_P',
            (4160, -3216, 4614), (0, 150, 0)),

        ]):

    # Now the actual hotfix
    mod.comment(label)
    mod.streaming_hotfix(map_path,
            '/Game/InteractiveObjects/GameSystemMachines/QuickChange/BP_QuickChange',
            location=(coords[0], coords[1], coords[2]-90),
            rotation=rotation)
    mod.newline()

# Move some level elements out of the way to make room
mod.header('Repositioning stock level assets')

mod.comment('Sandblast Scar')
for num, new_loc, new_rot in [
        (4, (-87092, 13652, -2479), (0, 58, 0)),
        (5, (-86520, 13635, -2459), (0, 102, 0)),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Convoy_P',
            f'/Game/Maps/Zone_3/Convoy/Convoy_IntroGarage.Convoy_IntroGarage:PersistentLevel.PD_Crate_Wood_{num}.DestructibleComponent0',
            'RelativeLocation',
            '(X={},Y={},Z={})'.format(new_loc[0], new_loc[1], new_loc[2]-100),
            notify=True)
    mod.reg_hotfix(Mod.LEVEL, 'Convoy_P',
            f'/Game/Maps/Zone_3/Convoy/Convoy_IntroGarage.Convoy_IntroGarage:PersistentLevel.PD_Crate_Wood_{num}.DestructibleComponent0',
            'RelativeRotation',
            '(Pitch={},Yaw={},Roll={})'.format(*new_rot),
            notify=True)
mod.newline()

mod.comment("Desolation's Edge")
for num, new_loc, new_rot in [
        (5, (15018, 12796, -1491.951782), (0, 80, 0)),
        (6, (15195, 12387, -1491.951782), (0, -10, 0)),
        ]:
    mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
            f'/Game/Maps/Zone_4/Desolate/Desolate_Loot.Desolate_Loot:PersistentLevel.BPIO_Lootable_Locker_{num}.Mesh_Chest1',
            'RelativeLocation',
            '(X={},Y={},Z={})'.format(*new_loc),
            notify=True)
    mod.reg_hotfix(Mod.LEVEL, 'Desolate_P',
            f'/Game/Maps/Zone_4/Desolate/Desolate_Loot.Desolate_Loot:PersistentLevel.BPIO_Lootable_Locker_{num}.Mesh_Chest1',
            'RelativeRotation',
            '(Pitch={},Yaw={},Roll={})'.format(*new_rot),
            notify=True)
mod.newline()

mod.close()

