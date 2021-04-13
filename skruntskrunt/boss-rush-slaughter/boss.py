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
from os.path import basename

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
    if boss['nloot'] > 0:
        if (boss.get("raid1",None) is not None):
            # old style Raid1 loot method
            # stolen from Apocalyptech 'BL3 Better Loot'
            out.append(f"SparkPatchEntry,(1,1,0,),/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1,CharacterExpansions.CharacterExpansions_Value[{boss['raid1']}].DropOnDeathItemPools[0].PoolProbability,0,,(BaseValueConstant=1,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
            out.append(f"SparkPatchEntry,(1,1,0,),/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1,CharacterExpansions.CharacterExpansions_Value[{boss['raid1']}].DropOnDeathItemPools[0].NumberOfTimesToSelectFromThisPool.BaseValueConstant,0,,{boss['nloot']}")
        else:
            # DLC style Loot manipulation
            out.append(f"SparkCharacterLoadedEntry,(1,1,0,{boss['bpchar']}),{boss['bpchar_path']}.{boss['bpchar']}_C:AIBalanceState_GEN_VARIABLE,DropOnDeathItemPools.ItemPools[0].PoolProbability,0,,(BaseValueConstant=1,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
            out.append(f"SparkCharacterLoadedEntry,(1,1,0,{boss['bpchar']}),{boss['bpchar_path']}.{boss['bpchar']}_C:AIBalanceState_GEN_VARIABLE,DropOnDeathItemPools.ItemPools[0].NumberOfTimesToSelectFromThisPool,0,,(BaseValueConstant={boss['nloot']},DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
    # health scaling
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
    ('Anointed Alpha','/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoe',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_AnointedJoe"),

    ('Anointed X-2','/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX2',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_AnointedX2"),
    ('Anointed X-3','/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX3',None,None),
    ('Anointed X-4','/Game/Enemies/Psycho_Male/_Unique/AnointedX4/Character/BPChar_PsychoAnointedX4',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","PsychoAnointedX4"),
    ('Archer Rowe','/Game/Enemies/Heavy/_Unique/DinerBoss/_Design/Character/BPChar_HeavyDinerBoss',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","DinerBoss"),

    ('Big Donny','/Game/Enemies/Tink/_Unique/MotorcadeBigD/_Design/Character/BPChar_TinkMotorcadeBigD',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_MotorcadeBigD"),

    ('Billy, the Anointed','/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBoss',None,None),
    # Holder is an NPC
    # ('Holder','/Game/NonPlayerCharacters/_Pandora/PrisonerHugs/_Design/Character/BPChar_PrisonerHugs',None,None),
    ('King Bobo','/Game/Enemies/Ape/_Unique/KingBobo/_Design/Character/BPChar_ApeKingBobo',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape_Unique","Ape_KingBobo"),
    ('King Gnasher','/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/BPChar_ApeJungleMonarch',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape","Ape_Badass"),
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

# I hand tested these ones
new_bosses = [
    ('The Shark','/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_PsychoShark',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TheShark"),
    ('Domino','/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina',"/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Balance/Table_Balance_DoubleDownDomino","Domino"),
    ('MachineGun Mikey','/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_MachineGunMikey',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath","Badass"),
    ('Yvan','/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan',"/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Balance/Table_Balance_RagingBot","Raging_Yvan"),
    ('Steel Dragon','/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part3/_Design/Character/BPChar_DoItForDigby_SteelDragon',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","SteelDragon"),
    ('BloodBucket','/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part2/Character/BPChar_DoItForDigby_BloodBucket',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","BloodBucket"),
    ('ThirdRail','/Dandelion/Enemies/Looters/_Unique/MeetTimothy/_Design/Character/BPChar_MeetTimothy_ThirdRail',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","ThirdRail"),
    ('Rudy Varlope','/Dandelion/Enemies/Looters/_Unique/GreatEscape/_Design/Character/BPChar_GreatEscape_Rudy',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","RudyVarlope"),
    ('Giorgio','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',"/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters","Tink_Badass"),
    ('Lawrence','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',"/Dandelion/Enemies/Looters/Enforcer/_Shared/_Design/Balance/Table_Enforcer_BalanceLooters","Enforcer_Badass"),
    ('Coco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco',"/Dandelion/Enemies/Looters/Goon/_Shared/_Design/Balance/Table_Balance_GoonLooter","Goon_BadassLooter"),
    ('Golden Bullion','/Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","GoldenBullion"),
    ('Handsome Jacket','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ('Handsome Slacks','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ('TricksyNick','/Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TricksyNick"),
    ('TonyBordel LLC','/Dandelion/Enemies/Looters/_Unique/OneMansTrash/_Design/Character/BPChar_OneMansTrash_TonyBordel',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TonyBordel"),
    ('Casinobot Janitor','/Dandelion/Enemies/ServiceBot/Unique_Janitor/_Design/Character/BPChar_CasinoBot_BigJanitor',"/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot","CasinoBot_Janitor"),
    ("Dandellion",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Dandellion"),
    ("Petunia",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Petunia"),
    ("Facemelt",'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Facemelt"),
    ("Loader_Gun",'/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1","Loader_Gun"),
    ("DebtCollector",'/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","DebtCollector"),
    ("Rider_And_Mount",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
    ("Dr Benedict",'/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict',"/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1","Basic"),
    ("Enforcer_Reaper",'/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper',"/Ixora/Enemies/CotV/Enforcer/_Shared/_Design/Balance/Table_Balance_Enforcer_Ixora","Enforcer_Reaper"),
    ("GeneralBlisterPuss",'/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","GeneralBlisterPuss"),
    ("TheBlackRook",'/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","TheBlackRook"),
    ("APBulletRider",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"),
    ("SpongeBoss",'/Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss',"/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss","SpongeBoss"),
    ("Security Sergeant",'/Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"),
    ("Security Chief",'/Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"),
    ("TheBlackKing",'/Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing',"/Alisma/Enemies/AliPsycho/_Shared/_Design/Balance/Table_Balance_AliPsycho_Unique","TheBlackKing"),
    ("Hyperion Warden",'/Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
]

newer_bosses = [
    ("Scraptrap Queen",'/Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character/BPChar_ClaptrapQueen',"/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1","Queen"),
    ("Kormash",'/Geranium/Enemies/LodgeBoss/_Design/Character/BPChar_SploderBoss',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance_Unique","GerEnforcer_SploderBoss"),
    ("Hildr",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidBossC"),
    ("Rota",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Character/BPChar_MechRaidBossB',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossB"),
    ("Sigrdrifa",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Character/BPChar_MechRaidBossA',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossA"),
    ("Aurelia",'/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Character/BPChar_AureliaBoss',"/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Balance/Table_Balance_AureliaBoss","AureliaBoss"),
]

safe_bosses = safe_bosses + new_bosses + newer_bosses

easy_bosses = [
    ("TheBlackKing",'/Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing',"/Alisma/Enemies/AliPsycho/_Shared/_Design/Balance/Table_Balance_AliPsycho_Unique","TheBlackKing"),
    ("Enforcer_Reaper",'/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper',"/Ixora/Enemies/CotV/Enforcer/_Shared/_Design/Balance/Table_Balance_Enforcer_Ixora","Enforcer_Reaper"),
    ("GeneralBlisterPuss",'/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","GeneralBlisterPuss"),
    ("TheBlackRook",'/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","TheBlackRook"),
    ("APBulletRider",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"),
    ('Coco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco',"/Dandelion/Enemies/Looters/Goon/_Shared/_Design/Balance/Table_Balance_GoonLooter","Goon_BadassLooter"),
    ('Golden Bullion','/Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","GoldenBullion"),
    ('Handsome Jacket','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ('Handsome Slacks','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ('TricksyNick','/Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TricksyNick"),

]

# safe_bosses = easy_bosses

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
    
def find_boss(bppath,bosses=safe_bosses):
    for boss in bosses:
        if boss[1] == bppath:
            return boss
    return None

# these are untested and redundant
# but these have balancetables
extracted_uniques = [
    ("GeneralBlisterPuss",'/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","GeneralBlisterPuss"),
    ("TheBlackRook",'/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","TheBlackRook"),
    ("Basic",'/Alisma/Enemies/AliGoliath/_Unique/TheBlackKing/_Design/Character/BPChar_AliGoliath_TheBlackKing',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath","Basic"),
    ("TheBlackKing",'/Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing',"/Alisma/Enemies/AliPsycho/_Shared/_Design/Balance/Table_Balance_AliPsycho_Unique","TheBlackKing"),
    ("AP",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"),
    ("Basic",'/Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"),
    ("Basic",'/Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"),
    ("Psycho_Basic",'/Alisma/Enemies/HibPsycho/_Unique/TheCellNeighbor/_Design/Character/BPChar_HibPsycho_TheCellNeighbor',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance","Psycho_Basic"),
    ("Punk_Badass",'/Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ("BigChestDaddy",'/Alisma/Enemies/Loader/_Unique/BigChestDaddy/_Design/Character/BPChar_Loader_BigChestDaddy',"/Alisma/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_AliLoader_Unique","BigChestDaddy"),
    ("ISeeYou",'/Alisma/Enemies/Loader/_Unique/ISeeYou/_Design/Character/BPChar_Loader_ISeeYou',"/Alisma/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_AliLoader_Unique","ISeeYou"),
    ("LeggyLarry",'/Alisma/Enemies/Loader/_Unique/LeggyLarry/_Design/Character/BPChar_Loader_LeggyLarry',"/Alisma/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_AliLoader_Unique","LeggyLarry"),
    ("TouchySandy",'/Alisma/Enemies/Loader/_Unique/TouchySandy/_Design/Character/BPChar_Loader_TouchySandy',"/Alisma/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_AliLoader_Unique","TouchySandy"),
    ("SpongeBoss",'/Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss',"/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss","SpongeBoss"),
    ("Facemelt",'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Facemelt"),
    ("DebtCollector",'/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","DebtCollector"),
    ("Loader_Gun",'/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1","Loader_Gun"),
    ("Dandellion",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Dandellion"),
    ("Petunia",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Petunia"),
    ("BloodBucket",'/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part2/Character/BPChar_DoItForDigby_BloodBucket',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","BloodBucket"),
    ("SteelDragon",'/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part3/_Design/Character/BPChar_DoItForDigby_SteelDragon',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","SteelDragon"),
    ("Domino",'/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina',"/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Balance/Table_Balance_DoubleDownDomino","Domino"),
    ("TheShark",'/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_PsychoShark',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TheShark"),
    ("RudyVarlope",'/Dandelion/Enemies/Looters/_Unique/GreatEscape/_Design/Character/BPChar_GreatEscape_Rudy',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","RudyVarlope"),
    ("Enforcer_Badass",'/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',"/Dandelion/Enemies/Looters/Enforcer/_Shared/_Design/Balance/Table_Enforcer_BalanceLooters","Enforcer_Badass"),
    ("Goon_BadassLooter",'/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco',"/Dandelion/Enemies/Looters/Goon/_Shared/_Design/Balance/Table_Balance_GoonLooter","Goon_BadassLooter"),
    ("Tink_Badass",'/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',"/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters","Tink_Badass"),
    ("ThirdRail",'/Dandelion/Enemies/Looters/_Unique/MeetTimothy/_Design/Character/BPChar_MeetTimothy_ThirdRail',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","ThirdRail"),
    ("TonyBordel",'/Dandelion/Enemies/Looters/_Unique/OneMansTrash/_Design/Character/BPChar_OneMansTrash_TonyBordel',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TonyBordel"),
    ("Badass",'/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_MachineGunMikey',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath","Badass"),
    ("Raging_Yvan",'/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan',"/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Balance/Table_Balance_RagingBot","Raging_Yvan"),
    ("GoldenBullion",'/Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","GoldenBullion"),
    ("TricksyNick",'/Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TricksyNick"),
    ("Punk_Badass",'/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ("Punk_Badass",'/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ("Ape_EdenBossFodder",'/Game/Enemies/Ape/_Unique/EdenBossFodder/_Design/Character/BPChar_ApeEdenBossFodder',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape_Unique","Ape_EdenBossFodder"),
    ("Ape_Jabbermogwai",'/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/BPChar_Ape_Hunt01',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape_Unique","Ape_Jabbermogwai"),
    ("Ape_Badass",'/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/BPChar_ApeJungleMonarch',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape","Ape_Badass"),
    ("Ape_Badass",'/Game/Enemies/Ape/_Unique/KGuard/_Design/Character/BPChar_ApeKGuard',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape","Ape_Badass"),
    ("Ape_KingBobo",'/Game/Enemies/Ape/_Unique/KingBobo/_Design/Character/BPChar_ApeKingBobo',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape_Unique","Ape_KingBobo"),
    ("Ape_Fire",'/Game/Enemies/Ape/_Unique/Squire/_Design/Character/BPChar_ApeSquire',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape","Ape_Fire"),
    ("Enforcer_AnointedJoeClone",'/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoeClone',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_AnointedJoeClone"),
    ("Enforcer_AnointedJoe",'/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoe',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_AnointedJoe"),
    ("Enforcer_Shield",'/Game/Enemies/Enforcer/_Unique/BlueBasic/_Design/Character/BPChar_EnforcerBlueBasic',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Shield"),
    ("Enforcer_Bounty01_HotKarl",'/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_Bounty01_HotKarl"),
    ("Enforcer_Shield",'/Game/Enemies/Enforcer/_Unique/Bounty02/_Design/Character/BPChar_Enforcer_Bounty02',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Shield"),
    ("Enforcer_BountyPrologue",'/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_BountyPrologue"),
    ("Enforcer_Gun",'/Game/Enemies/Enforcer/_Unique/Dentist/_Design/Character/BPChar_EnforcerDentist',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Gun"),
    ("Enforcer_KillaVolt",'/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_KillaVolt"),
    ("Enforcer_Melee",'/Game/Enemies/Enforcer/_Unique/RedMelee/_Design/Character/BPChar_EnforcerRedMelee',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Melee"),
    ("Enforcer_Mouthpiece",'/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_Mouthpiece"),
    ("Enforcer_Terror",'/Game/Enemies/Enforcer/_Unique/Terror/_Design/Character/BPChar_Terror',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_Terror"),
    ("Enforcer_Badass",'/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Badass"),
    ("Enforcer_Shield",'/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Shield"),
    ("Enforcer_WardenGuard",'/Game/Enemies/Enforcer/_Unique/WardenGuard/_Design/Character/BPChar_EnforcerMeleeWardenGuard',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_WardenGuard"),
    ("Bounty01",'/Game/Enemies/Goliath/_Unique/Bounty01/_Design/Character/BPChar_Goliath_Bounty01',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","Bounty01"),
    ("CageArena",'/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"),
    ("Badass",'/Game/Enemies/Goliath/_Unique/PlayerFriendly/_Design/Character/BPChar_Goliath_Badass_Friendly',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath","Badass"),
    ("Rare01",'/Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","Rare01"),
    ("Rare02",'/Game/Enemies/Goliath/_Unique/Rare02/_Design/Character/BPChar_Goliath_Rare02',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","Rare02"),
    ("Rare03",'/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","Rare03"),
    ("SlaughterBoss",'/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","SlaughterBoss"),
    ("Goon_MonsterTrucker",'/Game/Enemies/Goon/_Unique/MonsterTrucker/_Design/Character/BPChar_GoonMonsterTrucker',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_MonsterTrucker"),
    ("Goon_Rare01",'/Game/Enemies/Goon/_Unique/Rare01/_Design/Character/BPChar_Goon_Rare01',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_Rare01"),
    ("Goon_RoidRage",'/Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_RoidRage"),
    ("Goon_BossTrial",'/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial"),
    ("Guardian_BeachVault_TheBerserker",'/Game/Enemies/Guardian/_Unique/BeachVault/_Design/Character/BPChar_GuardianBeachVault',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_BeachVault_TheBerserker"),
    ("Guardian_SpectreBossFodder",'/Game/Enemies/Guardian/_Unique/BossFodder/Design/Character/BPChar_GuardianSpectreBossFodder',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian","Guardian_SpectreBossFodder"),
    ("Guardian_WraithBossFodder",'/Game/Enemies/Guardian/_Unique/BossFodder/Design/Character/BPChar_GuardianWraithBossFodder',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian","Guardian_WraithBossFodder"),
    ("Guardian_Herald",'/Game/Enemies/Guardian/_Unique/CityVault/_Design/Character/BPChar_Guardian_CityVault',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian","Guardian_Herald"),
    ("Guardian_EdenVault",'/Game/Enemies/Guardian/_Unique/EdenVault01/_Design/Character/BPChar_Guardian_EdenVault01',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian","Guardian_EdenVault"),
    ("Guardian_EdenVault",'/Game/Enemies/Guardian/_Unique/EdenVault02/_Design/Character/BPChar_Guardian_EdenVault02',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian","Guardian_EdenVault"),
    ("Guardian_GemGoblin",'/Game/Enemies/Guardian/_Unique/GemGoblin/_Design/Character/BPChar_GuardianGemGoblin',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_GemGoblin"),
    ("Guardian_Trial_Boss",'/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss"),
    ("Heavy_Bounty01",'/Game/Enemies/Heavy/_Unique/Bounty01/_Design/Character/BPChar_Heavy_Bounty01',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","Heavy_Bounty01"),
    ("Heavy_Traunt",'/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","Heavy_Traunt"),
    ("DinerBoss",'/Game/Enemies/Heavy/_Unique/DinerBoss/_Design/Character/BPChar_HeavyDinerBoss',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","DinerBoss"),
    ("FootstepsOfGiants",'/Game/Enemies/Heavy/_Unique/FootstepsOfGiants/_Design/Character/BPChar_HeavyFootstepsOfGiants',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","FootstepsOfGiants"),
    ("Heavy_Powerhouse",'/Game/Enemies/Heavy/_Unique/JavaCore/_Design/Character/BPChar_HeavyJavaCore',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy","Heavy_Powerhouse"),
    ("Heavy_Traunt",'/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","Heavy_Traunt"),
    ("Mech_EvilAI",'/Game/Enemies/Mech/_Unique/EvilAI/_Design/Character/BPChar_MechEvilAI',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_EvilAI"),
    ("Mech_Mini",'/Game/Enemies/Mech/_Unique/GenMini/_Design/Character/BPChar_MechGenMini',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_Mini"),
    ("DropShipTurret_Basic",'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/BallGun/Character/BPChar_BallGun',"/Game/Enemies/DropShipTurret/_Shared/_Design/Balance/Table_Balance_DropShipTurret","DropShipTurret_Basic"),
    ("Mech_TechSlaughterBoss1",'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech1',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_TechSlaughterBoss1"),
    ("Mech_TechSlaughterBoss1",'/Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech2',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_TechSlaughterBoss1"),
    ("Mech_TrialBoss",'/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_TrialBoss"),
    ("Nekrobug_BetterTimes",'/Game/Enemies/Nekrobug/_Unique/BetterTimes/_Design/Character/BPChar_Nekrobug_BetterTimes',"/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug_Unique","Nekrobug_BetterTimes"),
    ("Nekrobug_Flyer_Fodder",'/Game/Enemies/Nekrobug/_Unique/Fodder/_Design/Character/BPChar_Nekrobug_Flyer_Fodder',"/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug","Nekrobug_Flyer_Fodder"),
    ("Nekrobug_Broodmother",'/Game/Enemies/Nekrobug/_Unique/HopperSwarm/_Design/Character/BPChar_Nekrobug_HopperSwarm',"/Game/Enemies/Nekrobug/_Shared/_Design/Balance/Table_Balance_Nekrobug_Unique","Nekrobug_Broodmother"),
    ("Nog_Badass",'/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans',"/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog","Nog_Badass"),
    ("Nog_ChipHolder",'/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder',"/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique","Nog_ChipHolder"),
    ("Nog_ChipHolder_Adds",'/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_TrooperBasic_GigamindAdds',"/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique","Nog_ChipHolder_Adds"),
    ("HackedGamer",'/Game/Enemies/Nog/_Unique/HackedGamer/_Design/Character/BPChar_NogHackedGamer',"/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique","HackedGamer"),
    ("Nog01_Bounty",'/Game/Enemies/Nog/_Unique/Nog01_Bounty/_Design/Character/BPChar_Nog01_Bounty',"/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique","Nog01_Bounty"),
    ("Oversphere_Jackie",'/Game/Enemies/Oversphere/_Unique/Jackie/_Design/Character/BPChar_OversphereJackie',"/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique","Oversphere_Jackie"),
    #(,'/Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere',,),
    ("Oversphere_VRBig",'/Game/Enemies/Oversphere/_Unique/OversphereVRBig/Character/BPChar_OversphereVRBig',"/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique","Oversphere_VRBig"),
    ("Oversphere_VR",'/Game/Enemies/Oversphere/_Unique/OversphereVR/_Design/Character/BPChar_OversphereVR',"/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique","Oversphere_VR"),
    ("Oversphere_Rare01",'/Game/Enemies/Oversphere/_Unique/Rare01/_Design/Character/BPChar_OversphereRare01',"/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique","Oversphere_Rare01"),
    ("PsychoAnointedX4",'/Game/Enemies/Psycho_Male/_Unique/AnointedX4/Character/BPChar_PsychoAnointedX4',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","PsychoAnointedX4"),
    ("Psycho_Badass",'/Game/Enemies/Psycho_Male/_Unique/BadassPrologue/_Design/Character/BPChar_PsychoBadassPrologue',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance","Psycho_Badass"),
    ("Psycho_Suicide",'/Game/Enemies/Psycho_Male/_Unique/Bloodshine/_Design/Character/BPChar_PsychoBloodshine',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance","Psycho_Suicide"),
    ("Psycho_Infected",'/Game/Enemies/Psycho_Male/_Unique/InfectedOnes/_Design/Character/BPChar_PsychoInfectedOnes',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance","Psycho_Infected"),
    ("Psycho_Badass",'/Game/Enemies/Psycho_Male/_Unique/OilSheriff/_Design/Character/BPChar_PsychoOilSheriff',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance","Psycho_Badass"),
    ("OnePunch",'/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","OnePunch"),
    ("Psycho_Prologue",'/Game/Enemies/Psycho_Male/_Unique/Prologue/_Design/Character/BPChar_PsychoPrologue',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","Psycho_Prologue"),
    ("Rakkman",'/Game/Enemies/Psycho_Male/_Unique/Rakkman/_Design/Character/BPChar_Rakkman',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","Rakkman"),
    ("Rare02",'/Game/Enemies/Psycho_Male/_Unique/Rare02/_Design/Character/BPChar_PsychoRare02',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","Rare02"),
    ("Rare03",'/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","Rare03"),
    ("Psycho_WardenGuard",'/Game/Enemies/Psycho_Male/_Unique/WardenGuard/_Design/Character/BPChar_PsychoWardenGuard',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","Psycho_WardenGuard"),
    ("Punk_AnointedX2",'/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX2',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_AnointedX2"),
    ("Punk_Basic",'/Game/Enemies/Punk_Female/_Unique/BlueBasic/_Design/Character/BPChar_PunkBlueBasic',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Punk_Bounty02",'/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/a/BPChar_Punk_Bounty01a',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_Bounty02"),
    ("Punk_Bounty02",'/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/b/BPChar_Punk_Bounty01b',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_Bounty02"),
    ("Punk_Bounty02",'/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/c/BPChar_Punk_Bounty01c',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_Bounty02"),
    ("Punk_Bounty02",'/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/d/BPChar_Punk_Bounty01d',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_Bounty02"),
    ("Punk_Bounty02",'/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/BPChar_PunkBounty02',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_Bounty02"),
    ("Punk_BrewHag",'/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_BrewHag"),
    ("Punk_Basic",'/Game/Enemies/Punk_Female/_Unique/GameshowFour/_Design/_Character/BPChar_PunkGameshowFour',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Punk_Basic",'/Game/Enemies/Punk_Female/_Unique/GameshowOne/_Design/Character/BPChar_PunkGameshowOne',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Punk_Basic",'/Game/Enemies/Punk_Female/_Unique/GameshowThree/_Design/Character/BPChar_PunkGameshowThree',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Punk_Basic",'/Game/Enemies/Punk_Female/_Unique/GameshowTwo/_Design/Character/BPChar_PunkGameshowTwo',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Punk_MotherOfDragons",'/Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Character/BPChar_PunkMotherOfDragons',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_MotherOfDragons"),
    ("Punk_MovieGoer",'/Game/Enemies/Punk_Female/_Unique/MovieGoer/_Design/Character/BPChar_PunkMovieGoer',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_MovieGoer"),
    ("Punk_Prologue",'/Game/Enemies/Punk_Female/_Unique/Prologue/_Design/Character/BPChar_PunkPrologue',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Prologue"),
    ("Punk_Assaulter",'/Game/Enemies/Punk_Female/_Unique/RedAssaulter/_Design/Character/BPChar_PunkRedAssaulter',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Assaulter"),
    ("Punk_Shotgunner",'/Game/Enemies/Punk_Female/_Unique/RedShotgunner/_Design/Character/BPChar_PunkRedShotgunner',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Shotgunner"),
    ("Punk_Basic",'/Game/Enemies/Punk_Female/_Unique/SecretAgent/_Design/Character/BPChar_PunkSecretAgent',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Punk_DairyFarmer",'/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_DairyFarmer"),
    ("Punk_Badass",'/Game/Enemies/Punk_Female/_Unique/TumorHead/_Design/Character/BPChar_PunkBadass_Tumorhead',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ("Punk_WardenGuard",'/Game/Enemies/Punk_Female/_Unique/WardenGuard/_Design/Character/BPChar_PunkBasic_WardenGuard',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_WardenGuard"),
    ("Rakk_Dragon",'/Game/Enemies/Rakk/_Unique/DragonCryo/_Design/Character/BPChar_Rakk_DragonCryo',"/Game/Enemies/Rakk/_Shared/_Design/Balance/Table_Balance_Rakk_Unique","Rakk_Dragon"),
    ("Rakk_Dragon",'/Game/Enemies/Rakk/_Unique/Dragon/_Design/Character/BPChar_Rakk_Dragon',"/Game/Enemies/Rakk/_Shared/_Design/Balance/Table_Balance_Rakk_Unique","Rakk_Dragon"),
    ("Rakk_Rakk01_Hunt",'/Game/Enemies/Rakk/_Unique/Hunt01/_Design/Character/BPChar_Rakk_Hunt01',"/Game/Enemies/Rakk/_Shared/_Design/Balance/Table_Balance_Rakk_Unique","Rakk_Rakk01_Hunt"),
    ("Rakk_Skrakk01_Hunt",'/Game/Enemies/Rakk/_Unique/HuntSkrakk/_Design/Character/BPChar_Rakk_HuntSkrakk',"/Game/Enemies/Rakk/_Shared/_Design/Balance/Table_Balance_Rakk_Unique","Rakk_Skrakk01_Hunt"),
    ("Ratch_Gary",'/Game/Enemies/Ratch/_Unique/BadRat/_Design/Character/BPChar_RatchBadRat',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch_Unique","Ratch_Gary"),
    ("Ratch_Basic",'/Game/Enemies/Ratch/_Unique/EridiumBasic/_Design/Character/BPChar_RatchEridiumBasic',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch","Ratch_Basic"),
    ("Ratch_Gnat",'/Game/Enemies/Ratch/_Unique/Gnat/_Design/Character/BPChar_RatchGnat',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch_Unique","Ratch_Gnat"),
    ("Ratch_HiveAnchor",'/Game/Enemies/Ratch/_Unique/HiveAnchor/_Design/Character/BPChar_RatchHiveAnchor',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch_Unique","Ratch_HiveAnchor"),
    ("Ratch_01Hunt",'/Game/Enemies/Ratch/_Unique/Hunt01/_Design/Character/BPChar_Ratch_Hunt01',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch_Unique","Ratch_01Hunt"),
    ("Ratch_Larva",'/Game/Enemies/Ratch/_Unique/Larva/_Design/Character/BPChar_RatchLarva',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch","Ratch_Larva"),
    ("Ratch_Larva",'/Game/Enemies/Ratch/_Unique/SpaceSlug/_Design/Character/BPChar_RatchSpaceSlug',"/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch","Ratch_Larva"),
    ("Saurian_GrogPoisonFodder",'/Game/Enemies/Saurian/_Unique/Grog_Poison_Fodder/Character/BPChar_Saurian_Grog_Poison_Fodder',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_GrogPoisonFodder"),
    ("Saurian_Saurian01_Hunt",'/Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/BPChar_Saurian_Hunt01',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Saurian01_Hunt"),
    ("Saurian_Laser",'/Game/Enemies/Saurian/_Unique/Laser/_Design/Character/BPChar_SaurianLaser',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Laser"),
    ("Saurian_Queen",'/Game/Enemies/Saurian/_Unique/Queen/_Design/Character/BPChar_SaurianQueen',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Queen"),
    ("Saurian_Rare01",'/Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Rare01"),
    ("Saurian_Shield",'/Game/Enemies/Saurian/_Unique/Shield/_Design/Character/BPChar_SaurianShield',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Shield"),
    ("Saurian_Tyrant",'/Game/Enemies/Saurian/_Unique/SlaughterBoss/_Design/Character/BPChar_Saurian_SlaughterBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian","Saurian_Tyrant"),
    ("Saurian_TrialBoss",'/Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Character/BPChar_Saurian_TrialBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_TrialBoss"),
    ("ServiceBot_Basic",'/Game/Enemies/ServiceBot/_Unique/JanitorBot/_Design/Character/BPChar_ServiceBot_JanitorBot',"/Game/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_ServiceBot","ServiceBot_Basic"),
    ("ServiceBot_ServiceBot01_Rare",'/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01',"/Game/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_ServiceBot_Unique","ServiceBot_ServiceBot01_Rare"),
    ("AntEater",'/Game/Enemies/Skag/_Unique/AntEater/_Design/Character/BPChar_SkagAntEater',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","AntEater"),
    ("AntEaterPup",'/Game/Enemies/Skag/_Unique/AntEaterPup/_Design/Character/BPChar_SkagAntEatherPup',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","AntEaterPup"),
    ("Buttmunch",'/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","Buttmunch"),
    ("DemoSkag",'/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","DemoSkag"),
    ("SucculentAlpha",'/Game/Enemies/Skag/_Unique/SucculentAlpha/_Design/Character/BPChar_SkagSucculentAlpha',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","SucculentAlpha"),
    ("Succulent",'/Game/Enemies/Skag/_Unique/Succulent/_Design/Character/BPChar_SkagSucculent',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","Succulent"),
    ("TrialBoss",'/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss"),
    ("Trufflemunch",'/Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","Trufflemunch"),
    ("Spiderant_CakeRoyalty",'/Game/Enemies/Spiderant/_Unique/CakeRoyalty/_Design/Character/BPChar_SpiderantCakeRoyalty',"/Game/Enemies/Spiderant/_Shared/_Design/Balance/Table_Balance_Spiderant_Unique","Spiderant_CakeRoyalty"),
    ("Spiderant_Hunt01",'/Game/Enemies/Spiderant/_Unique/Hunt01/_Design/Character/BPChar_Spiderant_Hunt01',"/Game/Enemies/Spiderant/_Shared/_Design/Balance/Table_Balance_Spiderant_Unique","Spiderant_Hunt01"),
    ("Spiderant_CakeRoyalty",'/Game/Enemies/Spiderant/_Unique/Tarantella/_Design/Character/BPChar_SpiderantTarantella',"/Game/Enemies/Spiderant/_Shared/_Design/Balance/Table_Balance_Spiderant_Unique","Spiderant_CakeRoyalty"),
    ("TinkSentryRocketPod_BigD",'/Game/Enemies/Tink_SentryRocketPod/_Unique/BigD/_Design/Character/BPChar_Tink_SentryRocketPodBigD',"/Game/Enemies/Tink_SentryRocketPod/_Shared/_Design/Balance/Table_Balance_Tink_SentryRocketPod","TinkSentryRocketPod_BigD"),
    ("TinkSentryRocketPod_BigD",'/Game/Enemies/Tink_SentryRocketPod/_Unique/Blockade/_Design/Character/BPChar_Tink_SentryRocketPodBlockade',"/Game/Enemies/Tink_SentryRocketPod/_Shared/_Design/Balance/Table_Balance_Tink_SentryRocketPod","TinkSentryRocketPod_BigD"),
    ("TinkSentryRocketPod_GrowingPains",'/Game/Enemies/Tink_SentryRocketPod/_Unique/GrowingPains/_Design/Character/BPChar_Tink_SentryRocketPodGrowingPains',"/Game/Enemies/Tink_SentryRocketPod/_Shared/_Design/Balance/Table_Balance_Tink_SentryRocketPod","TinkSentryRocketPod_GrowingPains"),
    ("Tink_Anointed",'/Game/Enemies/Tink/_Unique/Archimedes/_Design/Character/BPChar_TinkArchimedes',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink","Tink_Anointed"),
    ("Tink_Basic",'/Game/Enemies/Tink/_Unique/BlueBasic/_Design/Character/BPChar_TinkBlueBasic',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink","Tink_Basic"),
    ("Tink_BossFodder",'/Game/Enemies/Tink/_Unique/BossFodder/_Design/Character/BPChar_TinkBossFodder',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_BossFodder"),
    ("Tink_Bounty01",'/Game/Enemies/Tink/_Unique/Bounty01/_Design/Character/BPChar_Tink_Bounty01',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_Bounty01"),
    ("Tink_BrewKid",'/Game/Enemies/Tink/_Unique/BrewKid/_Design/Character/BPChar_TinkBrewKid',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_BrewKid"),
    ("Tink_Demon",'/Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_Demon"),
    ("Tink_Basic",'/Game/Enemies/Tink/_Unique/GameshowEnforcer/_Design/Character/BPChar_TinkGameshowEnforcer',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink","Tink_Basic"),
    ("Tink_BadassArmored",'/Game/Enemies/Tink/_Unique/Interrogator/_Design/Character/BPChar_TinkInterrogator',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink","Tink_BadassArmored"),
    ("Tink_MotorcadeBigD",'/Game/Enemies/Tink/_Unique/MotorcadeBigD/_Design/Character/BPChar_TinkMotorcadeBigD',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_MotorcadeBigD"),
    ("Tink_Pain",'/Game/Enemies/Tink/_Unique/Pain/_Design/Character/BPChar_Pain',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_Pain"),
    ("Tink_Rare01",'/Game/Enemies/Tink/_Unique/Rare01/_Design/Character/BPChar_Tink_Rare01',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_Rare01"),
    ("Tink_Rare02",'/Game/Enemies/Tink/_Unique/Rare02/_Design/Character/BPChar_TinkRare02',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_Rare02"),
    ("Tink_RedJabber",'/Game/Enemies/Tink/_Unique/RedJabber/_Design/Character/BPChar_TinkRedJabber',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_RedJabber"),
    ("Tink_Stagehand",'/Game/Enemies/Tink/_Unique/Stagehand/_Design/Character/BPChar_TinkStagehand',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_Stagehand"),
    ("Tink_TrialBoss",'/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss"),
    ("Tink_BountyPrologue",'/Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_BountyPrologue"),
    ("Hunt01_Humanoid",'/Game/Enemies/Tink/_Unique/VarkidHunt01/BPChar_VarkidHunt01_Tink',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt01_Humanoid"),
    ("Tink_WardenGuard",'/Game/Enemies/Tink/_Unique/WardenGuard/_Design/Character/BPChar_TinkPsychoWardenGuard',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_WardenGuard"),
    ("Trooper_Bounty01",'/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Bounty01"),
    ("Trooper_Bounty02",'/Game/Enemies/Trooper/_Unique/Bounty02/Design/Character/BPChar_TrooperBounty02',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Bounty02"),
    ("Trooper_Bounty03",'/Game/Enemies/Trooper/_Unique/Bounty03/Design/Character/BPChar_TrooperBounty03',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Bounty03"),
    ("Trooper_ChumpBasic",'/Game/Enemies/Trooper/_Unique/ChumpBasic/_Design/Character/BPChar_TrooperChumpBasicDark',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_ChumpBasic"),
    ("Trooper_ChumpBasic",'/Game/Enemies/Trooper/_Unique/ChumpBasic/_Design/Character/BPChar_TrooperChumpBasic',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_ChumpBasic"),
    ("Trooper_ChumpMelee",'/Game/Enemies/Trooper/_Unique/ChumpMelee/_Design/Character/BPChar_TrooperChumpMeleeDark',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_ChumpMelee"),
    ("Trooper_ChumpMelee",'/Game/Enemies/Trooper/_Unique/ChumpMelee/_Design/Character/BPChar_TrooperChumpMelee',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_ChumpMelee"),
    ("Trooper_JavaFlasher",'/Game/Enemies/Trooper/_Unique/JavaFlasher/_Design/Character/BPChar_TrooperJavaFlasher',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_JavaFlasher"),
    ("Trooper_Rare01a",'/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01a',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Rare01a"),
    ("Trooper_Rare01b",'/Game/Enemies/Trooper/_Unique/Rare01b/_Design/Character/BPChar_Trooper_Rare01b',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Rare01b"),
    ("Trooper_Rare01c",'/Game/Enemies/Trooper/_Unique/Rare01c/_Design/Character/BPChar_Trooper_Rare01c',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Rare01c"),
    ("Trooper_Rare01d",'/Game/Enemies/Trooper/_Unique/Rare01d/_Design/Character/BPChar_Trooper_Rare01d',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Rare01d"),
    ("Trooper_Rare01e",'/Game/Enemies/Trooper/_Unique/Rare01e/_Design/Character/BPChar_Trooper_Rare01e',"/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique","Trooper_Rare01e"),
    ("BossFodder",'/Game/Enemies/Varkid/_Unique/BossFodder/_Design/Character/BPChar_VarkidBossFodder',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","BossFodder"),
    ("Hunt01",'/Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01_Larva',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt01"),
    ("Hunt01",'/Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt01"),
    ("Hunt02_Adult",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Adult/BPChar_VarkidHunt02_AdultA',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Adult"),
    ("Hunt02_Adult",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Adult/BPChar_VarkidHunt02_AdultB',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Adult"),
    ("Hunt02_Badass",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Badass/BPChar_VarkidHunt02_Badass',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Badass"),
    ("Hunt02_Larva",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaA',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Larva"),
    ("Hunt02_Larva",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaB',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Larva"),
    ("Hunt02_Larva",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaC',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Larva"),
    ("Hunt02_Larva",'/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaD',"/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique","Hunt02_Larva"),
    ("HeavyGatekeeper",'/Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/Gatekeeper/_Design/Character/BPChar_Heavy_BloodyHarvest_Gatekeeper',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","HeavyGatekeeper"),
    ("Boss_Uber",'/Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss_Uber',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Boss_Uber"),
    ("Boss_Normal",'/Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Boss_Normal"),
    ("Ratch_Badass",'/Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyBadass/_Design/Character/BPChar_RatchBloodyBadass',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Ratch_Badass"),
    ("Ratch_Birther",'/Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyBirther/_Design/Character/BPChar_RatchBloodyBirther',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Ratch_Birther"),
    ("Ratch_Basic",'/Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/Bloody/_Design/Character/BPChar_RatchBloody',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Ratch_Basic"),
    ("Ratch_BadassGatekeeper",'/Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyGatekeeper/_Design/Character/BPChar_RatchBloodyBadassGatekeeper',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Ratch_BadassGatekeeper"),
    ("Ratch_Hive",'/Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyHive/_Design/Character/BPChar_RatchBloodyHive',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","Ratch_Hive"),
    ("TrooperChumpBasic",'/Game/PatchDLC/BloodyHarvest/Enemies/Trooper/_Unique/ChumpBasic/_Design/Character/BPChar_TrooperChumpBasic_BloodyHarvest',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","TrooperChumpBasic"),
    ("TrooperChumpBasic",'/Game/PatchDLC/BloodyHarvest/Enemies/Trooper/_Unique/ChumpMelee/_Design/Character/BPChar_TrooperChumpMelee_BloodyHarvest',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","TrooperChumpBasic"),
    ("TrooperGatekeeper",'/Game/PatchDLC/BloodyHarvest/Enemies/Trooper/_Unique/Gatekeeper/_Design/Character/BPChar_Trooper_BloodyHarvest_Gatekeeper',"/Game/PatchDLC/BloodyHarvest/Enemies/_Shared/_Design/Balance/Table_Balance_HarvestEnemies","TrooperGatekeeper"),
    ("DropShipTurret_Basic",'/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/BrainBeams/Character/BPChar_BrainBeam',"/Game/Enemies/DropShipTurret/_Shared/_Design/Balance/Table_Balance_DropShipTurret","DropShipTurret_Basic"),
    ("Behemoth_Raid",'/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/_Design/Character/BPChar_BehemothRaid',"/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth","Behemoth_Raid"),
    ("Behemoth_RaidBrain",'/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/SpiderBrain/Character/BPChar_SpiderBrain',"/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth","Behemoth_RaidBrain"),
    ("BehemothRaid_UpperHalf",'/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/UpperHalf/Character/BPChar_UpperHalf',"/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth","BehemothRaid_UpperHalf"),
    ("Mech_RaidBossA",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Character/BPChar_MechRaidBossA',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossA"),
    ("Mech_Raid_BossBar",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossBar/_Design/Character/BPChar_MechRaidBossBar',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_Raid_BossBar"),
    ("Mech_RaidBossB",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Character/BPChar_MechRaidBossB',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossB"),
    ("MechRaidBossC",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidBossC"),
    ("MechRaidMiniBossAdds",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossMini/_Design/Character/BPChar_RaidBossMini',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidMiniBossAdds"),
    ("Oversphere_Harbinger",'/Game/PatchDLC/Raid1/Enemies/Oversphere/_Unique/BadassHarbinger/_Design/Character/BPChar_BadassHarbinger',"/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere","Oversphere_Harbinger"),
    ("OversphereBoss01_Raid",'/Game/PatchDLC/Raid1/Enemies/Oversphere/_Unique/RaidBoss/_Design/Character/BPChar_Oversphere_RaidBoss',"/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique","OversphereBoss01_Raid"),
    ("AlteredBeast",'/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","AlteredBeast"),
    ("BigJohn",'/Geranium/Enemies/Biobeast/_Unique/BigJohn/_Design/Character/BPChar_Biobeast_BigJohn',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","BigJohn"),
    ("Badass",'/Geranium/Enemies/Biobeast/_Unique/Biobetsy/_Design/Character/BPChar_Biobeast_Biobetsy',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast","Badass"),
    ("CopyBeast_Copy",'/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast_Copy',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","CopyBeast_Copy"),
    ("CopyBeast",'/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","CopyBeast"),
    ("PlasmaBeast",'/Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/BPChar_Biobeast_PlasmaBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","PlasmaBeast"),
    ("GerEnforcer_Dispatcher",'/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance_Unique","GerEnforcer_Dispatcher"),
    ("Enforcer_Gun",'/Geranium/Enemies/GerEnforcer/_Unique/LBN_Doctor/_Design/Character/BPChar_GerEnforcerLBN_Doctor_NoShield',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance","Enforcer_Gun"),
    ("Enforcer_Shield",'/Geranium/Enemies/GerEnforcer/_Unique/LBN_Doctor/_Design/Character/BPChar_GerEnforcerLBN_Doctor',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance","Enforcer_Shield"),
    ("GerEnforcer_Yarp",'/Geranium/Enemies/GerEnforcer/_Unique/Yarp/_Design/Character/BPChar_GerEnforcerYarp',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance_Unique","GerEnforcer_Yarp"),
    ("GerPsycho_DD_Steve",'/Geranium/Enemies/GerPsycho_Male/_Unique/DD_Steve/_Design/Character/BPChar_GerPsychoDD_Steve',"/Geranium/Enemies/GerPsycho_Male/_Shared/_Design/Balance/Table_GerPsycho_Balance_Unique","GerPsycho_DD_Steve"),
    ("GerPsycho_MoleMan",'/Geranium/Enemies/GerPsycho_Male/_Unique/MoleMan/_Design/Character/BPChar_GerPsychoMoleMan',"/Geranium/Enemies/GerPsycho_Male/_Shared/_Design/Balance/Table_GerPsycho_Balance_Unique","GerPsycho_MoleMan"),
    ("GerPsycho_PhaserPete",'/Geranium/Enemies/GerPsycho_Male/_Unique/PhaserPete/_Design/Character/BPChar_GerPsychoPhaserPete',"/Geranium/Enemies/GerPsycho_Male/_Shared/_Design/Balance/Table_GerPsycho_Balance_Unique","GerPsycho_PhaserPete"),
    ("GerPunk_Greg",'/Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/BPChar_GerPunkGreg_Rakk',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance_Unique","GerPunk_Greg"),
    ("GerPunk_Greg",'/Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/BPChar_GerPunkGreg',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance_Unique","GerPunk_Greg"),
    ("Punk_Basic",'/Geranium/Enemies/GerPunk_Female/_Unique/GS_Leader/_Design/Character/BPChar_GerPunkGS_Leader',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance","Punk_Basic"),
    ("GerPunk_Larry",'/Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/BPChar_GerPunkLarry',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance_Unique","GerPunk_Larry"),
    ("Punk_Basic",'/Geranium/Enemies/GerPunk_Female/_Unique/LBN_Bandit/_Design/Character/BPChar_GerPunkLBN_Bandit',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance","Punk_Basic"),
    ("Punk_Basic",'/Geranium/Enemies/GerPunk_Female/_Unique/LBN_Keem/_Design/Character/BPChar_GerPunkLBN_Keem',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance","Punk_Basic"),
    ("GerPunk_Number",'/Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/BPChar_GerPunkNumber',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance_Unique","GerPunk_Number"),
    ("GerPunkSOS_Doc",'/Geranium/Enemies/GerPunk_Female/_Unique/SOS_Doc/_Design/Character/BPChar_GerPunkSOS_Doc',"/Geranium/Enemies/GerPunk_Female/_Shared/_Design/Balance/Table_GerPunk_Balance_Unique","GerPunkSOS_Doc"),
    ("GerRakkBB_Assblaster",'/Geranium/Enemies/GerRakk/_Unique/BB_Assblaster/_Design/Character/BPChar_GerRakkBB_Assblaster',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkBB_Assblaster"),
    ("GerRakkLasodactyl",'/Geranium/Enemies/GerRakk/_Unique/Lasodactyl/_Design/Character/BPChar_GerRakkLasodactyl',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkLasodactyl"),
    ("GerRakkLM_Spirit",'/Geranium/Enemies/GerRakk/_Unique/LM_Spirit/_Design/Character/BPChar_GerRakkLM_Spirit',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkLM_Spirit"),
    ("GerRakkMother_Baby",'/Geranium/Enemies/GerRakk/_Unique/Mother/_Design/Character/BPChar_GerRakkMother_Baby',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkMother_Baby"),
    ("GerRakkMother",'/Geranium/Enemies/GerRakk/_Unique/Mother/_Design/Character/BPChar_GerRakkMother',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkMother"),
    ("GerRakkRod",'/Geranium/Enemies/GerRakk/_Unique/Rod/_Design/Character/BPChar_GerRakkRod',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkRod"),
    ("Devourer_GrogPoison",'/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_GrogPoison',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","Devourer_GrogPoison"),
    ("Devourer_Grog",'/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Grog',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","Devourer_Grog"),
    ("Devourer_HamtaurusBadass",'/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_HamBadass',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","Devourer_HamtaurusBadass"),
    ("Devourer_Pygmimus",'/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Pygmimus',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","Devourer_Pygmimus"),
    ("Devourer_Tyrant",'/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Tyrant',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","Devourer_Tyrant"),
    ("GerSaurian_Dispatcher",'/Geranium/Enemies/GerSaurian/_Unique/Dispatcher/_Design/Character/BPChar_GerSaurianDispatcher',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurian_Dispatcher"),
    ("GerSaurian_Grogzilla",'/Geranium/Enemies/GerSaurian/_Unique/Grogzilla/_Design/Character/BPChar_GerSaurianGrogzilla',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurian_Grogzilla"),
    ("GerSaurian_Horsemen1",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen1/_Design/Character/BPChar_GerSaurianHorsemen1',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurian_Horsemen1"),
    ("Tink_Basic",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen1/_Design/Rider/BPChar_GerTinkHorsemen1',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink","Tink_Basic"),
    ("GerSaurian_Horsemen2",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen2/_Design/Character/BPChar_GerSaurianHorsemen2',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurian_Horsemen2"),
    ("Enforcer_Shield",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen2/_Design/Rider/BPChar_GerEnforcerHorsemen2',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance","Enforcer_Shield"),
    ("GerSaurian_Horsemen3",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen3/_Design/Character/BPChar_GerSaurianHorsemen3',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurian_Horsemen3"),
    ("Punk_Basic",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen3/_Design/Rider/BPChar_GerPunkHorsemen3',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("GerSaurian_Horsemen4",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Character/BPChar_GerSaurianHorsemen4',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurian_Horsemen4"),
    ("Punk_Basic",'/Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Rider/BPChar_GerPunkHorsemen4',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    ("Saurian_Grog",'/Geranium/Enemies/GerSaurian/_Unique/LBN_GunGrog/_Design/Character/BPChar_GerSaurianLBN_GunGrog',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance","Saurian_Grog"),
    ("Saurian_Predator",'/Geranium/Enemies/GerSaurian/_Unique/LBN_GunPred/_Design/Character/BPChar_GerSaurianLBN_GunPred',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance","Saurian_Predator"),
    ("Punk_Basic",'/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur_Punk',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Basic"),
    # (,'/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur',,),
    ("GerSaurianSV_Daisy",'/Geranium/Enemies/GerSaurian/_Unique/SV_Daisy/_Design/Character/BPChar_GerSaurianSV_Daisy',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurianSV_Daisy"),
    ("GerSaurianSV_PGrog",'/Geranium/Enemies/GerSaurian/_Unique/SV_PGrog/_Design/Character/BPChar_SaurianSV_PGrog',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurianSV_PGrog"),
    ("GerSaurianSV_Predator",'/Geranium/Enemies/GerSaurian/_Unique/SV_Predator/_Design/Character/BPChar_SaurianSV_Predator',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique","GerSaurianSV_Predator"),
    ("Saurian_Hamtaurus",'/Geranium/Enemies/GerSaurian/_Unique/WW_Toge/_Design/Character/BPChar_GerSaurianWW_Toge',"/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance","Saurian_Hamtaurus"),
    ("GerTink_Prohibitor",'/Geranium/Enemies/GerTink/_Unique/Prohibitor/_Design/Character/BPChar_GerTinkProhibitor',"/Geranium/Enemies/GerTink/_Shared/_Design/Balance/Table_GerTink_Balance_Unique","GerTink_Prohibitor"),
    ("Gyro_Painless",'/Geranium/Enemies/Gyro/_Unique/Painless/_Design/Character/BPChar_GyroPainless',"/Geranium/Enemies/Gyro/_Shared/_Design/Balance/Table_Gyro_Balance_Unique","Gyro_Painless"),
    ("HibEnforcer_SpinMouth",'/Hibiscus/Enemies/FrostBiters/_Unique/_Design/Character/BPChar_Spinsmouth',"/Hibiscus/Enemies/FrostBiters/Enforcer/_Shared/_Design/Balance/Table_HibEnforcer_Balance","HibEnforcer_SpinMouth"),
    ("Hunt_GmorkWolf_Woods",'/Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child',"/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique","Hunt_GmorkWolf_Woods"),
    ("Hunt_Hampton_Camp",'/Hibiscus/Enemies/_Unique/Hunt_Hampton/Character/BPChar_Hib_Hunt_Hampton',"/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique","Hunt_Hampton_Camp"),
    ("Slug_Badass_Hunt_Kratch",'/Hibiscus/Enemies/_Unique/Hunt_Kratch/Character/BPChar_SlugBadass_Kratch',"/Hibiscus/Enemies/Slug/_Shared/_Design/Balance/Table_Balance_Slug_PT1","Slug_Badass_Hunt_Kratch"),
    ("Hunt_Kritchy_Village",'/Hibiscus/Enemies/_Unique/Hunt_Kritchy/Character/BPChar_Hib_Hunt_Kritchy',"/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique","Hunt_Kritchy_Village"),
    ("Ape_Cryo",'/Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti_Adds_ApeCryo',"/Game/Enemies/Ape/_Shared/_Design/Balance/Table_Balance_Ape","Ape_Cryo"),
    ("Hunt_Yeti_Lake",'/Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti',"/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique","Hunt_Yeti_Lake"),
    ("EP1_SlugMama",'/Hibiscus/Enemies/_Unique/Mission/EP1_SlugMama/BPChar_SlugCarrier_Child_Mama',"/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique","EP1_SlugMama"),
    ("PrivateEye_NekroBugBadass",'/Hibiscus/Enemies/_Unique/Mission_Other/NekroBug_Spirit/Character/BPChar_Hib_Nekro_SpiritBadass',"/Hibiscus/Enemies/Wolf/_Shared/_Design/Balance/Table_Balance_Wolven","PrivateEye_NekroBugBadass"),
    ("PrivateEye_NekrobugSpirit",'/Hibiscus/Enemies/_Unique/Mission_Other/NekroBug_Spirit/Character/BPChar_Hib_Nekro_Spirit',"/Hibiscus/Enemies/Wolf/_Shared/_Design/Balance/Table_Balance_Wolven","PrivateEye_NekrobugSpirit"),
    ("SM_WhereIBelong_BadassKrich",'/Hibiscus/Enemies/_Unique/Mission/SM_WhereIBelong/BPChar_SlugCarrier_WhereIBelong',"/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique","SM_WhereIBelong_BadassKrich"),
    ("Frost_Dragon_Rare",'/Hibiscus/Enemies/_Unique/Rare_Frost_Dragon/Character/BPChar_Rare_Frost_Dragon',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Frost_Dragon_Rare"),
    ("LostOne_Badass",'/Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","LostOne_Badass"),
    ("Zealot_Nightmare",'/Hibiscus/Enemies/_Unique/Rare_Shocker/Character/BPChar_ZealotNightmareShocker_Rare',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Zealot_Nightmare"),
    ("Zealot_PilferEye_Rare",'/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_PilferEyeBasic_Child_Rare',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Zealot_PilferEye_Rare"),
    ("Zealot_Pilfer_Rare",'/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Zealot_Pilfer_Rare"),
]
