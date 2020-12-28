from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

# Finally better randomize some items (looking at you COMs and Artifacts)
# Had to remove randomization of weapon materials in order to play with other randomizers

mod=Mod('gear_randomizer_com.bl3hotfix.gz',
'Gear Randomizer: Class Mods',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
cats='gear-general'
)

data=BL3Data()

#List the Balances
cbal_name=[
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_01_Common',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_02_Uncommon',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_03_Rare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster_05_Legendary',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_BountyHunter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_DE4DEYE',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RakkCommander',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Alisma',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/L01/InvBalD_CM_Ixora_BSM_L01',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_01_Common',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_02_Uncommon',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_03_Rare',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/PartSets/InvBalD_CM_Ixora_BSM_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner_01_Common',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner_02_Uncommon',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner_03_Rare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner_05_Legendary',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BearTrooper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BlastMaster',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_BloodLetter',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_MindSweeper',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Gunner/InvBalD_ClassMod_Gunner_Rocketeer',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Alisma',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/L01/InvBalD_CM_Ixora_GUN_L01',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_01_Common',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_02_Uncommon',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_03_Rare',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/PartSets/InvBalD_CM_Ixora_GUN_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative_01_Common',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative_02_Uncommon',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative_03_Rare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative_05_Legendary',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_ColdWarrior',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Executor',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_FireBrand',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Infiltrator',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_Techspert',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Alisma',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L01/InvBalD_CM_Ixora_OPE_L01',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/L02/InvBalD_CM_Ixora_OPE_L02',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_01_Common',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_02_Uncommon',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_03_Rare',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/PartSets/InvBalD_CM_Ixora_OPE_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_01_Common',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_02_Uncommon',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_03_Rare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_04_VeryRare',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren_05_Legendary',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Breaker',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus',
    '/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/InvBalD_CM_Siren_DLC1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Alisma',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/L01/InvBalD_CM_Ixora_SRN_L01',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_01_Common',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_02_Uncommon',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_03_Rare',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/PartSets/InvBalD_CM_Ixora_SIR_04_VeryRare'
]

cmod_part=[
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond11',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond2',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond3',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond4',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Bond7',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_DangerousGame',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FastAndFurry',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Frenzy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_FullTank',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GeneticLink',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_GotThisForYou',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HeadCount',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR1',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR2',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR3',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR4',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR7',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR8',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HR9',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt1',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt2',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Hunt5',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_HuntersEye',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_InterStalker',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_LifeTraining',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_Symbiosis',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/BeastMaster/ClassMod_Part_Skill_BeastMaster_TwoFang',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_GrimHarvest_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_HeadCount_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/CM_Part_Skill_BeastMaster_PackTactics_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_Furry_dlc1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_HuntersEye_dlc1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/BSM/Skills/ClassMod_Part_Skill_BeastMaster_PackTac',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_Ferocity',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_GrimHarvest',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_Hib_BeastMaster_PackTac',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_11',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_13',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_15',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_16',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_18',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/BSM/Skills/CM_Part_Skill_BSM_DLCSkill_4',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_ArmoredInfantry',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_CarryGrenades',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_ClickClickBoom',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_CloudOfLead',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Deadlines',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_DesperateMeasures',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_DrowningInBrass',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_ExperimentalMunitions',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_ExplosivePunctuation',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_FireSkagDen',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Forge',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_GrenadeCanCrit',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Grizzled',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_IronBank',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_MatchingSet',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_MeansOfDesctruction',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_PhalanxDoctrine',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Redistribution',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_ScorchingRPM',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Scrappy',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_SelflessVengeance',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_SomeForTheRoad',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_StainlessSteelBear',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_StokeTheEmbers',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_ThinRedLine',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Torgue',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_Vampyr',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Gunner/ClassMod_Part_Skill_Gunner_VladofIngenuity',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/CM_Part_Skill_Gunner_Deadlines_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/CM_Part_Skill_Gunner_StainlessSteelBear_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/GUN/CM_Part_Skill_Gunner_StokeTheEmbers_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/Skills/ClassMod_Part_Skill_Gunner_ClickClikc_DLC1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/Skills/ClassMod_Part_Skill_Gunner_IronBank_dlc1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/Skills/ClassMod_Part_Skill_Gunner_ScorchingRPM_dlc1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/ClassMod_Part_Skill_Gunner_IronBank_HIB',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/ClassMod_Part_Skill_Gunner_MatchedSEt_HIB',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/ClassMod_Part_Skill_Gunner_MeansOfDestruction_HIB',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill_1',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill_13',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill_14',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill_3',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill_6',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/GUN/Skills/CM_Part_Skill_GUN_DLCSkill_9',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Adrenaline',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_BorrowedTime',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Chancer',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_ColdBore',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_CoolerHeads',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_CoolHand',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Donnybrook',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_DroneDelivery',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_DuctTape',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_ExtraParts',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_GoodMisfortune',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_LikeAGhost',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_MultiTasker',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Ordnance',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_PlayingDirty',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_PocketFullOfGrenades',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Praemunitus',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_ReadyForAction',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_ReallyExpensiveJacket',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Refreshment',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_SupersonicMan',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Teamwork',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_TheWantVsNeed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Violent_Momentum',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_Violent_Speed',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Operative/ClassMod_Part_Skill_Operative_ViolentViolence',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/CM_Part_Skill_Operative_Supersonic_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/CM_Part_Skill_Operative_ViolentMomentum_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/CM_Part_Skill_Operative_ViolentSpeed_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/Skills/ClassMod_Part_Skill_Operative_Donnybrook_dlc1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/Skills/ClassMod_Part_Skill_Operative_PlayingDirty_dlc1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/OPE/Skills/ClassMod_Part_Skill_Operative_ViolentViolence_dlc1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/CM_Part_Skill_OPE_Hib_Adrenaline',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/CM_Part_Skill_OPE_Hib_BorrowedTime',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/CM_Part_Skill_OPE_Hib_GoodMisfortune',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_10',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_12',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_16',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_3',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_4',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/OPE/Skills/CM_Part_Skill_OPE_DLCSkill_6',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Alacrity',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Anima',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_ArmsDeal',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_BareKnuckle',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Clarity',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Conflux',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_DeepWell',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_DoHarm',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Dread',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Empowered',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_FastHands',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_FearPassThroughMe',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_FindYourCenter',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_FromRest',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_IlluminatedFist',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Infusion',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Mindfulness',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_OneWithNature',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_PersonalSpace',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Remnant',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Restless',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Samsara',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_SteadyHands',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Tempest',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Transcend',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Vigor',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_ViolentTapestry',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_WildFire',
    '/Game/Gear/ClassMods/_Design/PartSets/Part_Skills/Siren/ClassMod_Part_Skill_Siren_Wrath',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/CM_Part_Skill_Siren_Clarity_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/CM_Part_Skill_Siren_HelpingHands_Raid1',
    '/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/SRN/CM_Part_Skill_Siren_Mindfulness_Raid1',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/Skills/ClassMod_Part_Skill_Siren_HelpingHands',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/Skills/ClassMod_Part_Skill_Siren_LaidBare',
    '/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/SRN/Skills/ClassMod_Part_Skill_Siren_Mindfulness_dlc1',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/CM_Part_Skill_Siren_Awakening_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/CM_Part_Skill_Siren_DoHarm_Hib',
    '/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/CM_Part_Skill_Siren_ViolentTapestry_Hib',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_AmbushPredator_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_EagerToImpress_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/BSM/ClassMod_Part_Skill_BeastMaster_InterplanetaryStalker_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/ClassMod_Part_Skill_Gunner_CloudOfLead_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/ClassMod_Part_Skill_Gunner_MeansOfDestruction_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/GUN/ClassMod_Part_Skill_Gunner_SpecialistBear_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/CM_Part_Skill_OPE_Adrenaline_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/CM_Part_Skill_OPE_Brainfreeze_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/OPE/CM_Part_Skill_OPE_LikeAGhost_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/CM_Part_Skill_Siren_IlluminatedFist_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/CM_Part_Skill_Siren_JabCross_Alisma',
    '/Game/PatchDLC/Alisma/Gear/ClassMods/_Design/SRN/CM_Part_Skill_Siren_LaidBare_Alisma',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill_10',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill_14',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill_15',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill_16',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill_2',
    '/Game/PatchDLC/Ixora/Gear/ClassMods/_Design/SRN/Skills/CM_Part_Skill_SRN_DLCSkill_5'
]

cbase_bal=[
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Beastmaster',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Gunner',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Operative',
    '/Game/Gear/ClassMods/_Design/BalanceDefs/InvBalD_ClassMod_Siren'
]

for bal in cbal_name:
    cbals=Balance.from_data(data, bal)
    for cat in cbals.categories:
        '''if cat.index==1:
            for bals in cbal_name:
                cbalslist=Balance.from_data(data, bals)
                for cats in cbalslist.categories:
                    if (cats.index==2) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
            if cat.enabled is False:
                cat.enabled=True
            cat.select_multiple=True
            cat.num_min=1
            cat.num_max=2'''
        if cat.index==2:
            for bals2 in cbal_name:
                cbalslist2=Balance.from_data(data, bals2)
                for cats2 in cbalslist2.categories:
                    if (cats2.index==2) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
            if cat.enabled is False:
                cat.enabled=True
        if cat.index==5:
            for bals3 in cbase_bal:
                cbalslist3=Balance.from_data(data, bals3)
                for cats3 in cbalslist3.categories:
                    if (cats3.index==5) & (len(cats3)!=0):
                        parts=cats3.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            cat.enabled=True
            cat.num_min=7
            cat.num_max=7
            break
    cbals.hotfix_full(mod)

for asset in cmod_part:
    mod.reg_hotfix(Mod.PATCH, '',
    asset,
    'Dependencies',
    ''
    )

mod.close()