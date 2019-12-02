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

# Eh, gonna give up on this, too many combinations going on.

mod.reg_hotfix(Mod.PATCH, '',
        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.Default__MissionEnableConditionObjective:Conditions_MissionEnableConditionObjective',
        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:Conditions_MissionEnableConditionObjective',
        #'/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:MissionEnableConditionObjective_0',
        '/Game/Gear/Game/Resonator/_Design/UsabilityData_Resonator.UsabilityData_Resonator:Conditions_MissionEnableConditionObjective_0',
        'ObjectiveRef',
        """(
            Mission=Mission'"/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C"',
            ObjectiveName="Obj_GetAcrossBridgeGap_Objective",
            ObjectiveGuid="70fa4d4d4d4891f3482ec68258d0cce3"
        )""",
        )

mod.close()
