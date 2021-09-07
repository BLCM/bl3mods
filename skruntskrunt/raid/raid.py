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
ITEM_POOL_INDEX='item_pool_index'
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
        # this is for Alisma and locomobius
        item_pool_index = boss.get(ITEM_POOL_INDEX,0)
        if item_pool_index != 0:
            out.append(f"# item_pool_index: {item_pool_index}")
        out.append(f"SparkCharacterLoadedEntry,(1,1,0,{boss['bpchar']}),{boss['bpchar_path']}.{boss['bpchar']}_C:AIBalanceState_GEN_VARIABLE,DropOnDeathItemPools.ItemPools[{item_pool_index}].PoolProbability,0,,(BaseValueConstant=1,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
        out.append(f"SparkCharacterLoadedEntry,(1,1,0,{boss['bpchar']}),{boss['bpchar_path']}.{boss['bpchar']}_C:AIBalanceState_GEN_VARIABLE,DropOnDeathItemPools.ItemPools[{item_pool_index}].NumberOfTimesToSelectFromThisPool,0,,(BaseValueConstant={boss['nloot']},DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)")
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
        ITEM_POOL_INDEX:options.get(ITEM_POOL_INDEX,0),
    }

# name, BP Path, Balance Table, Row Key in Balance Table
more_bosses = [
    ('Tyreen',
     '/Game/Enemies/FinalBoss/_Shared/_Design/Character/BPChar_FinalBoss',
     '/Game/Enemies/FinalBoss/_Shared/_Design/Balance/Table_Balance_FinalBoss_PT1',
     'FinalBoss'),
    ('Troy',
     '/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/BPChar_TroyBoss',
     '/Game/NonPlayerCharacters/Troy/_Design/Balance/Table_Balance_TroyBoss_PT1',
     'TroyBoss'),
    ('Rampager','/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager',
     '/Game/Enemies/PrometheaBoss/_Shared/_Design/Balance/Table_Balance_PromBoss_PT1',
     'Rampager',
     {
         'nloot':DEFAULT_NLOOT,
         'health':[2*DEFAULT_HEALTH,2*DEFAULT_HEALTH],
         'damage':DEFAULT_DAMAGE
     }
    ),
    ('Ruiner', '/Geranium/Enemies/Ruiner/Boss/_Design/Character/BPChar_RuinerBoss', '/Geranium/Enemies/Ruiner/_Shared/_Design/Balance/Table_Ruiner_Balance', 'Ruiner_Boss_PT2',{"health":[DEFAULT_HEALTH*3 for health in HEALTHS],"damage":50,"nloot":20}),
    ('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur'),
    ('Dumptruck',
     '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_BountyPrologue',
     {"raid1":43},
    ),
    ('MouthPiece',
     '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_Mouthpiece'),
    ('HotKarl',
     '/Game/Enemies/Enforcer/_Unique/Bounty01/_Design/Character/BPChar_Enforcer_Bounty01',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_Bounty01_HotKarl'),
    ('Shiv',
     '/Game/Enemies/Psycho_Male/_Unique/BadassPrologue/_Design/Character/BPChar_PsychoBadassPrologue',
     "/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance",
     "Psycho_Badass"),
    ('RoadDog','/Game/Enemies/Goliath/_Unique/Rare02/_Design/Character/BPChar_Goliath_Rare02','/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique','Rare02'),
    ('Princess Tarantella II','/Game/Enemies/Spiderant/_Unique/Tarantella/_Design/Character/BPChar_SpiderantTarantella','/Game/Enemies/Spiderant/_Shared/_Design/Balance/Table_Balance_Spiderant_Unique','Spiderant_CakeRoyalty'),
    ('Waylon Hurd','/Geranium/Enemies/GerPsycho_Male/_Unique/MoleMan/_Design/Character/BPChar_GerPsychoMoleMan','/Geranium/Enemies/GerPsycho_Male/_Shared/_Design/Balance/Table_GerPsycho_Balance_Unique','GerPsycho_MoleMan'),
    ('Lasodactyl','/Geranium/Enemies/GerRakk/_Unique/Lasodactyl/_Design/Character/BPChar_GerRakkLasodactyl',"/Geranium/Enemies/GerRakk/_Shared/_Design/Balance/Table_GerRakk_Balance_Unique","GerRakkLasodactyl"),
    ('Lectrikor','/Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/BPChar_Biobeast_PlasmaBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","PlasmaBeast"),
    ('Hydragoian','/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast',"/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique","CopyBeast"),
    ('Bellik Primis','/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast','/Geranium/Enemies/Biobeast/_Shared/_Design/Balance/Table_Balance_Biobeast_Unique',"AlteredBeast"),
    ('Shiverous the Unscathed','/Hibiscus/Enemies/_Unique/Rare_Frost_Dragon/Character/BPChar_Rare_Frost_Dragon',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Frost_Dragon_Rare"),
    ('Empowered Scholar','/Hibiscus/Enemies/Minion/Possessed/_Design/Character/BPChar_MinionPossessed',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Boss_Minion"),
    ('Empowered Grawn','/Hibiscus/Enemies/Lunatic/Possessed/_Design/Character/BPChar_LunaticPossessed',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists",'Boss_Lunatic'),
    ('Amach','/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare',"/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists","Zealot_Pilfer_Rare"),
    ('Kritchy','/Hibiscus/Enemies/_Unique/Hunt_Kritchy/Character/BPChar_Hib_Hunt_Kritchy','/Hibiscus/Enemies/_Unique/Table_Balance_Hib_Unique','Hunt_Kritchy_Village'),
    ('Scraptrap Prime','/Game/PatchDLC/Dandelion/Enemies/Claptrap/Claptrap_Queen/_Design/Character/BPChar_ClaptrapQueen','/Game/PatchDLC/Dandelion/Enemies/Claptrap/_Shared/_Design/Balance/Table_Balance_Claptrap_PT1','Queen_PT2'), #Queen_PT2 or Queen
    ('Tyrant of Instinct','/Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Character/BPChar_Saurian_TrialBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_TrialBoss",
     {"raid1":60}),
    ('Tremendous Rex','/Game/Enemies/Saurian/_Unique/SlaughterBoss/_Design/Character/BPChar_Saurian_SlaughterBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian","Saurian_Tyrant"),
    ('Tink of Cunning','/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss",
     {"raid1":66}),
    ('Skag of Survival','/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss",
     {"raid1":62}),
    ('Sera of Supremacy','/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss",{"raid1":49}),
    ('Mr. Titan','/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique",'SlaughterBoss'),
    ('Hag of Fervor','/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial",{"raid1":48}),
    ('Arbalest of Discipline','/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique","Mech_TrialBoss",{"raid1":54}), # There was also Mech_Basic
    ('IndoTyrant','/Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Rare01",{"raid1":58}),
    ('Demoskaggon','/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique',"DemoSkag",
     {"health":[0.5*DEFAULT_HEALTH],"raid1":61}),
    ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"),
    ('Agonizer 9000','/Game/Enemies/Agonizer_9k/_Shared/Character/BPChar_Agonizer_9k',"/Game/Enemies/Agonizer_9k/_Shared/Balance/Table_Balance_Agonizer_9k","A9K"),
    ('Wick','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare03'),
    ('Borman Nates','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare02','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare02'),
    ('Warty','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare01','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare01',{"raid1":64}),
    ('OnePunch','/Game/Enemies/Psycho_Male/_Unique/OnePunch/Design/Character/BPChar_OnePunch','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','OnePunch'),
    # ('Tumorhead','/Game/Enemies/Punk_Female/_Unique/TumorHead/_Design/Character/BPChar_PunkBadass_Tumorhead',None,None), #punk_badass non-unique
    ('Judge Hightower','/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01','/Game/NonPlayerCharacters/_Shared/_Design/Table_Balance_NPC','AtlasSoldier_Bounty'),
    # This is buggy, you need to dupe Enforcer_Shield to another entry in that balance table
    # and then you need to set the row of BalanceTable to the Urist
    # if you figure out how to do this you can make tumorhead unique too...
    ('Urist McEnforcer','/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance','Enforcer_Shield'), # I hope this is safe
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'),
    # Katagawa Jr has holograms too, row KatagawaJR_Hologram
    ('Katagawa Jr.','/Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR','/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/Table_Balance_KatagawaJR_PT1','KatagawaJR_Boss'),
    # Make the holograms kinda wimpy
    ('Katagawa Jr (Hologram).','/Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR','/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/Table_Balance_KatagawaJR_PT1','KatagawaJR_Hologram',{'health':[DEFAULT_HEALTH/4]}),
    ('Kratch','/Hibiscus/Enemies/_Unique/Hunt_Kratch/Character/BPChar_SlugBadass_Kratch','/Hibiscus/Enemies/Slug/_Shared/_Design/Balance/Table_Balance_Slug_PT1','Slug_Badass_Hunt_Kratch',{"health":[DEFAULT_HEALTH/4,DEFAULT_HEALTH/4,DEFAULT_HEALTH/4,DEFAULT_HEALTH/4]}),
    ('Fungal Gorger','/Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child','/Hibiscus/Enemies/_Shared/_Design/Balance/Table_Balance_Cultists','LostOne_Badass'),
    ('AMBER LAMPS','/Game/Enemies/ServiceBot/LOOT/_Design/Character/BPChar_ServiceBot_LOOT','/Game/Enemies/ServiceBot/_Shared/_Design/Balance/Table_Balance_ServiceBot','ServiceBot_LOOT'),
    ('Captain Traunt','/Game/Enemies/Heavy/_Unique/Traunt/_Design/Character/BPChar_Heavy_Traunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":51}),
    # Is general traunt shared??
    ('General Traunt','/Game/Enemies/Heavy/_Unique/DarkTraunt/_Design/Character/BPChar_HeavyDarkTraunt','/Game/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_Heavy_Unique','Heavy_Traunt',{"raid1":52}),
    ('Gigamind','/Game/Enemies/Nog/_Unique/ChipHolder/_Design/Character/BPChar_NogChipHolder','/Game/Enemies/Nog/_Shared/_Design/Balance/Table_Balance_Nog_Unique','Nog_ChipHolder'),
    ('Undertaker','/Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker','/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique','Tink_BountyPrologue'),
    ('Trufflemunch','/Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Trufflemunch',{"health":[DEFAULT_HEALTH/2],"raid1":89}),
    ('Buttmunch','/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique','Buttmunch',{"health":[DEFAULT_HEALTH/2],"raid1":88}),
    ('Cybil Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaA','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Edie Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaB','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Martha Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaC','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Matty Crawly','/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaD','/Game/Enemies/Varkid/_Shared/_Design/Balance/Table_Varkid_Balance_Unique','Hunt02_Larva'),
    ('Chupacabratch','/Game/Enemies/Ratch/_Unique/Hunt01/_Design/Character/BPChar_Ratch_Hunt01','/Game/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_Ratch_Unique',"Ratch_01Hunt"),
    # this is probably a bad idea
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
    ('El Dragón Jr.','/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',
     '/Game/Enemies/Goliath/_Unique/Rare03/Character/BPChar_Goliath_Rare03',
     'Rare03'),
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'),
    ('Pyschobillies (d)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/d/BPChar_Punk_Bounty01d',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Pyschobillies (c)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/c/BPChar_Punk_Bounty01c',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Pyschobillies (b)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/b/BPChar_Punk_Bounty01b',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Pyschobillies (a)','/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/a/BPChar_Punk_Bounty01a',
     '/Game/Enemies/Punk_Female/_Shared/_Design/Balance/Table_Balance_Punk_Unique','Punk_Bounty02',JUST_QUARTER_HEALTH),
    ('Katagawa Ball','/Game/Enemies/Oversphere/_Unique/KatagawaSphere/_Design/Character/BPChar_Oversphere_KatagawaSphere',
     '/Game/Enemies/Oversphere/_Shared/_Design/Balance/Table_Balance_Oversphere_Unique','Oversphere_Katagawa'),
    ('The Unstoppable','/Game/Enemies/Goliath/_Unique/Rare01/Character/BPChar_Goliath_Rare01',
     '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique','Rare01'),
    # ('LocoMobius','/Alisma/Enemies/TrainBoss/_Shared/_Design/Character/BPChar_TrainBoss','/Alisma/Enemies/TrainBoss/_Shared/_Design/Balance/Table_Balance_TrainBoss_PT1','Basic',{"health":[DEFAULT_HEALTH for health in HEALTHS],"damage":10,"nloot":12,ITEM_POOL_INDEX:1}),
    ('LocoMobius','/Alisma/Enemies/TrainBoss/_Shared/_Design/Character/BPChar_TrainBoss','/Alisma/Enemies/TrainBoss/_Shared/_Design/Balance/Table_Balance_TrainBoss_PT1','Basic',{"health":[DEFAULT_HEALTH*4 for health in HEALTHS],"damage":10,"nloot":20,'item_pool_index':1}),
]

# manual header (open the static header file)
for line in open('raid.bl3hotfix.HEAD').readlines():
    print(line,end='')

bosses = [mk_boss(*x) for x in more_bosses]

for boss in bosses:
    print(buff_boss(boss))
    print("\n\n")
