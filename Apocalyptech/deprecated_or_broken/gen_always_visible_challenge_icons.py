#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('always_visible_challenge_icons.txt',
        'Sets all the challenge icons to be visible on the map at all times',
        [],
        'ChallengeIcons',
        )

# I wonder if this is *too* big?
radius = 999999999
# Though a smaller value didn't really help either, so eh.
#radius = 99999

height = 3000

# For the last part of the extended object name:
#
# BP_CrewChallengeComponent_Collection - Typhon Logs
# BP_CrewChallengeComponent_CollectionDeadDrop - Typhon Dead Drop
# BP_CrewChallengeComponent_Hijack_Spawner - Ellie Vehicle Theft
# BP_CrewChallengeComponent_Hunt_Spawner - Hammerlock Hunt
# BP_CrewChallengeComponent_Sabotage - Radios
# BP_CrewChallengeComponent_Salvage - Claptraps

for (label, level_name, object_names) in sorted([
        ('Ascension Bluff', 'Sacrifice_P', [
            # Working:
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_BroadcastControlBox_Sabotage.BP_CrewChallengeComponent_Sabotage',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_HuntCrewChallenge-Skrakk.BP_CrewChallengeComponent_Hunt_Spawner',

            # Not working for some damn reason:
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart_GasTank.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_HijackCrewChallenge.BP_CrewChallengeComponent_Hijack_Spawner',

            # This would be correct, but needs an `_x` after `EchoJournal`, and the numbers are, as
            # you'd expect, somewhat random.  Examples seen in GBX hotfixes are 2, 120, and 161.
            # I assume that the only way to get the numbers is ingame.
            #'/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal.BP_CrewChallengeComponent_Collection',
            ]),

        ('Droughts', 'Prologue_P', [
            '/Game/Maps/Zone_0/Prologue/Prologue_Terrain.Prologue_Terrain:PersistentLevel.BP_IO_Salvage_ClapTrapPart1_Motor.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_Salvage_ClapTrapPart2_GyroscopicRotor.BP_CrewChallengeComponent_Salvage',
            '/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_HuntCrewChallenge.BP_CrewChallengeComponent_Hunt_Spawner',
            #'/Game/Maps/Zone_0/Prologue/Prologue_Dynamic.Prologue_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal.BP_CrewChallengeComponent_Collection',
            ]),
        ]):

    mod.comment(label)
    for object_name in object_names:
        mod.reg_hotfix(Mod.LEVEL, level_name,
                object_name,
                'DetectionRadius',
                radius,
                notify=True)
        mod.reg_hotfix(Mod.LEVEL, level_name,
                object_name,
                'DetectionHalfHeight',
                height,
                notify=True)
    mod.newline()

if False:
    # Didn't even work, anyway.
    mod.comment('What the hell, will give this a quick try')
    for num in range(200):
        mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
                '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_{}.BP_CrewChallengeComponent_Collection'.format(num),
                'DetectionRadius',
                radius,
                notify=True)
        mod.reg_hotfix(Mod.LEVEL, 'Sacrifice_P',
                '/Game/Maps/Zone_0/Sacrifice/Sacrifice_Dynamic.Sacrifice_Dynamic:PersistentLevel.BP_IO_Collection_EchoJournal_{}.BP_CrewChallengeComponent_Collection'.format(num),
                'DetectionHalfHeight',
                height,
                notify=True)

mod.newline()

mod.close()
