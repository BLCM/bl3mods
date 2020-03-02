#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('eridian_unlocks_full.txt',
        'pffff',
        [],
        'EridianUnlocks',
        )

###
### Various console shenanigans to unlock the Resonator (hitting eridium crystal growth)
###

# >>> getall UsabilityDataSelection
# (works, didn't capture output)
# >>> getall GbxCondition_Compound
# (works, didn't capture output)
#
# >>> getall GbxCondition_Compound condition1 name=enabledcondition_gbxcondition_compound
# GbxCondition_Compound /Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:EnabledCondition_GbxCondition_Compound.Condition1 = Condition1_GbxCondition_List
# 
# >>> getall GbxCondition_Compound condition2 name=enabledcondition_gbxcondition_compound
# GbxCondition_Compound /Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:EnabledCondition_GbxCondition_Compound.Condition2 = Condition2_Condition_CompareDistance
# (don't really care about this one at the moment)
#
# >>> getall gbxcondition_list foo name=Condition1_GbxCondition_List
# GbxCondition_List /Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:EnabledCondition_GbxCondition_Compound.Condition1_GbxCondition_List
#
# >>> ... operator
# Or
# >>> ... Conditions
# 0: Conditions_MissionEnableConditionObjective
# 1: Conditions_Condition_IsChallengeComplete
#
# >>> getall condition_ischallengecomplete_c challenge name=conditions_condition_ischallengecomplete
# 0) Condition_IsChallengeComplete_C /Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:EnabledCondition_GbxCondition_Compound.Condition1_GbxCondition_List.Conditions_Condition_IsChallengeComplete
# Challenge = BlueprintGeneratedClass'/Game/GameData/Challenges/Account/Challenge_VaultReward_Resonator.Challenge_VaultReward_Resonator_C'
#
# >>> getall missionenableconditionobjective objectiveref name=Conditions_MissionEnableConditionObjective
# MissionEnableConditionObjective /Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:EnabledCondition_GbxCondition_Compound.Condition1_GbxCondition_List.Conditions_MissionEnableConditionObjective
# (
#    Mission=/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C,
#    ObjectiveName="Obj_GetAcrossBridgeGap_Objective",
#    ObjectiveGuid=70FA4D4D4D4891F3482EC68258D0CCE3,
#    Objective=None
# )

# (from a different but similar object, just wanted to make sure that the `None` objective wasn't a problem)
# (
#    Mission=/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep07_TheHeist.Mission_DLC1_Ep07_TheHeist_C,
#    ObjectiveName="Obj_PunchOutHole_Objective",
#    ObjectiveGuid=6DA1350646FD6246153AACA58D151E76,
#    Objective=None
# )

###
### Some actual code follows
###

# This hotfix *works*, in that it sets the object in the way I expect, but it turns out that this object is
# basically beside the point, doesn't seem to have any bearing on anything
#mod.reg_hotfix(Mod.PATCH, '',
#    '/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator',
#    'EnabledCondition.Object..Condition1.Object..Conditions[0].Object..ObjectiveRef',
#    """(
#        Mission=Mission'"/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C"',
#        ObjectiveName=Obj_Cinematic_BusDrivesOff_Objective,
#        ObjectiveGuid=546ee010488fd162de7dfaa46960466c
#    )""")

###
### More console shenanigans after noticing the melee-themed object in the same dir.
###

# >>> getall bpclass_playermeleedata_c overridecondition name=meleedata_resonator
# BPClass_PlayerMeleeData_C /Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator.OverrideCondition = GbxConditionList'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List'
#
# >>> getall gbxcondition_list conditions name=overridecondition_gbxcondition_list
# 0: GbxCondition_List'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List.Conditions_GbxCondition_List
# 1: Condition_CompareDistance_C'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List:Conditions_Condition_CompareDistance'
# 2: Condition_CanUseResonator_C'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List:Conditions_Condition_CanUseResonator'
#
# >>> getall gbxcondition_list foo name=conditions_gbxcondition_list
# operator:
#    Or
# conditions:
#    0: MissionEnableConditionObjective'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List.Conditions_GbxCondition_List.Conditions_MissionEnableConditionObjective'
#    1: Condition_IsChallengeComplete_C'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List.Conditions_GbxCondition_List.Conditions_Condition_IsChallengeComplete'
#
# >>> getall missionenableconditionobjective objectiveref name=conditions_missionenableconditionobjective
# MissionEnableConditionObjective /Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxConditionList.Conditions_GbxCondition_List.Conditions_MissionEnableConditionObjective

# I seem to recall that this *worked* like the UsabilityData object above, but similarly didn't seem
# to actually give me breakable crystals
#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator',
#        'OverrideCondition.Object..Conditions[0].Object..Conditions[0].Object..ObjectiveRef',
#        """(
#            Mission=Mission'"/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C"',
#            ObjectiveName=Obj_Cinematic_BusDrivesOff_Objective,
#            ObjectiveGuid=546ee010488fd162de7dfaa46960466c
#        )""")

# Aaaand, finally, this one *does* actually work!  It's very stupid, basically reduces the whole condition list
# to *just* a the distance check.  Still: breakable crystals from the start!
mod.comment('Always allow Resonator')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator',
        'OverrideCondition.Object..Conditions',
        """(
            Condition_CompareDistance_C'/Game/Gear/Game/Resonator/_Design/MeleeData_Resonator.MeleeData_Resonator:OverrideCondition_GbxCondition_List:Conditions_Condition_CompareDistance'
        )""")
mod.newline()

###
### Now, work begins on trying to unlock eridian writings (Analyzer).
### Console shenanigans first.
###

# >>> getall usablecomponent
# UsableComponent /Game/InteractiveObjects/EridianWriting/IO_EridianWriting.IO_EridianWriting_C:UsableNoAnalyzer_GEN_VARIABLE
# UsableComponent /Game/InteractiveObjects/EridianWriting/IO_EridianWriting.IO_EridianWriting_C:Usable_GEN_VARIABLE
#
# >>> getall usablecomponent enabledcondition name=Usable_GEN_VARIABLE
# ... EnabledCondition_Condition_IsChallengeComplete_EridianWriting
#
# >>> getall condition_ischallengecomplete_eridianwriting_c binvertcondition
# Condition_IsChallengeComplete_EridianWriting_C /Game/InteractiveObjects/EridianWriting/IO_EridianWriting.IO_EridianWriting_C:UsableNoAnalyzer_GEN_VARIABLE.EnabledCondition_Condition_IsChallengeComplete_EridianWriting.bInvertCondition = True
# Condition_IsChallengeComplete_EridianWriting_C /Game/InteractiveObjects/EridianWriting/IO_EridianWriting.IO_EridianWriting_C:Usable_GEN_VARIABLE.EnabledCondition_Condition_IsChallengeComplete_EridianWriting.bInvertCondition = False
#
# ... analyzerchallenge (assumed the ending there, didn't feel like digging through memory)
#    .AnalyzerChallenge = BlueprintGeneratedClass'/Game/GameData/Challenges/Account/Challenge_VaultReward_Analyzer.Challenge_VaultReward_Analyzer_C'

###
### Which brings us to some statements which sort-of work.  We can set the required
### challenge to one of our "general" game challenges (I chose the crit-kill one here),
### set that challenge to be really easily-achievable, and then we can interact with
### the writing and have it marked off the list of writings in the map challenge
### area.  HOWEVER, the sigil does *not* glow beforehand, you don't get the audio
### when you press it, and the message does *not* show up in your log.
###

mod.comment('Swap required challenge for Analyzer and hax the challenge')

# Hax the challenge we're going to use (note that if you load a save that's passed
# this, you'll need to get one more crit kill for it to trigger properly)
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Challenges/GeneralCombat/Challenge_Combat_KillWith_Crits.Default__Challenge_Combat_KillWith_Crits_C',
        'ProgressGoalInfo',
        """(
            (GoalValue=1,NotificationThreshold=1),
            (GoalValue=2,NotificationThreshold=2),
            (GoalValue=3,NotificationThreshold=3),
            (GoalValue=4,NotificationThreshold=4),
            (GoalValue=5,NotificationThreshold=5)
        )""")

# Now set the IO to use that challenge (only implemented in The Droughts at the moment)
mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
        '/Game/InteractiveObjects/EridianWriting/IO_EridianWriting.IO_EridianWriting_C:UsableNoAnalyzer_GEN_VARIABLE.EnabledCondition_Condition_IsChallengeComplete_EridianWriting',
        'AnalyzerChallenge',
        "BlueprintGeneratedClass'/Game/GameData/Challenges/GeneralCombat/Challenge_Combat_KillWith_Crits.Challenge_Combat_KillWith_Crits_C'")
mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
        '/Game/InteractiveObjects/EridianWriting/IO_EridianWriting.IO_EridianWriting_C:Usable_GEN_VARIABLE.EnabledCondition_Condition_IsChallengeComplete_EridianWriting',
        'AnalyzerChallenge',
        "BlueprintGeneratedClass'/Game/GameData/Challenges/GeneralCombat/Challenge_Combat_KillWith_Crits.Challenge_Combat_KillWith_Crits_C'")

mod.newline()

###
### A bit of further testing once I'd done that, seeing if there was anything else obvious I could tweak.
### One thing was that there's individual Challenge_EridianWriting_* challenges with their own
### challenge-prerequisite attributes, so I figured I'd try those.  No dice, in the end.
###
### From the console: getall Challenge_EridianWriting_C
###

mod.comment('Testing individual challenge swaps...')

# This didn't actually change anything:
#mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',
#        '/Game/GameData/Challenges/EridianWriting/Challenge_EridianWriting.Default__Challenge_EridianWriting_C',
#        'PrerequisiteChallenge',
#        "BlueprintGeneratedClass'/Game/GameData/Challenges/GeneralCombat/Challenge_Combat_KillWith_Crits.Challenge_Combat_KillWith_Crits_C'")

# These *did* change the objects as intended, but behavior was just the same anyway:
for (level, nums) in [
        # Obviously at some point it doesn't make sense to keep doing these.  Whatever.
        ('Prologue_P', [1, 2]),
        ('Sacrifice_P', [3]),
        ('Outskirts_P', [4]),
        ('City_P', [5]),
        ('Towers_P', [6]),
        ('AtlasHQ_P', [7]),
        ('OrbitalPlatform_P', [8]),
        ('CityVault_P', [9]),
        ('Monastery_P', [10]),
        ('MarshFields_P', [11, 15]),
        ('Wetlands_P', [12, 13]),
        ('Watership_P', [14]),
        ('Prison_P', [16]),
        ('Mansion_P', [17]),
        ('WetlandsVault_P', [18]),
        ('Desert_P', [19, 20]),
        ('Mine_P', [21]),
        ('Motorcade_P', [22]),
        ('MotorcadeInterior_P', [23]),
        ('Desertvault_P', [24]),
        ('MotorcadeFestival_P', [25]),
        ('Desolate_P', [26, 27]),
        ('Beach_P', [28]),
        ('Crypt_P', [29]),
        ('FinalBoss_P', [30]),
        ]:
    for num in nums:
        mod.reg_hotfix(Mod.LEVEL, level,
                '/Game/GameData/Challenges/EridianWriting/Challenge_EridianWriting_{:02d}.Default__Challenge_EridianWriting_{:02d}_C'.format(num, num),
                'PrerequisiteChallenge',
                "BlueprintGeneratedClass'/Game/GameData/Challenges/GeneralCombat/Challenge_Combat_KillWith_Crits.Challenge_Combat_KillWith_Crits_C'")

mod.newline()

mod.close()
