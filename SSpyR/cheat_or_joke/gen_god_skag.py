from bl3hotfixmod import Mod

#Buff Other Pets?
#Buff Attack Command
#Buff Radius?

mod=Mod('god_skag.bl3hotfix',
'God Skag',
'SSpyR',
[
    'Buffs Skag Damage by a lot.',
    'Also infinite Gamma Burst'
],
lic=Mod.CC_BY_SA_40,
cats='cheat, joke'
)

mod.comment('Buffing Skag melee damage multiplier')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance',
'Global_Pet_MeleeDamage',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
99999999)
mod.newline()

mod.comment('Buffing Skag ranged damage multiplier')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance',
'Global_Pet_RangedAttack',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
99999999)
mod.newline()

mod.comment('Reducing Gamma cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance',
'Skill_PetEnrage',
'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
0)
mod.newline()

mod.comment('Increasing Gamma duration')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance',
'Skill_PetEnrage',
'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
99999)
mod.newline()

mod.close