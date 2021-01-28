from bl3hotfixmod import Mod

# Give Commitment Negative Accuracy instead of CDR

mod=Mod('zane_anarchy.bl3hotfix',
'Zane Anarchy',
'SSpyR',
[
    'Turning Commitments CDR into Negative Accuracy'
],
lic=Mod.CC_BY_SA_40,
cats='skill-system, char-operative'
)

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/StatusEffect_Operative_DLCSkill_6.StatusEffect_Operative_DLCSkill_6',
'AttributeEffects.AttributeEffects[1].AttributeData',
'/Game/GameData/Accuracy/Att_AccuracyMaxValue.Att_AccuracyMaxValue'
)
mod.newline()

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/StatusEffect_Operative_DLCSkill_6.StatusEffect_Operative_DLCSkill_6',
'AttributeEffects.AttributeEffects[2].AttributeData',
'/Game/GameData/Accuracy/Att_AccuracyMaxValue.Att_AccuracyMaxValue'
)
mod.newline()

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/StatusEffect_Operative_DLCSkill_6.StatusEffect_Operative_DLCSkill_6',
'AttributeEffects.AttributeEffects[3].AttributeData',
'/Game/GameData/Accuracy/Att_AccuracyMaxValue.Att_AccuracyMaxValue'
)
mod.newline()

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/StatusEffect_Operative_DLCSkill_6.StatusEffect_Operative_DLCSkill_6',
'AttributeEffects.AttributeEffects[4].AttributeData',
'/Game/GameData/Accuracy/Att_AccuracyMaxValue.Att_AccuracyMaxValue'
)
mod.newline()

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/Passive_OperativeDLC_6.Default__Passive_OperativeDLC_6_C',
'AbilityDescription',
'[skillbold]Kill Skill[/skillbold]. Zane gains increased [skillbold]Gun Damage[/skillbold] and decreased [skillbold]Accuracy[/skillbold].'
)
mod.newline()

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/Passive_OperativeDLC_6.Default__Passive_OperativeDLC_6_C:UIStatData_OakPassiveAbilityAttribute_0',
'Attribute',
'/Game/GameData/Accuracy/Att_AccuracyMaxValue.Att_AccuracyMaxValue'
)
mod.newline()

mod.comment('Making Commitment Accuracy Instead of CDR')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/Passive_OperativeDLC_6.Default__Passive_OperativeDLC_6_C:UIStatData_OakPassiveAbilityAttribute_0',
'FormatText',
'[skillbold]Accuracy[/skillbold]: $VALUE$'
)
mod.newline()

mod.comment('Adjusting Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/Table_Operative_DLCPassiveContantValues.Table_Operative_DLCPassiveConstantValues',
'DLCSkill6_CooldownRate',
'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
4.0
)
mod.newline()

mod.close()