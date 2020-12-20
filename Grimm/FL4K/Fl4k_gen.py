from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('Fl4k.bl3hotfix',
'Fl4k Redone',
'Grimm',
[
    'My own version of Fl4k.',
    'Includes :',
    'Skill balancing',
    'Augments balancing',
    'Pet bonuses balancing',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'   
],
lic=Mod.CC_BY_SA_40,
)

hunter='/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport'
stalker='/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_HitAndRun'
master='/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_Bond'
trapper='/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Character/AbilityTree_Beastmaster_DLCTree'

###SKILL BALANCE###

mod.comment('Buffing Overall Skill Damage')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/Att_Calc_Beastmaster_GlobalSkillDamage',
'Value.Power',
'(BaseValueConstant=1.35)'
)
mod.newline()

#STALKER TREE

mod.comment('Reducing Self Repairing Systems Max Health')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun4',
'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
-0.06
)
mod.newline()

mod.comment('Buffing Self Repairing Systems Health Regen')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun4',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.012
)
mod.newline()

mod.comment('Changing Self Repairing Systems Description')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun4/Passive_Beastmaster_HitAndRun4.Default__Passive_Beastmaster_HitAndRun4_C',
'AbilityDescription',
"FL4K's [skillbold]Maximum Health[/skillbold] is decreased, but they constantly [skillbold]Regenerate Health[/skillbold]."
)
mod.newline()

mod.comment('Buffing SicEm damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun2',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.12
)
mod.newline()

mod.comment('Buffing SicEm cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun2',
'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
0.15
)
mod.newline()

mod.comment('Buffing SicEm cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun2',
'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
0.15
)
mod.newline()

mod.comment('Buffing Turn Tail and Run damage reduction')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun5',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
-0.12
)
mod.newline()

mod.comment('Buffing Turn Tail and Run Move Speed')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun5',
'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
0.1
)
mod.newline()

mod.comment('Buffing Turn Tail and Recoil Reduction')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun5',
'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
-0.15
)
mod.newline()

mod.comment('Changing Turn Tail and Run Description')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C',
'AbilityDescription',
"FL4K gains [skillbold]Bonus Movement Speed[/skillbold], while moving he gains [skillbold]Damage Reduction[/skillbold].\n While Still, FL4K gains [skillbold]Increased Gun Damage[/skillbold] and [skillbold]Lowered Recoil[/skillbold]."
)
mod.newline()

mod.comment('Giving Turn Tail and Run Bonus Movement Speed')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
'Attribute',
'/Game/GameData/Attributes/Character/Att_GroundSpeedScale.Att_GroundSpeedScale'
)
mod.newline()

mod.comment('Giving Turn Tail and Run Bonus Movement Speed')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
'FormatText',
"[skillbold]Movement Speed:[/skillbold] $VALUE$"
)
mod.newline()

mod.comment('Giving Turn Tail and Run Bonus Movement Speed')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Status_Beastmaster_HitAndRun5_Moving',
'AttributeEffects.AttributeEffects[1].AttributeData',
'/Game/GameData/Attributes/Character/Att_GroundSpeedScale.Att_GroundSpeedScale'
)
mod.newline()

mod.comment('Giving Turn Tail and Run Reduced Recoil')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_2',
'Attribute',
'/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale.Att_Weapon_RecoilHeightScale'
)
mod.newline()

mod.comment('Giving Turn Tail and Run Bonus Reduced Recoil')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_2',
'FormatText',
"[skillbold]Recoil Reduction:[/skillbold] $VALUE$"
)
mod.newline()

mod.comment('Giving Turn Tail and Run Bonus Reduced Recoil')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Status_Beastmaster_HitAndRun5_Still',
'AttributeEffects.AttributeEffects[1].AttributeData',
'/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale.Att_Weapon_RecoilHeightScale'
)
mod.newline()

mod.comment('Buffing The Fast and the Furryous projectile speed bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'HitAndRun_10',
'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
0.15
)
mod.newline()

mod.comment('Changing The Fast and the Furryous Description')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10.Default__Passive_Beastmaster_HitAndRun10_C',
'AbilityDescription',
"While above half health, FL4K's [skillbold]Gun Damage[/skillbold] and [skillbold]Projectile Speed[/skillbold] are increased and their pet gains increased [skillbold]Damage[/skillbold]."
)
mod.newline()

mod.comment('Giving The Fast and the Furryous Bonus Projectile Speed')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10.Default__Passive_Beastmaster_HitAndRun10_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
'Attribute',
'/Game/GameData/Weapons/Att_Weapon_ProjectileSpeedScale.Att_Weapon_ProjectileSpeedScale'
)
mod.newline()

mod.comment('Giving The Fast and the Furryous Bonus Projectile Speed')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10.Default__Passive_Beastmaster_HitAndRun10_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
'FormatText',
"[skillbold]Projectile Speed:[/skillbold] $VALUE$"
)
mod.newline()

mod.comment('Giving The Fast and the Furryous Bonus Projectile Speed')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Status_HitAndRun10_WeaponDamage_DA',
'AttributeEffects.AttributeEffects[1].AttributeData',
'/Game/GameData/Weapons/Att_Weapon_ProjectileSpeedScale.Att_Weapon_ProjectileSpeedScale'
)
mod.newline()

mod.comment('Buffing Rage and Recover health regen')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun3',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.05
)
mod.newline()

mod.comment('Buffing Rage and Recover health regen')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_HitAndRun3',
'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
0.05
)
mod.newline()

#HUNTER TREE

mod.comment('Buffing Second Intention reload speed bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Ranged2',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
-0.05
)
mod.newline()

mod.comment('Buffing Second Intention reload speed bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Ranged2',
'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
-0.1
)
mod.newline()

mod.comment('Buffing Ambush Predator Crit Bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Ranged5',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.05
)
mod.newline()

#MASTER TREE

mod.comment('Buffing He Bites Reflected Damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Bond11',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.25
)
mod.newline()

mod.comment('Buffing Who Rescued Who ? health regen')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'P_Bond3',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.006
)
mod.newline()

#TRAPPER TREE

mod.comment('Buffing Keep Then Safe Cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
'DLCSkill15_CooldownTime',
'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
6.0
)
mod.newline()

mod.comment('Buffing Better Toys')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
'DLCSkill4_ShieldRegenRate',
'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
0.10
)
mod.newline()

mod.comment('Buffing Better Toys')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
'DLCSkill4_ShieldRegenDelay',
'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
0.12
)
mod.newline()

#AUGMENTS

###STALKER

mod.comment('Buffing Guerillas in the Mist damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Ultimate_Spiderant_Mod3',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.50
)
mod.newline()

mod.comment('Buffing Guerillas in the Mist duration')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Ultimate_Spiderant_Mod3',
'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
8
)
mod.newline()

mod.comment('Buffing Not My Circus duration')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Ultimate_Spiderant_Mod1',
'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
8
)
mod.newline()

###HUNTER

mod.comment('Buffing Rakk Attack base damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Ultimate_Skag',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.85
)
mod.newline()

mod.comment('Buffing Falconers Feast heal percent')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Ultimate_Skag_Mod1',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.15
)
mod.newline()

###MASTER

mod.comment('Buffing Atomic Aroma damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Skill_PetEnrage_Mod2',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.18
)
mod.newline()

###PETS BALANCE

mod.comment('Buffing global pet skill damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Global_Pet_SkillDamage',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
35.0
)
mod.newline()

mod.comment('Buffing global pet melee damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Global_Pet_MeleeDamage',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
12.0
)
mod.newline()

mod.comment('Buffing global pet ranged damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Global_Pet_RangedAttack',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.6
)
mod.newline()

###SKAGS

mod.comment('Buffing Skag fire rate bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Buffs_PetSkag',
'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
0.08
)
mod.newline()

#SPIDERANTS

mod.comment('Buffing Spiderants health regen bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Buffs_PetSpiderant',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.02
)
mod.newline()

mod.comment('Buffing Spiderants damage reduction bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Buffs_PetSpiderant',
'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
-0.08
)
mod.newline()

###JABBERS

mod.comment('Buffing Jabbers health bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Buffs_PetJabbermon',
'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
0.12
)
mod.newline()

mod.comment('Buffing Jabbers move speed bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Buffs_PetJabbermon',
'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
0.15
)
mod.newline()

mod.comment('Buffing Jabbers critical bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
'Buffs_PetJabbermon',
'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
0.10
)
mod.newline()