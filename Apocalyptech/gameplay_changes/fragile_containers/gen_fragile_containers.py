#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2023 Christopher J. Kucera
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

import os
import sys
import argparse
import multiprocessing
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC, LVL_TO_ENG_LOWER

# Regarding BPIO_Lootable_Eridian_WhiteChestCrystal objects:
#
# No clue how to get those to be shoot-to-open.  They spawn in differently than
# everything else, along with the eridium crystal clusters -- via some spawner
# objects which randomize things up a bit and have parameters for the max number
# to spawn in the level at any one time, etc.  So we generally don't find them
# hardcoded in levels, with very few exceptions, so our main processing chunk
# down there won't ever find them.  They do seem to spawn in under LevelName_P,
# like streaming-hotfix-added chests, so I'd thought that maybe I *could* alter
# their `Default__` attrs to make the change, but that doesn't work.  I also
# tried putting in my *own* streaming-hotfix chest, to make sure the object was
# loaded, and that *did* result in an extra chest in the level, but even then
# the `Default__` method was for naught.  I'd also tried just assuming I knew the
# exact object name; like in OrbitalPlatform_P you end up with:
#
#   /Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P.OrbitalPlatform_P:PersistentLevel.BPIO_Lootable_Eridian_WhiteChestCrystal_C_0
#   /Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P.OrbitalPlatform_P:PersistentLevel.BPIO_Lootable_Eridian_WhiteChestCrystal_C_1
#
# ... but hardcoding those objects didn't actually change the attr either.  So,
# whatever, those will just have to be an exception.
#
# I believe the same is true for Typhon Dead Drops as well, though I investigated
# those even less.  Also the bank of strongboxes in the intro lobby in Atlas HQ!
# Though *some* of those lobby boxes *do* seem to work.  Go figure.
#
# There's also an OakSpawner for white chests in Atlas HQ (see export 777 in
# AtlasHQ_FoyerLobby) which creates a white chest or two which, similarly, is
# like that.
#
# Also also: chests in Slaughter arenas.

parser = argparse.ArgumentParser(
        description='Mod-generation script for Fragile Containers',
        epilog="""
            This mod-generation script ends up serializing basically every single
            map object in the game (minus whichever stragglers JWP still can't
            serialize).  That ends up eating up a fair bit of space (8GBish)
            which you may not want to keep around, so there's a couple of
            auto-cleaning options available.  -c/--clean will delete all existing
            map-object serializations without generating the mod at all, whereas
            -w/--while-clean will remove the serializations one-by-one as the
            mod processes.  With no arguments specified, the app will leave all
            the serializations on-disk.

            The serialization process is paralellized, and by default will spawn
            as many threads as detected CPUs.  I suspect there are diminishing
            returns for that, especially with hyperthreaded CPUs; I'd personally
            recommend using -p/--process to just specify about half your CPUs
            instead.
            """
        )
parser.add_argument('-p', '--processes',
        type=int,
        help="""Number of serialization processes to run at once.  (Defaults to
            the number of CPUs detected by Python).""",
        )
clean_group = parser.add_mutually_exclusive_group()
clean_group.add_argument('-c', '--clean',
        action='store_true',
        help='Instead of generating mod, clean up level serialization JSON files',
        )
clean_group.add_argument('-w', '--while-clean',
        action='store_true',
        help='Clean up level serialization JSON files as we process them',
        )
args = parser.parse_args()

# No matter what we do, we'll want a data object
data = BL3Data()

# Magic string to use for hardcoded entries
HARDCODE = '__HARDCODE__'
type_set = {HARDCODE}

if args.clean:
    print('Skipping mod generation; just cleaning level serializations')
else:

    # Start the mod
    mod = Mod('fragile_containers.bl3hotfix',
            'Fragile Containers',
            'Apocalyptech',
            [
                "Makes the majority of containers in the game openable by taking damage",
                "from any source -- guns, grenades, barrel explosions, etc.  There are",
                "a handful of exceptions throughout the game.  See the README for those!",
            ],
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.0.0',
            cats='chests, qol',
            ss='https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/gameplay_changes/fragile_containers/simpsons-homer.gif',
            )

    # Initial list found via:
    #   find $(find . -name Lootables) -name "BPIO*.uasset" -o -name "IO*.uasset"  | cut -d. -f2 | sort -i
    #
    # ... and then pruned by hand a bit.  Also added in a few extras by hand, which weren't found under
    # a "Lootables" dir:
    #   * BPIO_Lootable_TimedBomb_AmmoCrate
    #   * IO_EP04_Lootable_Industrial_Dumpster
    #mod.header('Defaults for spawned-in Containers')
    for obj_name in [
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_AmmoCase',
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_LootCase',
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_PortaPotty',
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_PortaPottyPoor',
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_RedChest',
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_SingleBox',
            '/Alisma/Lootables/_Design/Classes/Hyperion/BPIO_Ali_Lootable_Hyperion_WeaponBox',
            #'/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_BlackJackChest',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_AmmoCase',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_LootCase',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_PortaPotty',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_PortaPottyPoor',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_RedChest',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_SingleBox',
            #'/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_SlotMachine',
            '/Dandelion/Lootables/_Design/Classes/Hyperion/BPIO_Lootable_Hyperion_WeaponBox',
            '/Dandelion/Missions/Plot/Ep04_Trashtown/IO_EP04_Lootable_Industrial_Dumpster',
            '/Game/Lootables/_Design/Classes/Atlas/BPIO_Lootable_Atlas_RedChest',
            '/Game/Lootables/_Design/Classes/Atlas/BPIO_Lootable_Crate_Ammo_Atlas',
            '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_AmmoCrate',
            '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_AmmoCrate_Slaughter',
            #'/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_CardboardBox',
            '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_OfferingBox',
            '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_RedCrate',
            '/Game/Lootables/_Design/Classes/CoV/BPIO_Lootable_COV_RedCrate_Slaughter',
            #'/Game/Lootables/_Design/Classes/Eden6/BPIO_Lootable_SaurianCluster',
            '/Game/Lootables/_Design/Classes/Eridian/BPIO_Lootable_Eridian_AmmoCrate',
            '/Game/Lootables/_Design/Classes/Eridian/BPIO_Lootable_Eridian_RedChest',
            '/Game/Lootables/_Design/Classes/Eridian/BPIO_Lootable_Eridian_WhiteChest',
            '/Game/Lootables/_Design/Classes/Eridian/BPIO_Lootable_Eridian_WhiteChestCrystal',
            #'/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_BonePile',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_DeadDropChest',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_Global_AmmoCrate',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_Global_WhiteCrate',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_Locker',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_Mailbox',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_TrashCan',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_TrialsChest',
            '/Game/Lootables/_Design/Classes/Global/BPIO_Lootable_Typhon_DeadDrop',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_CashRegister',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_CarTrunk',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_Dumpster',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_Lockbox',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_PortaPotty',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_Refrigerator',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_Safe',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_Industrial_StrongBox',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_IndustrialToilet',
            #'/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_TrashPile',
            '/Game/Lootables/_Design/Classes/Industrial/BPIO_Lootable_WashingMachine',
            '/Game/Lootables/_Design/Classes/Jakobs/BPIO_Lootable_Jakobs_GunRack',
            '/Game/Lootables/_Design/Classes/Jakobs/BPIO_Lootable_Jakobs_Lockbox',
            '/Game/Lootables/_Design/Classes/Jakobs/BPIO_Lootable_Jakobs_MusicBox',
            '/Game/Lootables/_Design/Classes/Jakobs/BPIO_Lootable_Jakobs_RedChest',
            '/Game/Lootables/_Design/Classes/Jakobs/BPIO_Lootable_Jakobs_WhiteChest',
            '/Game/Lootables/_Design/Classes/Maliwan/BPIO_Lootable_Maliwan_AmmoCrate',
            '/Game/Lootables/_Design/Classes/Maliwan/BPIO_Lootable_Maliwan_AmmoCrate_Slaughter',
            '/Game/Lootables/_Design/Classes/Maliwan/BPIO_Lootable_Maliwan_RedChest',
            '/Game/Lootables/_Design/Classes/Maliwan/BPIO_Lootable_Maliwan_RedChest_Slaughter',
            '/Game/Lootables/_Design/Classes/Maliwan/BPIO_Lootable_Maliwan_WhiteChest',
            '/Game/Lootables/_Design/Classes/MissionSpecific/BPIO_Lootable_Global_MedicalCrate',
            '/Game/Lootables/_Design/Classes/MissionSpecific/BPIO_Lootable_Monastery_Rock',
            #'/Game/Lootables/_Design/Classes/Pandora/BPIO_Lootable_VarkidPile',
            '/Game/Lootables/_Design/Classes/Promethea/BPIO_Lootable_Cooler',
            '/Game/Lootables/_Design/Classes/Promethea/BPIO_Lootable_Gashapon',
            #'/Game/Lootables/_Design/Classes/Promethea/BPIO_Lootable_RatchPile',
            #'/Game/Lootables/_Design/Classes/Promethea/BPIO_Lootable_RatchPile_Small',
            '/Game/Lootables/_Design/Classes/Promethea/BPIO_Lootable_Spewer',
            #'/Game/Lootables/_Design/Classes/Sanctuary/BPIO_Lootable_Global_GoldenKey',
            #'/Game/Lootables/_Design/Shared/BPIO_Lootable',
            #'/Game/Lootables/_Design/Shared/BPIO_LootableDamageable',
            #'/Game/Lootables/_Design/Shared/BPIO_Lootable_Pile',
            '/Game/Lootables/_Design/Shared/BPIO_Lootable_RedChest',
            #'/Game/Lootables/_Design/Shared/BPIO_LootableWithSurpriseEnemy',
            '/Game/MapSpecific/Motorcade/CarnivoraInterior/Arena/BPIO_Lootable_TimedBomb_AmmoCrate',
            '/Game/Missions/Plot/EP01_ChildrenOfTheVault/BPIO_Lootable_COV_RedCrate_Ep01_Shields',
            '/Game/PatchDLC/BloodyHarvest/Lootables/_Design/Classes/BloodyHarvest/BPIO_Lootable_BloodyHarvest',
            #'/Game/PatchDLC/Event2/Lootables/_Design/BPIO_Lootable_EridiumDustPile',
            '/Game/PatchDLC/Event2/Lootables/_Design/BPIO_Lootable_IndustrialToilet_Cartels',
            '/Game/PatchDLC/Event2/Lootables/_Design/BPIO_Lootable_Jakobs_GunRack_Cartels',
            '/Game/PatchDLC/Event2/Lootables/_Design/BPIO_Lootable_Jakobs_GunRack_Cartels_NonMission',
            '/Game/PatchDLC/Event2/Lootables/_Design/BPIO_Lootable_Jakobs_WhiteChest_Cartels',
            '/Game/PatchDLC/Ixora/Lootables/_Design/BPIO_Lootable_AmmoCrate_GearUp',
            '/Game/PatchDLC/Ixora/Lootables/_Design/BPIO_Lootable_RedCrate_Airdrop_GearUp',
            '/Game/PatchDLC/Ixora/Lootables/_Design/BPIO_Lootable_RedCrate_GearUp',
            '/Game/PatchDLC/Ixora/Lootables/_Design/BPIO_Lootable_RedCrate_World_GearUp',
            '/Game/PatchDLC/Ixora/Lootables/_Design/BPIO_Lootable_WhiteCrate_GearUp',
            '/Game/PatchDLC/Ixora/Lootables/_Design/BPIO_Lootable_WhiteCrate_GearUp_StarterChest',
            #'/Geranium/Lootables/_Design/Classes/BPIO_Lootable_BiobeastBonepile',
            '/Geranium/Lootables/_Design/Classes/BPIO_Lootable_CashRegister_Ger',
            '/Geranium/Lootables/_Design/Classes/BPIO_Lootable_Industrial_Outhouse',
            '/Geranium/Lootables/_Design/Classes/BPIO_Lootable_Jakobs_Lockbox_GER',
            '/Geranium/Lootables/_Design/Classes/BPIO_Lootable_Jakobs_MoneyBack',
            '/Geranium/Lootables/_Design/Classes/JakobsJournalChest/BPIO_Lootable_JakobsJournal_DeadDrop',
            '/Geranium/Lootables/_Design/Classes/TreasureMapChest/BPIO_Lootable_TreasureMap_DeadDrop',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/Cultists/BPIO_Hib_Lootable_Cultist_AmmoCrate',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/Cultists/BPIO_Hib_Lootable_Cultist_RedChest',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/Cultists/BPIO_Hib_Lootable_Cultist_WhiteChest',
            # Portal chests *do* activate properly when shot, but they don't actually spawn loot properly.
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/Cultists/BPIO_Hib_Lootable_PortalChest',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/FrostBiters/BPIO_Hib_Lootable_FrostBiters_AmmoCrate',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/FrostBiters/BPIO_Hib_Lootable_FrostBiters_RedChest',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/FrostBiters/BPIO_Hib_Lootable_FrostBiters_Treasure',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/FrostBiters/BPIO_Hib_Lootable_FrostBiters_WhiteChest',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_BonePile',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_Carcass',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_FishNet',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_MonsterPile',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_Mush',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_Pimple',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_Pimple2',
            #'/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_SingingAnimal',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_SlugShell',
            '/Hibiscus/InteractiveObjects/Lootables/_Design/Classes/_Global/BPIO_Hib_Lootable_TentacleToilet',
            ]:

        obj_data = data.get_data(obj_name)
        obj_last = obj_name.rsplit('/', 1)[-1]
        obj_c = f'{obj_last}_C'
        found_default = False
        for export in obj_data:
            if export['export_type'] == obj_c:
                found_default = True
                if 'bOpenInResponseToDamage' not in export or export['bOpenInResponseToDamage'] == False:

                    # I'd orginally tried to just set the `Default__` attrs here, but it just
                    # doesn't work -- the attributes on the in-level objects don't change.  So,
                    # we're skipping the `Default__` attempt, but we *do* want to create a set
                    # here anyway, so we'll do that and break.
                    type_set.add(obj_c)
                    break

                    #if 'DamagedOpeningInteractions' in export:
                    #    print(f'wtf: {obj_name}')
                    default_name = export['_jwp_object_name']
                    full_obj = f'{obj_name}.{default_name}'
                    for hf_type in [Mod.EARLYLEVEL, Mod.LEVEL]:
                        for notify in [True, False]:
                            mod.reg_hotfix(hf_type, 'MatchAll',
                                    full_obj,
                                    'bOpenInResponseToDamage',
                                    'True',
                                    notify=notify)
                break

        if not found_default:
            print(f'WARNING: Did not find default for {obj_name}')

    mod.newline()

# There are a couple of objects that we'd ordinarily skip which I'm hardcoding.
hardcodes = {
        'Prison_P': {
            # Tina's "sauce" cardboard boxes during Hammerlocked
            'Prison_M_EP08PrisonBreak': [
                'BPIO_Lootable_COV_CardboardBox_1903',
                'BPIO_Lootable_COV_CardboardBox_2642',
                'BPIO_Lootable_COV_CardboardBox_968',
                ],
            },
        'Venue_P': {
            # Boxes which between them contain an antler, to open a passageway
            'Venue_Plot_M': [
                'MISSIONLOOT_DONOTDELETEORDUPLICATE_FirstObject',
                'MISSIONLOOT_DONOTDELETEORDUPLICATE_SecondObject',
                'MISSIONLOOT_DONOTDELETEORDUPLICATE_ThirdObject',
                ],
            },
        }

# transform our hardcodes to a format easier for the code, later.
for main_level, sublevels in hardcodes.items():
    for sublevel, objects in sublevels.items():
        hardcodes[main_level][sublevel] = [{'export_type': HARDCODE, '_jwp_object_name': name} for name in objects]


class MapResult:

    def __init__(self, name, header):
        self.name = name
        self.header = header
        self.statements = []
        self.cleaned = 0

    def append(self, *args):
        self.statements.append(args)

    def __iter__(self):
        return iter(self.statements)

    def __len__(self):
        return len(self.statements)

    def __bool__(self):
        return len(self.statements) > 0


def process_map(map_name, header, level_short, args, data, type_set, hardcodes):
    map_last = map_name.rsplit('/', 1)[-1]
    result = MapResult(map_last, header)
    if not args.clean:
        print(f'Processing: {map_name}')
        map_data = data.get_data(map_name)
        if map_data:
            if level_short in hardcodes and map_last in hardcodes[level_short]:
                map_data.extend(hardcodes[level_short][map_last])
            for export in map_data:
                if export['export_type'] in type_set:
                    obj_name = export['_jwp_object_name']
                    result.append(Mod.LEVEL, level_short,
                            f'{map_name}.{map_last}:PersistentLevel.{obj_name}',
                            'bOpenInResponseToDamage',
                            'True',
                            )

    if args.clean or args.while_clean:
        # Kind of abusing the BL3Data object here, I suppose; finding the "real" path
        # to the JSON should probably be API'd
        json_file = os.path.join(data.data_dir, f'{map_name[1:]}.json')
        if os.path.exists(json_file):
            os.unlink(json_file)
            result.cleaned += 1

    return result


# Now loop through all levels and create a queue of sub-map-objects to process
map_objects = []
for level_orig in [
        '/Alisma/Maps/Anger/Anger_P',
        '/Alisma/Maps/Chase/Chase_P',
        '/Alisma/Maps/Eldorado/Eldorado_P',
        '/Alisma/Maps/Experiment/Experiment_P',
        '/Alisma/Maps/Sanctum/Sanctum_P',
        '/Dandelion/Maps/CasinoIntro/CasinoIntro_P',
        '/Dandelion/Maps/Core/Core_P',
        '/Dandelion/Maps/Impound/Impound_P',
        '/Dandelion/Maps/Strip/Strip_P',
        '/Dandelion/Maps/TowerLair/TowerLair_P',
        '/Dandelion/Maps/Trashtown/Trashtown_P',
        '/Game/Maps/ProvingGrounds/Trial1/ProvingGrounds_Trial1_P',
        '/Game/Maps/ProvingGrounds/Trial4/ProvingGrounds_Trial4_P',
        '/Game/Maps/ProvingGrounds/Trial5/ProvingGrounds_Trial5_P',
        '/Game/Maps/ProvingGrounds/Trial6/ProvingGrounds_Trial6_P',
        '/Game/Maps/ProvingGrounds/Trial7/ProvingGrounds_Trial7_P',
        '/Game/Maps/ProvingGrounds/Trial8/ProvingGrounds_Trial8_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_P',
        '/Game/Maps/Slaughters/COVSlaughter/COVSlaughter_P',
        '/Game/Maps/Slaughters/CreatureSlaughter/CreatureSlaughter_P',
        '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_P',
        '/Game/Maps/Zone_0/FinalBoss/FinalBoss_P',
        '/Game/Maps/Zone_0/Prologue/Prologue_P',
        '/Game/Maps/Zone_0/Recruitment/Recruitment_P',
        '/Game/Maps/Zone_0/Sacrifice/Sacrifice_P',
        '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_P',
        '/Game/Maps/Zone_1/City/City_P',
        '/Game/Maps/Zone_1/CityBoss/CityBoss_P',
        '/Game/Maps/Zone_1/CityVault/CityVault_P',
        '/Game/Maps/Zone_1/Monastery/Monastery_P',
        '/Game/Maps/Zone_1/OrbitalPlatform/OrbitalPlatform_P',
        '/Game/Maps/Zone_1/Outskirts/Outskirts_P',
        '/Game/Maps/Zone_1/Towers/Towers_P',
        '/Game/Maps/Zone_2/Mansion/Mansion_P',
        '/Game/Maps/Zone_2/MarshFields/MarshFields_P',
        '/Game/Maps/Zone_2/Prison/Prison_P',
        '/Game/Maps/Zone_2/Watership/Watership_P',
        '/Game/Maps/Zone_2/Wetlands/Wetlands_P',
        '/Game/Maps/Zone_2/WetlandsBoss/WetlandsBoss_P',
        '/Game/Maps/Zone_2/WetlandsVault/WetlandsVault_P',
        '/Game/Maps/Zone_3/Convoy/Convoy_P',
        '/Game/Maps/Zone_3/Desert/Desert_P',
        '/Game/Maps/Zone_3/DesertBoss/DesertBoss_P',
        '/Game/Maps/Zone_3/DesertVault/Desertvault_P',
        '/Game/Maps/Zone_3/Mine/Mine_P',
        '/Game/Maps/Zone_3/Motorcade/Motorcade_P',
        '/Game/Maps/Zone_3/MotorcadeFestival/MotorcadeFestival_P',
        '/Game/Maps/Zone_3/MotorcadeInterior/MotorcadeInterior_P',
        '/Game/Maps/Zone_4/Beach/Beach_P',
        '/Game/Maps/Zone_4/Crypt/Crypt_P',
        '/Game/Maps/Zone_4/Desolate/Desolate_P',
        '/Game/PatchDLC/BloodyHarvest/Maps/Seasons/BloodyHarvest/BloodyHarvest_P',
        '/Game/PatchDLC/Event2/Maps/Cartels_P',
        '/Game/PatchDLC/Raid1/Maps/Raid/Raid_P',
        '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_P',
        '/Geranium/Maps/CraterBoss/CraterBoss_P',
        '/Geranium/Maps/Facility/Facility_P',
        '/Geranium/Maps/Forest/Forest_P',
        '/Geranium/Maps/Frontier/Frontier_P',
        '/Geranium/Maps/Lodge/Lodge_P',
        '/Geranium/Maps/Town/Town_P',
        '/Hibiscus/Maps/Archive/Archive_P',
        '/Hibiscus/Maps/Bar/Bar_P',
        '/Hibiscus/Maps/Camp/Camp_P',
        '/Hibiscus/Maps/Lake/Lake_P',
        '/Hibiscus/Maps/Venue/Venue_P',
        '/Hibiscus/Maps/Village/Village_P',
        '/Hibiscus/Maps/Woods/Woods_P',
        '/Ixora/Maps/FrostSite/FrostSite_P',
        '/Ixora2/Maps/Boss/SacrificeBoss_p',
        '/Ixora2/Maps/Cabin/Cabin_P',
        '/Ixora2/Maps/Mystery/Nekro/NekroMystery_p',
        '/Ixora2/Maps/Mystery/Pandora/PandoraMystery_p',
        '/Ixora2/Maps/Noir/Noir_P',
        ]:
    level_base, level_short = level_orig.rsplit('/', 1)
    level_eng = LVL_TO_ENG_LOWER[level_short.lower()]
    header = f'{level_eng} ({level_short})'
    for map_name in sorted(data.find(level_base, ''), key=str.casefold):
        map_objects.append((map_name, header, level_short, args, data, type_set, hardcodes))

# Now loop through and do the work.  Splitting this out via multiprocessing.Pool 'cause it
# can take quite awhile when single-threaded.
cur_header = None
cleaned = 0
p = multiprocessing.Pool(processes=args.processes)
for result in p.starmap(process_map, map_objects):
    cleaned += result.cleaned
    if result:
        if result.header != cur_header:
            mod.header(result.header)
            cur_header = result.header
        mod.comment(result.name)
        for statement in result:
            mod.reg_hotfix(*statement)
        mod.newline()

if not args.clean:
    mod.close()

if args.clean or args.while_clean:
    print(f'Cleaned up {cleaned:,} level serialization files')
else:
    print('Run again with -c/--clean to remove level serializations')

