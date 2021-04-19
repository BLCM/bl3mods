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
    ("Loader_Gun",'/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1","Loader_Gun"),
    ("DebtCollector",'/Dandelion/Enemies/Loader/_Unique/BrotherlyLove/_Design/Character/BPChar_SisterlyLove_DebtCollectorLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","DebtCollector"),
    # ("Harker",'/Ixora/Enemies/GearUpBoss/Mount/_Design/Character/BPChar_FrontRider_Mount',"/Ixora/Enemies/GearUpBoss/_Shared/Balance/Table_GearUpBoss_Balance","Rider_And_Mount"),
    ("Dr Benedict",'/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict',"/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1","Basic"),
    ("Enforcer_Reaper",'/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper',"/Ixora/Enemies/CotV/Enforcer/_Shared/_Design/Balance/Table_Balance_Enforcer_Ixora","Enforcer_Reaper"),
    ("GeneralBlisterPuss",'/Alisma/Enemies/AliEnforcer/_Unique/GeneralBlisterPuss/BPChar_GeneralBlisterPuss',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","GeneralBlisterPuss"),
    ("TheBlackRook",'/Alisma/Enemies/AliEnforcer/_Unique/TheBlackRook/BPChar_AliEnforcer_TheBlackRook',"/Alisma/Enemies/AliEnforcer/_Shared/_Design/Balance/Table_Balance_AliEnforcer_Unique","TheBlackRook"),
    ("APBulletRider",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"),
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
    ('Judge Hightower','/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01','/Game/NonPlayerCharacters/_Shared/_Design/Table_Balance_NPC','AtlasSoldier_Bounty'),
    ('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur'),
    ('Dumptruck',
     '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_BountyPrologue',
     {"raid1":43},
    ),
    ('Archer Rowe','/Game/Enemies/Heavy/_Unique/DinerBoss/_Design/Character/BPChar_HeavyDinerBoss',"/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique","DinerBoss"),
    ('Handsome Jackie','/Game/Enemies/Punk_Female/_Unique/Bounty02/_Design/Character/BPChar_PunkBounty02',None,None),
    ('Big Donny','/Game/Enemies/Tink/_Unique/MotorcadeBigD/_Design/Character/BPChar_TinkMotorcadeBigD',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_MotorcadeBigD"),
    ('Atomic','/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01',None,None),
    ('Baron Noggin','/Game/Enemies/Nog/_Unique/Nog01_Bounty/_Design/Character/BPChar_Nog01_Bounty',None,None), # E
    # ('Crushjaw','/Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01',None,None), # E
    # ('Sky Bully','/Game/Enemies/Tink/_Unique/Bounty01/_Design/Character/BPChar_Tink_Bounty01',None,None), # E
    # ('Warty','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare01','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare01',{"raid1":64}), # E
    ('Sheega','/Game/Enemies/Punk_Female/_Unique/SkagLady/_Design/Character/BPChar_PunkSkagLady',None,None), # E
    ('Rudy Varlope','/Dandelion/Enemies/Looters/_Unique/GreatEscape/_Design/Character/BPChar_GreatEscape_Rudy',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","RudyVarlope"), # E
    ('Coco Chantelle','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_GoonBadass_Coco',"/Dandelion/Enemies/Looters/Goon/_Shared/_Design/Balance/Table_Balance_GoonLooter","Goon_BadassLooter"), # E
    ('Golden Bullion','/Dandelion/Enemies/Looters/_Unique/RegainingOnesFeet/_Design/Character/BPChar_RegainingFeet_GoldenBullion',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","GoldenBullion"), # E
    ('Handsome Jacket','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeJacket',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"), # E
    ('Handsome Slacks','/Dandelion/Enemies/Looters/_Unique/ThePlan/JacksuitLooters/_Design/Character/BPChar_ThePlan_HandsomeSlacks',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"), # E
    ('TricksyNick','/Dandelion/Enemies/Looters/_Unique/ThePlan/_Design/Character/BPChar_ThePlan_TricksyNick',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TricksyNick"), # E
    ("Loader_Gun",'/Dandelion/Enemies/Loader/_Unique/Impound/_Design/Character/BPChar_BudLoader',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_PT1","Loader_Gun"), # E
    ("APBulletRider",'/Alisma/Enemies/BulletRider/_Unique/AP/_Design/Character/BPChar_BulletRider_AP',"/Alisma/Enemies/BulletRider/_Shared/_Design/Balance/Table_Balance_BulletRider_Unique","AP"), # E

]
medium_bosses = [
    ('Turnkey Tim','/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey',None,None),

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
    ('Trufflemunch','/Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Trufflemunch',{"health":[DEFAULT_HEALTH/2],"raid1":89}),
    ('Undertaker','/Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker','/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique','Tink_BountyPrologue'),
    ('Fungal Gorger','/Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child','/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists','LostOne_Badass'),
    ('OnePunch','/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','OnePunch'),
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
    ('Billy, the Anointed','/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBoss',None,None),
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
    ('Blinding Banshee','/Game/Enemies/Nekrobug/_Unique/Hunt01/_Design/Character/BPChar_Nekrobug_Hunt01',None,None), # M
    ('Azalea','/Game/Enemies/Punk_Female/_Unique/BrewHag/_Design/Character/BPChar_PunkBrewHag',None,None), # M
    ('Lagromar','/Game/Enemies/Tink/_Unique/Demon/_Design/Character/BPChar_TinkDemon',None,None), # M
    ('The Shark','/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_PsychoShark',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TheShark"), # M
    ('Domino','/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Character/BPChar_DoubleDown_DoubleDownDomina',"/Dandelion/Enemies/Looters/_Unique/DoubleDown/_Design/Balance/Table_Balance_DoubleDownDomino","Domino"), # M
    ('MachineGun Mikey','/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_MachineGunMikey',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath","Badass"), # M
    ('Yvan','/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Character/BPChar_RagingBot_Yvan',"/Dandelion/Enemies/Looters/_Unique/RagingBot/_Design/Balance/Table_Balance_RagingBot","Raging_Yvan"), # M
    ('Steel Dragon','/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part3/_Design/Character/BPChar_DoItForDigby_SteelDragon',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","SteelDragon"), # M
    ('BloodBucket','/Dandelion/Enemies/Looters/_Unique/DoItForDigby_Part2/Character/BPChar_DoItForDigby_BloodBucket',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","BloodBucket"), # M
    ('ThirdRail','/Dandelion/Enemies/Looters/_Unique/MeetTimothy/_Design/Character/BPChar_MeetTimothy_ThirdRail',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","ThirdRail"), # M
    ('Giorgio','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_TinkBadass_Giorgio',"/Dandelion/Enemies/Looters/Tink/_Shared/_Design/Balance/Table_Balance_TinkLooters","Tink_Badass"), # M
    ('Lawrence','/Dandelion/Enemies/Looters/_Unique/KillChallenges/BPChar_EnforcerBadass_Lawrence',"/Dandelion/Enemies/Looters/Enforcer/_Shared/_Design/Balance/Table_Enforcer_BalanceLooters","Enforcer_Badass"), # M
    ('TonyBordel LLC','/Dandelion/Enemies/Looters/_Unique/OneMansTrash/_Design/Character/BPChar_OneMansTrash_TonyBordel',"/Dandelion/Enemies/Looters/_Shared/Balance/Table_Looters_Balance_Unique","TonyBordel"), # M
    ('Casinobot Janitor','/Dandelion/Enemies/ServiceBot/Unique_Janitor/_Design/Character/BPChar_CasinoBot_BigJanitor',"/Game/PatchDLC/Dandelion/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_CasinoBot","CasinoBot_Janitor"), # M
    ("Dandellion",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Dandelion_FreddieBot/_Design/Character/BPChar_VIPOnly_Dandelion',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Dandellion"), # M
    ("Petunia",'/Dandelion/Enemies/Loader/_Unique/VIPOnly/Petunia_FreddieBot/_Design/Character/BPChar_VIPOnly_Petunia',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Petunia"), # M
    ("Facemelt",'/Dandelion/Enemies/Loader/_Unique/AcidTrip/Facemelt/_Design/Character/BPChar_AcidTrip_Facemelt',"/Game/PatchDLC/Dandelion/Enemies/Loader/_Shared/_Design/Balance/Table_Balance_Loader_Uniques","Facemelt"), # M
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
    ('Skag of Survival','/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss",
     {"raid1":62}),
    ('Sera of Supremacy','/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss",{"raid1":49}),
    ('Hag of Fervor','/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial",{"raid1":48}),    
    ('Wick','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare03'), # H
    ('Tink of Cunning','/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss", {"raid1":66}), # H
    ('Mr. Titan','/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique",'SlaughterBoss'), # H
    ('Caber Dowd','/Geranium/Enemies/GerPunk_Female/_Unique/Larry/_Design/Character/BPChar_GerPunkLarry',None,None), # H
    ('Maxitrillion','/Game/Enemies/ServiceBot/_Unique/Rare01/_Design/Character/BPChar_ServiceBot_Rare01',None,None), # H
    ('Tom','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_BigBro',None,None), # H
    ('Voltborn','/Hibiscus/Enemies/_Unique/Rare_Shocker/Character/BPChar_ZealotNightmareShocker_Rare',None,None), # H
    ('Xam','/Hibiscus/Enemies/LostOne/LostTwo/_Design/Character/BPChar_LostTwo_ToughBro',None,None), # H
    ('Lani Dixon','/Geranium/Enemies/GerPunk_Female/_Unique/Number/_Design/Character/BPChar_GerPunkNumber',None,None), # H
    ('Procurer','/Hibiscus/Enemies/Zealot/Badass/_Design/Character/BPChar_Zealot_Badass_Procurer',None,None), # H
    ('Ipswitch Dunne','/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher',None,None), # H
    ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"), # H
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'), # H
    ("Dr Benedict",'/Alisma/Enemies/DrBenedict/_Shared/_Design/Character/BPChar_DrBenedict',"/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1","Basic"), # H
    ("Enforcer_Reaper",'/Ixora/Enemies/CotV/Enforcer/Reaper/_Design/Character/BPChar_Enforcer_Reaper',"/Ixora/Enemies/CotV/Enforcer/_Shared/_Design/Balance/Table_Balance_Enforcer_Ixora","Enforcer_Reaper"), # H
    ("SpongeBoss",'/Alisma/Enemies/_Unique/SpongeBoss/_Design/Character/BPChar_SpongeBoss',"/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss","SpongeBoss"), # H
    ("Security Sergeant",'/Alisma/Enemies/Constructor/_Unique/SecuritySergeant/_Design/Character/BPChar_Constructor_SecuritySergeant',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"), # H
    ("Security Chief",'/Alisma/Enemies/Constructor/_Unique/SecurityChief/_Design/Character/BPChar_Constructor_SecurityChief',"/Game/PatchDLC/Dandelion/Enemies/Constructor/_Shared/_Design/Balance/Table_Balance_Constructor","Basic"), # H
    ("Hyperion Warden",'/Alisma/Enemies/HyperionPunk/_Unique/TheWarden/_Design/Character/BPChar_HyperionPunk_TheWarden',"/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk","Punk_Badass"), # H
    ("Scraptrap Queen",'/Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character/BPChar_ClaptrapQueen',"/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1","Queen"), # H
    ("Kormash",'/Geranium/Enemies/LodgeBoss/_Design/Character/BPChar_SploderBoss',"/Geranium/Enemies/GerEnforcer/_Shared/_Design/Balance/Table_GerEnforcer_Balance_Unique","GerEnforcer_SploderBoss"), # H
    ("Hildr",'/Game/PatchDLC/Raid1/Enemies/Mech/_Unique/RaidBossC/_Design/Character/BPChar_MechRaidBossC',"/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1","MechRaidBossC"), # H

]
