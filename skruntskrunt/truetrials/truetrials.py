import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

BALANCE_DATA = "/Game/GameData/Loot/RarityWeighting/DataTable_Lootable_BalanceData.DataTable_Lootable_BalanceData"
RARITY_MODIFIERS = [
    "CommonWeightModifier_21_3D483428462299E5B6AF02B6CC0F65CC",
    "UncommonWeightModifier_12_A1CB19B648A9D93482D9DC83713A2FB5",
    "RareWeightModifier_16_F11E138D458B57D473F062A6C52A5F58",
    "VeryRareWeightModifier_17_8A0A186D4D4FC53ADDFB71A8A7F589DA",
]
CHEST_GEMS = ["TrialsChestNoGem","TrialsChestOneGem","TrialsChestTwoGems","TrialsChestThreeGems"]
LEVELS = sorted(["ProvingGrounds_Trial8_P","ProvingGrounds_Trial7_P","ProvingGrounds_Trial6_P","ProvingGrounds_Trial5_P","ProvingGrounds_Trial4_P","ProvingGrounds_Trial1_P"])
QUANTITY = "Quantity.BaseValueConstant"
BASE_QUANTITY = 4
XPVALUE = "NewEnumerator7"
EXPERIENCE_MODIFIER="ExperienceType_8_73D53DF14EC1787599308F9A13A91D97"
DAMAGE_MODIFIER = "DamageMultiplier_LevelBased_23_3CAF34804D650A98AB8FAFAB37CB87FF"
HEALTH_MODIFIERS = ["HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12",
                    "HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49"
]
ITEMPOOL_ENTRY="BalancedItems"

bosses = {
    "BPChar_Goon_TrialBoss":{
        "bpchar":"BPChar_Goon_TrialBoss",
        "balance_name":"Goon_BossTrial",
        "level":"ProvingGrounds_Trial4_P",
        "balance_table":"/Game/Enemies/Goon/_Shared/_Design/Balance/Table_Balance_Goon_Unique.Table_Balance_Goon_Unique",
        "item_pool":"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon",
        # this is combined the OG drops + the gearbox drops
        "assign_loot":"((InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_FireBrand.InvBalD_ClassMod_Operative_FireBrand,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/Operative/InvBalD_ClassMod_Operative_FireBrand.InvBalD_ClassMod_Operative_FireBrand\"'),(InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker.InvBalD_ClassMod_Siren_Phasezerker,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Phasezerker.InvBalD_ClassMod_Siren_Phasezerker\"'),(InventoryBalanceData=/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie\"'),(InventoryBalanceData=/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence.Balance_SG_HYP_Convergence,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence.Balance_SG_HYP_Convergence\"'))",
        "health":[1000,1000], # nerf'd the gb values of 2000,20000
        "damage":2.2, # upped her damage
    },
    "BPChar_Tink_TrialBoss":{
        "bpchar":"BPChar_Tink_TrialBoss",
        "balance_name":"Tink_TrialBoss",
        "level":"ProvingGrounds_Trial5_P",
        "balance_table":"/Game/Enemies/Tink/_Shared/_Design/Balance/Table_Balance_Tink_Unique.Table_Balance_Tink_Unique",
        "item_pool":"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink",
        # this is combined the OG drops + the gearbox drops
        "assign_loot":"((InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon.InvBalD_ClassMod_Siren_Dragon,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Dragon.InvBalD_ClassMod_Siren_Dragon\"'),(InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1.InvBalD_CM_Beastmaster_Raid1,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/BSM/InvBalD_CM_Beastmaster_Raid1.InvBalD_CM_Beastmaster_Raid1\"',Weight=(BaseValueAttribute=GbxAttributeData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/Mayhem4/Att_CharacterWeight_Beastmaster_M4.Att_CharacterWeight_Beastmaster_M4\"')),(InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle\"'),(InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher.Balance_SR_JAK_Skullmasher,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher.Balance_SR_JAK_Skullmasher\"'))",
        "health":[800],
        "damage":2.2,
    },
    "BPChar_Guardian_TrialBoss":{
        "bpchar":"BPChar_Guardian_TrialBoss",
        "balance_name":"Guardian_Trial_Boss",
        "level":"ProvingGrounds_Trial6_P",
        "balance_table":"/Game/Enemies/Guardian/_Shared/_Design/Balance/Table_Balance_Guardian_Unique.Table_Balance_Guardian_Unique",
        "item_pool":"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian",
        # this is combined the OG drops + the gearbox drops
        "assign_loot":"((InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus.InvBalD_ClassMod_Siren_Nimbus,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Nimbus.InvBalD_ClassMod_Siren_Nimbus\"'),(InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist.InvBalD_ClassMod_Siren_Elementalist,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/Siren/InvBalD_ClassMod_Siren_Elementalist.InvBalD_ClassMod_Siren_Elementalist\"'),(InventoryBalanceData=/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch.Balance_AR_VLA_Monarch,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch.Balance_AR_VLA_Monarch\"',Weight=(BaseValueAttribute=GbxAttributeData'\"/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/Att_Mayhem2_Only_DropChance.Att_Mayhem2_Only_DropChance\"')),(InventoryBalanceData=/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Replay/Balance/Balance_PS_ATL_Replay.Balance_PS_ATL_Replay,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Replay/Balance/Balance_PS_ATL_Replay.Balance_PS_ATL_Replay\"'))",

        "health":[800,50],
        "damage":2.3, # didn't see this in the hotfix
    },
    "BPChar_Mech_TrialBoss":{
        "bpchar":"BPChar_Mech_TrialBoss",
        "balance_name":"Mech_TrialBoss",
        "level":"ProvingGrounds_Trial7_P",
        "balance_table":"/Game/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Unique.Table_Balance_Mech_Unique",
        "item_pool":"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech",
        # this is combined the OG drops + the gearbox drops
        "assign_loot":"((InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot.InvBalD_ClassMod_Beastmaster_FriendBot,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_FriendBot.InvBalD_ClassMod_Beastmaster_FriendBot\"'),(InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1.InvBalD_CM_Operative_Raid1,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/CM/_D/PartSets/_U/OPE/InvBalD_CM_Operative_Raid1.InvBalD_CM_Operative_Raid1\"',Weight=(BaseValueAttribute=GbxAttributeData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/Mayhem4/Att_CharacterWeight_Operative_M4.Att_CharacterWeight_Operative_M4\"')),(InventoryBalanceData=/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper.Balance_SM_MAL_Flipper,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper.Balance_SM_MAL_Flipper\"'),(InventoryBalanceData=/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson.Balance_SM_DAHL_Kaoson,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson.Balance_SM_DAHL_Kaoson\"',Weight=(BaseValueAttribute=GbxAttributeData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/Mayhem4/Att_CharacterWeight_Operative_M4.Att_CharacterWeight_Operative_M4\"')))",
        "health":[800,500],
        "damage":2.3,
    },
    "BPChar_Saurian_TrialBoss":{
        "bpchar":"BPChar_Saurian_TrialBoss",
        "balance_name":"Saurian_TrialBoss",
        "level":"ProvingGrounds_Trial8_P",
        "balance_table":"/Game/Enemies/Saurian/_Shared/_Design/Balance/Table_Balance_Saurian_Unique.Table_Balance_Saurian_Unique",
        "item_pool":"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian",
        # this is combined the OG drops + the gearbox drops
        "assign_loot":"((InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker.InvBalD_ClassMod_Beastmaster_CosmicStalker,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_CosmicStalker.InvBalD_ClassMod_Beastmaster_CosmicStalker\"'),(InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang.InvBalD_ClassMod_Beastmaster_RedFang,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/ClassMods/BeastMaster/InvBalD_ClassMod_Beastmaster_RedFang.InvBalD_ClassMod_Beastmaster_RedFang\"'),(InventoryBalanceData=/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner.Balance_HW_VLA_ETech_BackBurner,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner.Balance_HW_VLA_ETech_BackBurner\"'),(InventoryBalanceData=/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy.Balance_PS_COV_Tizzy,ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy.Balance_PS_COV_Tizzy\"'))",
        "health":[800],
        "damage":2,
    },
    
}
level_to_boss = {bosses[x]["level"]:bosses[x]["bpchar"] for x in bosses}

# Stolen from DexManly
SUBHEADER="SubHeader"
DISPLAYNAME="DisplayName"
TRIAL_NAMES=[
    ('/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-1.PlanetMapData_ProvingGround-1',  'Proving Grounds - True Survival'   , 'Gradient of Dawn (True Survival)')         ,
    ('/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-4.PlanetMapData_ProvingGround-4',  'Proving Grounds - True Fervor'     , 'The Skydrowned Pulpit (True Fervor)')      ,
    ('/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-5.PlanetMapData_ProvingGround-5',  'Proving Grounds - True Cunning'    , 'Ghostlight Beacon (True Cunning)')         ,
    ('/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-6.PlanetMapData_ProvingGround-6',  'Proving Grounds - True Supremacy'  , 'The Hall Obsidian (True Supremacy)')       ,
    ('/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-7.PlanetMapData_ProvingGround-7',  'Proving Grounds - True Discipline' , 'Precipice Anchor (True Discipline)')       ,
    ('/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-8.PlanetMapData_ProvingGround-8',  'Proving Grounds - True Instinct'   , 'Wayward Tether (True Instinct)')           ,
]



mod = Mod('truetrials.bl3hotfix',
        'True Trials',
        'SkruntSkrunt, DexManly',
        [
            "Borrowing from Gearboxes Weekly Events, RAID-IFY all the trials. ",
            "Also restore both the weekly event drops and the original drops. ",
            "Also changes Trial Names using DexManly's code."
        ],
        lic=Mod.CC_BY_SA_40,
        v='0.1.0',
        cats='gameplay',
)

def trial_names(mod):
    mod.newline()
    mod.comment(f"Dexmanly's trial names")
    for (level, subheader, displayname) in TRIAL_NAMES:        
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll', level, SUBHEADER, subheader)
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll', level, displayname, displayname)

def change_trial_drops(mod,levels=LEVELS,gems=CHEST_GEMS,rarities=RARITY_MODIFIERS):
    for level in levels:
        mod.newline()
        mod.comment(f"Final Chest for level {level}")
        for gem in gems:
            for rarity in rarities:
                # 1,2,0
                mod.table_hotfix(Mod.LEVEL, level, BALANCE_DATA, gem, rarity, 0.0)

def buff_boss(mod,boss):
    mod.newline()
    mod.comment(f"buffing boss: {boss['bpchar']}")
    # could we do this just for the level?
    # change the drop number
    mod.reg_hotfix(Mod.PATCH, '', boss["item_pool"], QUANTITY, BASE_QUANTITY)
    # change the item pool itself
    mod.reg_hotfix(Mod.PATCH, '', boss["item_pool"], ITEMPOOL_ENTRY, boss["assign_loot"])
    # buff the boss
    # - XP
    mod.reg_hotfix(Mod.CHAR, boss['bpchar'], boss["balance_table"], EXPERIENCE_MODIFIER, XPVALUE)
    # - DAMAGE
    if not boss["damage"] is None:
        mod.reg_hotfix(Mod.CHAR, boss['bpchar'], boss["balance_table"], DAMAGE_MODIFIER, boss["damage"])
    # - HEALTH
    for (healthv, healthm) in zip(boss["health"],HEALTH_MODIFIERS):
        mod.reg_hotfix(Mod.CHAR, boss['bpchar'], boss["balance_table"], healthm, healthv)

def buff_all_bosses(mod,bosses=bosses):
    for boss in bosses:
        buff_boss(mod, bosses[boss])

trial_names(mod)
change_trial_drops(mod)
buff_all_bosses(mod)


mod.close()
