#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('hardcode_mayhem2_drops.txt',
        'Hardcode Mayhem 2.0 World Drops',
        [
            "Mayhem 2.0 introduced a bug where various enemies don't drop gear",
            "in Mayhem mode.  A hotfix a week later fixed it, theoretically, and",
            "seemed to work fine, but running through some DLC2 content felt",
            "awfully a lot like the drop rates still weren't right.  I don't",
            "actually care if the drop rates get better at higher Mayhem levels",
            "anyway, so I'm just keeping this 'fix' in place.",
            "",
            "This should be run BEFORE my Better Loot mod, if you're using both",
            "and want Better Loot's enhanced eridium drop rate.",
        ])

class PoolList(object):
    
    def __init__(self, label, obj_name, chars,
            gun_idx=None,
            artifact_idx=None, com_idx=None,
            grenade_idx=None, shield_idx=None,
            eridium_idx=None):

        self.label = label
        self.obj_name = obj_name
        self.chars = chars

        self.gun_idx = gun_idx
        self.artifact_idx = artifact_idx
        self.com_idx = com_idx
        self.grenade_idx = grenade_idx
        self.shield_idx = shield_idx
        self.eridium_idx = eridium_idx

# Technically we should also fix the following:
#  - ItemPoolList_BloodyHarvest_BasicGhost
#  - ItemPoolList_BloodyHarvest_BadassGhost
#  - ItemPoolList_BloodyHarvest_AmmoHealthCash
#  - ItemPoolList_CyberObjectBadassLoot
#
# ... but who cares about the Bloody Harvest ones, at the moment, and that
# Cyber one doesn't seem to actually be referenced by anything.
poollists = [
        PoolList('Base Game Standard Enemies',
            '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear',
            ['MatchAll'],
            gun_idx=4,
            com_idx=5,
            shield_idx=6,
            artifact_idx=7,
            grenade_idx=8,
            eridium_idx=10,
            ),
        PoolList('Base Game Badasses',
            '/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear',
            ['MatchAll'],
            com_idx=5,
            shield_idx=6,
            artifact_idx=7,
            grenade_idx=8,
            ),
        PoolList('Goliaths (non-enraging)',
            '/Game/GameData/Loot/ItemPools/Goliath/ItemPoolList_Goliath_NonEnraging',
            ['BPChar_Goliath'],
            gun_idx=4,
            com_idx=5,
            ),
        PoolList('DLC1 Standard Loaders',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_StandardEnemyGunsandGearLoader',
            ['MatchAll'],
            gun_idx=4,
            shield_idx=6,
            artifact_idx=7,
            grenade_idx=8,
            eridium_idx=10,
            ),
        PoolList('DLC1 Badass Loaders',
            '/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/ItemPools/ItemPoolList_BadassEnemyGunsGearLoader1',
            ['MatchAll'],
            shield_idx=6,
            artifact_idx=7,
            grenade_idx=8,
            ),
        PoolList('DLC1 Standard Enemies',
            '/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Dandelion',
            ['MatchAll'],
            gun_idx=4,
            shield_idx=6,
            artifact_idx=7,
            grenade_idx=8,
            eridium_idx=10,
            ),
        PoolList('DLC1 Badasses',
            '/Game/PatchDLC/Dandelion/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Dandelion',
            ['MatchAll'],
            shield_idx=6,
            artifact_idx=7,
            grenade_idx=8,
            ),
        PoolList('DLC2 Standard Enemies',
            '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_StandardEnemyGunsandGear_Hibiscus',
            ['MatchAll'],
            gun_idx=4,
            artifact_idx=7,
            grenade_idx=8,
            eridium_idx=10,
            ),
        PoolList('DLC2 Badasses',
            '/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_BadassEnemyGunsGear_Hibiscus',
            ['MatchAll'],
            artifact_idx=6,
            ),
        ]

for section_label, new_att, attr_name in [
        ('Guns', '/Game/GameData/Loot/ItemPools/Attributes/Att_GunsAndGear_DropOdds', 'gun_idx'),
        ('Artifacts', '/Game/GameData/Loot/ItemPools/Attributes/Att_Artifact_DropOdds', 'artifact_idx'),
        ('COMs', '/Game/GameData/Loot/ItemPools/Attributes/Att_ClassMods_DropOdds', 'com_idx'),
        ('Grenade Mods', '/Game/GameData/Loot/ItemPools/Attributes/Att_GrenadeMod_DropOdds', 'grenade_idx'),
        ('Shields', '/Game/GameData/Loot/ItemPools/Attributes/Att_Shields_DropOdds', 'shield_idx'),
        ('Eridium Sticks', '/Game/GameData/Loot/ItemPools/Attributes/Att_EridiumStick_DropOdds', 'eridium_idx'),
        ]:
    new_att_full = Mod.get_full_cond(new_att, 'GbxAttributeData')
    mod.header(section_label)
    for poollist in poollists:
        index = getattr(poollist, attr_name)
        if index is not None:
            mod.comment(poollist.label)
            for char in poollist.chars:
                mod.reg_hotfix(Mod.CHAR, char,
                        poollist.obj_name,
                        'ItemPools.ItemPools[{}].PoolProbability.BaseValueAttribute'.format(index),
                        new_att_full)
            mod.newline()

mod.close()
