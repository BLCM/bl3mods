#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('always_visible_challenge_icons.txt',
        'Attempt to make the various challenge icons always visible on the map',
        [],
        'Icons',
        )

# eh?
mod.reg_hotfix(Mod.LEVEL, 'City_P',
        '/Game/GameData/Challenges/CrewChallenges/Collection/Challenge_Collection_Journal.Challenge_Collection_Journal',
        'bHideInUI',
        'False')

for obj_name in [
        'UIData_ChallengeIcon_Journal',
        'UIData_ChallengeIcon_AwesomeTheftAuto',
        'UIData_ChallengeIcon_Hunt',
        'UIData_ChallengeIcon_Sabotage',
        'UIData_ChallengeIcon_Salvage',
        ]:
    # Have tried both low and high numbers for both VisibleDistance and HiddenDistance
    # Have also tried using obj_name.Default__InWorldIconData instead of obj_name.obj_name
    # And also I've tried using SparkLevelPatchEntry
    # There are doubtless various combinations I *didn't* try, of course - lots of permutations.
    mod.reg_hotfix(Mod.LEVEL, 'City_P',
            '/Game/UI/InWorldContainer/{}.{}'.format(obj_name, obj_name),
            'bUseVisibilityRange',
            'False')
    mod.reg_hotfix(Mod.LEVEL, 'City_P',
            '/Game/UI/InWorldContainer/{}.{}'.format(obj_name, obj_name),
            'VisibleDistance',
            200000000)
    #mod.reg_hotfix(Mod.LEVEL, 'City_P',
    #        '/Game/UI/InWorldContainer/{}.{}'.format(obj_name, obj_name),
    #        'HiddenDistance',
    #        0)

mod.close()
