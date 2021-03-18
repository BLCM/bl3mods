# Boss Rush 3000 Slaughter Generator
# Copyright (C) 2021 abram/skruntksrunt, altef-4, Christopher J. Kucera
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random

HEALTHS= ['HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
          'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
          'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
          'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
          'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113'
]
DAMAGE='DamageMultiplier_LevelBased_23_3CAF34804D650A98AB8FAFAB37CB87FF'
DEFAULT_DAMAGE=30
DEFAULT_HEALTH=1000
DEFAULT_NLOOT=12
QUARTER_HEALTH=[DEFAULT_HEALTH/4 for health in HEALTHS]
TWO_THIRDS_HEALTH=[2*DEFAULT_HEALTH/3 for health in HEALTHS]
HALF_HEALTH=[DEFAULT_HEALTH/2 for health in HEALTHS]
JUST_QUARTER_HEALTH={"health":QUARTER_HEALTH}
JUST_TWO_THIRDS_HEALTH={"health":TWO_THIRDS_HEALTH}

def buff_boss(boss): #bpchar, bpchar_path, balance_table, rowname, health,damage,nloot
    """ Generate hotfix code for buffing a boss """
    out = []
    out.append(f"##### {boss['name']} #####")
    out.append(f"# BPChar: {boss['bpchar']}")
    out.append(f"# bpchar_path: {boss['bpchar_path']}")
    out.append(f"# balance_table: {boss['balance_table']}")
    out.append(f"# balance rowname: {boss['rowname']}\n")
    if (boss.get("raid1",None) is not None):
        # old style Raid1 loot method
        # stolen from Apocalyptech 'BL3 Better Loot'
        out.append(f"SparkPatchEntry,(1,1,0,),/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1,CharacterExpansions.CharacterExpansions_Value[{boss['raid1']}].DropOnDeathItemPools[0].PoolProbability,0,,(BaseValueConstant=1,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
        out.append(f"SparkPatchEntry,(1,1,0,),/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1,CharacterExpansions.CharacterExpansions_Value[{boss['raid1']}].DropOnDeathItemPools[0].NumberOfTimesToSelectFromThisPool.BaseValueConstant,0,,{boss['nloot']}")
    else:
        # DLC style Loot manipulation
        out.append(f"SparkCharacterLoadedEntry,(1,1,0,{boss['bpchar']}),{boss['bpchar_path']}.{boss['bpchar']}_C:AIBalanceState_GEN_VARIABLE,DropOnDeathItemPools.ItemPools[0].PoolProbability,0,,(BaseValueConstant=1,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
        out.append(f"SparkCharacterLoadedEntry,(1,1,0,{boss['bpchar']}),{boss['bpchar_path']}.{boss['bpchar']}_C:AIBalanceState_GEN_VARIABLE,DropOnDeathItemPools.ItemPools[0].NumberOfTimesToSelectFromThisPool,0,,(BaseValueConstant={boss['nloot']},DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
    for healthname,health in zip(HEALTHS,boss['health']):
        out.append(f"SparkCharacterLoadedEntry,(1,2,0,{boss['bpchar']}),{boss['balance_table']}.{basename(boss['balance_table'])},{boss['rowname']},{healthname},0,,{health}")
    out.append(f"SparkCharacterLoadedEntry,(1,2,0,{boss['bpchar']}),{boss['balance_table']}.{basename(boss['balance_table'])},{boss['rowname']},{DAMAGE},0,,{boss['damage']}")
    return "\n".join(out)

def mk_boss(name, bpchar_path, balance_table, rowname,options=None):
    """ factory for boss definitions (hint: shoulda been a class) """
    if options is None:
        options = dict()
    return {
        'name':name,
        'bpchar':basename(bpchar_path),
        'bpchar_path':bpchar_path,
        'rowname':rowname,
        'balance_table':balance_table,
        'nloot':options.get('nloot',DEFAULT_NLOOT),
        'health':options.get('health',[DEFAULT_HEALTH,DEFAULT_HEALTH,DEFAULT_HEALTH,DEFAULT_HEALTH,DEFAULT_HEALTH]),
        'damage':options.get('damage',DEFAULT_DAMAGE),
        'raid1':options.get('raid1',None),
    }


################## SAFE BOSSES ###################



safe_bosses = [
    ('Pyschobillies (d)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/d/BPChar_Punk_Bounty01d',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Pyschobillies (c)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/c/BPChar_Punk_Bounty01c',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Pyschobillies (b)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/b/BPChar_Punk_Bounty01b',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Pyschobillies (a)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/a/BPChar_Punk_Bounty01a',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('The Unstoppable','/Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01',
     '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique','Rare01'),
    ('Private Beans','/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog','Nog_Badass',JUST_TWO_THIRDS_HEALTH),
    ('Rax','/Game/Enemies/Trooper/_Unique/Bounty02/Design/Character/BPChar_TrooperBounty02',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Bounty02',
     {'raid1':91,'health':HALF_HEALTH}
    ),
    ('Max','/Game/Enemies/Trooper/_Unique/Bounty02/Design/Character/BPChar_TrooperBounty03',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Bounty03',
     {'raid1':92,'health':HALF_HEALTH}
    ),
    ('Force Trooper Citrine','/Game/Enemies/Trooper/_Unique/Rare01b/_Design/Character/BPChar_Trooper_Rare01b',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01b',
     {'raid1':68,'health':HALF_HEALTH}
    ),
    ('Force Trooper Onyx','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01a',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01a',
     {'raid1':67,'health':HALF_HEALTH}
    ),
    ('Force Trooper Ruby','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01c',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01c',
     {'raid1':69,'health':HALF_HEALTH}
    ),
    ('Force Trooper Tourmaline','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01d',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01d',
     {'raid1':70,'health':HALF_HEALTH}
    ),
    ('Force Trooper Tourmaline','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01e',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01e',
     {'raid1':71,'health':HALF_HEALTH}
    ),
    ('Buttmunch','/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Buttmunch',{"health":[DEFAULT_HEALTH/2],"raid1":88}),
    ('Undertaker','/Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker','/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique','Tink_BountyPrologue'),
    ('Trufflemunch','/Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Trufflemunch',{"health":[DEFAULT_HEALTH/2],"raid1":89}),
    ('Buttmunch','/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Buttmunch',{"health":[DEFAULT_HEALTH/2],"raid1":88}),
    ('Fungal Gorger','/Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child','/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists','LostOne_Badass'),
    # ('AMBER LAMPS','/Game/Enemies/ServiceBot/LOOT/_Design/Character/BPChar_ServiceBot_LOOT','/Game/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_ServiceBot','ServiceBot_LOOT'),
    ('OnePunch','/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','OnePunch'),
    ('Tumorhead','/Game/Enemies/Punk_Female/_Unique/TumorHead/_Design/Character/BPChar_PunkBadass_Tumorhead',None,None), #punk_badass non-unique
    ('Judge Hightower','/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01','/Game/NonPlayerCharacters/_Shared/_Design/Table_Balance_NPC','AtlasSoldier_Bounty'),
    ('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur'),
    ('Dumptruck',
     '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_BountyPrologue',
     {"raid1":43},
    ),
    ('HotKarl',
     '/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_Bounty01_HotKarl'),
    ('Shiv',
     '/Game/Enemies/Psycho_Male/_Unique/BadassPrologue/_Design/Character/BPChar_PsychoBadassPrologue',
     "/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance",
     "Psycho_Badass"),
    ('RoadDog','/Game/Enemies/Goliath/_Unique/Rare02/_Design/Character/BPChar_Goliath_Rare02','/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique','Rare02'),
    ('Waylon Hurd','/Geranium/Enemies/GerPsycho_Male/_Unique/MoleMan/_Design/Character/BPChar_GerPsychoMoleMan','/Geranium/Enemies/GerPsycho_Male/_Shared/_Design/Balance/Table_GerPsycho_Balance_Unique','GerPsycho_MoleMan'),
    ('Lectrikor','/Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/BPChar_Biobeast_PlasmaBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","PlasmaBeast"),
    ('Hydragoian','/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","CopyBeast"),
    ('Amach','/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Zealot_Pilfer_Rare"),
    # Danger zone
    ('Anointed Alpha','/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoe',None,None),
    ('Anointed X-2','/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX2',None,None),
    ('Anointed X-3','/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX3',None,None),
    ('Anointed X-4','/Game/Enemies/Psycho_Male/_Unique/AnointedX4/Character/BPChar_PsychoAnointedX4',None,None),
    ('Archer Rowe','/Game/Enemies/Heavy/_Unique/DinerBoss/_Design/Character/BPChar_HeavyDinerBoss',None,None),
    ('Big Donny','/Game/Enemies/Tink/_Unique/MotorcadeBigD/_Design/Character/BPChar_TinkMotorcadeBigD',None,None),
    ('Billy, the Anointe','/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBos',None,None),
    ('Holder','/Game/NonPlayerCharacters/_Pandora/PrisonerHugs/_Design/Character/BPChar_PrisonerHugs',None,None),
    ('King Bobo','/Game/Enemies/Ape/_Unique/KingBobo/_Design/Character/BPChar_ApeKingBobo',None,None),
    ('King Gnasher','/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/BPChar_ApeJungleMonarch',None,None),
    ('Queen Ant Wanette','/Game/Enemies/Spiderant/_Unique/CakeRoyalty/_Design/Character/BPChar_SpiderantCakeRoyalty',None,None),
    ('Rachael, the Anointed','/Game/Enemies/Goon/Anointed/_Design/Character/BPChar_GoonAnointed',None,None),
    ('Turnkey Tim','/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey',None,None),
    ('Vermilingua','/Game/Enemies/Skag/_Unique/AntEater/_Design/Character/BPChar_SkagAntEater',None,None),
    ('Atomic','/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01',None,None),
    ('Baron Noggin','/Game/Enemies/Nog/_Unique/Nog01_Bounty/_Design/Character/BPChar_Nog01_Bounty',None,None),
    ('Crushjaw','/Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01',None,None),
    ('Handsome Jackie','/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/BPChar_PunkBounty02',None,None),
    ('DJ Deadsk4g','/Game/Enemies/Enforcer/_Unique/Bounty02/_Design/Character/BPChar_Enforcer_Bounty02',None,None),
    ('Heckle','/Game/Enemies/Goliath/_Unique/Bounty01/_Design/Character/BPChar_Goliath_Bounty01',None,None),
    ('Sky Bully','/Game/Enemies/Tink/_Unique/Bounty01/_Design/Character/BPChar_Tink_Bounty01',None,None),
    ('Sylestro','/Game/Enemies/Heavy/_Unique/Bounty01/_Design/Character/BPChar_Heavy_Bounty01',None,None),
    ('Antalope','/Game/Enemies/Spiderant/_Unique/Hunt01/_Design/Character/BPChar_Spiderant_Hunt01',None,None),
    ('Demoskaggon','/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique',"DemoSkag",
     {"health":[0.5*DEFAULT_HEALTH],"raid1":61}),
    ('El Dragón Jr.','/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',
     '/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',
     'Rare03'),
    # 3 successful bootup ^^^
    # DANGER DANGER
    ('Cybil Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaA','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Edie Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaB','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Martha Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaC','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Matty Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaD','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Urist McEnforcer','/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance','Enforcer_Shield'), # I hope this is safe
    ('Wick','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare03'),
    ('Borman Nates','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare02','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare02'),
    ('Warty','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare01','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare01',{"raid1":64}),
    ('IndoTyrant','/Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Rare01",{"raid1":58}),
    # 1 crash
    # Trying again with corrected Matty Crawly
    # 1 try: good
    # 2 try: good
    ('Tyrant of Instinct','/Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Character/BPChar_Saurian_TrialBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_TrialBoss",
     {"raid1":60}),
    # Even more unsafe!
    ('Tremendous Rex','/Game/Enemies/Saurian/_Unique/SlaughterBoss/_Design/Character/BPChar_Saurian_SlaughterBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian","Saurian_Tyrant"),
    ('Tink of Cunning','/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss",
     {"raid1":66}),
    ('Skag of Survival','/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss",
     {"raid1":62}),
    ('Sera of Supremacy','/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss",{"raid1":49}),
    ('Mr. Titan','/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique",'SlaughterBoss'),
    ('Hag of Fervor','/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial",{"raid1":48}),
    ('Arbalest of Discipline','/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_TrialBoss",{"raid1":54}), # There was also
    # ('Lasodactyl','/Geranium/Enemies/GerRakk/_Unique/Lasodactyl/_Design/Character/BPChar_GerRakkLasodactyl',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkLasodactyl"), # doesn't fly well
    
    ('Jerrick Logan','/Geranium/Enemies/GerPsycho_Male/_Unique/PhaserPete/_Design/Character/BPChar_GerPsychoPhaserPete',None,None),
    ('Caber Dowd','/Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/BPChar_GerPunkLarry',None,None),
    ('Dickon Goyle','/Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/BPChar_GerPunkGreg_Rakk',None,None),
    ('Maxitrillion','/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01',None,None),
    ('Princess Tarantella II','/Game/Enemies/Spiderant/_Unique/Tarantella/_Design/Character/BPChar_SpiderantTarantella','/Game/Enemies/Spiderant/_Shared/_Design/Balance/Table_Balance_Spiderant_Unique','Spiderant_CakeRoyalty'),
    
    ('Sloth','/Game/Enemies/Goon/_Unique/Rare01/_Design/Character/BPChar_Goon_Rare01',None,None),
    ('DEGEN-3','/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass_Venchy',None,None),
    ('Gorgeous Armada','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',None,None),
    ('Evil St. Lawrence','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',None,None),
    ('Junpai Goat Eater','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_PunkBadass_Gaud',None,None),
    ('Loco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coc',None,None),
    ('Gmork','/Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child',None,None),
    ('Kukuwajack','/Hibiscus/Enemies/_Unique/Hunt_Hampton/Character/BPChar_Hib_Hunt_Hampton',None,None),
    # danger
    ('Tom','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_BigBro',None,None),
    ('Voltborn','/Hibiscus/Enemies/_Unique/Rare_Shocker/Character/BPChar_ZealotNightmareShocker_Rare',None,None),
    ('Xam','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_ToughBro',None,None),
    ('Yeti','/Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti',None,None),
    ('Abbadoxis','/Geranium/Enemies/GerSaurian/_Unique/Grogzilla/_Design/Character/BPChar_GerSaurianGrogzilla',None,None),
    ('Garriden Loch','/Geranium/Enemies/GerTink/_Unique/Prohibitor/_Design/Character/BPChar_GerTinkProhibitor',None,None),
    ('Haddon Marr','/Geranium/Enemies/GerEnforcer/_Unique/Yarp/_Design/Character/BPChar_GerEnforcerYarp',None,None),
    ('Lani Dixon','/Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/BPChar_GerPunkNumber',None,None),
    # ('Pterodomini','/Geranium/Enemies/GerRakk/_Unique/Rod/_Design/Character/BPChar_GerRakkRod',None,None), # gets stuck
    # ('Slithermaw','/Geranium/Enemies/GerRakk/_Unique/Mother/_Design/Character/BPChar_GerRakkMother',None,None), # get's stuck
    #('Wrendon Esk','/Geranium/Enemies/Gyro/_Unique/Painless/_Design/Character/BPChar_GyroPainless',None,None), # he gets stuck alot
    # booted up just fine?
    # ('Skrakk','/Game/Enemies/Rakk/_Unique/HuntSkrakk/_Design/Character/BPChar_Rakk_HuntSkrakk',None,None), # flies poorly
    ('Jabbermogwai','/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/BPChar_Ape_Hunt01',None,None),
    ('Blinding Banshee','/Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01',None,None),
    ('Chonk Stomp','/Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/BPChar_Saurian_Hunt01',None,None),
    ('Sheega','/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady',None,None),
    ('The Tink-Train','/Game/Enemies/Goon/_Unique/MonsterTrucker/_Design/Character/BPChar_GoonMonsterTrucker',None,None),
    ('Azalea','/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag',None,None),
    ('Manvark','/Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01',None,None),
    ('Lagromar','/Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon',None,None),
    ('Procurer','/Hibiscus/Enemies/Zealot/Badass/_Design/Character/BPChar_Zealot_Badass_Procurer',None,None),
    ('Ipswitch Dunne','/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher',None,None),
    # These guys can cause problems
    ('Captain Traunt','/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":51}),
    ('General Traunt','/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":52}),
    #('Katagawa Ball','/Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere',
    # '/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique','Oversphere_Katagawa'), # 
    ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"),
    ('Bellik Primis','/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast','/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique',"AlteredBeast"), # works
    # Killavolt kinda works but then we got blocked?
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'),
    ('Gigamind','/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique','Nog_ChipHolder'),

]

# I use this for testing
dumb_bosses = [
    # ('Lasodactyl','/Geranium/Enemies/GerRakk/_Unique/Lasodactyl/_Design/Character/BPChar_GerRakkLasodactyl',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkLasodactyl"),

    # # ('Skrakk','/Game/Enemies/Rakk/_Unique/HuntSkrakk/_Design/Character/BPChar_Rakk_HuntSkrakk',None,None), # Bad?
    # ('Jabbermogwai','/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/BPChar_Ape_Hunt01',None,None),
    # ('Blinding Banshee','/Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01',None,None),
    # ('Chonk Stomp','/Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/BPChar_Saurian_Hunt01',None,None),
    # ('Sheega','/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady',None,None),
    # ('The Tink-Train','/Game/Enemies/Goon/_Unique/MonsterTrucker/_Design/Character/BPChar_GoonMonsterTrucker',None,None),
    # ('Azalea','/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag',None,None),
    # ('Manvark','/Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01',None,None),
    # ('Lagromar','/Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon',None,None),
    # ('Procurer','/Hibiscus/Enemies/Zealot/Badass/_Design/Character/BPChar_Zealot_Badass_Procurer',None,None),
    # ('Ipswitch Dunne','/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher',None,None),
    # # works
    # # Is general traunt shared??
    # # works
    # ('Captain Traunt','/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":51}),
    # ('General Traunt','/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":52}),
    # # works
    # #('Gigamind','/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique','Nog_ChipHolder'),
    # # works
    # ('Katagawa Ball','/Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere',
    # '/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique','Oversphere_Katagawa'), # might work. unreliabile
    # # works
    # ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"),
    # # ('Empowered Grawn','/Hibiscus/Enemies/Lunatic/Possessed/_Design/Character/BPChar_LunaticPossessed',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists",'Boss_Lunatic'), # infinite immunity phase
    # # ('Dinklebot','/Game/Enemies/Oversphere/_Unique/Rare01/_Design/Character/BPChar_OversphereRare01',None,None), # doesn't work
    # # ('MouthPiece',
    # #  '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss',
    # #  '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
    # #  'Enforcer_Mouthpiece'), # gets in a "Beatings per minute" loop
    # # works
    # ('Bellik Primis','/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast','/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique',"AlteredBeast"), # works
    # # ('Shiverous the Unscathed','/Hibiscus/Enemies/_Unique/Rare_Frost_Dragon/Character/BPChar_Rare_Frost_Dragon',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Frost_Dragon_Rare"), #gets stuck up top
    # # Killavolt kinda works but then we got blocked?
    # ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'),
    # # ('Katagawa Jr.','/Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR','/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/Table_Balance_KatagawaJR_PT1','KatagawaJR_Boss'),# appears dies then locks?
    # # ('Dreg','/Game/Enemies/Rakk/_Unique/Dragon/_Design/Character/BPChar_Rakk_Dragon',None,None), # they don't engage
    # # ('Vice','/Game/Enemies/Rakk/_Unique/DragonCryo/_Design/Character/BPChar_Rakk_DragonCryo',None,None), # they don't engage
]

# Want list:
# * [X] Katagawa Ball?
# * [X] Warden?
# * [X] Gigamind?
# * Mokdan Urgash (DLC4)
# * The Caretaker (DLC4)
# * General Blisterpus (DLC4)
# * ward watcher alpha (DLC4)
# * ward watcher beta  (DLC4)
# * black heart king   (DLC4)
# * evil brick
# * sponge boss bullet pants
# * [X] Jabbermogwai
# * Queen iOsaur iOsaur, Queen of the Scaleon
# * [X] Skrakk
# * [ ] Long Arm the Smasher
# * Apollo
# * Artemis
def choose_random_slaughter_boss(bosses=safe_bosses):
    return random.choice(bosses)
    
