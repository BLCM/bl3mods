import boss
from boss import JUST_QUARTER_HEALTH, HALF_HEALTH, JUST_TWO_THIRDS_HEALTH, DEFAULT_HEALTH

heavy_bosses = [
    ('Junpai Goat Eater','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_PunkBadass_Gaud',None,None),
    ('Loco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coc',None,None),
    ("Hildr",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidBossC"),
    ("Rota",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Character/BPChar_MechRaidBossB',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossB"),
    ("Sigrdrifa",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Character/BPChar_MechRaidBossA',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossA"),
    ('Captain Traunt','/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":51}),
    ('General Traunt','/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":52}),
    ('Gigamind','/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique','Nog_ChipHolder'),
    ('Billy, the Anointed','/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBoss',None,None),
]

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
    ('Fungal Gorger','/Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child','/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists','LostOne_Badass'),
    ('OnePunch','/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','OnePunch'),
    ('Judge Hightower','/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01','/Game/NonPlayerCharacters/_Shared/_Design/Table_Balance_NPC','AtlasSoldier_Bounty'),
    # works
    ('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur'),
    # works
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
    # works
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
    ('Rachael, the Anointed','/Game/Enemies/Goon/Anointed/_Design/Character/BPChar_GoonAnointed',None,None),
    ('Turnkey Tim','/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey',None,None),
    ('Atomic','/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01',None,None),
    ('Baron Noggin','/Game/Enemies/Nog/_Unique/Nog01_Bounty/_Design/Character/BPChar_Nog01_Bounty',None,None),
    ('Crushjaw','/Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01',None,None),
    ('Handsome Jackie','/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/BPChar_PunkBounty02',None,None),
    ('DJ Deadsk4g','/Game/Enemies/Enforcer/_Unique/Bounty02/_Design/Character/BPChar_Enforcer_Bounty02',None,None),
    ('Heckle','/Game/Enemies/Goliath/_Unique/Bounty01/_Design/Character/BPChar_Goliath_Bounty01',None,None),
    ('Sky Bully','/Game/Enemies/Tink/_Unique/Bounty01/_Design/Character/BPChar_Tink_Bounty01',None,None),
    # works
    ('Sylestro','/Game/Enemies/Heavy/_Unique/Bounty01/_Design/Character/BPChar_Heavy_Bounty01',None,None),
    # works
    ('Demoskaggon','/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique',"DemoSkag",
     {"health":[0.5*DEFAULT_HEALTH],"raid1":61}),
    ('El Dragón Jr.','/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',
     '/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',
     'Rare03'),
    ('Urist McEnforcer','/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance','Enforcer_Shield'), # I hope this is safe
    # works
    ('Wick','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare03'),
    ('Borman Nates','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare02','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare02'),
    # works
    ('Warty','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare01','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare01',{"raid1":64}),
    ('Tink of Cunning','/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss",
     {"raid1":66}),
    ('Skag of Survival','/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss",
     {"raid1":62}),
    ('Sera of Supremacy','/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss",{"raid1":49}),
    ('Mr. Titan','/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique",'SlaughterBoss'),
    ('Hag of Fervor','/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial",{"raid1":48}),    
    ('Jerrick Logan','/Geranium/Enemies/GerPsycho_Male/_Unique/PhaserPete/_Design/Character/BPChar_GerPsychoPhaserPete',None,None),
    ('Caber Dowd','/Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/BPChar_GerPunkLarry',None,None),
    # ('Dickon Goyle','/Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/BPChar_GerPunkGreg_Rakk',None,None),
    ('Maxitrillion','/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01',None,None),
    #('Sloth','/Game/Enemies/Goon/_Unique/Rare01/_Design/Character/BPChar_Goon_Rare01',None,None),
    ('DEGEN-3','/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass_Venchy',None,None),
    ('Gorgeous Armada','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',None,None),
    ('Evil St. Lawrence','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',None,None),
    # ('Junpai Goat Eater','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_PunkBadass_Gaud',None,None),
    # ('Loco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coc',None,None),
    ('Gmork','/Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child',None,None),
    ('Tom','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_BigBro',None,None),
    ('Voltborn','/Hibiscus/Enemies/_Unique/Rare_Shocker/Character/BPChar_ZealotNightmareShocker_Rare',None,None),
    ('Xam','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_ToughBro',None,None),
    ('Yeti','/Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti',None,None),
    ('Garriden Loch','/Geranium/Enemies/GerTink/_Unique/Prohibitor/_Design/Character/BPChar_GerTinkProhibitor',None,None),
    ('Haddon Marr','/Geranium/Enemies/GerEnforcer/_Unique/Yarp/_Design/Character/BPChar_GerEnforcerYarp',None,None),
    ('Lani Dixon','/Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/BPChar_GerPunkNumber',None,None),
    ('Blinding Banshee','/Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01',None,None),
    ('Sheega','/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady',None,None),
    # ('The Tink-Train','/Game/Enemies/Goon/_Unique/MonsterTrucker/_Design/Character/BPChar_GoonMonsterTrucker',None,None),
    ('Azalea','/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag',None,None),
    ('Lagromar','/Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon',None,None),
    ('Procurer','/Hibiscus/Enemies/Zealot/Badass/_Design/Character/BPChar_Zealot_Badass_Procurer',None,None),
    ('Ipswitch Dunne','/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher',None,None),
    # These guys can cause problems
    # ('Captain Traunt','/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":51}),
    # ('General Traunt','/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":52}),
    #('Katagawa Ball','/Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere',
    # '/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique','Oversphere_Katagawa'), #
    # Warden Partially spawns
    ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"),
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'),
    # ('Gigamind','/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique','Nog_ChipHolder'),
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
    #("Loader_Gun",'/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1","Loader_Gun"),
    ("DebtCollector",'/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","DebtCollector"),
    # ("Harker",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
    ("Dr Benedict",'/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict',"/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1","Basic"),
    ("Enforcer_Reaper",'/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper',"/Ixora/Enemies/CotV/Enforcer/_Shared/_Design/Balance/Table_Balance_Enforcer_Ixora","Enforcer_Reaper"),
    ("GeneralBlisterPuss",'/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","GeneralBlisterPuss"),
    ("TheBlackRook",'/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","TheBlackRook"),
    #("APBulletRider",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"),
    #("SpongeBoss",'/Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss',"/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss","SpongeBoss"),
    ("Security Sergeant",'/Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"),
    ("Security Chief",'/Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"),
    ("TheBlackKing",'/Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing',"/Alisma/Enemies/AliPsycho/_Shared/_Design/Balance/Table_Balance_AliPsycho_Unique","TheBlackKing"),
    ("Hyperion Warden",'/Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"),
    ("Scraptrap Queen",'/Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character/BPChar_ClaptrapQueen',"/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1","Queen"),
    ("Kormash",'/Geranium/Enemies/LodgeBoss/_Design/Character/BPChar_SploderBoss',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance_Unique","GerEnforcer_SploderBoss"),
    # ("Hildr",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidBossC"),
    #("Rota",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Character/BPChar_MechRaidBossB',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossB"),
    #("Sigrdrifa",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Character/BPChar_MechRaidBossA',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","Mech_RaidBossA"),
    ("Aurelia",'/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Character/BPChar_AureliaBoss',"/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Balance/Table_Balance_AureliaBoss","AureliaBoss"),
]



easy_bosses = [
    # 1
    ('Pyschobillies (d)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/d/BPChar_Punk_Bounty01d',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    # 1
    ('Pyschobillies (c)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/c/BPChar_Punk_Bounty01c',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    # 1
    ('Pyschobillies (b)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/b/BPChar_Punk_Bounty01b',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    # 1
    ('Pyschobillies (a)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/a/BPChar_Punk_Bounty01a',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    # 5
    ('The Unstoppable','/Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01',
     '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique','Rare01'),
    # 1
    ('Private Beans','/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog','Nog_Badass',JUST_TWO_THIRDS_HEALTH),
    # 1
    ('Judge Hightower','/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01','/Game/NonPlayerCharacters/_Shared/_Design/Table_Balance_NPC','AtlasSoldier_Bounty'),
    ('Archer Rowe','/Game/Enemies/Heavy/_Unique/DinerBoss/_Design/Character/BPChar_HeavyDinerBoss',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","DinerBoss"),
    # 1
    ('Handsome Jackie','/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/BPChar_PunkBounty02',None,None),
    ('Big Donny','/Game/Enemies/Tink/_Unique/MotorcadeBigD/_Design/Character/BPChar_TinkMotorcadeBigD',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_MotorcadeBigD"),
    ('Atomic','/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01',None,None),
    ('Baron Noggin','/Game/Enemies/Nog/_Unique/Nog01_Bounty/_Design/Character/BPChar_Nog01_Bounty',None,None), # E
    # ('Crushjaw','/Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01',None,None), # E
    # ('Sky Bully','/Game/Enemies/Tink/_Unique/Bounty01/_Design/Character/BPChar_Tink_Bounty01',None,None), # E
    # ('Warty','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare01','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare01',{"raid1":64}), # E
    ('Sheega','/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady',None,None), # E
    ('Rudy Varlope','/Dandelion/Enemies/Looters/_Unique/GreatEscape/_Design/Character/BPChar_GreatEscape_Rudy',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","RudyVarlope"), # E
    # ('Coco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco',"/Dandelion/Enemies/Looters/Goon/_Shared/_Design/Balance/Table_Balance_GoonLooter","Goon_BadassLooter"), # E
    ('Golden Bullion','/Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","GoldenBullion"), # E
    # ('Handsome Jacket','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"), # E
    # ('Handsome Slacks','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"), # E
    ('TricksyNick','/Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TricksyNick"), # E
    #("Loader_Gun",'/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1","Loader_Gun"), # E
    #("APBulletRider",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"), # E
    ('Undertaker','/Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker','/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique','Tink_BountyPrologue'),

    ('Force Trooper Citrine','/Game/Enemies/Trooper/_Unique/Rare01b/_Design/Character/BPChar_Trooper_Rare01b',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01b',
     {'raid1':68,'health':HALF_HEALTH}
    ),
    ('Force Trooper Ruby','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01c',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01c',
     {'raid1':69,'health':HALF_HEALTH}
    ),
    ('Force Trooper Tourmaline','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01d',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01d',
     {'raid1':70,'health':HALF_HEALTH}
    ),
    ('Force Trooper E','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01e',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01e',
     {'raid1':71,'health':HALF_HEALTH}
    ),
    ('Blinding Banshee','/Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01',None,None), # M

]
medium_bosses = [
    ('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur'),
    ('Dumptruck',
     '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_BountyPrologue',
     {"raid1":43},
    ),

    ('Turnkey Tim','/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey',None,None),

    ('Rax','/Game/Enemies/Trooper/_Unique/Bounty02/Design/Character/BPChar_TrooperBounty02',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Bounty02',
     {'raid1':91,'health':HALF_HEALTH}
    ),
    ('Max','/Game/Enemies/Trooper/_Unique/Bounty02/Design/Character/BPChar_TrooperBounty03',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Bounty03',
     {'raid1':92,'health':HALF_HEALTH}
    ),
    ('Force Trooper Onyx','/Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01a',
     '/Game/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_Trooper_Unique','Trooper_Rare01a',
     {'raid1':67,'health':HALF_HEALTH}
    ),
    ('Buttmunch','/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Buttmunch',{"health":[DEFAULT_HEALTH/2],"raid1":88}),
    ('Trufflemunch','/Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Trufflemunch',{"health":[DEFAULT_HEALTH/2],"raid1":89}),
    ('Fungal Gorger','/Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child','/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists','LostOne_Badass'),
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
    ('Hydragoian','/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","CopyBeast"),
    # ('Billy, the Anointed','/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBoss',None,None),
    ('Rachael, the Anointed','/Game/Enemies/Goon/Anointed/_Design/Character/BPChar_GoonAnointed',None,None),
    ('Borman Nates','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare02','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare02'),
    ('DJ Deadsk4g','/Game/Enemies/Enforcer/_Unique/Bounty02/_Design/Character/BPChar_Enforcer_Bounty02',None,None), # M
    ('Heckle','/Game/Enemies/Goliath/_Unique/Bounty01/_Design/Character/BPChar_Goliath_Bounty01',None,None), # M
    ('Sylestro','/Game/Enemies/Heavy/_Unique/Bounty01/_Design/Character/BPChar_Heavy_Bounty01',None,None), # M
    ('Demoskaggon','/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique',"DemoSkag", {"health":[0.5*DEFAULT_HEALTH],"raid1":61}),# M
    ('El Dragón Jr.','/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03','/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03', 'Rare03'), # M
    ('Urist McEnforcer','/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance','Enforcer_Shield'), # M
    ('Jerrick Logan','/Geranium/Enemies/GerPsycho_Male/_Unique/PhaserPete/_Design/Character/BPChar_GerPsychoPhaserPete',None,None), # M
    ('DEGEN-3','/Game/PatchDLC/Dandelion/Enemies/Loader/Badass/_Design/Character/BPChar_LoaderBadass_Venchy',None,None), # M
    ('Gorgeous Armada','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',None,None), # M
    ('Evil St. Lawrence','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',None,None), # M
    ('Gmork','/Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child',None,None), # M
    ('Yeti','/Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti',None,None), # M
    ('Garriden Loch','/Geranium/Enemies/GerTink/_Unique/Prohibitor/_Design/Character/BPChar_GerTinkProhibitor',None,None), # M
    ('Haddon Marr','/Geranium/Enemies/GerEnforcer/_Unique/Yarp/_Design/Character/BPChar_GerEnforcerYarp',None,None), # M
    # 1
    ('Azalea','/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag',None,None), # M
    ('Lagromar','/Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon',None,None), # M
    ('The Shark','/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_PsychoShark',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TheShark"), # M
    ('Domino','/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina',"/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Balance/Table_Balance_DoubleDownDomino","Domino"), # M
    ('MachineGun Mikey','/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_MachineGunMikey',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath","Badass"), # M
    # ('Yvan','/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan',"/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Balance/Table_Balance_RagingBot","Raging_Yvan"), # M
    ('Steel Dragon','/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part3/_Design/Character/BPChar_DoItForDigby_SteelDragon',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","SteelDragon"), # M
    ('BloodBucket','/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part2/Character/BPChar_DoItForDigby_BloodBucket',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","BloodBucket"), # M
    # I've never seen ThirdRail spawn
    # ('ThirdRail','/Dandelion/Enemies/Looters/_Unique/MeetTimothy/_Design/Character/BPChar_MeetTimothy_ThirdRail',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","ThirdRail"), # M
    ('Giorgio','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',"/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters","Tink_Badass"), # M
    ('Lawrence','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',"/Dandelion/Enemies/Looters/Enforcer/_Shared/_Design/Balance/Table_Enforcer_BalanceLooters","Enforcer_Badass"), # M
    ('TonyBordel LLC','/Dandelion/Enemies/Looters/_Unique/OneMansTrash/_Design/Character/BPChar_OneMansTrash_TonyBordel',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TonyBordel"), # M
    ('Casinobot Janitor','/Dandelion/Enemies/ServiceBot/Unique_Janitor/_Design/Character/BPChar_CasinoBot_BigJanitor',"/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot","CasinoBot_Janitor"), # M
    ("Dandellion",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Dandellion"), # M
    ("Petunia",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Petunia"), # M
    #("Facemelt",'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Facemelt"), # M
    # ("DebtCollector",'/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","DebtCollector"), # M
    ("GeneralBlisterPuss",'/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","GeneralBlisterPuss"), # M
    ("TheBlackRook",'/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","TheBlackRook"), # M
    ("TheBlackKing",'/Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing',"/Alisma/Enemies/AliPsycho/_Shared/_Design/Balance/Table_Balance_AliPsycho_Unique","TheBlackKing"), # M

]

hard_bosses = [
    ('Lectrikor','/Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/BPChar_Biobeast_PlasmaBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","PlasmaBeast"),
    ('Amach','/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Zealot_Pilfer_Rare"),
    ('Anointed Alpha','/Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoe',"/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique","Enforcer_AnointedJoe"),

    ('Anointed X-2','/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX2',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique","Punk_AnointedX2"),
    ('Anointed X-3','/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX3',None,None),
    ('Anointed X-4','/Game/Enemies/Psycho_Male/_Unique/AnointedX4/Character/BPChar_PsychoAnointedX4',"/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique","PsychoAnointedX4"),
    ("Aurelia",'/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Character/BPChar_AureliaBoss',"/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Balance/Table_Balance_AureliaBoss","AureliaBoss"),
    # ('Skag of Survival','/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss",
    # {"raid1":62}),
    #('Sera of Supremacy','/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss",{"raid1":49}),
    # ('Hag of Fervor','/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial",{"raid1":48}),    
    ('Wick','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare03'), # H
    #('Tink of Cunning','/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss", {"raid1":66}), # H
    ('Mr. Titan','/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique",'SlaughterBoss'), # H
    ('Caber Dowd','/Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/BPChar_GerPunkLarry',None,None), # H
    # Too annoying
    # ('Maxitrillion','/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01',None,None), # H
    ('Tom','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_BigBro',None,None), # H
    ('Voltborn','/Hibiscus/Enemies/_Unique/Rare_Shocker/Character/BPChar_ZealotNightmareShocker_Rare',None,None), # H
    ('Xam','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_ToughBro',None,None), # H
    ('Lani Dixon','/Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/BPChar_GerPunkNumber',None,None), # H
    ('Procurer','/Hibiscus/Enemies/Zealot/Badass/_Design/Character/BPChar_Zealot_Badass_Procurer',None,None), # H
    ('Ipswitch Dunne','/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher',None,None), # H
    # ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"), # H
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'), # H
    ("Dr Benedict",'/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict',"/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1","Basic"), # H
    # 1
    ("Enforcer_Reaper",'/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper',"/Ixora/Enemies/CotV/Enforcer/_Shared/_Design/Balance/Table_Balance_Enforcer_Ixora","Enforcer_Reaper"), # H
    # too hard in arm's race
    # ("SpongeBoss",'/Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss',"/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss","SpongeBoss"), # H
    #("Security Sergeant",'/Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"), # H
    #("Security Chief",'/Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"), # H
    #("Hyperion Warden",'/Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"), # H
    # scraptrap is too hard
    #("Scraptrap Queen",'/Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character/BPChar_ClaptrapQueen',"/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1","Queen"), # H
    ("Kormash",'/Geranium/Enemies/LodgeBoss/_Design/Character/BPChar_SploderBoss',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance_Unique","GerEnforcer_SploderBoss"), # H
    ('OnePunch','/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','OnePunch'),
    #("Hildr",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidBossC"), # H

]


# Easy E, Medium M, Hard H, Ignore I
bpchars_text_tuple="""E /Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01
I /Game/Enemies/Goon/_Unique/Rare01/_Design/Character/BPChar_Goon_Rare01
I /Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss
I /Game/Enemies/Goon/_Unique/MonsterTrucker/_Design/Character/BPChar_GoonMonsterTrucker
I /Game/Enemies/Guardian/_Unique/BossFodder/Design/Character/BPChar_GuardianSpectreBossFodder
I /Game/Enemies/Guardian/_Unique/BossFodder/Design/Character/BPChar_GuardianWraithBossFodder
E /Game/Enemies/Guardian/_Unique/EdenVault02/_Design/Character/BPChar_Guardian_EdenVault02
E /Game/Enemies/Guardian/_Unique/GemGoblin/_Design/Character/BPChar_GuardianGemGoblin
I /Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss
E /Game/Enemies/Guardian/_Unique/BeachVault/_Design/Character/BPChar_GuardianBeachVault
E /Game/Enemies/Guardian/_Unique/EdenVault01/_Design/Character/BPChar_Guardian_EdenVault01
E /Game/Enemies/Guardian/_Unique/CityVault/_Design/Character/BPChar_Guardian_CityVault
H /Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss
M /Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01
I /Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena
M /Game/Enemies/Goliath/_Unique/Rare02/_Design/Character/BPChar_Goliath_Rare02
M /Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03
M /Game/Enemies/Goliath/_Unique/Bounty01/_Design/Character/BPChar_Goliath_Bounty01
I /Game/Enemies/Goliath/_Unique/PlayerFriendly/_Design/Character/BPChar_Goliath_Badass_Friendly
I /Game/Enemies/Tink_SentryRocketPod/_Unique/GrowingPains/_Design/Character/BPChar_Tink_SentryRocketPodGrowingPains
I /Game/Enemies/Tink_SentryRocketPod/_Unique/Blockade/_Design/Character/BPChar_Tink_SentryRocketPodBlockade
I /Game/Enemies/Tink_SentryRocketPod/_Unique/BigD/_Design/Character/BPChar_Tink_SentryRocketPodBigD
E /Game/Enemies/Saurian/_Unique/Laser/_Design/Character/BPChar_SaurianLaser
I /Game/Enemies/Saurian/_Unique/Hunt01/_Design/Character/BPChar_Saurian_Hunt01
I /Game/Enemies/Saurian/_Unique/SlaughterBoss/_Design/Character/BPChar_Saurian_SlaughterBoss
I /Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01
I /Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Character/BPChar_Saurian_TrialBoss
M /Game/Enemies/Saurian/_Unique/Shield/_Design/Character/BPChar_SaurianShield
I /Game/Enemies/Saurian/_Unique/Queen/_Design/Character/BPChar_SaurianQueen
I /Game/Enemies/Saurian/_Unique/Grog_Poison_Fodder/Character/BPChar_Saurian_Grog_Poison_Fodder
I /Game/Enemies/Tink/_Unique/RedJabber/_Design/Character/BPChar_TinkRedJabber
I /Game/Enemies/Tink/_Unique/GameshowEnforcer/_Design/Character/BPChar_TinkGameshowEnforcer
I /Game/Enemies/Tink/_Unique/Stagehand/_Design/Character/BPChar_TinkStagehand
E /Game/Enemies/Tink/_Unique/BlueBasic/_Design/Character/BPChar_TinkBlueBasic
I /Game/Enemies/Tink/_Unique/BossFodder/_Design/Character/BPChar_TinkBossFodder
E /Game/Enemies/Tink/_Unique/Rare01/_Design/Character/BPChar_Tink_Rare01
E /Game/Enemies/Tink/_Unique/Rare02/_Design/Character/BPChar_TinkRare02
E /Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon
I /Game/Enemies/Tink/_Unique/VarkidHunt01/BPChar_VarkidHunt01_Tink
I /Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss
M /Game/Enemies/Tink/_Unique/Archimedes/_Design/Character/BPChar_TinkArchimedes
E /Game/Enemies/Tink/_Unique/Bounty01/_Design/Character/BPChar_Tink_Bounty01
E /Game/Enemies/Tink/_Unique/WardenGuard/_Design/Character/BPChar_TinkPsychoWardenGuard
I /Game/Enemies/Tink/_Unique/Pain/_Design/Character/BPChar_Pain
E /Game/Enemies/Tink/_Unique/Interrogator/_Design/Character/BPChar_TinkInterrogator
E /Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker
E /Game/Enemies/Tink/_Unique/MotorcadeBigD/_Design/Character/BPChar_TinkMotorcadeBigD
E /Game/Enemies/Tink/_Unique/BrewKid/_Design/Character/BPChar_TinkBrewKid
E /Game/Enemies/Trooper/_Unique/Rare01b/_Design/Character/BPChar_Trooper_Rare01b
E /Game/Enemies/Trooper/_Unique/Bounty02/Design/Character/BPChar_TrooperBounty02
E /Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01
I /Game/Enemies/Trooper/_Unique/ChumpMelee/_Design/Character/BPChar_TrooperChumpMeleeDark
I /Game/Enemies/Trooper/_Unique/ChumpMelee/_Design/Character/BPChar_TrooperChumpMelee
E /Game/Enemies/Trooper/_Unique/Rare01c/_Design/Character/BPChar_Trooper_Rare01c
E /Game/Enemies/Trooper/_Unique/Rare01e/_Design/Character/BPChar_Trooper_Rare01e
I /Game/Enemies/Trooper/_Unique/ChumpBasic/_Design/Character/BPChar_TrooperChumpBasicDark
I /Game/Enemies/Trooper/_Unique/ChumpBasic/_Design/Character/BPChar_TrooperChumpBasic
E /Game/Enemies/Trooper/_Unique/JavaFlasher/_Design/Character/BPChar_TrooperJavaFlasher
E /Game/Enemies/Trooper/_Unique/Rare01d/_Design/Character/BPChar_Trooper_Rare01d
E /Game/Enemies/Trooper/_Unique/Rare01a/_Design/Character/BPChar_Trooper_Rare01a
E /Game/Enemies/Trooper/_Unique/Bounty03/Design/Character/BPChar_TrooperBounty03
I /Game/Enemies/Mech/_Unique/EvilAI/_Design/Character/BPChar_MechEvilAI
I /Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss
M /Game/Enemies/Mech/_Unique/GenMini/_Design/Character/BPChar_MechGenMini
I /Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech2
I /Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/Character/BPChar_GiganticMech1
I /Game/Enemies/Mech/_Unique/TechSlaughterBoss/_Design/BallGun/Character/BPChar_BallGun
I /Game/Enemies/Nekrobug/_Unique/Fodder/_Design/Character/BPChar_Nekrobug_Flyer_Fodder
E /Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01
I /Game/Enemies/Nekrobug/_Unique/HopperSwarm/_Design/Character/BPChar_Nekrobug_HopperSwarm
I /Game/Enemies/Nekrobug/_Unique/BetterTimes/_Design/Character/BPChar_Nekrobug_BetterTimes
M /Game/Enemies/Nekrobug/_Unique/BadVibes/_Design/Character/BPChar_Nekrobug_BadVibes
H /Game/Enemies/Spiderant/_Unique/Hunt01/_Design/Character/BPChar_Spiderant_Hunt01
I /Game/Enemies/Spiderant/_Unique/Tarantella/_Design/Character/BPChar_SpiderantTarantella
I /Game/Enemies/Spiderant/_Unique/CakeRoyalty/_Design/Character/BPChar_SpiderantCakeRoyalty
I /Game/Enemies/Rakk/_Unique/Hunt01/_Design/Character/BPChar_Rakk_Hunt01
I /Game/Enemies/Rakk/_Unique/HuntSkrakk/_Design/Character/BPChar_Rakk_HuntSkrakk
I /Game/Enemies/Rakk/_Unique/Dragon/_Design/Character/BPChar_Rakk_Dragon
I /Game/Enemies/Rakk/_Unique/DragonCryo/_Design/Character/BPChar_Rakk_DragonCryo
I /Game/Enemies/Psycho_Male/_Unique/InfectedOnes/_Design/Character/BPChar_PsychoInfectedOnes
M /Game/Enemies/Psycho_Male/_Unique/Rare02/_Design/Character/BPChar_PsychoRare02
M /Game/Enemies/Psycho_Male/_Unique/Prologue/_Design/Character/BPChar_PsychoPrologue
M /Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03
M /Game/Enemies/Psycho_Male/_Unique/OilSheriff/_Design/Character/BPChar_PsychoOilSheriff
M /Game/Enemies/Psycho_Male/_Unique/WardenGuard/_Design/Character/BPChar_PsychoWardenGuard
M /Game/Enemies/Psycho_Male/_Unique/Rakkman/_Design/Character/BPChar_Rakkman
M /Game/Enemies/Psycho_Male/_Unique/BadassPrologue/_Design/Character/BPChar_PsychoBadassPrologue
M /Game/Enemies/Psycho_Male/_Unique/AnointedX4/Character/BPChar_PsychoAnointedX4
M /Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch
M /Game/Enemies/Psycho_Male/_Unique/Bloodshine/_Design/Character/BPChar_PsychoBloodshine
M /Game/Enemies/Skag/_Unique/AntEaterPup/_Design/Character/BPChar_SkagAntEatherPup
M /Game/Enemies/Skag/_Unique/AntEater/_Design/Character/BPChar_SkagAntEater
M /Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01
M /Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch
I /Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss
M /Game/Enemies/Skag/_Unique/Succulent/_Design/Character/BPChar_SkagSucculent
M /Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch
M /Game/Enemies/Skag/_Unique/SucculentAlpha/_Design/Character/BPChar_SkagSucculentAlpha
I /Game/Enemies/Ratch/_Unique/EridiumBasic/_Design/Character/BPChar_RatchEridiumBasic
E /Game/Enemies/Ratch/_Unique/Hunt01/_Design/Character/BPChar_Ratch_Hunt01
I /Game/Enemies/Ratch/_Unique/NoFeastBasic/_Design/Character/BPChar_RatchNoFeastBasic
I /Game/Enemies/Ratch/_Unique/Larva/_Design/Character/BPChar_RatchLarva
E /Game/Enemies/Ratch/_Unique/BadRat/_Design/Character/BPChar_RatchBadRat
I /Game/Enemies/Ratch/_Unique/NoFeastPup/_Design/Character/BPChar_RatchNoFeastPup
I /Game/Enemies/Ratch/_Unique/Gnat/_Design/Character/BPChar_RatchGnat
I /Game/Enemies/Ratch/_Unique/HiveAnchor/_Design/Character/BPChar_RatchHiveAnchor
I /Game/Enemies/Ratch/_Unique/SpaceSlug/_Design/Character/BPChar_RatchSpaceSlug
M /Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans
M /Game/Enemies/Nog/_Unique/HackedGamer/_Design/Character/BPChar_NogHackedGamer
M /Game/Enemies/Nog/_Unique/Nog01_Bounty/_Design/Character/BPChar_Nog01_Bounty
M /Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder
M /Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_TrooperBasic_GigamindAdds
E /Game/Enemies/ServiceBot/_Unique/JanitorBot/_Design/Character/BPChar_ServiceBot_JanitorBot
I /Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01
I /Game/Enemies/ServiceBot/_Unique/Abomination/_Design/Character/BPChar_ServiceBot_Abomination
E /Game/Enemies/ServiceBot/_Unique/Maliwan/_Design/Character/BPChar_ServiceBot_Maliwan
I /Game/Enemies/ServiceBot/_Unique/PattyWorker/_Design/Character/BPChar_ServiceBot_PattyWorker
I /Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01_Larva
I /Game/Enemies/Varkid/_Unique/Hunt01/_Design/Character/BPChar_VarkidHunt01
I /Game/Enemies/Varkid/_Unique/BossFodder/_Design/Character/BPChar_VarkidBossFodder
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaA
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaC
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaD
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaB
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Badass/BPChar_VarkidHunt02_Badass
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Adult/BPChar_VarkidHunt02_AdultA
I /Game/Enemies/Varkid/_Unique/Hunt02/_Design/Adult/BPChar_VarkidHunt02_AdultB
M /Game/Enemies/Punk_Female/_Unique/MotherOfDragons/_Design/Character/BPChar_PunkMotherOfDragons
M /Game/Enemies/Punk_Female/_Unique/BlueBasic/_Design/Character/BPChar_PunkBlueBasic
M /Game/Enemies/Punk_Female/_Unique/Prologue/_Design/Character/BPChar_PunkPrologue
M /Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/BPChar_PunkBounty02
M /Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/b/BPChar_Punk_Bounty01b
M /Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/c/BPChar_Punk_Bounty01c
M /Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/d/BPChar_Punk_Bounty01d
M /Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/a/BPChar_Punk_Bounty01a
M /Game/Enemies/Punk_Female/_Unique/WardenGuard/_Design/Character/BPChar_PunkBasic_WardenGuard
I /Game/Enemies/Punk_Female/_Unique/RedAssaulter/_Design/Character/BPChar_PunkRedAssaulter
I /Game/Enemies/Punk_Female/_Unique/GameshowTwo/_Design/Character/BPChar_PunkGameshowTwo
H /Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX3
H /Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX2
I /Game/Enemies/Punk_Female/_Unique/RedShotgunner/_Design/Character/BPChar_PunkRedShotgunner
I /Game/Enemies/Punk_Female/_Unique/SecretAgent/_Design/Character/BPChar_PunkSecretAgent
M /Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag
I /Game/Enemies/Punk_Female/_Unique/GameshowFour/_Design/_Character/BPChar_PunkGameshowFour
M /Game/Enemies/Punk_Female/_Unique/TumorHead/_Design/Character/BPChar_PunkBadass_Tumorhead
I /Game/Enemies/Punk_Female/_Unique/GameshowOne/_Design/Character/BPChar_PunkGameshowOne
M /Game/Enemies/Punk_Female/_Unique/MovieGoer/_Design/Character/BPChar_PunkMovieGoer
M /Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady
I /Game/Enemies/Oversphere/_Unique/Rare01/_Design/Character/BPChar_OversphereRare01
I /Game/Enemies/Oversphere/_Unique/OversphereVR/_Design/Character/BPChar_OversphereVR
I /Game/Enemies/Oversphere/_Unique/OversphereVRBig/Character/BPChar_OversphereVRBig
I /Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere
I /Game/Enemies/Oversphere/_Unique/Jackie/_Design/Character/BPChar_OversphereJackie
M /Game/Enemies/Heavy/_Unique/DinerBoss/_Design/Character/BPChar_HeavyDinerBoss
M /Game/Enemies/Heavy/_Unique/JavaCore/_Design/Character/BPChar_HeavyJavaCore
I /Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt
M /Game/Enemies/Heavy/_Unique/Bounty01/_Design/Character/BPChar_Heavy_Bounty01
M /Game/Enemies/Heavy/_Unique/FootstepsOfGiants/_Design/Character/BPChar_HeavyFootstepsOfGiants
I /Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt
I /Game/Enemies/Enforcer/_Unique/FilmBuff/_Design/Character/BPChar_KillaVoltNPC
M /Game/Enemies/Enforcer/_Unique/BlueBasic/_Design/Character/BPChar_EnforcerBlueBasic
M /Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt
M /Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist
I /Game/Enemies/Enforcer/_Unique/Terror/_Design/Character/BPChar_Terror
M /Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey
M /Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue
M /Game/Enemies/Enforcer/_Unique/Bounty02/_Design/Character/BPChar_Enforcer_Bounty02
M /Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01
M /Game/Enemies/Enforcer/_Unique/WardenGuard/_Design/Character/BPChar_EnforcerMeleeWardenGuard
I /Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss
M /Game/Enemies/Enforcer/_Unique/RedMelee/_Design/Character/BPChar_EnforcerRedMelee
M /Game/Enemies/Enforcer/_Unique/Dentist/_Design/Character/BPChar_EnforcerDentist
M /Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoe
M /Game/Enemies/Enforcer/_Unique/AnointedJoe/_Design/Character/BPChar_AnointedJoeClone
I /Game/Enemies/Ape/_Unique/KingBobo/_Design/Character/BPChar_ApeKingBobo
M /Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/BPChar_Ape_Hunt01
M /Game/Enemies/Ape/_Unique/Squire/_Design/Character/BPChar_ApeSquire
I /Game/Enemies/Ape/_Unique/EdenBossFodder/_Design/Character/BPChar_ApeEdenBossFodder
H /Game/Enemies/Ape/_Unique/KGuard/_Design/Character/BPChar_ApeKGuard
M /Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/BPChar_ApeJungleMonarch
I /Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossA/_Design/Character/BPChar_MechRaidBossA
I /Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossBar/_Design/Character/BPChar_MechRaidBossBar
I /Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC
I /Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossMini/_Design/Character/BPChar_RaidBossMini
I /Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossB/_Design/Character/BPChar_MechRaidBossB
I /Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/UpperHalf/Character/BPChar_UpperHalf
I /Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/BrainBeams/Character/BPChar_BrainBeam
I /Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/SpiderBrain/Character/BPChar_SpiderBrain
I /Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/_Design/Character/BPChar_BehemothRaid
I /Game/PatchDLC/Raid1/Enemies/Oversphere/_Unique/BadassHarbinger/_Design/Character/BPChar_BadassHarbinger
I /Game/PatchDLC/Raid1/Enemies/Oversphere/_Unique/RaidBoss/_Design/Character/BPChar_Oversphere_RaidBoss
I /Game/PatchDLC/BloodyHarvest/Enemies/Trooper/_Unique/ChumpMelee/_Design/Character/BPChar_TrooperChumpMelee_BloodyHarvest
I /Game/PatchDLC/BloodyHarvest/Enemies/Trooper/_Unique/Gatekeeper/_Design/Character/BPChar_Trooper_BloodyHarvest_Gatekeeper
I /Game/PatchDLC/BloodyHarvest/Enemies/Trooper/_Unique/ChumpBasic/_Design/Character/BPChar_TrooperChumpBasic_BloodyHarvest
I /Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/Bloody/_Design/Character/BPChar_RatchBloody
I /Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyGatekeeper/_Design/Character/BPChar_RatchBloodyBadassGatekeeper
I /Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyHive/_Design/Character/BPChar_RatchBloodyHive
I /Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyBirther/_Design/Character/BPChar_RatchBloodyBirther
I /Game/PatchDLC/BloodyHarvest/Enemies/Ratch/_Unique/BloodyBadass/_Design/Character/BPChar_RatchBloodyBadass
I /Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss
I /Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/HarvestBoss/_Design/Character/BPChar_HarvestBoss_Uber
I /Game/PatchDLC/BloodyHarvest/Enemies/Heavy/_Unique/Gatekeeper/_Design/Character/BPChar_Heavy_BloodyHarvest_Gatekeeper
E /Geranium/Enemies/GerSaurian/_Unique/Horsemen2/_Design/Character/BPChar_GerSaurianHorsemen2
I /Geranium/Enemies/GerSaurian/_Unique/Horsemen2/_Design/Rider/BPChar_GerEnforcerHorsemen2
E /Geranium/Enemies/GerSaurian/_Unique/WW_Toge/_Design/Character/BPChar_GerSaurianWW_Toge
E /Geranium/Enemies/GerSaurian/_Unique/Dispatcher/_Design/Character/BPChar_GerSaurianDispatcher
E /Geranium/Enemies/GerSaurian/_Unique/Horsemen3/_Design/Character/BPChar_GerSaurianHorsemen3
I /Geranium/Enemies/GerSaurian/_Unique/Horsemen3/_Design/Rider/BPChar_GerPunkHorsemen3
E /Geranium/Enemies/GerSaurian/_Unique/SV_Predator/_Design/Character/BPChar_SaurianSV_Predator
I /Geranium/Enemies/GerSaurian/_Unique/Grogzilla/_Design/Character/BPChar_GerSaurianGrogzilla
I /Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Pygmimus
M /Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_HamBadass
I /Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Tyrant
M /Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_GrogPoison
M /Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Grog
M /Geranium/Enemies/GerSaurian/_Unique/Horsemen1/_Design/Character/BPChar_GerSaurianHorsemen1
I /Geranium/Enemies/GerSaurian/_Unique/Horsemen1/_Design/Rider/BPChar_GerTinkHorsemen1
H /Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur
I /Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur_Punk
M /Geranium/Enemies/GerSaurian/_Unique/SV_PGrog/_Design/Character/BPChar_SaurianSV_PGrog
M /Geranium/Enemies/GerSaurian/_Unique/LBN_GunPred/_Design/Character/BPChar_GerSaurianLBN_GunPred
I /Geranium/Enemies/GerSaurian/_Unique/SV_Daisy/_Design/Character/BPChar_GerSaurianSV_Daisy
M /Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Character/BPChar_GerSaurianHorsemen4
I /Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Rider/BPChar_GerPunkHorsemen4
M /Geranium/Enemies/GerSaurian/_Unique/LBN_GunGrog/_Design/Character/BPChar_GerSaurianLBN_GunGrog
I /Geranium/Enemies/Gyro/_Unique/Painless/_Design/Character/BPChar_GyroPainless
M /Geranium/Enemies/GerPsycho_Male/_Unique/PhaserPete/_Design/Character/BPChar_GerPsychoPhaserPete
M /Geranium/Enemies/GerPsycho_Male/_Unique/DD_Steve/_Design/Character/BPChar_GerPsychoDD_Steve
M /Geranium/Enemies/GerPsycho_Male/_Unique/MoleMan/_Design/Character/BPChar_GerPsychoMoleMan
M /Geranium/Enemies/GerEnforcer/_Unique/Yarp/_Design/Character/BPChar_GerEnforcerYarp
M /Geranium/Enemies/GerEnforcer/_Unique/LBN_Doctor/_Design/Character/BPChar_GerEnforcerLBN_Doctor_NoShield
M /Geranium/Enemies/GerEnforcer/_Unique/LBN_Doctor/_Design/Character/BPChar_GerEnforcerLBN_Doctor
M /Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher
I /Geranium/Enemies/GerRakk/_Unique/BB_Assblaster/_Design/Character/BPChar_GerRakkBB_Assblaster
I /Geranium/Enemies/GerRakk/_Unique/Mother/_Design/Character/BPChar_GerRakkMother_Baby
I /Geranium/Enemies/GerRakk/_Unique/Mother/_Design/Character/BPChar_GerRakkMother
I /Geranium/Enemies/GerRakk/_Unique/Rod/_Design/Character/BPChar_GerRakkRod
I /Geranium/Enemies/GerRakk/_Unique/LM_Spirit/_Design/Character/BPChar_GerRakkLM_Spirit
I /Geranium/Enemies/GerRakk/_Unique/Lasodactyl/_Design/Character/BPChar_GerRakkLasodactyl
M /Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/BPChar_GerPunkLarry
M /Geranium/Enemies/GerPunk_Female/_Unique/GS_Leader/_Design/Character/BPChar_GerPunkGS_Leader
M /Geranium/Enemies/GerPunk_Female/_Unique/SOS_Doc/_Design/Character/BPChar_GerPunkSOS_Doc
M /Geranium/Enemies/GerPunk_Female/_Unique/LBN_Bandit/_Design/Character/BPChar_GerPunkLBN_Bandit
M /Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/BPChar_GerPunkNumber
M /Geranium/Enemies/GerPunk_Female/_Unique/LBN_Keem/_Design/Character/BPChar_GerPunkLBN_Keem
I /Geranium/Enemies/GerPunk_Female/_Unique/JL_Half/_Design/Character/BPChar_GerPunkJL_Half
I /Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/BPChar_GerPunkGreg
I /Geranium/Enemies/GerPunk_Female/_Unique/Greg/_Design/Character/BPChar_GerPunkGreg_Rakk
M /Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/BPChar_Biobeast_PlasmaBeast
M /Geranium/Enemies/Biobeast/_Unique/Biobetsy/_Design/Character/BPChar_Biobeast_Biobetsy
I /Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast
I /Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast_Copy
M /Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast
M /Geranium/Enemies/Biobeast/_Unique/BigJohn/_Design/Character/BPChar_Biobeast_BigJohn
M /Geranium/Enemies/GerTink/_Unique/Prohibitor/_Design/Character/BPChar_GerTinkProhibitor
I /Hibiscus/Enemies/_Unique/Mission_Other/NekroBug_Spirit/Character/BPChar_Hib_Nekro_Spirit_Invisible
I /Hibiscus/Enemies/_Unique/Mission_Other/NekroBug_Spirit/Character/BPChar_Hib_Nekro_Spirit
I /Hibiscus/Enemies/_Unique/Mission_Other/NekroBug_Spirit/Character/BPChar_Hib_Nekro_SpiritBadass
M /Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child
H /Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child
I /Hibiscus/Enemies/_Unique/Mission/SM_WhereIBelong/BPChar_SlugCarrier_WhereIBelong
I /Hibiscus/Enemies/_Unique/Mission/EP1_SlugMama/BPChar_SlugCarrier_Child_Mama
I /Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_PilferEyeBasic_Child_Rare
M /Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare
M /Hibiscus/Enemies/_Unique/Hunt_Kratch/Character/BPChar_SlugBadass_Kratch
M /Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti_Adds_ApeCryo
M /Hibiscus/Enemies/_Unique/Hunt_Yeti/Character/BPChar_Yeti
M /Hibiscus/Enemies/_Unique/Rare_Shocker/Character/BPChar_ZealotNightmareShocker_Rare
I /Hibiscus/Enemies/_Unique/Hunt_Kritchy/Character/BPChar_Hib_Hunt_Kritchy
I /Hibiscus/Enemies/_Unique/Hunt_Hampton/Character/BPChar_Hib_Hunt_Hampton
I /Hibiscus/Enemies/_Unique/Rare_Frost_Dragon/Character/BPChar_Rare_Frost_Dragon
M /Hibiscus/Enemies/FrostBiters/_Unique/_Design/Character/BPChar_Spinsmouth
I /Hibiscus/Enemies/FlyingSlug/Badass/_Design/Character/BPChar_FlyingSlugLakeUnique
M /Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden
I /Alisma/Enemies/HyperionPunk/_Unique/HagMother/BPChar_HagMother
I /Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss
I /Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant
I /Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief
M /Alisma/Enemies/AliPsycho/_Unique/TheBlackKing/_Design/Character/BPChar_AliPsycho_TheBlackKing
I /Alisma/Enemies/HibPsycho/_Unique/TheCellNeighbor/_Design/Character/BPChar_HibPsycho_TheCellNeighbor
I /Alisma/Enemies/Loader/_Unique/BigChestDaddy/_Design/Character/BPChar_Loader_BigChestDaddy
I /Alisma/Enemies/Loader/_Unique/ISeeYou/_Design/Character/BPChar_Loader_ISeeYou
I /Alisma/Enemies/Loader/_Unique/TouchySandy/_Design/Character/BPChar_Loader_TouchySandy
I /Alisma/Enemies/Loader/_Unique/LeggyLarry/_Design/Character/BPChar_Loader_LeggyLarry
M /Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss
M /Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook
H /Alisma/Enemies/AliGoliath/_Unique/TheBlackKing/_Design/Character/BPChar_AliGoliath_TheBlackKing
I /Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP
M /Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_PsychoShark
M /Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina
I /Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_GorgeousRoger
E /Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_BomberGary
E /Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_MachineGunMikey
I /Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan
M /Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part3/_Design/Character/BPChar_DoItForDigby_SteelDragon
M /Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part2/Character/BPChar_DoItForDigby_BloodBucket
M /Dandelion/Enemies/Looters/_Unique/MeetTimothy/_Design/Character/BPChar_MeetTimothy_ThirdRail
M /Dandelion/Enemies/Looters/_Unique/GreatEscape/_Design/Character/BPChar_GreatEscape_Rudy
E /Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio
E /Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence
I /Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco
E /Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_PunkBadass_Gaudy
M /Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion
I /Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket
I /Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks
I /Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick
M /Dandelion/Enemies/Looters/_Unique/OneMansTrash/_Design/Character/BPChar_OneMansTrash_TonyBordel
M /Dandelion/Enemies/ServiceBot/Unique_Janitor/_Design/Character/BPChar_CasinoBot_BigJanitor
H /Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion
H /Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia
M /Dandelion/Enemies/Loader/_Unique/AcidTrip/EarlyPrototypes/_Design/Character/BPChar_AcidTrip_EarlyPrototype
M /Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt
M /Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader
M /Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader"""

cartels = """I /Game/PatchDLC/Event2/Enemies/Tiny/Psycho/Badass/_Design/Character/BPChar_PsychoBadassTinyEvent2
M /Game/PatchDLC/Event2/Enemies/Cyber/Trooper/Capo/_Design/Character/BPChar_CyberTrooperCapo
M /Game/PatchDLC/Event2/Enemies/Cyber/Punk/TechLt/_Design/Character/BPChar_PunkCyberLt
M /Game/PatchDLC/Event2/Enemies/Meat/Punk/RoasterLT/_Design/Character/BPChar_Punk_Roaster
M /Game/PatchDLC/Event2/Enemies/Meat/Tink/TenderizerLt/_Design/Character/BPChar_Tink_Tenderizer
H /Game/PatchDLC/Event2/Enemies/Tiny/Trooper/Badass/_Design/Character/BPChar_TrooperBadassTinyEvent2
E /Game/PatchDLC/Event2/Enemies/Cyber/ServiceBots/Law/BPChar_ServiceBot_LAWEvent2
E /Game/PatchDLC/Event2/Enemies/Cyber/ServiceBots/Officer/BPChar_ServiceBot_Officer"""

maliwanmechs = """M /Game/Enemies/Mech/Basic/_Design/Character/UIName_MechBasicDark_PT2
M /Game/Enemies/Mech/Basic/_Design/Character/BPChar_MechBasicDark
E /Game/PatchDLC/Raid1/Enemies/Mech/BasicMini/_Design/Character/BPChar_MechBasicMini
M /Game/Enemies/Mech/Charger/_Design/Character/BPChar_MechCharger
H /Game/Enemies/Mech/Grenadier/_Design/Character/BPChar_MechGrenadier
M /Game/Enemies/Mech/MG/_Design/Character/BPChar_MechMG
H /Game/PatchDLC/Event2/Enemies/Cyber/Behemoth/Gunner/_Design/Character/BPChar_BehemothGunnerEvent2
H /Game/PatchDLC/Raid1/Enemies/Behemoth/Gunner/_Design/Character/BPChar_BehemothGunner
H /Game/PatchDLC/Event2/Enemies/Cyber/Behemoth/Mini/_Design/Character/BPChar_BehemothMiniWalker_Event2
M /Game/PatchDLC/Raid1/Enemies/Behemoth/Carrier/_Design/Character/BPChar_BehemothCarrier
E /Game/PatchDLC/Raid1/Enemies/Behemoth/MiniWalker/_Design/Character/BPChar_BehemothMiniWalker
M /Game/PatchDLC/Raid1/Enemies/Behemoth/Rocketeer/_Design/Character/BPChar_BehemothRocketeer
M /Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Character/BPChar_Behemoth"""

bpchars_text_tuple = bpchars_text_tuple + "\n" + cartels
#+ maliwanmechs

#bpchars_text_tuple = maliwanmechs
override = False

def tuple_line_to_bpchar(l):
    difficulty,bpchar = l.split(" ")
    return (bpchar,bpchar,None,None)

bt=bpchars_text_tuple.split("\n")

def bosses_of_type(bt,btype="E"):
    return [tuple_line_to_bpchar(x) for x in bt if x[0] == btype]

if override:
    easy_bosses   = bosses_of_type(bt,"E")
    medium_bosses = bosses_of_type(bt,"M")
    hard_bosses   = bosses_of_type(bt,"H")
else:
    easy_bosses   = easy_bosses   + bosses_of_type(bt,"E")
    medium_bosses = medium_bosses + bosses_of_type(bt,"M")
    hard_bosses   = hard_bosses   + bosses_of_type(bt,"H")
