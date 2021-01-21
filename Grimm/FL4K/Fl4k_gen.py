from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('Fl4k.bl3hotfix',
'Fl4k',
'Grimm',
[
    'Categories: char-overhaul, char-beastmaster',
    'Find the entire details here :',
    'https://www.nexusmods.com/borderlands3/mods/248',
    'My own version of Fl4k.',
    'Includes :',
    'Skill balancing and skill changes.',
    'Augments balancing',
    'Pet bonuses overhaul.',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'   
],
lic=Mod.CC_BY_SA_40,
)

hunter='/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport'
stalker='/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_HitAndRun'
master='/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_Bond'
trapper='/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Character/AbilityTree_Beastmaster_DLCTree'

mod.comment('General Changes')
if True:

    mod.comment('Buffing Overall Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/Att_Calc_Beastmaster_GlobalSkillDamage',
    'Value.Power',
    '(BaseValueConstant=1.35)'
    )
    mod.newline()

mod.comment('Skills')
if True:

    mod.comment('Stalker Tree Skills')
    if True:

        mod.comment('Reducing Self Repairing Systems Max Health')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun4',
        'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
        -0.06
        )
        mod.newline()

        mod.comment('Buffing Self Repairing Systems Health Regen')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun4',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.012
        )
        mod.newline()

        mod.comment('Changing Self Repairing Systems Description')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun4/Passive_Beastmaster_HitAndRun_4.Default__Passive_Beastmaster_HitAndRun_4_C',
        'AbilityDescription',
        "FL4K's [skillbold]Maximum Health[/skillbold] is decreased, but they constantly [skillbold]Regenerate Health[/skillbold]."
        )
        mod.newline()

        mod.comment('Furrious Attack')
        if True:

            mod.comment('Values Scaling')
            if True:

                mod.comment('Furious Attack Action Skill Cooldown rate')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun1',
                'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
                0.0006
                )
                mod.newline()

                mod.comment('Furious Attack Infinite Duration')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun1',
                'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
                5000000.0
                )
                mod.newline()

                mod.comment('Furious Attack Max Stack Count')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun1',
                'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
                99.0
                )
                mod.newline()

                mod.comment('Furious Attack Unused')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun1',
                'Radius_11_A1466BA242034461180E58B6E902078D',
                0.0
                )
                mod.newline()

                mod.comment('Furious Attack Unused')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun1',
                'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
                0.0
                )
                mod.newline()

                mod.comment('Ajusting Furious Pet Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Att_BST_HitAndRun1_PetDamage.Att_BST_HitAndRun1_PetDamage:ValueResolver_ConstantAttributeValueResolver',
                'Value.BaseValueConstant',
                0.0007
                )
                mod.newline()

            mod.comment('Description')
            if True:
                mod.comment('Changing Furious Attack Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C',
                'AbilityDescription',
                "[skillbold]Hunter Skill[/skillbold]. After shooting an enemy, FL4K gains a stack of [skillbold]Furious Attack[/skillbold].<br>For each stack of [skillbold]Furious Attack[/skillbold], FL4K's [skillbold]Action Skill Cooldown Rate[/skillbold] is increased.<br>Additionally their pet gains increased [skillbold]Damage[/skillbold] per stack.<br>Stacks last until you enter fight for your life or die."
                )
                mod.newline()

            mod.comment('Stacks')
            if True:

                mod.comment('Changing Furious Attack Description To Remove The Stack Duration')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer_0',
                'FormatText',
                ''
                )
                mod.newline()

                mod.comment('Changing Furious Attack Stack Limit To 99')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1',
                'StackingStrategy',
                '/Game/GameData/StackingStrategy/StackingStrategy_Capped_99.StackingStrategy_Capped_99'
                )
                mod.newline()

            mod.comment('Cooldown Rate')
            if True:
                
                mod.comment('Changing Furious Attack Description To Action Skill Cooldown Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C:UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]Action Skill Cooldown Rate:[/skillbold] $VALUE$ per stack"
                )
                mod.newline()

                mod.comment('Changing Furious Attack Description To Action Skill Cooldown Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C:UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Attributes/Character/Att_Character_ActionSkill_GlobalCooldownRate.Att_Character_ActionSkill_GlobalCooldownRate'
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Add Action Skill Cooldown Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1.Status_Beastmaster_HitAndRun_1:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    (BaseValueConstant=0.0,
                    DataTableValue=(DataTable=DataTable'"/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas"',RowName="HitAndRun1_Damage",ValueName=""),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.0006
                )
                """                
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Add Action Skill Cooldown Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1',
                'AttributeEffects.AttributeEffects[3]',
                """
                (
                    AttributeData=GbxAttributeData'"/Game/GameData/Attributes/Character/Att_Character_ActionSkill_GlobalCooldownRate.Att_Character_ActionSkill_GlobalCooldownRate"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0006),
                    Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1.Status_Beastmaster_HitAndRun_1:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'                        
                )
                """                
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Add Action Skill Cooldown Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_Damage_P.Status_Beastmaster_HitAndRun_Damage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    BaseValueScale=0.0006                     
                )
                """                
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Add Action Skill Cooldown Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_Damage_P',
                'AttributeEffects.AttributeEffects[0]',
                """
                (
                    AttributeData=GbxAttributeData'"/Game/GameData/Attributes/Character/Att_Character_ActionSkill_GlobalCooldownRate.Att_Character_ActionSkill_GlobalCooldownRate"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0006),
                    Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_Damage_P.Status_Beastmaster_HitAndRun_Damage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'"'                       
                )
                """                
                )
                mod.newline()

            mod.comment('Removing Handling')
            if True:
                mod.comment('Changing Furious Attack To Remove Handling')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'Attribute',
                ''
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Remove Handling')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'FormatText',
                ''
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Remove Handling')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1',
                'AttributeEffects.AttributeEffects[0].AttributeData',
                ''
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Remove Handling')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_Handling_P',
                'AttributeEffects.AttributeEffects[0].AttributeData',
                ''
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Remove Handling')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1',
                'AttributeEffects.AttributeEffects[1].AttributeData',
                ''
                )
                mod.newline()

                mod.comment('Changing Furious Attack To Remove Handling')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Status_Beastmaster_HitAndRun_1',
                'AttributeEffects.AttributeEffects[2].AttributeData',
                ''
                )
                mod.newline()

            mod.comment('Pet Damage')
            if True:

                mod.comment('Fixing Furious Attack Description For Pet Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1.Default__Passive_Beastmaster_HitAndRun_1_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]Pet Damage:[/skillbold] $VALUE$ per stack"
                )
                mod.newline()

        mod.comment('Buffing SicEm damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun2',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.12
        )
        mod.newline()

        mod.comment('Buffing SicEm cooldown')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun2',
        'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
        0.15
        )
        mod.newline()

        mod.comment('Buffing SicEm cooldown')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun2',
        'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
        0.15
        )
        mod.newline()

        mod.comment('Overclocked')
        if True:

            mod.comment('Values Scaling')
            if True:

                mod.comment('Overclocked Fire Rate')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun8',
                'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
                -0.02
                )
                mod.newline()

                mod.comment('Overclocked Fire Rate After Reload')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun8',
                'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
                0.04
                )
                mod.newline()

            mod.comment('Description')
            if True:

                mod.comment('Changing Overclocked Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C',
                'AbilityDescription',
                "FL4K gains [skillbold]Bullet Damage[/skillbold] at the cost of [skillbold]Fire Rate[/skillbold]. The [skillbold]Fire Rate[/skillbold] penalty is reversed after reloading."
                )
                mod.newline()

            mod.comment('Fire Rate')
            if True:
                mod.comment('Changing Overclocked Fire Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'SignStyle',
                'EUIStatValueSignStyle::Negative'
                )
                mod.newline()

                mod.comment('Changing Overclocked Fire Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'bDisplayPlusSign',
                'false'
                )
                mod.newline()

                mod.comment('Changing Overclocked Fire Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]Fire Rate:[/skillbold] $VALUE$ "
                )
                mod.newline()

            mod.comment('Bullet Damage')
            if True:

                mod.comment('Changing Overclocked Bullet Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Bullet.Att_DamageSourceInstigatorMultiplier_Bullet'
                )
                mod.newline()

                mod.comment('Changing Overclocked Bullet Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'StatusEffectData',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Status_Beastmaster_HitAndRun8.Status_Beastmaster_HitAndRun8'
                )
                mod.newline()

                mod.comment('Changing Overclocked Bullet Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8.Default__Passive_Beastmaster_HitAndRun8_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'FormatText',
                "[skillbold]Gun Damage:[/skillbold] $VALUE$ "
                )
                mod.newline()  

                mod.comment('Changing Overclocked Bullet Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Status_Beastmaster_HitAndRun8',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=/Game/GameData/Weapons/Att_Weapon_FireRate.Att_Weapon_FireRate,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=0.0),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Status_Beastmaster_HitAndRun8.Status_Beastmaster_HitAndRun8:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0"'
                    ),
                    (
                        AttributeData=/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Bullet.Att_DamageSourceInstigatorMultiplier_Bullet,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=0.0),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Status_Beastmaster_HitAndRun8_Triggered.Status_Beastmaster_HitAndRun8_Triggered:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0"'
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Fire Rate After Reloading')
            if True:

                mod.comment('Changing Overclocked Fire Rate')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Status_Beastmaster_HitAndRun8_Triggered',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=/Game/GameData/Weapons/Att_Weapon_FireRate.Att_Weapon_FireRate,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=0.0),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Status_Beastmaster_HitAndRun8_Triggered.Status_Beastmaster_HitAndRun8_Triggered:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0"'
                    )
                )
                """
                )
                mod.newline()

        mod.comment('Turn Tail and Run')
        if True:

            mod.comment('Values Scaling')
            if True:

                mod.comment('Buffing Turn Tail and Run damage reduction')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun5',
                'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
                -0.12
                )
                mod.newline()

                mod.comment('Buffing Turn Tail and Run Move Speed')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun5',
                'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
                0.1
                )
                mod.newline()

                mod.comment('Buffing Turn Tail and Recoil Reduction')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_HitAndRun5',
                'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
                -0.15
                )
                mod.newline()

            mod.comment('Description')
            if True:

                mod.comment('Changing Turn Tail and Run Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C',
                'AbilityDescription',
                "FL4K gains [skillbold]Bonus Movement Speed[/skillbold], while moving he gains [skillbold]Damage Reduction[/skillbold].\n While Still, FL4K gains [skillbold]Increased Gun Damage[/skillbold] and [skillbold]Lowered Recoil[/skillbold]."
                )
                mod.newline()

            mod.comment('Movement Speed')
            if True:

                mod.comment('Giving Turn Tail and Run Bonus Movement Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Attributes/Character/Att_GroundSpeedScale.Att_GroundSpeedScale'
                )
                mod.newline()

                mod.comment('Giving Turn Tail and Run Bonus Movement Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]Movement Speed:[/skillbold] $VALUE$"
                )
                mod.newline()

                mod.comment('Giving Turn Tail and Run Bonus Movement Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Status_Beastmaster_HitAndRun5_Moving',
                'AttributeEffects.AttributeEffects[1].AttributeData',
                '/Game/GameData/Attributes/Character/Att_GroundSpeedScale.Att_GroundSpeedScale'
                )
                mod.newline()

            mod.comment('Recoil Reduction')
            if True:

                mod.comment('Giving Turn Tail and Run Reduced Recoil')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_2',
                'Attribute',
                '/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale.Att_Weapon_RecoilHeightScale'
                )
                mod.newline()

                mod.comment('Giving Turn Tail and Run Bonus Reduced Recoil')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5.Default__Passive_Beastmaster_HitAndRun_5_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_2',
                'FormatText',
                "[skillbold]Recoil Reduction:[/skillbold] $VALUE$"
                )
                mod.newline()

                mod.comment('Giving Turn Tail and Run Bonus Reduced Recoil')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Status_Beastmaster_HitAndRun5_Still',
                'AttributeEffects.AttributeEffects[1].AttributeData',
                '/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale.Att_Weapon_RecoilHeightScale'
                )
                mod.newline()

        mod.comment('The Fast and the Furryous')
        if True:

            mod.comment('Values Scaling')
            if True:
                mod.comment('Buffing The Fast and the Furryous projectile speed bonus')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'HitAndRun_10',
                'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
                0.1
                )
                mod.newline()

            mod.comment('Description')
            if True:

                mod.comment('Changing The Fast and the Furryous Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10.Default__Passive_Beastmaster_HitAndRun10_C',
                'AbilityDescription',
                "While above half health, FL4K's [skillbold]Gun Damage[/skillbold] and [skillbold]Projectile Speed[/skillbold] are increased and their pet gains increased [skillbold]Damage[/skillbold]."
                )
                mod.newline()

            mod.comment('Projectile Speed')
            if True:

                mod.comment('Giving The Fast and the Furryous Bonus Projectile Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10.Default__Passive_Beastmaster_HitAndRun10_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Weapons/Att_Weapon_ProjectileSpeedScale.Att_Weapon_ProjectileSpeedScale'
                )
                mod.newline()

                mod.comment('Giving The Fast and the Furryous Bonus Projectile Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10.Default__Passive_Beastmaster_HitAndRun10_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]Projectile Speed:[/skillbold] $VALUE$"
                )
                mod.newline()

                mod.comment('Giving The Fast and the Furryous Bonus Projectile Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Status_HitAndRun10_WeaponDamage_DA',
                'AttributeEffects.AttributeEffects[1].AttributeData',
                '/Game/GameData/Weapons/Att_Weapon_ProjectileSpeedScale.Att_Weapon_ProjectileSpeedScale'
                )
                mod.newline()

        mod.comment('Buffing Rage and Recover health regen')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun3',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.018
        )
        mod.newline()

        mod.comment('Buffing Rage and Recover health regen')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_HitAndRun3',
        'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
        0.018
        )
        mod.newline()

    mod.comment('Hunter Tree Skills')
    if True:

        mod.comment('Interplanetary Stalker')
        if True:

            mod.comment('Values Scaling')
            if True:

                mod.comment('Interplanetary Stalker AS Damage')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged3',
                'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
                0.05
                )
                mod.newline()

                mod.comment('Interplanetary Stalker Fire Damage')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged3',
                'Radius_11_A1466BA242034461180E58B6E902078D',
                0.02
                )
                mod.newline()

                mod.comment('Interplanetary Stalker Cryo Damage')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged3',
                'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
                0.02
                )
                mod.newline()

                mod.comment('Interplanetary Stalker Corrosive Damage')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged3',
                'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
                0.02
                )
                mod.newline()

            mod.comment('Description')
            if True:

                mod.comment('Adjusting Interplanetary Stalker Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C',
                'AbilityDescription',
                "[skillbold]Hunter Kill Skill[/skillbold]. Whenever FL4K kills an enemy, they gain a stack of [skillbold]Interplanetary Stalker[/skillbold].<br>For each stack of [skillbold]Interplanetary Stalker[/skillbold], they gain [skillbold]Action Skill Damage[/skillbold] and [skillbold]Pet Damage[/skillbold].<br>Additionally, they gain a unique stacking bonus depending on the type of enemy killed. Each unique bonus can stack up to 3 times. Each stack decays after 10 seconds."
                )
                mod.newline()

            mod.comment('Base Attribute')
            if True:

                mod.comment('Interplanetary Stalker Duration')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C',
                'TriggeredEffect.Duration',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=Ranged3_Duration,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveDurationScale.Att_Beastmaster_HuntSkillPassiveDurationScale,
                    AttributeInitializer=None,
                    BaseValueScale=10.0
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Action Skill Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'FormatText',
                "[skillbold]Action Skill Damage:[/skillbold] $VALUE$ per stack"
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Action Skill Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill'
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Action Skill Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA',
                'AttributeEffects.AttributeEffects[0]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Action Skill Damage')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation',
                'AttributeEffects.AttributeEffects[0]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

            mod.comment('Human Bonus')
            if True:
                mod.comment('Giving Interplanetary Stalker Radiation Damage as Human Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "Human Bonus: [skillbold]Radiation Damage:[/skillbold] $VALUE$ per stack"
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Radiation Damage as Human Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Radiation.Att_DamageInstigatorMultiplier_Radiation'
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Radiation Damage as Human Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA.Status_Beastmaster_Ranged3_BulletDamage_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_2',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/DataTable_Ranged3_KillSkillBonuses.DataTable_Ranged3_KillSkillBonuses,RowName=KillSkillBonus_Humanoid,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.02
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Radiation Damage as Human Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA',
                'AttributeEffects.AttributeEffects[1]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Radiation.Att_DamageInstigatorMultiplier_Radiation\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Radiation Damage as Human Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation.Status_Beastmaster_Ranged3_Presentation:Mutator_OakPassiveAbilityAttributeEffectMutatorData_2',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged3,ValueName=Radius_11_A1466BA242034461180E58B6E902078D),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.02
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Radiation Damage as Human Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation',
                'AttributeEffects.AttributeEffects[1]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Radiation.Att_DamageInstigatorMultiplier_Radiation\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

            mod.comment('Robot Bonus')
            if True:
                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "Robot Bonus: [skillbold]Cryo Damage:[/skillbold] $VALUE$ per stack"
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:UIStatData_OakPassiveAbilityAttribute_0',
                'bDisplayPercentAsFloat',
                'false'
                )
                mod.newline()


                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Cryo.Att_DamageInstigatorMultiplier_Cryo'
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA.Status_Beastmaster_Ranged3_BulletDamage_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/DataTable_Ranged3_KillSkillBonuses.DataTable_Ranged3_KillSkillBonuses,RowName=KillSkillBonus_Robot,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.02
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA',
                'AttributeEffects.AttributeEffects[2]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Cryo.Att_DamageInstigatorMultiplier_Cryo\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation.Status_Beastmaster_Ranged3_Presentation:OakPassiveAbilityAttributeEffectMutatorData_0',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged3,ValueName=Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.02
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Corrosive Damage as Robot Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation',
                'AttributeEffects.AttributeEffects[3]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Cryo.Att_DamageInstigatorMultiplier_Cryo\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

            mod.comment('Beast Bonus')
            if True:
                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:UIStatData_OakPassiveAbilityAttribute_1',
                'FormatText',
                "Beast Bonus: [skillbold]Fire Damage:[/skillbold] $VALUE$ per stack"
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:UIStatData_OakPassiveAbilityAttribute_1',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Fire.Att_DamageInstigatorMultiplier_Fire'
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3.Default__Passive_Beastmaster_Ranged3_C:UIStatData_OakPassiveAbilityAttribute_1',
                'bDisplayPercentAsFloat',
                'false'
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA.Status_Beastmaster_Ranged3_BulletDamage_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_1',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/DataTable_Ranged3_KillSkillBonuses.DataTable_Ranged3_KillSkillBonuses,RowName=KillSkillBonus_Beast,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.02
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_BulletDamage_DA',
                'AttributeEffects.AttributeEffects[3]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Fire.Att_DamageInstigatorMultiplier_Fire\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation.Status_Beastmaster_Ranged3_Presentation:Mutator_OakPassiveAbilityAttributeEffectMutatorData_1',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged3,ValueName=Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.02
                )
                """
                )
                mod.newline()

                mod.comment('Giving Interplanetary Stalker Fire Damage as Beast Bonus')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Status_Beastmaster_Ranged3_Presentation',
                'AttributeEffects.AttributeEffects[2]',
                """
                (
                    AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Fire.Att_DamageInstigatorMultiplier_Fire\"',
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=P_Ranged3,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0)    
                )
                """
                )
                mod.newline()

        mod.comment('Second Intention')
        if True:

            mod.comment('Values Scaling')
            if True:
                mod.comment('Second Intention reload speed bonus')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged2',
                'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
                -0.02
                )
                mod.newline()

                mod.comment('Second Intention reload speed bonus')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged2',
                'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
                -0.4
                )
                mod.newline()

                mod.comment('Buffing Second Intention reload Duration')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Ranged2',
                'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
                10.0
                )
                mod.newline()

            mod.comment('Description')
            if True:

                mod.comment('Adjusting Second Intention Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C',
                'AbilityDescription',
                "[skillbold]Hunter Kill Skill[/skillbold]. Whenever FL4K kills an enemy, they gain increased [skillbold]Reload Speed[/skillbold]. <br>This bonus is increased if FL4K scores a [skillbold]Critical Kill[/skillbold]. <br>Stacks up to 3 times."
                )
                mod.newline()

            mod.comment('HUD')
            if True:

                mod.comment('Adjusting Second Intention HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'Attribute',
                '/Game/GameData/Weapons/Att_Weapon_ReloadTime.Att_Weapon_ReloadTime'
                )
                mod.newline()

                mod.comment('Adjusting Second Intention HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'bCalculateWithReductionMath',
                'false'
                )
                mod.newline()

                mod.comment('Adjusting Second Intention HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Weapons/Att_Weapon_ReloadTime.Att_Weapon_ReloadTime'
                )
                mod.newline()

                mod.comment('Adjusting Second Intention HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'bCalculateWithReductionMath',
                'false'
                )
                mod.newline()

                mod.comment('Adjusting Second Intention HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
                'FormatText',
                "[skillbold]Stack Duration:[/skillbold] $VALUE$ seconds"
                )
                mod.newline()

                mod.comment('Adjusting Second Intention HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2.Default__Passive_Beastmaster_Ranged2_C:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
                'Initializer',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged2,ValueName=Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveDurationScale.Att_Beastmaster_HuntSkillPassiveDurationScale,
                    AttributeInitializer=None,
                    BaseValueScale=10.0
                )
                """
                )
                mod.newline()

            mod.comment('Base Attribute')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA',
                'StackingStrategy',
                '/Game/GameData/StackingStrategy/StackingStrategy_Capped_3.StackingStrategy_Capped_3'
                
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA.Status_Beastmaster_Ranged2_ReloadSpeed_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=Ranged2_ReloadSpeed,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=-0.03
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA.Status_Beastmaster_Ranged2_ReloadSpeed_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=Ranged2_ReloadSpeed,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=-0.03
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA.Status_Beastmaster_Ranged2_ReloadSpeed_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_1',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=Ranged2_ReloadSpeed,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=-0.03
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_ReloadTime.Att_Weapon_ReloadTime\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=-0.03),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA.Status_Beastmaster_Ranged2_ReloadSpeed_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'   
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_TapedReloadTime.Att_Weapon_TapedReloadTime\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=-0.03),    
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA.Status_Beastmaster_Ranged2_ReloadSpeed_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0"' 
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_HeatCoolDownRate.Att_Weapon_HeatCoolDownRate\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=-0.03),    
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_ReloadSpeed_DA.Status_Beastmaster_Ranged2_ReloadSpeed_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData_1"' 
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed // HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_DA.Status_Beastmaster_Ranged2_Presentation_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged2,ValueName=Scalar_5_230D633C4A306BF04AB690B7CD89D6AA),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.03
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed // HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_DA',
                'StackingStrategy',
                '/Game/GameData/StackingStrategy/StackingStrategy_Capped_3.StackingStrategy_Capped_3'
                
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed // HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_DA',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_ReloadTime.Att_Weapon_ReloadTime\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0),   
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_DA.Status_Beastmaster_Ranged2_Presentation_DA:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed // HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_Crit.Status_Beastmaster_Ranged2_Presentation_Crit:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged2,ValueName=Scalar_5_230D633C4A306BF04AB690B7CD89D6AA),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.06
                )
                """
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed // HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_Crit',
                'StackingStrategy',
                '/Game/GameData/StackingStrategy/StackingStrategy_Capped_3.StackingStrategy_Capped_3'
                
                )
                mod.newline()

                mod.comment('Second Intention Reload Speed // HUD')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_Crit',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_ReloadTime.Att_Weapon_ReloadTime\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,BaseValueScale=0.0),    
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Status_Beastmaster_Ranged2_Presentation_Crit.Status_Beastmaster_Ranged2_Presentation_Crit:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'
                    )
                )
                """
                )
                mod.newline()

        mod.comment('Hunters Eye')
        if True:

            mod.comment('Description')
            if True:

                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Passive_Beastmaster_Ranged4.Default__Passive_Beastmaster_Ranged4_C',
                'AbilityDescription',
                "[skillbold]Hunter Skill[/skillbold]. FL4K gains [skillbold]bonuses[/skillbold] when fighting different types of enemies.<br>Bosses are not affected."
                )
                mod.newline()
            
            mod.comment('Displaying the Hunter Skills Buff on the Card')
            if True:
                
                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Status_Beastmaster_Ranged4_Presentation_CritDmg.Status_Beastmaster_Ranged4_Presentation_CritDmg:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged4,ValueName=Scalar_5_230D633C4A306BF04AB690B7CD89D6AA),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.03
                )
                """
                )
                mod.newline()

                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Status_Beastmaster_Ranged4_Presentation_CritDmg',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=/Game/PlayerCharacters/_Shared/_Design/Attributes/_Shared/Att_PassiveAbility_TestGrade.Att_PassiveAbility_TestGrade,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged4,ValueName=Scalar_5_230D633C4A306BF04AB690B7CD89D6AA),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.03)
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Status_Beastmaster_Ranged4_Presentation_DmgTaken.Status_Beastmaster_Ranged4_Presentation_DmgTaken:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged4,ValueName=Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=-0.053
                )
                """
                )
                mod.newline()

                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Status_Beastmaster_Ranged4_Presentation_DmgTaken',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=/Game/PlayerCharacters/_Shared/_Design/Attributes/_Shared/Att_PassiveAbility_TestGrade.Att_PassiveAbility_TestGrade,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged4,ValueName=Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=-0.053)
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Status_Beastmaster_Ranged4_Presentation_DmgVsArmor.Status_Beastmaster_Ranged4_Presentation_DmgVsArmor:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged4,ValueName=Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.06
                )
                """
                )
                mod.newline()

                mod.comment('Adjusting Hunters Eye Description')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Status_Beastmaster_Ranged4_Presentation_DmgVsArmor',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=/Game/PlayerCharacters/_Shared/_Design/Attributes/_Shared/Att_PassiveAbility_TestGrade.Att_PassiveAbility_TestGrade,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Ranged4,ValueName=Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.06)
                    )
                )
                """
                )
                mod.newline()

        mod.comment('Buffing Ambush Predator Crit Bonus')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_Ranged5',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.05
        )
        mod.newline()

        mod.comment('The Most Dangerous Game')
        if True:

            mod.comment('HUD')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C',
                'AbilityDescription',
                "[skillbold]Hunter Kill Skill[/skillbold]. Whenever FL4K kills a [skillbold]Badass[/skillbold] or stronger enemy, they gain increased [skillbold]Damage[/skillbold]. Their [skillbold]Gun Damage[/skillbold] and [skillbold]Action Skill Damage[/skillbold] are further increased. <br>Their pet receives increased [skillbold]Damage[/skillbold].<br>They also receive a [skillbold]cash reward[/skillbold] from the Intergalactic Bureau of Bounty Hunting."
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'Attribute',
                '/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier'
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'FormatText',
                "[skillbold]Damage:[/skillbold] $VALUE$"
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:UIStatData_OakPassiveAbilityAttribute_1',
                'Attribute',
                '/Game/GameData/Attributes/Damage/Att_CriticalDamageDealtMultiplier.Att_CriticalDamageDealtMultiplier'
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:UIStatData_OakPassiveAbilityAttribute_0',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill'
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:UIStatData_OakPassiveAbilityAttribute_0',
                'bCalculateWithReductionMath',
                'false'
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]Action Skill Damage:[/skillbold] $VALUE$"
                )
                mod.newline()

            mod.comment('Attributes')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.05)
                    ),
                    (
                        AttributeData=/Game/GameData/Attributes/Damage/Att_CriticalDamageDealtMultiplier.Att_CriticalDamageDealtMultiplier,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.03)
                    ),
                    (
                        AttributeData=/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.05)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Displaying the Hunter Skills Buff on the Card')
            if True:

                mod.comment('Duration')
                if True:

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6.Default__Passive_Beastmaster_Ranged6_C:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
                    'Initializer',
                    """
                    (
                        BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                        BaseValueScale=120.0
                    )
                    """
                    )
                    mod.newline()

                mod.comment('Critical Damage')
                if True:

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_CritDamage_P.Status_Beastmaster_Ranged6_CritDamage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData_1',
                    'PerGradeUpgrade',
                    """
                    (
                        BaseValueConstant=0.0,
                        DataTableValue=(),
                        BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                        AttributeInitializer=None,
                        BaseValueScale=0.03
                    )
                    """
                    )
                    mod.newline()

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_CritDamage_P',
                    'AttributeEffects.AttributeEffects[0]',
                    """
                    (
                        AttributeData=/Game/GameData/Attributes/Damage/Att_CriticalDamageDealtMultiplier.Att_CriticalDamageDealtMultiplier,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.0),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_CritDamage_P.Status_Beastmaster_Ranged6_CritDamage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData_1"'
                    )
                    """
                    )
                    mod.newline()

                mod.comment('Action Skill Damage')
                if True:

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_Handling_P.Status_Beastmaster_Ranged6_Handling_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0',
                    'PerGradeUpgrade',
                    """
                    (
                        BaseValueConstant=0.0,
                        DataTableValue=(),
                        BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                        AttributeInitializer=None,
                        BaseValueScale=0.05
                    )
                    """
                    )
                    mod.newline()

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_Handling_P',
                    'AttributeEffects.AttributeEffects[0]',
                    """
                    (
                        AttributeData=/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.0),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_Handling_P.Status_Beastmaster_Ranged6_Handling_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData_0"'
                    )
                    """
                    )
                    mod.newline()

                mod.comment('All Damage')
                if True:

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_WeapDamage_P.Status_Beastmaster_Ranged6_WeapDamage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                    'PerGradeUpgrade',
                    """
                    (
                        BaseValueConstant=0.0,
                        DataTableValue=(),
                        BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                        AttributeInitializer=None,
                        BaseValueScale=0.05
                    )
                    """
                    )
                    mod.newline()

                    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_WeapDamage_P',
                    'AttributeEffects.AttributeEffects[0]',
                    """
                    (
                        AttributeData=/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.0),
                        Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Status_Beastmaster_Ranged6_WeapDamage_P.Status_Beastmaster_Ranged6_WeapDamage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'
                    )
                    """
                    )
                    mod.newline()

    mod.comment('Master Tree Skills')
    if True:

        mod.comment('Buffing He Bites Reflected Damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'P_Bond11',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.25
        )
        mod.newline()

        mod.comment('Frenzy')
        if True:

            mod.comment('Displaying the Hunter Skills Buff on the Card')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond_Frenzy/Status_BondFrenzy_Damage_P.Status_BondFrenzy_Damage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData',
                'PerGradeUpgrade',
                """
                (
                    BaseValueConstant=0.0,
                    DataTableValue=(),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.008
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond_Frenzy/Status_BondFrenzy_Damage_P',
                'AttributeEffects.AttributeEffects[0]',
                """
                (
                    AttributeData=/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier,
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=P_Frenzy,ValueName=Scalar_5_230D633C4A306BF04AB690B7CD89D6AA),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale,AttributeInitializer=None,BaseValueScale=0.0),
                    Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond_Frenzy/Status_BondFrenzy_Damage_P.Status_BondFrenzy_Damage_P:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'
                )                
                """
                )
                mod.newline()
            
        mod.comment('Who Rescued Who ?')
        if True:

            mod.comment('Values Scaling')
            if True:

                mod.comment('Buffing Who Rescued Who ? health regen')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Bond3',
                'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
                0.015
                )
                mod.newline()

                mod.comment('Buffing Who Rescued Who ? health regen')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
                'P_Bond3',
                'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
                1.0
                )
                mod.newline()

            mod.comment('Description')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond3/Passive_Beastmaster_Bond3.Default__Passive_Beastmaster_Bond3_C',
                'AbilityDescription',
                "Whenever FL4K's [actionskill]Pet[/actionskill] deals damage, a portion of FL4K's [skillbold]health[/skillbold] is restored. Whenever FL4K deals damage to an enemy, their [actionskill]Pet's[/actionskill] health is restored for a portion of the damage dealt."
                )
                mod.newline()

            mod.comment('Attributes')
            if True:

                mod.comment('Giving Who Rescued Who ? life steal')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond3/Passive_Beastmaster_Bond3.Default__Passive_Beastmaster_Bond3_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
                'FormatText',
                "[skillbold]FL4K's Health restored:[/skillbold] $VALUE$"
                )
                mod.newline()

    mod.comment('Trapper Tree Skills')
    if True:

        mod.comment('Success Imminent')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCSimpleFormulas',
            'DLCSkill2_NovaDamageCalc',
            'Level',
            """
            (
                BaseValueConstant=0.0,
                BaseValueAttribute=/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Shield.Att_DamageSourceInstigatorMultiplier_Shield,
                BaseValueScale=0.15
            )
            """
            )
            mod.newline()

        mod.comment('Better Toys')
        if True:

            mod.comment('HUD')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/DLCSkill_04/Passive_Beastmaster_DLCSkill_4.Default__Passive_Beastmaster_DLCSkill_4_C',
                'AbilityDescription',
                "FL4K and their [actionskill]Pet[/actionskill] gain increased [skillbold]Shield Recharge Delay[/skillbold] and improved [skillbold]Shield Damage Effects[/skillbold]."
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/DLCSkill_04/Passive_Beastmaster_DLCSkill_4.Default__Passive_Beastmaster_DLCSkill_4_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'Attribute',
                '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Shield.Att_DamageSourceInstigatorMultiplier_Shield'
                )
                mod.newline()

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/DLCSkill_04/Passive_Beastmaster_DLCSkill_4.Default__Passive_Beastmaster_DLCSkill_4_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
                'FormatText',
                "[skillbold]Shield Damage Effects:[/skillbold] $VALUE$"
                )
                mod.newline()
            
            mod.comment('Attributes')
            if True:

                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/DLCSkill_04/StatusEffect_Beastmaster_DLCSkill_4',
                'AttributeEffects.AttributeEffects[0]',
                """
                (
                    AttributeData=/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Shield.Att_DamageSourceInstigatorMultiplier_Shield,
                    ModifierType=EGbxAttributeModifierType::Scale,
                    BaseModifierValue=(BaseValueConstant=0.0,DataTableValue=(),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0.0),
                    Mutator=OakPassiveAbilityAttributeEffectMutatorData'"/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/DLCSkill_04/StatusEffect_Beastmaster_DLCSkill_4.StatusEffect_Beastmaster_DLCSkill_4:Mutator_OakPassiveAbilityAttributeEffectMutatorData"'
                )                
                """
                )
                mod.newline()

            mod.comment('Values Scaling')
            if True:

                mod.comment('Recharge Delay')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
                'DLCSkill4_ShieldRegenDelay',
                'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
                -0.12
                )
                mod.newline()

                mod.comment('Shield Effect Damage')
                mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
                'DLCSkill4_ShieldRegenRate',
                'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
                0.1
                )
                mod.newline()

        mod.comment('EXP Loader')
        if True:

            mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
            '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCSimpleFormulas',
            'Ability_Loader_EXPLode',
            'Multiplier',
            '(BaseValueConstant=3.8)'
            )
            mod.newline()

        mod.comment('Buffing Keep Then Safe Cooldown')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
        'DLCSkill15_CooldownTime',
        'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
        6.0
        )
        mod.newline()

mod.comment('Augment')
if True:

    mod.comment('Stalker Tree Augments')
    if True:

        mod.comment('Buffing Guerillas in the Mist damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Ultimate_Spiderant_Mod3',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.50
        )
        mod.newline()

        mod.comment('Buffing Guerillas in the Mist duration')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Ultimate_Spiderant_Mod3',
        'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
        8
        )
        mod.newline()

        mod.comment('Buffing Not My Circus duration')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Ultimate_Spiderant_Mod1',
        'Cooldown_8_237733FC43C8C6F2B3A6558D8A0FB0C1',
        8
        )
        mod.newline()

    mod.comment('Hunter Tree Augments')
    if True:

        mod.comment('Buffing Rakk Attack base damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Ultimate_Skag',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.85
        )
        mod.newline()

        mod.comment('Buffing Falconers Feast heal percent')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Ultimate_Skag_Mod1',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.15
        )
        mod.newline()

        mod.comment('Double the ammount of rakks instead of +1 charge')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/StatusEffects/StatusEffect_Mod3_AdditionalCharge',
        'AttributeEffects.AttributeEffects[0]',
        """
        (
            AttributeData=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/Att_Beastmaster_RakkAttack_MaxCharges.Att_Beastmaster_RakkAttack_MaxCharges,
            ModifierType=EGbxAttributeModifierType::Scale,
            BaseModifierValue=(BaseValueConstant=1.0)
        )
        """
        )
        mod.newline()

        mod.comment('Double the ammount of rakks instead of +1 charge')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Augments/Augment_Beastmaster_RakkAttack_Mod3',
        'Description',
        "FL4K's [actionskill]Rakk[/actionskill] gain [skillbold]Double The Amount Of Charges[/skillbold]."
        )
        mod.newline()

        mod.comment('Removing text for the +1 charge')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Augments/Augment_Beastmaster_RakkAttack_Mod3.Augment_Beastmaster_RakkAttack_Mod3:StatDataItems_UIStatData_Text',
        'Text',
        ''
        )
        mod.newline()

        mod.comment('Removing CD')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Augments/Augment_Beastmaster_RakkAttack_Mod3.Augment_Beastmaster_RakkAttack_Mod3:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
        'Initializer',
        """
        (
            DataTableValue=()
        )
        """
        )
        mod.newline()

        mod.comment('Removing CD')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Augments/Augment_Beastmaster_RakkAttack_Mod3.Augment_Beastmaster_RakkAttack_Mod3:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
        'FormatText',
        ''
        )
        mod.newline()

    mod.comment('Master Tree Augments')
    if True:

        mod.comment('Buffing Atomic Aroma damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Skill_PetEnrage_Mod2',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.18
        )
        mod.newline()

        mod.comment('Endurance')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill3_LightningTrap/StatusEFfect/Status_HulkOut_Pet_DamageBuff_Mod3',
        'StackingStrategy',
        '/Game/GameData/StackingStrategy/StackingStrategy_Infinite.StackingStrategy_Infinite'
        )
        mod.newline()

        mod.comment('Endurance')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill3_LightningTrap/Augments/Augment_Beastmaster_Enrage_Mod3',
        'Description',
        "When FL4K or FL4K's [actionskill]Pet[/actionskill] kills an enemy while [actionskill]Gamma Burst[/actionskill] is active, the duration of [actionskill]Gamma Burst[/actionskill] is extended and pet damage is increased."
        )
        mod.newline()

        mod.comment('Endurance Damage')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Skill_PetEnrage_Mod3',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.05
        )
        mod.newline()

        mod.comment('Endurance Duration')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Skill_PetEnrage_Mod3',
        'Secondary_21_5ED678CA4FB7C9C602D841A55EDD67B9',
        1.0
        )
        mod.newline()

        mod.comment('Endurance Stack Limit')
        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Skill_PetEnrage_Mod3',
        'Tertiary_20_8B581C1746A7BAAB3F3F7BA08BD29453',
        500000.0
        )
        mod.newline()
    
    mod.comment('Trapper Tree Augments')
    if True:

        mod.comment('Forage drop ammo less often')
        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/ActionSkill/Defs/ItemPool_Beastmaster_Mod5',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Pickups/Health/DA_InventoryBalance_Health.DA_InventoryBalance_Health,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Health/DA_InventoryBalance_Health.DA_InventoryBalance_Health\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_AllAmmo.DA_InventoryBalance_Ammo_AllAmmo,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_AllAmmo.DA_InventoryBalance_Ammo_AllAmmo\"',
                Weight=(BaseValueConstant=0.5,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/ActionSkill/Defs/InvBal_Beastmaster_Mod5ShieldBooster.InvBal_Beastmaster_Mod5ShieldBooster,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/ActionSkill/Defs/InvBal_Beastmaster_Mod5ShieldBooster.InvBal_Beastmaster_Mod5ShieldBooster\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues',
        'Trap_PulseTime',
        'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
        2.0
        )
        mod.newline()

mod.comment('Pets')
if True:

    mod.comment('Pet Bonuses and Scaling')
    if True:

        mod.comment('Skags')
        if True:

            mod.comment('Base')
            if True:

                mod.comment('Skags')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/StatusEffects/Status_Beastmaster_PetSkagBuff_Base',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_ActionSkill_Beastmaster_SkillCooldownRate_Skill3.Att_ActionSkill_Beastmaster_SkillCooldownRate_Skill3\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSkag_Base,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.2)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Evo1')
            if True:

                mod.comment('Skags')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/StatusEffects/Status_Beastmaster_PetSkagBuff_Evo1',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=None,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=1.0)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Melee.Att_DamageSourceInstigatorMultiplier_Melee\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSkag_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.3)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Evo2')
            if True:

                mod.comment('Skags')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Skag/_Design/StatusEffects/Status_Beastmaster_PetSkagBuff_Evo2',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=None,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=1.0)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Radiation.Att_DamageInstigatorMultiplier_Radiation\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSkag_Evo2,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    )
                )
                """
                )
                mod.newline()

        mod.comment('Spiderants')
        if True:

            mod.comment('Base')
            if True:

                mod.comment('Spiderants')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/StatusEffects/Status_Beastmaster_PetSpidBuff_Base',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Base,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.2)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Evo1')
            if True:

                mod.comment('Spiderant')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/StatusEffects/Status_Beastmaster_PetSpidBuff_Evo1',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=None,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=1.0)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Corrosive.Att_DamageInstigatorMultiplier_Corrosive\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.1)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Cryo.Att_DamageInstigatorMultiplier_Cryo\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.1)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Fire.Att_DamageInstigatorMultiplier_Fire\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.1)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Radiation.Att_DamageInstigatorMultiplier_Radiation\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.1)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Shock.Att_DamageInstigatorMultiplier_Shock\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.1)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Evo2')
            if True:

                mod.comment('Spiderant')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Spiderant/_Design/StatusEffects/Status_Beastmaster_PetSpidBuff_Evo2',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=None,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=1.0)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetSpid_Evo2,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    )
                )
                """
                )
                mod.newline()

        mod.comment('Jabbers')
        if True:

            mod.comment('Base')
            if True:

                mod.comment('Jabbers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/StatusEffects/Status_Beastmaster_PetJabbBuff_Base',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/PlayerCharacters/_Shared/_Design/Attributes/_Shared/Att_Players_Slide_SpeedScale.Att_Players_Slide_SpeedScale\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetJabb_Base,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.3)
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Base Initializers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon.Augment_Pet_Jabbermon:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
                'Initializer',
                """
                (
                    BaseValueConstant=1.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=PlayerBuff_PetJabb_Base,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.3
                )
                """
                )
                mod.newline()

            mod.comment('Evo1')
            if True:

                mod.comment('Jabbers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/StatusEffects/Status_Beastmaster_PetJabbBuff_Evo1',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=None,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=1.0)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/Character/Att_GroundSpeedScale.Att_GroundSpeedScale\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetJabb_Evo1,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale',BaseValueScale=0.15)
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Evo1 Initializers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Beefcake.Augment_Pet_Jabbermon_Beefcake:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
                'Initializer',
                """
                (
                    BaseValueConstant=1.0,
                    DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                    BaseValueAttribute=None,
                    AttributeInitializer=None,
                    BaseValueScale=1.0
                )
                """
                )
                mod.newline()

                mod.comment('Evo1 Initializers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Beefcake.Augment_Pet_Jabbermon_Beefcake:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer_0',
                'Initializer',
                """
                (
                    BaseValueConstant=1.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=PlayerBuff_PetJabb_Evo1,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.15
                )
                """
                )
                mod.newline()

            mod.comment('Evo2')
            if True:

                mod.comment('Jabbers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/StatusEffects/Status_Beastmaster_PetJabbBuff_Evo2',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=None,
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,BaseValueScale=1.0)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_ProjectileSpeedScale.Att_Weapon_ProjectileSpeedScale\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SimpleFormulas.DataTable_Beastmaster_SimpleFormulas,RowName=PlayerBuff_PetJabb_Evo2,ValueName=None),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    )
                )
                """
                )
                mod.newline()

                mod.comment('Evo2 Initializers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Gunslinger.Augment_Pet_Jabbermon_Gunslinger:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
                'Initializer',
                """
                (
                    BaseValueConstant=1.0,
                    DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                    BaseValueAttribute=None,
                    AttributeInitializer=None,
                    BaseValueScale=1.0
                )
                """
                )
                mod.newline()

                mod.comment('Evo2 Initializers')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Gunslinger.Augment_Pet_Jabbermon_Gunslinger:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer_0',
                'Initializer',
                """
                (
                    BaseValueConstant=1.0,
                    DataTableValue=(DataTable=/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance.DataTable_Beastmaster_SkillBalance,RowName=PlayerBuff_PetJabb_Evo2,ValueName=None),
                    BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,
                    AttributeInitializer=None,
                    BaseValueScale=0.15
                )
                """
                )
                mod.newline()

        mod.comment('Loaders')
        if True:

            mod.comment('Base')
            if True:

                mod.comment('Loaders')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/StatusEffects/Status_Beastmaster_PetLoaderBuff_Evo1',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageReceiverMultiplier_Corrosive.Att_DamageReceiverMultiplier_Corrosive\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo1,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageReceiverMultiplier_Cryo.Att_DamageReceiverMultiplier_Cryo\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo1,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageReceiverMultiplier_Fire.Att_DamageReceiverMultiplier_Fire\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo1,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageReceiverMultiplier_Radiation.Att_DamageReceiverMultiplier_Radiation\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo1,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/DamageMultipliers/Att_DamageReceiverMultiplier_Shock.Att_DamageReceiverMultiplier_Shock\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo1,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Evo1')
            if True:

                mod.comment('Loaders')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/StatusEffects/Status_Beastmaster_PetLoaderBuff_Base',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Attributes/Shield/Att_ShieldMaxValue.Att_ShieldMaxValue\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Base,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.15)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Evo2')
            if True:

                mod.comment('Loaders')
                mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
                '/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/StatusEffects/Status_Beastmaster_PetLoaderBuff_Evo2',
                'AttributeEffects',
                """
                (
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_FireRate.Att_Weapon_FireRate\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo2,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.12)
                    ),
                    (
                        AttributeData=GbxAttributeData'\"/Game/GameData/Weapons/Att_Weapon_BurstFireDelay.Att_Weapon_BurstFireDelay\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        BaseModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Passives/Table_Beastmaster_DLCPassiveConstantValues.Table_Beastmaster_DLCPassiveConstantValues,RowName=PlayerBuff_PetLoader_Evo2,ValueName=Base_17_28B25EC8493D1EB6C2138A962F659BCD),BaseValueAttribute=/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_PetBuffPassiveScale.Att_Beastmaster_PetBuffPassiveScale,BaseValueScale=0.12)
                    )
                )
                """
                )
                mod.newline()

    #Global pet damage

    mod.comment('Buffing global pet skill damage')
    mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
    'Global_Pet_SkillDamage',
    'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
    35.0
    )
    mod.newline()

    mod.comment('Buffing global pet melee damage')
    mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
    'Global_Pet_MeleeDamage',
    'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
    12.0
    )
    mod.newline()

    mod.comment('Buffing global pet ranged damage')
    mod.table_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
    'Global_Pet_RangedAttack',
    'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
    0.6
    )
    mod.newline()

    ###SKAGS

    mod.comment('Description for The Base Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag',
    'Description',
    "FL4K is joined by a loyal [Actionskill]Skag[/Actionskill] companion, which gets an increased Gamma Burst [skillbold]Cooldown Rate[/skillbold].<br><br>Hold {OakPC_ActionSkill} to issue an [skillbold]Attack Command[/skillbold], which will cause the [Actionskill]Skag[/Actionskill] to vomit acid onto enemies."
    )
    mod.newline()

    mod.comment('Description for The Base Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag.Augment_Pet_Skag:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'FormatText',
    "[skillbold]Gamma Burst Cooldown Rate:[/skillbold] $VALUE$"
    )
    mod.newline()

    mod.comment('Giving The Base Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag.Augment_Pet_Skag:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'Attribute',
    '/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_ActionSkill_Beastmaster_SkillCooldownRate_Skill3.Att_ActionSkill_Beastmaster_SkillCooldownRate_Skill3'
    )
    mod.newline()

    mod.comment('Description for The Evo1 Skag Bonus Melee Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_GreatHorned',
    'Description',
    "FL4K's [Actionskill]Skag[/Actionskill] evolves into a larger, [Actionskill]Great Horned Skag[/Actionskill] which will increase FL4K's [skillbold]Melee Damage[/skillbold].<br><br>When FL4K issues an [skillbold]Attack Command[/skillbold], the Great Horned Skag will charge at enemies and knock them into the air."
    )
    mod.newline()

    mod.comment('Removing The Evo1 Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_GreatHorned.Augment_Pet_Skag_GreatHorned:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
    'FormatText',
    ""
    )
    mod.newline()

    mod.comment('Removing The Evo1 Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_GreatHorned.Augment_Pet_Skag_GreatHorned:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
    'Attribute',
    ''
    )
    mod.newline()

    mod.comment('Description for The Evo1 Skag Bonus Melee Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_GreatHorned.Augment_Pet_Skag_GreatHorned:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'FormatText',
    "[skillbold]Melee Damage[/skillbold]: $VALUE$"
    )
    mod.newline()

    mod.comment('Giving The Evo1 Skag Bonus Melee Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_GreatHorned.Augment_Pet_Skag_GreatHorned:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'Attribute',
    '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Melee.Att_DamageSourceInstigatorMultiplier_Melee'
    )
    mod.newline()

    mod.comment('Description for The Evo2 Skag Bonus Radiation Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_Badass',
    'Description',
    "FL4K's [actionskill]Skag[/actionskill] evolves into an [actionskill]Eridian Skag[/actionskill], which will increase FL4K's [skillbold]Radiation Damage[/skillbold].<br><br>When FL4K issues an [skillbold]Attack Command[/skillbold], their [actionskill]Eridian Skag[/actionskill] pulls nearby enemies in by generating a [skillbold]Singularity[/skillbold]."
    )
    mod.newline()

    mod.comment('Removing The Evo2 Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_Badass.Augment_Pet_Skag_Badass:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
    'FormatText',
    ""
    )
    mod.newline()

    mod.comment('Removing The Evo2 Skag Bonus Pet Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_Badass.Augment_Pet_Skag_Badass:StatDataItems_UIStatData_OakPassiveAbilityAttribute_0',
    'Attribute',
    ''
    )
    mod.newline()

    mod.comment('Description for The Evo2 Skag Bonus Radiation Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_Badass.Augment_Pet_Skag_Badass:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'FormatText',
    "[skillbold]Radiation Damage[/skillbold]: $VALUE$"
    )
    mod.newline()

    mod.comment('Giving The Evo2 Skag Bonus Radiation Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Skag_Badass.Augment_Pet_Skag_Badass:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'Attribute',
    '/Game/GameData/Attributes/DamageMultipliers/Att_DamageInstigatorMultiplier_Radiation.Att_DamageInstigatorMultiplier_Radiation'
    )
    mod.newline()

    #SPIDERANTS

    mod.comment('Description for The Base Spiderant Bonus Action Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant',
    'Description',
    "FL4K is joined by a loyal [actionskill]Spiderant[/actionskill] companion, which will cause FL4K to gain increased [skillbold]Action Skill Damage[/skillbold].<br><br>Hold {OakPC_ActionSkill} to issue an [skillbold]Attack Command[/skillbold], which will cause the [Actionskill]Spiderant[/Actionskill] to charge into enemies."
    )
    mod.newline()

    mod.comment('Description for The Base Spiderant Bonus Action Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant.Augment_Pet_Spiderant:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'FormatText',
    "[skillbold]Action SKill Damage[/skillbold]: $VALUE$"
    )
    mod.newline()

    mod.comment('Giving The Base Spiderant Bonus Action Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant.Augment_Pet_Spiderant:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'Attribute',
    '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Skill.Att_DamageSourceInstigatorMultiplier_Skill'
    )
    mod.newline()

    mod.comment('Description for The Evo1 Spiderant Bonus Elemental Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_Badass',
    'Description',
    "FL4K's [actionskill]Spiderant[/actionskill] evolves into a [actionskill]Scorcher[/actionskill], occasionally dealing Incendiary Damage to all enemies nearby. While accompanied by the [actionskill]Scorcher[/actionskill], FL4K gains increased [skillbold]Elemental Damage[/skillbold].<br><br>When FL4K issues an [skillbold]Attack Command[/skillbold], the [actionskill]Scorcher[/actionskill] will charge enemies."
    )
    mod.newline()

    mod.comment('Description for The Evo1 Spiderant Bonus Elemental Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_Badass.Augment_Pet_Spiderant_Badass:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'FormatText',
    ""
    )
    mod.newline()

    mod.comment('Giving The Base Spiderant Bonus Action Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_Badass.Augment_Pet_Spiderant_Badass:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'Attribute',
    ''
    )
    mod.newline()

    mod.comment('Description for The Evo2 Spiderant Bonus Hunt Skill Efficienty')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_King',
    'Description',
    "FL4K's [actionskill]Spiderant[/actionskill] evolves into a [actionskill]Countess[/actionskill], which will cause FL4K to gain increased [skillbold]Hunter Skill Effects[/skillbold].<br><br>When FL4K issues an [skillbold]Attack Command[/skillbold], the [actionskill]Countess[/actionskill] will burrow underground and then emerge dealing [skillbold]Corrosive Damage[/skillbold] in an area."
    )
    mod.newline()

    mod.comment('Removing The Evo2 Spiderant Bonus Action Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_King.Augment_Pet_Spiderant_King:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'FormatText',
    ''
    )
    mod.newline()

    mod.comment('Removing The Evo2 Spiderant Bonus Action Skill Damage')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_King.Augment_Pet_Spiderant_King:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    'Attribute',
    ''
    )
    mod.newline()

    mod.comment('Giving The Evo2 Spiderant Bonus Hunter Skill Effect')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_King.Augment_Pet_Spiderant_King:UIStatData_OakPassiveAbilityAttribute_0',
    'FormatText',
    "[skillbold]Hunter Skill Effects[/skillbold]: $VALUE$"
    )
    mod.newline()

    mod.comment('Giving The Evo2 Spiderant Bonus Hunter Skill Effect')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Spiderant_King.Augment_Pet_Spiderant_King:UIStatData_OakPassiveAbilityAttribute_0',
    'Attribute',
    '/Game/PlayerCharacters/_Shared/_Design/Attributes/Beastmaster/Att_Beastmaster_HuntSkillPassiveScale.Att_Beastmaster_HuntSkillPassiveScale'
    )
    mod.newline()

    ###JABBERS

    mod.comment('Description for The Base Jabber Bonus Slide Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon',
    'Description',
    "FL4K is joined by a loyal [actionskill]Jabber[/actionskill] companion, armed with a [skillbold]Pistol[/skillbold]. While accompanied by the [actionskill]Jabber[/actionskill], FL4K's [skillbold]Slide Speed[/skillbold] is increased.<br><br>Hold {OakPC_ActionSkill} to issue an [skillbold]Attack Command[/skillbold], which will cause the [Actionskill]Jabber[/Actionskill] to throw a [skillbold]Radiation Barrel[/skillbold] at enemies."
    )
    mod.newline()

    mod.comment('Description for The Base Jabber Bonus Slide Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon.Augment_Pet_Jabbermon:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
    'FormatText',
    "[skillbold]Slide Speed[/skillbold]: $VALUE$"
    )
    mod.newline()

    mod.comment('Description for The Evo1 Jabber Bonus Movement Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Beefcake',
    'Description',
    "FL4K's [Actionskill]Jabber[/Actionskill] evolves into a [Actionskill]Beefcake[/Actionskill], discarding its pistol and equipping a [skillbold]Shotgun[/skillbold]. While accompanied by the [Actionskill]Beefcake[/Actionskill], FL4K gains increased [skillbold]Movement Speed[/skillbold].<br><br>When FL4K issues an [skillbold]Attack Command[/skillbold], the [Actionskill]Beefcake[/Actionskill] will summon a melee weapon to deliver a powerful attack that [skillbold]knocks enemies back[/skillbold]."
    )
    mod.newline()

    mod.comment('Description for The Evo1 Jabber Bonus Movement Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Beefcake.Augment_Pet_Jabbermon_Beefcake:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
    'FormatText',
    ""
    )
    mod.newline()

    mod.comment('Description for The Evo1 Jabber Bonus Movement Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Beefcake.Augment_Pet_Jabbermon_Beefcake:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer_0',
    'FormatText',
    "[skillbold]Movement Speed[/skillbold]: $VALUE$"
    )
    mod.newline()

    mod.comment('Description for The Evo2 Jabber Bonus Projectile Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Gunslinger',
    'Description',
    "FL4K's [actionskill]Jabber[/actionskill] upgrades his gear and equips an [skillbold]SMG[/skillbold]. While accompanied by the [actionskill]Gunslinger[/actionskill], FL4K gains increased [skillbold]Projectile Speed[/skillbold].<br><br>When FL4K issues an [skillbold]Attack Command[/skillbold], the [actionskill]Gunslinger[/actionskill] equips a [skillbold]Rocket Launcher[/skillbold] to attack the target."
    )
    mod.newline()

    mod.comment('Description for The Evo2 Jabber Bonus Projectile Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Gunslinger.Augment_Pet_Jabbermon_Gunslinger:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer',
    'FormatText',
    ""
    )
    mod.newline()

    mod.comment('Description for The Evo2 Jabber Bonus Projectile Speed')
    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/Augment_Pet_Jabbermon_Gunslinger.Augment_Pet_Jabbermon_Gunslinger:StatDataItems_UIStatData_OakPassiveAbilityAttributeInitializer_0',
    'FormatText',
    "[skillbold]Projectile Speed[/skillbold]: $VALUE$"
    )
    mod.newline()