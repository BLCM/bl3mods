#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('eridian_unlocks.txt',
        'pffff',
        [],
        'EridianUnlocks',
        )

#mod.reg_hotfix(Mod.PATCH, '',
#        '/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.Default__Condition_IsChallengeComplete_C:Conditions_Condition_IsChallengeComplete',
#        'Challenge',
#        'None',
#        )

# Eh, gonna give up on this, too many combinations going on.  Even if I
# have the right syntax for the object/attr, I could have the wrong data
# in the ObjectiveRef statement.  Something I try could end up screwing
# up the object in general, and then all my future tests might have
# worked if I'd started with a totally-clean object, but of course doing
# a full quit/restart inbetween these is way more time than I'm willing
# to spend.  I might not even understand the object  enough -- what I'm
# trying here might be doomed to failure anyway.  To me it looks like
# the check does an AND check against proximity and then a list of
# conditions, and the list is an OR which checks for either a challenge
# completion or a mission objective.  If that's true, then the mission
# objective is my best target, since I can grab that data pretty easily
# and just use an objective from the very first mission.  But, of course,
# even if all that is true, perhaps that challenge needs to be complete
# before it even *gets* to this check, so there's about a million
# unknowns here.  An `obj dump` would do wonders for this, of course.

#mod.reg_hotfix(Mod.PATCH, '',
mod.reg_hotfix(Mod.LEVEL, 'Prologue_P',

        # Come, marvel at my increasingly-desperate attempt to try every possible combination
        # of somewhat-likely names!

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.Default__MissionEnableConditionObjective:Conditions_MissionEnableConditionObjective',
        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:Conditions_MissionEnableConditionObjective',
        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:MissionEnableConditionObjective_0',
        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:Conditions_MissionEnableConditionObjective_0',
        #'ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:UsabilityDataSelection_0.EnabledCondition_GbxCondition_Compound',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator',
        #'EnabledCondition.Object..Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:UsabilityDataSelection.EnabledCondition_GbxCondition_Compound',
        #'Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:UsabilityDataSelection_0.EnabledCondition_GbxCondition_Compound',
        #'Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:Conditions_MissionEnableConditionObjective',
        #'EnabledCondition.Object..Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:UsabilityDataSelection_0.EnabledCondition_GbxCondition_Compound.Condition1_GbxCondition_List.Conditions_MissionEnableConditionObjective',
        #'EnabledCondition.Object..Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:UsabilityDataSelection.EnabledCondition_GbxCondition_Compound.Condition1_GbxCondition_List.Conditions_MissionEnableConditionObjective',
        #'EnabledCondition.Object..Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:EnabledCondition_GbxCondition_Compound.Condition1_GbxCondition_List.Conditions_MissionEnableConditionObjective',
        #'EnabledCondition.Object..Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:Conditions_MissionEnableConditionObjective',
        #'EnabledCondition.Object..Condition1.Object..Conditions.Conditions[0].Object..ObjectiveRef',

        # newest attempt, Jan 3 2020
        # Finally managed to get an ingame console -- the below *does* seem to work, actually, it's just that apparently
        # this alone isn't sufficient to allow early eridium-smashing.  Woo!
        '/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator',
        'EnabledCondition.Object..Condition1.Object..Conditions[0].Object..ObjectiveRef',

        """(
            Mission=Mission'"/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C"',
            ObjectiveName=Obj_GetAcrossBridgeGap_Objective,
            ObjectiveGuid=70fa4d4d4d4891f3482ec68258d0cce3
        )""",
        )

mod.close()
