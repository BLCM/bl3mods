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

def buff_boss(boss): #bpchar, bpchar_path, balance_table, rowname, health,damage,nloot
    """ Generate hotfix code for buffing a boss """
    out = []
    out.append(f"##### {boss['name']} #####")
    out.append(f"# BPChar: {boss['bpchar']}")
    out.append(f"# bpchar_path: {boss['bpchar_path']}")
    out.append(f"# balance_table: {boss['balance_table']}")
    out.append(f"# balance rowname: {boss['rowname']}\n")
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
         'health':[4*DEFAULT_HEALTH,4*DEFAULT_HEALTH],
         'damage':DEFAULT_DAMAGE
     }
    ),
    ('Ruiner', '/Geranium/Enemies/Ruiner/Boss/_Design/Character/BPChar_RuinerBoss', '/Geranium/Enemies/Ruiner/_Shared/_Design/Balance/Table_Ruiner_Balance', 'Ruiner_Boss_PT2',{"health":[DEFAULT_HEALTH*3 for health in HEALTHS],"damage":50,"nloot":20}),
    ('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur'),
    ('Dumptruck',
     '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue',
     '/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique',
     'Enforcer_BountyPrologue'),
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
    ('Tyrant of Instinct','/Game/Enemies/Saurian/_Unique/TrialBoss/_Design/Character/BPChar_Saurian_TrialBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_TrialBoss"),
    ('Tremendous Rex','/Game/Enemies/Saurian/_Unique/SlaughterBoss/_Design/Character/BPChar_Saurian_SlaughterBoss',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian","Saurian_Tyrant"),
    ('Tink of Cunning','/Game/Enemies/Tink/_Unique/TrialBoss/_Design/Character/BPChar_Tink_TrialBoss',"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique","Tink_TrialBoss"),
    ('Skag of Survival','/Game/Enemies/Skag/_Unique/TrialBoss/_Design/Character/BPChar_Skag_TrialBoss',"/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique","TrialBoss"),
    ('Sera of Supremacy','/Game/Enemies/Guardian/_Unique/TrialBoss/_Design/Character/BPChar_Guardian_TrialBoss',"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique","Guardian_Trial_Boss"),
    ('Mr. Titan','/Game/Enemies/Goliath/_Unique/SlaughterBoss/_Design/Character/BPChar_Goliath_SlaughterBoss',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique",'SlaughterBoss'),
    ('Hag of Fervor','/Game/Enemies/Goon/_Unique/TrialBoss/_Design/Character/BPChar_Goon_TrialBoss',"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique","Goon_BossTrial"),
    ('Arbalest of Discipline','/Game/Enemies/Mech/_Unique/TrialBoss/_Design/Character/BPChar_Mech_TrialBoss',"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech","Mech_TrialBoss"), # There was also Mech_Basic
    ('IndoTyrant','/Game/Enemies/Saurian/_Unique/Rare01/_Design/Character/BPChar_Saurian_Rare01',"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique","Saurian_Rare01"),
    ('Demoskaggon','/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01','/Game/Enemies/Skag/_Shared/_Design/Balance/Table_Skag_Balance_Unique',"DemoSkag"),
    ('Warden','/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena',"/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique","CageArena"),
    ('Agonizer 9000','/Game/Enemies/Agonizer_9k/_Shared/Character/BPChar_Agonizer_9k',"/Game/Enemies/Agonizer_9k/_Shared/Balance/Table_Balance_Agonizer_9k","A9K"),
    ('Wick','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare03'),
    ('Borman Nates','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare02','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare02'),
    ('Warty','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare01','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','Rare01'),
    ('OnePunch','/Game/Enemies/Psycho_Male/_Unique/Rare03/_Design/Character/BPChar_PsychoRare03','/Game/Enemies/Psycho_Male/_Shared/_Design/Balance/Table_Psycho_Balance_Unique','OnePunch'),
    # ('Tumorhead','/Game/Enemies/Punk_Female/_Unique/TumorHead/_Design/Character/BPChar_PunkBadass_Tumorhead',None,None), #punk_badass non-unique
    ('Judge Hightower','/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01','/Game/NonPlayerCharacters/_Shared/_Design/Table_Balance_NPC','AtlasSoldier_Bounty'),
    ('Urist McEnforcer','/Game/Enemies/Enforcer/_Unique/Urist/_Design/Character/BPChar_EnforcerUrist','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance','Enforcer_Shield'), # I hope this is safe
    ('Killavolt (Kenneth)','/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt','/Game/Enemies/Enforcer/_Shared/_Design/Balance/Table_Enforcer_Balance_Unique','Enforcer_KillaVolt'),
    # Katagawa Jr has holograms too, row KatagawaJR_Hologram
    ('Katagawa Jr.','/Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR','/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/Table_Balance_KatagawaJR_PT1','KatagawaJR_Boss'),
    # Make the holograms kinda wimpy
    ('Katagawa Jr (Hologram).','/Game/Enemies/KatagawaJR/KJR/_Design/Character/BPChar_KJR','/Game/Enemies/KatagawaJR/_Shared/_Design/Balance/Table_Balance_KatagawaJR_PT1','KatagawaJR_Hologram',{'health':[DEFAULT_HEALTH/4]}),
]

bosses = [mk_boss(*x) for x in more_bosses]

for boss in bosses:
    print(buff_boss(boss))
    print("\n\n")
