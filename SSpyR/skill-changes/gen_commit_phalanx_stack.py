from bl3hotfixmod import Mod

mod=Mod('commit_phalanx_stack.bl3hotfix',
'"Fixing" Commitment and Phalanx Stacking',
'SSpyR',
[
	'Caps Commitment Skill at 2 stacks with values unchanged (updated card)',
	'And un-caps Phalanx Doctrine (as stated in card).',
	'Cheers to Grimm and EpicNNG for actually attempting to cap',
	'Commitment and not just thinking you couldnt like me :).'
],
lic=Mod.CC_BY_SA_40,
cats='skill-system, char-gunner, char-operative'
)

mod.comment('Capping Commitment at 2')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/StatusEffect_Operative_DLCSkill_6.StatusEffect_Operative_DLCSkill_6',
'StackingStrategy',
'/Game/GameData/StackingStrategy/StackingStrategy_Capped_2.StackingStrategy_Capped_2'
)
mod.newline()

mod.comment('Adjusting Commitment Card Text')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Operative/_DLC/Ixora/Passives/DLCSkill_06/Passive_OperativeDLC_6.Default__Passive_OperativeDLC_6_C',
'AbilityDescription',
'[skillbold]Kill Skill[/skillbold]. Zane gains increased [skillbold]Gun Damage[/skillbold] and [skillbold]Action Skill Cooldown Rate[/skillbold]. This effect stacks twice.'
)
mod.newline()

mod.comment('Un-Capping Phalanx Doctrine')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/PhalanxDoctrine/Status_Gunner_PhalanxDoctrine_DA.Status_Gunner_PhalanxDoctrine_DA',
'StackingStrategy',
'None'
)
mod.newline()


mod.close()