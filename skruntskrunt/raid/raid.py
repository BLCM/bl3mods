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

tyreen = {
    'name':'Tyreen',
    'bpchar':'BPChar_FinalBoss',
    'bpchar_path':'/Game/Enemies/FinalBoss/_Shared/_Design/Character/BPChar_FinalBoss',
    'rowname':'FinalBoss',
    'balance_table':'/Game/Enemies/FinalBoss/_Shared/_Design/Balance/Table_Balance_FinalBoss_PT1',
    'nloot':DEFAULT_NLOOT,
    'health':[DEFAULT_HEALTH,DEFAULT_HEALTH],
    'damage':DEFAULT_DAMAGE
}
troy = {
    'name':'Troy',
    'bpchar':'BPChar_TroyBoss',
    'bpchar_path':'/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/BPChar_TroyBoss',
    'rowname':'TroyBoss',
    'balance_table':'/Game/NonPlayerCharacters/Troy/_Design/Balance/Table_Balance_TroyBoss_PT1',
    'nloot':DEFAULT_NLOOT,
    'health':[DEFAULT_HEALTH,DEFAULT_HEALTH],
    'damage':DEFAULT_DAMAGE
}
rampager = {
    'name':'Rampager',
    'bpchar':'BPChar_Rampager',
    'bpchar_path':'/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager',
    'rowname':'Rampager',
    'balance_table':'/Game/Enemies/PrometheaBoss/_Shared/_Design/Balance/Table_Balance_PromBoss_PT1',
    'nloot':DEFAULT_NLOOT,
    'health':[DEFAULT_HEALTH,DEFAULT_HEALTH],
    'damage':DEFAULT_DAMAGE    
}
def mk_boss(name, bpchar_path, balance_table, rowname):
    return {
        'name':name,
        'bpchar':basename(bpchar_path),
        'bpchar_path':bpchar_path,
        'rowname':rowname,
        'balance_table':balance_table,
        'nloot':DEFAULT_NLOOT,
        'health':[DEFAULT_HEALTH,DEFAULT_HEALTH],
        'damage':DEFAULT_DAMAGE    
    }

ruiner = mk_boss('Ruiner', '/Geranium/Enemies/Ruiner/Boss/_Design/Character/BPChar_RuinerBoss', '/Geranium/Enemies/Ruiner/_Shared/_Design/Balance/Table_Ruiner_Balance', 'Ruiner_Boss')
minosaur = mk_boss('Minosaur','/Geranium/Enemies/GerSaurian/_Unique/Saurtaur/_Design/Character/BPChar_GerSaurianSaurtaur','/Geranium/Enemies/GerSaurian/_Shared/_Design/Balance/Table_GerSaurian_Balance_Unique','GerSaurian_Saurtaur')
bosses = [tyreen, troy, rampager, ruiner, minosaur]

for boss in bosses:
    print(buff_boss(boss))
    print("\n\n")
