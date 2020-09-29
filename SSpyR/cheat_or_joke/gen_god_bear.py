from bl3hotfixmod import Mod  

mod=Mod('god_bear.bl3hotfix',
'God Bear',
'SSpyR',
[
    'Adjusts Auto Bear to feel more like Scorpio Turret, etc.',
    'Also buffing general Iron Bear stuff.',
    'God.'
],
lic=Mod.CC_BY_SA_40,
cats='cheat, joke'
)

mod.comment('Increasing Iron Bear Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_Player_Scalar_Constants',
'SkillDamage_Gunner',
'Scaler_6_5C32556442B4DA4D7EAE1A8610E0A950',
999999.00
)
mod.newline()

mod.comment('Increasing Auto-Bear Duration')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'C_SurpriseForYou',
'Cooldown_4_8A38A09E46E89B75CDB6F39A50278802',
60
)
mod.newline()

mod.comment('Melee Bad, so Separate Buff')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'BearFist',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
52.5
)
mod.newline()

#Doesn't Work, Fix at some Point
mod.comment('Buffing Iron Bear Health')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Global_IronBear_Health',
'DamageScalar_2_28B25EC8493D1EB6C2138A962F659BCD',
9999.00
)
mod.newline()

mod.comment('Reducing Iron Bear Cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Gunner/DataTable_Gunner_SkillsBalance',
'Global_IronBear_Cooldown',
'Cooldown_4_8A38A09E46E89B75CDB6F39A50278802',
0.00
)
mod.newline()

mod.close()