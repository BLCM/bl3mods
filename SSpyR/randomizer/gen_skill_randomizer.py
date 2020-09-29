from bl3hotfixmod import Mod
from bl3data import BL3Data
import random

#No way to really restructure each time, will need to just re-build the mod each time
#Find a way for ItemFrameName to work cross class (Doesn't look like you can? Just do blanks)

mod=Mod('skill_randomizer.bl3hotfix',
'Skill Randomizer',
'SSpyR',
[
    'A supplement mod to my Runtime Randomizer mod that',
    'will randomize skills on your character with skills from all VHs.'
],
lic=Mod.CC_BY_SA_40,
cats='skill-system'
)

data=BL3Data()

#EXAMPLES
#mod.reg_hotfix(Mod.PATCH, '',
#            '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
#            'Tiers.Tiers[1].Object..Items.Items[1].Object..AbilityClass',
#            Mod.get_full_cond('/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/RootToRise/PassiveSkill_Siren_RootToRise.PassiveSkill_Siren_RootToRise_C', 'BlueprintGeneratedClass'))

#mod.reg_hotfix(Mod.PATCH, '',
#            '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
#            'Tiers.Tiers[1].Object..Items.Items[1].Object..ItemFrameName',
#            'rootsToRise')


skilltrees=[
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_Bond',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_HitAndRun',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkill/SkillTree/AbilityTree_Branch_RangedSupport',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_Explosions',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_Guardian',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/Inventory/AbilityTree_Operative_Gadgeteer',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/Inventory/AbilityTree_Operative_Hitman',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/Inventory/AbilityTree_Operative_Rampart',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_FistOfTheElements',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_MysticalAssault'
    ]

skills=[
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond1/Passive_Beastmaster_Bond_1',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond10/Passive_Beastmaster_Bond10',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond11/Passive_Beastmaster_Bond11',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond3/Passive_Beastmaster_Bond3',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond4/Passive_Beastmaster_Bond4',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond5/Passive_Beastmaster_Bond5',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond7/Passive_Beastmaster_Bond7',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond8/Passive_Beastmaster_Bond8',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond9/Passive_Beastmaster_Bond9',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond_Frenzy/Passive_Beastmaster_Bond_Frenzy',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun6/Passive_Beastmaster_HitAndRun',
    '/Game/PlayerCharacters/Beastmaster/Pet/_Shared/_Design/Abilities/Ability_PetShared_GeneticLink',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Bond2/Passive_Beastmaster_Bond2',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun1/Passive_Beastmaster_HitAndRun_1',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun10/Passive_Beastmaster_HitAndRun10',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun11/Passive_Beastmaster_HitAndRun11',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun2/Passive_Beastmaster_HitAndRun_2',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun3/Passive_Beastmaster_HitAndRun_3',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun4/Passive_Beastmaster_HitAndRun_4',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun5/Passive_Beastmaster_HitAndRun_5',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun7/Passive_Beastmaster_HitAndRun_7',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun8/Passive_Beastmaster_HitAndRun8',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/HitAndRun9/Passive_Beastmaster_HitAndRun9_NotBroken',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged1/Passive_Beastmaster_Ranged1',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged10/Passive_Beastmaster_Ranged10_NEW',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged11/Passive_Beastmaster_Ranged11',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged2/Passive_Beastmaster_Ranged2',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged3/Passive_Beastmaster_Ranged3',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged4/Passive_Beastmaster_Ranged4',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged5/Passive_Beastmaster_Ranged5',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged6/Passive_Beastmaster_Ranged6',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged7/Passive_Beastmaster_Ranged7',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged8/Passive_Beastmaster_Ranged8',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged9/Passive_Beastmaster_Ranged9',
    '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Passives/Ranged_Capstone/Passive_Beastmaster_Ranged_Capstone',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/AmmoRegen/Passive_Gunner_Forge',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/BotJockBlitz/Passive_Gunner_BotJockBlitz',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/PassiveSkill_Gunner_ClickClick',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/CloudOfLead/PassiveSkill_Gunner_CloudOfLead',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/MatchedSet/Passive_Gunner_MatchedSet',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/Redistribution/Passive_Gunner_Redistribution',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ScorchingRPMs/PassiveSkill_Gunner_ScorchingRPM',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/Scrappy/PassiveSkill_Gunner_Scrappy',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/SomeForTheRoad/Passive_Gunner_SomeForTheRoad',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/StokeTheEmbers/PassiveSkill_Gunner_StokeTheEmbers',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/TheIronBank/PassiveSkill_Gunner_TheIronBank',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/AceUpIronBear/PassiveSkill_Gunner_AceUpIronBear',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/FireInTheSkagDen/PassiveSkill_Gunner_FireInSkagDen',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/FiveYearPlan/Passive_Gunner_ExplosivePuncutation',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/GrenadeCrit/PassiveSkill_Gunner_GrenadeCrit',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/Grizzled/PassiveSkill_Gunnerner_Grizzled',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/MeansOfDestruction/PassiveSkill_Gunner_MeansOfDestruction',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/NewDemoPassive/Passive_Gunner_Vampyr',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/NewDemoPassive2/Passive_Gunner_TorgueCrossPromo',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/ShortFuse/PassiveSkill_IronBear_ShortFuse',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/StainlessSteelBear/PassiveSkill_Gunner_StainlessSteelBear',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/SteelHardpoints/Passive_Gunner_Deadlines',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_DemolitionWoman/WhyCantICarryAllTheseGrenades/PassiveSkill_Gunner_WhyCantICarryAllTheseGrenades',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/ArmoredInfantry/Passive_Gunner_ArmoredInfantry',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/BehindTheIronCurtain/PassiveSkill_Gunner_BehindTheIronCurtain_New',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/DrowningInBrass/PassiveSkill_Gunner_DrowningInBrass',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/ExperimentalMunitions/Passive_Gunner_ExperimentalMunitions',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/ForceFeedback/PassiveSkill_Gunner_ForceFeedback',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/FullCan/Passive_Gunner_FullCan',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/PassiveSkill_Gunner_LowHPDamage',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/PhalanxDoctrine/Passive_Gunner_PhalanxDoctrine',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/SelflessVengeance/Passive_Gunner_SelflessVengeance',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/ShieldCapacity/Passive_Gunner_ThinRedLine',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Passive_Gunner_Tenacious',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/VladofIngenuity/PassiveSkill_Gunner_VladofIngenuity',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/AbstractGrenades/PassiveSkill_Operative_AbstractGrenades',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/BoomEnhance/PassiveSkill_Operative_BoomEnhance',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/BorrowedTime/PassiveSkill_Operative_BorrowedTime',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/Donnybrook/PassiveSkill_Operative_Donnybrook',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/DuctTapeMod/PassiveSkill_Operative_DuctTapeMod',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/LikeAGhost/PassiveSkill_Operative_LikeAGhost',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/MultiTasker/PassiveSkill_Operative_Multitasker',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/PocketFullOfGrenades/PassiveSkill_Operative_PocketFullOfGrenades',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/Praemunitus/PassiveSkill_Operative_Praemunitus',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/SupersonicMan/PassiveSkill_Operative_SupersonicMan',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/TrickOfTheLight/PassiveSkill_Operative_TrickOfTheLight',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/ColdBore/PassiveSkill_Operative_ColdBore',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/CoolHand/PassiveSkill_Operative_CoolHand',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/DeathFollowsClose/PassiveSkill_Operative_DeathFollowsClose',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/GoodMisfortune/PassiveSkill_Operative_GoodMisfortune',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/PlayingDirty/PassiveSkill_Operative_PlayingDirty',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/SeeinRed/PassiveSkill_Operative_SeeinRed',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/Violent_Momentum/PassiveSkill_Operative_Violent_Momentum',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/Violent_Speed/Passive_Operative_Violent_Speed',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/ViolentViolence/PassiveSkill_Operative_ViolentViolence',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/DroneTree/WantVsNeed/PassiveSkill_Operative_WantVsNeed',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/Adrenaline/PassiveSkill_Operative_Adrenaline',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/CalmCoolCollected/PassiveSkill_Operative_CalmCoolCollected',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/Chancer/PassiveSkill_Operative_Chancer',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/PassiveSkill_Operative_ConfidentCompetence',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/CoolerHeads/PassiveSkill_Operative_CoolerHeads',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ElementalNullifier/PassiveSkill_Operative_ElementalNullifier',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ExtraParts/PassiveSkill_Operative_ExtraParts',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/NervesOfSteel/PassiveSkill_Operative_NervesOfSteel',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/NotOrdinaryOrdnance/PassiveSkill_Operative_NotOrdinaryOrdnance',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ReadyForAction/PassiveSkill_Operative_ReadyForAction',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ReallyExpensiveJacket/PassiveSkill_Operative_ReallyExpensiveJacket',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/Refreshment/PassiveSkill_Operative_Refreshment',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/SelfModulatingShields/PassiveSkill_Operative_SelfModulatingShields',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/ArmsDeal/PassiveSkill_Siren_ArmsDeal',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/PassiveSkill_Siren_BareKnuckle',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Clarity/PassiveSkill_Siren_Clarity',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/DoUntoOthers/PassiveSkill_Siren_DoUntoOthers',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/FindYourCenter/PassiveSkill_Siren_FindYourCenter',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/GuardianAngel/PassiveSkill_Siren_GuardianAngel',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/HelpingHands/PassiveSkill_Siren_HelpingHands',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Mindfulness/PassiveSkill_Siren_Mindfulness',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/OneWithNature/PassiveSkill_Siren_OneWithNature',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Overrun/PassiveSkill_Siren_Overrun',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/PersonalSpace/PassiveSkill_Siren_PersonalSpace',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/RootToRise/PassiveSkill_Siren_RootToRise',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/PassiveSkill_Siren_Samsara',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Vigor/PassiveSkill_Siren_Vigor',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Anima/PassiveSkill_Siren_Anima',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Conflux/PassiveSkill_Siren_Conflux',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/DeepWell/Passive_Siren_DeepWell',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Dread/PassiveSkill_Siren_Dread',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Empowered/PassiveSkill_Siren_Empowered',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/FearPassThroughMe/PassiveSkill_Siren_FearPassThroughMe',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/IlluminatedFist/PassiveSkill_Siren_IlluminatedFist',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Infusion/Passive_Siren_Infusion',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/ShieldOfThought/PassiveSkill_Siren_ShieldOfThought',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/SteadyHands/Passive_Siren_SteadyHands',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Sustainment/Passive_Siren_Sustainment',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Tempest/PassiveSkill_Siren_Tempest',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/ManifestTree/Wildfire/PassiveSkill_Siren_Wildfire',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Alacrity/PassiveSkill_Siren_Alacrity',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Ascendant/PassiveSkill_Siren_Ascendant',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Avatar/PassiveSkill_Siren_Avatar',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Awakening/Passive_Siren_Awakening',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/DoHarm/PassiveSkill_Siren_DoHarm',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/FastHands/PassiveSkill_Siren_FastHands',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/FromRest/PassiveSkill_Siren_FromRest',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/LaidBare/PassiveSkill_Siren_LaidBare',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Remnant/PassiveSkill_Siren_Remnant',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Restless/PassiveSkill_Siren_Restless',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Transcend/Passive_Siren_Transcend',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/ViolentTapestry/PassiveSkill_Siren_ViolentTapestry',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/RuinTree/Wrath/Passive_Siren_Wrath'
    ]


#Basic way of grabbing randomly from a list without duplicates, do a separate instance of this for each VH
#aux=range(len(data))
#while aux:
#    posit=random.randrange(len(aux))
#    index=aux[posit]
#    elem=data[index]
#    #alters the auxiliary list only
#    del aux[posit] 
#    #elem is the skill in this case


#Need to do each tree by each tier in order found in the serialized file, due to structures of trees, lots of hotfixes

for tree in skilltrees:
    aux=skills.copy()
    tier=1
    while tier<=6:
        item=0
        while item<=2:
            randskill=random.choice(aux)
            skill=randskill
            index=aux.index(skill)
            del aux[index] 

            skill_ref=skill.split('/')
            skill_ref=skill_ref[(len(skill_ref)-1)]
            skill_ref=skill_ref+'.'+skill_ref+'_C'

            mod.reg_hotfix(Mod.PATCH, '',
            tree,
            'Tiers.Tiers[{}].Object..Items.Items[{}].Object..AbilityClass'.format(tier, item),
            Mod.get_full_cond(skill_ref, 'BlueprintGeneratedClass'))

            mod.reg_hotfix(Mod.PATCH, '',
            tree,
            'Tiers.Tiers[{}].Object..Items.Items[{}].Object..ItemFrameName'.format(tier, item),
            '')

            item=item+1
        tier=tier+1
