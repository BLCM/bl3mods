#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import lzma

challenges_init = [
        ('Typhon Logs', 'BP_CrewChallengeComponent_Collection'),
        ('Ellie Vehicle Theft', 'BP_CrewChallengeComponent_Hijack_Spawner'),
        ('Hammerlock Hunt', 'BP_CrewChallengeComponent_Hunt_Spawner'),
        ('Crimson Radio', 'BP_CrewChallengeComponent_Sabotage'),
        ('Claptrap Salvage', 'BP_CrewChallengeComponent_Salvage'),
        ('Zer0 Assassination', 'BP_CrewChallengeComponent_KillTarget_Spawner'),
        ('Eridian Writing?', 'BP_ChallengeComponent_IconEridian'),

        # DLC1 challenges:
        #   Mayor's Killer Look
        #   Torgue's Marketing Mistake
        #   Pieces of Résistance
        # Not totally sure what the actual associations are, though the following
        # at least makes some Torgue ones show up.  The KillTarget ones aren't
        # showing w/ initial tests, but I wonder if they don't show until you
        # meet the Mayor.  Likewise, Pieces of Résistance aren't showing, but
        # maybe they don't until you meet Ember?
        ("Mayor's Killer Look", 'BP_CrewChallengeComp_KillTarget_DLC1'),
        ("Torgue's Marketing Mistake", 'BP_CrewChallengeComp_Sabotage_DLC1'),

        # DLC2 challenges:
        #   Gaige's Gifts
        #   Hammerlock's Occult Hunt
        #   Mancubus Eldritch Statues
        ("Mancubus Eldritch Statues", 'BP_CrewChallengeComp_Mancubus_DLC2'),
        ("Hammerlock's Occult Hunt", 'BP_CrewChallengeComp_Hunt_DLC2'),
        ("Gaige's Gifts", 'BP_CrewChallengeComp_Gifts_DLC2'),

        # DLC3 challenges:
        #    Creature Feature
        #    Gehenna's Most Wanted
        #    Good Prospects
        #    Sato's Saga
        #    Skin to Win
        # ... though it looks like they might all use the exact same obj type, apart
        # from Good Prospects, which functions totally differently.
        ("DLC3 Challenges", 'BP_CrewChallengeComponent_Geranium'),
        ]

level_to_eng = {
        'AtlasHQ_P': "Atlas HQ",
        'Beach_P': "Tazendeer Ruins",
        'BloodyHarvest_P': "Heck Hole",
        'COVSlaughter_P': "Slaughter Shaft",
        'CasinoIntro_P': "Grand Opening",
        'CityBoss_P': "Forgotten Basilica",
        'CityVault_P': "Neon Arterial",
        'City_P': "Meridian Metroplex",
        'Convoy_P': "Sandblast Scar",
        'Core_P': "Jack's Secret",
        'CreatureSlaughter_P': "Cistern of Slaughter",
        'Crypt_P': "Pyre of Stars",
        'DesertBoss_P': "Great Vault",
        'Desert_P': "Devil's Razor",
        'Desertvault_P': "Cathedral of the Twin Gods",
        'Desolate_P': "Desolation's Edge",
        'FinalBoss_P': "Destroyer's Rift",
        'Impound_P': "Impound Deluxe",
        'Mansion_P': "Jakobs Estate",
        'MarshFields_P': "Ambermire",
        'Mine_P': "Konrad's Hold",
        'Monastery_P': "Athenas",
        'MotorcadeFestival_P': "Carnivora",
        'MotorcadeInterior_P': "Guts of Carnivora",
        'Motorcade_P': "Splinterlands",
        'OrbitalPlatform_P': "Skywell-27",
        'Outskirts_P': "Meridian Outskirts",
        'Prison_P': "Anvil",
        'Prologue_P': "Droughts",
        'ProvingGrounds_Trial1_P': "Gradient of Dawn (Survival)",
        'ProvingGrounds_Trial4_P': "Skydrowned Pulpit (Fervor)",
        'ProvingGrounds_Trial5_P': "Ghostlight Beacon (Cunning)",
        'ProvingGrounds_Trial6_P': "Hall Obsidian (Supremacy)",
        'ProvingGrounds_Trial7_P': "Precipice Anchor (Discipline)",
        'ProvingGrounds_Trial8_P': "Wayward Tether (Instinct)",
        'Raid_P': "Midnight's Cairn (Maliwan Takedown)",
        'Recruitment_P': "Covenant Pass",
        'Sacrifice_P': "Ascension Bluff",
        'Sanctuary3_P': "Sanctuary",
        'Strip_P': "Spendopticon",
        'TechSlaughter_P': "Slaughterstar 3000",
        'TowerLair_P': "VIP Tower",
        'Towers_P': "Lectra City",
        'Trashtown_P': "Compactor",
        'Watership_P': "Voracious Canopy",
        'WetlandsBoss_P': "Floating Tomb",
        'WetlandsVault_P': "Blackbarrel Cellars",
        'Wetlands_P': "Floodmoor Basin",

        # DLC1
        'CasinoIntro_P': "Grand Opening",
        'Core_P': "Jack's Secret",
        'Impound_P': "Impound Deluxe",
        'Strip_P': "Spendopticon",
        'TowerLair_P': "VIP Tower",
        'Trashtown_P': "Compactor",

        # DLC2
        'Archive_P': "Dustbound Archives",
        'Bar_P': "Lodge",
        'Camp_P': "Negul Neshai",
        'Lake_P': "Skittermaw Basin",
        'Venue_P': "Heart's Desire",
        'Village_P': "Cursehaven",
        'Woods_P': "Cankerwood",

        # DLC3
        'CraterBoss_P': "Crater's Edge",
        'Facility_P': "Bloodsun Canyon",
        'Forest_P': "Obsidian Forest",
        'Frontier_P': "The Blastplains",
        'Lodge_P': "Ashfall Peaks",
        'Town_P': "Vestige",
    }

num_re = re.compile('^(.*)_(\d+)$')
level_package = os.path.basename(os.getcwd())
level_name = level_to_eng[level_package]

# Compile some regex ahead of time
challenges = []
for (label, obj_type) in challenges_init:
    challenges.append((label, obj_type, re.compile(r'^.* {}_C (\S+)\.(PersistentLevel\..*)\.{}$'.format(obj_type, obj_type))))

# Figure out what directory the map lives in.  Far more data getting shoved
# in this dict that needs to be, but whatever.
map_to_full = {}
map_re = re.compile(r'^.*(\/Game\/Maps\/.*)\/([^\.\/]+)\.\2$')
dlc1_map_re = re.compile(r'^.*(\/Dandelion\/Maps\/.*)\/([^\.\/]+)\.\2$')
dlc2_map_re = re.compile(r'^.*(\/Hibiscus\/Maps\/.*)\/([^\.\/]+)\.\2$')
dlc3_map_re = re.compile(r'^.*(\/Geranium\/Maps\/.*)\/([^\.\/]+)\.\2$')
with lzma.open('UE4Tools_NamesDump.txt.xz', 'rt', encoding='latin1') as df:
    for line in df:
        match = map_re.match(line)
        if match:
            dirname = match.group(1)
            obj_name = match.group(2)
            map_to_full['{}.{}'.format(obj_name, obj_name)] = '{}/{}.{}'.format(dirname, obj_name, obj_name)
        else:
            match = dlc1_map_re.match(line)
            if match:
                dirname = match.group(1)
                obj_name = match.group(2)
                map_to_full['{}.{}'.format(obj_name, obj_name)] = '{}/{}.{}'.format(dirname, obj_name, obj_name)
            else:
                match = dlc2_map_re.match(line)
                if match:
                    dirname = match.group(1)
                    obj_name = match.group(2)
                    map_to_full['{}.{}'.format(obj_name, obj_name)] = '{}/{}.{}'.format(dirname, obj_name, obj_name)
                else:
                    match = dlc3_map_re.match(line)
                    if match:
                        dirname = match.group(1)
                        obj_name = match.group(2)
                        map_to_full['{}.{}'.format(obj_name, obj_name)] = '{}/{}.{}'.format(dirname, obj_name, obj_name)

# Now find our challenge objects
print('        ("{}", \'{}\', ['.format(level_name, level_package))
with lzma.open('UE4Tools_ObjectsDump.txt.xz', 'rt', encoding='latin1') as df:
    for line in df:
        for (label, obj_type, challenge_re) in challenges:
            match = challenge_re.match(line)
            if match:
                # I don't *think* we need these...
                if obj_type == 'BP_CrewChallengeComponent_Collection' and 'CollectionParentCrewChallenge' in line:
                    break
                level_name = match.group(1)
                rest_object = match.group(2)
                num_match = num_re.match(rest_object)
                if num_match:
                    # It *looks* like these numbers are always off by 1.  We'll find out!
                    prefix = num_match.group(1)
                    number = int(num_match.group(2))
                    obj_name = '{}:{}_{}.{}'.format(map_to_full[level_name], prefix, number-1, obj_type)
                else:
                    obj_name = '{}:{}.{}'.format(map_to_full[level_name], rest_object, obj_type)
                print("            '{}',".format(obj_name))
                break
print('            ]),')
