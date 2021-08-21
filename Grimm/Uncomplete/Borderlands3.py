from bl3hotfixmod import Mod
from LIBRARY_CM_stats import *
from LIBRARY_FL4K_stalker import *
from LIBRARY_FL4K_hunter import *
from LIBRARY_FL4K_master import *
from LIBRARY_FL4K_trapper import *
from LIBRARY_FL4K_class_mods import *
from Library_ATLAS import *
from Library_COV import *
from Library_DAHL import *
from Library_HYPERION import *
from Library_JAKOBS import *
from Library_MALIWAN import *
from Library_TEDIORE import *
from Library_TORGUE import *
from Library_VLADOF import *
from Library_WEAPON_TYPE import *
from Library_Shields import *
from LIBRARY_Grenades import *

mod=Mod('Borderlands3.bl3hotfix',
'Borderlands 3',
'Grimm',
[
    'Categories: major-pack, mode-balance, scaling, mayhem, gear-general, gear-anointments, gear-brand, gear-pack, gear-ar, gear-pistol, gear-heavy, gear-shotgun, gear-smg, gear-sniper, gear-grenade, vendor, qol',
    'Huge overhaul that includes: QOL, TVHM is harder, mayhem rescale, anointement removal, DLC4 bosses rescale, Takedowns rescale, overall weapon and grenade balance, and all the unique gear rebalanced as well.',
    'QOL stuff : No more anointed enemies, no more engorged rakks in the slaughters, loot enemies spawn more often, you can get all the gear from lvl1, and all the slots are uvailable at lvl1 (uncompatible with early bloomer, it does the same thing) and CoV badasses have less rocket launchers',
    'Changes in this version only : Mayhem scaling has been removed, Mayhem is now modifiers only, and m11 is used to scale NVHM to your level. The game is naturally harder, and TVHM is harder as well. You dont receive mayhem specific gear anymore (m10 gear is the same than non mayhem or m5).',
    'All the guns/grenades should now be closer to each other in term of each other',
    'You should play in M11 at all times, since without it you wont get mayhem exclusive gear.',
    'This mod took a long time to make, please report any issues, stuff that dont work, or works too well. The balance is not definitive, so please report that as well. And ofc enjoy',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'

],
lic=Mod.CC_BY_SA_40,
)

str_invbalance = ''

str_toc = ''
int_index = 0
int_numparts = 0

str_partset = ''

str_dep = ''

str_dep_cm = ''

enemyhp=[
"HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68",
"ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6",
"ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8"
]
exp="ExpGainScalar_39_2159F009466933AA733AE688E55B1B93"
cash="CashScalar_22_B7B11DC94BBB45C94A96279146EC193E"
drop1="DropWeightCommonScalar_21_59A2FB124E32B955768A7B9D93C25A99"
drop2="DropWeightUncommonScalar_25_809615334E7F0DB3B8712DAC221015C3"
drop3="DropWeightRareScalar_27_A09CF5314C51796896A83EA0806C7520"
drop4="DropWeightVeryRareScalar_29_F2CA570046CD50A7C514EDB0AE1BE591"
drop5="DropWeightLegendaryScalar_31_D9DA03C54065EA981BE218B11942C24E"
dropnum="DropNumberChanceSimpleScalar_40_115637764B3918F01E6FAFADDC005388"
eridium="DropEridiumChanceSimpleScalar_41_E89AD7E9473FDF3CBED395BA6641FA68"
loot="LootQuality_56_03E220E0495C6B37CD6C7195F5EA289B"
asd="DamageScalarActionSkill_60_39AF483140740A38FC71BA897155CBFF"
melee="DamageScalarMelee_67_9948929F4FF34364CED2EAB51A881946"
slide="DamageScalarSlide_68_B48D0E3A4DF57196839BB58D5AE3E638"
slam="DamageScalarSlam_69_15DB6EDC4CCA52620BF25398CFFD9B26"
petdmg="DamageScalarPet_72_0DD7977D44C4A71D0A6B56B7884E023C"
env="DamageScalarEnviornmental_111_E2A582AA47FC000789FC68BBD31D2CFC"
passiveskill="DamageScalarPassive_115_6A30229E4CC04F751ED01CB64A71880F"
vehicledmg="DamageDealtScalarVehicles_103_5739171948322B35CDA36487F78AF0CE"
vehiclehp="DamageTakenScalarVehicles_104_B75AB4EC482624FDEAAF31B0FA369A77"
gear="DamageScalarGear_119_9FC89117424C6619F2CA958FA2842FC2"
pethp="PetHealth_84_E5B903B4452F4310CCD13C931474E12B"
comphp="CompanionHealth_89_294A6BE7439072AE9F934CAA127D8D83"

mod.comment('General Changes')
if True:

    mod.comment('Adjusting Vending Machine Pool')
    if True:

        mod.comment('Adjusting Weapon of the Day Machine Pool')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            1.5
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            2.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Weapons_OfTheDay',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            1.2
            )
            mod.newline()

        mod.comment('Adjusting Grenade of the Day Machine Pool')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            1.5
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            2.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Ammo_OfTheDay',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            1.2
            )
            mod.newline()

        mod.comment('Adjusting Shield of the Day Machine Pool')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[0].Weight.BaseValueScale',
            1.5
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[1].Weight.BaseValueScale',
            2.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[2].Weight.BaseValueScale',
            1.2
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[3].Weight.BaseValueScale',
            1.5
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[4].Weight.BaseValueScale',
            2.0
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_Health_OfTheDay',
            'BalancedItems.BalancedItems[5].Weight.BaseValueScale',
            1.2
            )
            mod.newline()

    mod.comment('Ammo loot is based on missing ammo')
    if True :

        health=[ 
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Health_Resolver_NeedandGreed.Att_Health_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Health_DropOdds.Att_Health_DropOdds:ResourceWeightAttributeValueResolver_0'
        ]

        ammo=[ 
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_AssaultRifle_Resolver_NeedandGreed.Att_Ammo_AssaultRifle_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_AssaultRifle_Resolver_NeedOnly.Att_Ammo_AssaultRifle_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Grenade_Resolver_NeedandGreed.Att_Ammo_Grenade_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Grenade_Resolver_NeedOnly.Att_Ammo_Grenade_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Heavy_Resolver_NeedandGreed.Att_Ammo_Heavy_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Heavy_Resolver_NeedOnly.Att_Ammo_Heavy_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Pistol_Resolver_NeedandGreed.Att_Ammo_Pistol_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Pistol_Resolver_NeedOnly.Att_Ammo_Pistol_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Shotgun_Resolver_NeedandGreed.Att_Ammo_Shotgun_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Shotgun_Resolver_NeedOnly.Att_Ammo_Shotgun_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_SMG_Resolver_NeedandGreed.Att_Ammo_SMG_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_SMG_Resolver_NeedOnly.Att_Ammo_SMG_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Sniper_Resolver_NeedandGreed.Att_Ammo_Sniper_Resolver_NeedandGreed:ResourceWeightAttributeValueResolver_0',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Sniper_Resolver_NeedOnly.Att_Ammo_Sniper_Resolver_NeedOnly:ResourceWeightAttributeValueResolver_0'
        ]

        for type in health :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'ResourceThreshold',
            '(BaseValueConstant=0.5,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'AboveThresholdWeight',
            '(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'NoPoolWeight',
            '(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'MinBelowThresholdWeight',
            '(BaseValueConstant=20.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'MaxBelowThresholdWeight',
            '(BaseValueConstant=50.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

        for type in ammo :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'ResourceThreshold',
            '(BaseValueConstant=0.5,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'AboveThresholdWeight',
            '(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'NoPoolWeight',
            '(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'MinBelowThresholdWeight',
            '(BaseValueConstant=20.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            type,
            'MaxBelowThresholdWeight',
            '(BaseValueConstant=200.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None))'
            )
            mod.newline()

        mod.comment('Scaling The ammo Pool')
        if True :        

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[0].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_AssaultRifle_Resolver_NeedOnly.Att_Ammo_AssaultRifle_Resolver_NeedOnly'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[1].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Grenade_Resolver_NeedOnly.Att_Ammo_Grenade_Resolver_NeedOnly'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[2].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Heavy_Resolver_NeedOnly.Att_Ammo_Heavy_Resolver_NeedOnly'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[3].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Pistol_Resolver_NeedOnly.Att_Ammo_Pistol_Resolver_NeedOnly'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[4].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Shotgun_Resolver_NeedOnly.Att_Ammo_Shotgun_Resolver_NeedOnly'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[5].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_SMG_Resolver_NeedOnly.Att_Ammo_SMG_Resolver_NeedOnly'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/Ammo/ItemPool_Ammo',
            'BalancedItems.BalancedItems[6].Weight.BaseValueAttribute',
            '/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Sniper_Resolver_NeedOnly.Att_Ammo_Sniper_Resolver_NeedOnly'
            )
            mod.newline()

        mod.comment('Ammo Crate Pool')
        if True :  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate',
            'BalancedItems',
            """
            (
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_AssaultRifle.DA_InventoryBalance_Ammo_AssaultRifle,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_AssaultRifle.DA_InventoryBalance_Ammo_AssaultRifle\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_AssaultRifle_Resolver_NeedandGreed.Att_Ammo_AssaultRifle_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Pistol.DA_InventoryBalance_Ammo_Pistol,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Pistol.DA_InventoryBalance_Ammo_Pistol\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Pistol_Resolver_NeedandGreed.Att_Ammo_Pistol_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Shotgun.DA_InventoryBalance_Ammo_Shotgun,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Shotgun.DA_InventoryBalance_Ammo_Shotgun\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Shotgun_Resolver_NeedandGreed.Att_Ammo_Shotgun_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_SMG.DA_InventoryBalance_Ammo_SMG,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_SMG.DA_InventoryBalance_Ammo_SMG\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_SMG_Resolver_NeedandGreed.Att_Ammo_SMG_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_SniperRifle.DA_InventoryBalance_Ammo_SniperRifle,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_SniperRifle.DA_InventoryBalance_Ammo_SniperRifle\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Sniper_Resolver_NeedandGreed.Att_Ammo_Sniper_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Heavy.DA_InventoryBalance_Ammo_Heavy,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Heavy.DA_InventoryBalance_Ammo_Heavy\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Heavy_Resolver_NeedandGreed.Att_Ammo_Heavy_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Grenade.DA_InventoryBalance_Ammo_Grenade,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Grenade.DA_InventoryBalance_Ammo_Grenade\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Ammo_Grenade_Resolver_NeedandGreed.Att_Ammo_Grenade_Resolver_NeedandGreed)
                ),
                (
                    ItemPoolData=None,
                    InventoryBalanceData=/Game/Pickups/Health/DA_InventoryBalance_Health.DA_InventoryBalance_Health,
                    ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Pickups/Health/DA_InventoryBalance_Health.DA_InventoryBalance_Health\"',
                    Weight=(BaseValueAttribute=/Game/GameData/Loot/ItemPools/Attributes/Att_Health_Resolver_NeedandGreed.Att_Health_Resolver_NeedandGreed)
                )
            )
            """
            )
            mod.newline()

        mod.comment('Ammo Chest Global')
        if True :  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Lootables/_Design/Data/Global/LootDef_Global_AmmoChest',
            'DefaultLoot.DefaultLoot[0].ItemAttachments',
            """
            (
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopMiddle
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomMiddle
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopLeft
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopRight
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomLeft
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomRight
                )
            )
            """
            )
            mod.newline()

        mod.comment('Ammo Chest CoV')
        if True :  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Lootables/_Design/Data/CoV/LootDef_COV_AmmoChest',
            'DefaultLoot.DefaultLoot[0].ItemAttachments',
            """
            (
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopMiddle
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomMiddle
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopLeft
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopRight
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomLeft
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomRight
                )
            )
            """
            )
            mod.newline()

        mod.comment('Ammo Chest CoV')
        if True :  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Lootables/_Design/Data/Eridian/LootDef_Eridian_AmmoCrate',
            'DefaultLoot.DefaultLoot[0].ItemAttachments',
            """
            (
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopMiddle
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomMiddle
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopLeft
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=TopRight
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomLeft
                ),
                (
                    ItemPool=/Game/GameData/Loot/ItemPools/ItemPool_AmmoCrate.ItemPool_AmmoCrate,
                    AttachmentPointName=BottomRight
                )
            )
            """
            )
            mod.newline()

    mod.comment('Making the Guardian Ranks Cosmetic Only')
    if True :

        mod.comment('Enforcer')
        if True :

            mod.comment('Enforcer 10')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_10',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_10',
                'Description',
                'Unlock the Weapon Skin [red]Burnished Steele[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_10',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_1.WeaponSkin_1'
                )
                mod.newline()

            mod.comment('Enforcer 15')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_15',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_15',
                'Description',
                'Unlock the Weapon Skin [red]Thunderhead[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_15',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_2.WeaponSkin_2'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_15',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Enforcer 25')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_25',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_25',
                'Description',
                'Unlock the Weapon Skin [red]Psychodelic[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_25',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_3.WeaponSkin_3'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_25',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Enforcer 35')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_35',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_35',
                'Description',
                'Unlock the Weapon Skin [red]Deep Nebula[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_35',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_4.WeaponSkin_4'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_35',
                'PerkCustomizations',
                ''
                )
                mod.newline()

            mod.comment('Enforcer 50')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_50',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_50',
                'Description',
                'Unlock the Weapon Skin [red]Dead Set[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_50',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_5.WeaponSkin_5'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_50',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Enforcer 75')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_75',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_75',
                'Description',
                'Unlock the Weapon Skin [red]Hot Blooded[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_75',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_6.WeaponSkin_6'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_75',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Enforcer 100')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_100',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_100',
                'Description',
                'Unlock the Weapon Skin [red]Red Sands[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_100',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_7.WeaponSkin_7'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_100',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Enforcer 125')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_125',
                'DisplayName',
                'Weapon Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_125',
                'Description',
                'Unlock the Weapon Skin [red]Gun-fetti[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_125',
                'PerkWeaponSkins',
                '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_8.WeaponSkin_8'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Enforcer_125',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

        mod.comment('Hunter')
        if True :

            mod.comment('Hunter 10')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_10',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_10',
                'Description',
                'Unlock the Player Skin [red]Jungle Jams[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_10',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_1.CustomSkin_Beastmaster_1
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_1.CustomSkin_Siren_1
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_1.CustomSkin_Operative_1
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_1.CustomSkin_Gunner_1
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_10',
                'PerkWeaponSkins',
                ''
                )
                mod.newline()
            
            mod.comment('Hunter 15')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_15',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_15',
                'Description',
                'Unlock the Player Skin [red]Labradortilla[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_15',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_2.CustomSkin_Beastmaster_2
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_2.CustomSkin_Siren_2
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_2.CustomSkin_Operative_2
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_2.CustomSkin_Gunner_2
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_15',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Hunter 25')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_25',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_25',
                'Description',
                'Unlock the Player Skin [red]Teal Appeal[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_25',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_3.CustomSkin_Beastmaster_3
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_3.CustomSkin_Siren_3
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_3.CustomSkin_Operative_3
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_3.CustomSkin_Gunner_3
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_25',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Hunter 35')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_35',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_35',
                'Description',
                'Unlock the Player Skin [red]Extreme Caution[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_35',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_4.CustomSkin_Beastmaster_4
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_4.CustomSkin_Siren_4
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_4.CustomSkin_Operative_4
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_4.CustomSkin_Gunner_4
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_35',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Hunter 50')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_50',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_50',
                'Description',
                'Unlock the Player Skin [red]Amp Stamp[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_50',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_5.CustomSkin_Beastmaster_5
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_5.CustomSkin_Siren_5
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_5.CustomSkin_Operative_5
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_5.CustomSkin_Gunner_5
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_50',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Hunter 75')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_75',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_75',
                'Description',
                'Unlock the Player Skin [red]Sure, Why Not?[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_75',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_6.CustomSkin_Beastmaster_6
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_6.CustomSkin_Siren_6
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_6.CustomSkin_Operative_6
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_6.CustomSkin_Gunner_6
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_75',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Hunter 100')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_100',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_100',
                'Description',
                'Unlock the Player Skin [red]Anshin Wash Only[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_100',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_7.CustomSkin_Beastmaster_7
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_7.CustomSkin_Siren_7
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_7.CustomSkin_Operative_7
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_7.CustomSkin_Gunner_7
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_100',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Hunter 125')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_125',
                'DisplayName',
                'Player Skin'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_125',
                'Description',
                'Unlock the Player Skin [red]Pimp My Raider[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_125',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_8.CustomSkin_Beastmaster_8
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_8.CustomSkin_Siren_8
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_8.CustomSkin_Operative_8
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_8.CustomSkin_Gunner_8
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Hunter_125',
                'PerkAbilityClass',
                ''
                )
                mod.newline()
        
        mod.comment('Survivor')
        if True :

            mod.comment('Survivor 10')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_10',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_10',
                'Description',
                'Unlock the Head Models [red]Simul4crum[/red], [red]Fresh to Death[/red], [red]Ronin[/red] and [red]Cry Havoc[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_10',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_1.CustomHead_Beastmaster_1
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_1.CustomHead_Siren_1
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_1.CustomHead_Operative_1
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_1.CustomHead_Gunner_1
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_10',
                'PerkWeaponSkins',
                ''
                )
                mod.newline()
            
            mod.comment('Survivor 15')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_15',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_15',
                'Description',
                'Unlock the Head Models [red]4ction Figure[/red], [red]Eyes on Target[/red], [red]One Last Job[/red] and [red]Motosaurus[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_15',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_4.CustomHead_Beastmaster_4
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_4.CustomHead_Siren_4
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_4.CustomHead_Operative_4
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_4.CustomHead_Gunner_4
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_15',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Survivor 25')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_25',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_25',
                'Description',
                'Unlock the Head Models [red]He4d in the Cloud[/red], [red]Insulation[/red], [red]Wanderer[/red] and [red]A Few Scrapes[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_25',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_5.CustomHead_Beastmaster_5
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_5.CustomHead_Siren_5
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_5.CustomHead_Operative_5
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_5.CustomHead_Gunner_5
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_25',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Survivor 35')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_35',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_35',
                'Description',
                'Unlock the Head Models [red]Dre4dful Visage[/red], [red]Toxic Behavior[/red], [red]Demon Could Weep[/red] and [red]Starry Eyed[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_35',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_6.CustomHead_Beastmaster_6
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_6.CustomHead_Siren_6
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_6.CustomHead_Operative_6
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_6.CustomHead_Gunner_6
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_35',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Survivor 50')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_50',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_50',
                'Description',
                'Unlock the Head Models [red]De4thless[/red], [red]Cy-Ops[/red], [red]Tusk Raider[/red] and [red]Transmission Vector[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_50',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_7.CustomHead_Beastmaster_7
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_7.CustomHead_Siren_7
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_7.CustomHead_Operative_7
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_7.CustomHead_Gunner_7
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_50',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Survivor 75')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_75',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_75',
                'Description',
                'Unlock the Head Models [red]Anim4tronic[/red], [red]Bull Mozer[/red], [red]Jawperative[/red] and [red]Chokella[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_75',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_8.CustomHead_Beastmaster_8
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_8.CustomHead_Siren_8
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_8.CustomHead_Operative_8
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_8.CustomHead_Gunner_8
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_75',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Survivor 100')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_100',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_100',
                'Description',
                'Unlock the Head Models [red]Cr4cked[/red], [red]Iron Baron[/red], [red]Suction Filter[/red] and [red]Jawbreaker[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_100',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_9.CustomHead_Beastmaster_9
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_9.CustomHead_Siren_9
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_9.CustomHead_Operative_9
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_9.CustomHead_Gunner_9
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Hibiscus/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_100',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

            mod.comment('Survivor 125')
            if True :
            
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_125',
                'DisplayName',
                'Head Models'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_125',
                'Description',
                'Unlock the Head Models [red]Sh4man[/red], [red]Shark Tank[/red], [red]Weathered[/red] and [red]Cyber Hawk[/red].'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_125',
                'PerkCustomizations',
                """
                (
                    /Game/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_10.CustomHead_Beastmaster_10
                ),
                (
                    /Game/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_10.CustomHead_Siren_10
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_10.CustomHead_Operative_10
                ),
                (
                    /Game/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_10.CustomHead_Gunner_10
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Geranium/PlayerCharacters/_Shared/_Design/GuardianRank/GuardianPerk_Survivor_125',
                'PerkAbilityClass',
                ''
                )
                mod.newline()

    mod.comment('Enemies Changes')
    if True:

        mod.comment('Immunity Phases')
        if True :

            mod.comment('Mouthpiece')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerSacrificeBoss',
                '/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss.Default__BPChar_EnforcerSacrificeBoss_C:DefaultDamageComponent',
                'DamageEvents',
                '()'
                )
                mod.newline()

            mod.comment('Killavolt')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerKillaVolt',
                '/Game/Enemies/Enforcer/_Unique/KillaVolt/_Design/Character/BPChar_EnforcerKillaVolt.Default__BPChar_EnforcerKillaVolt_C:DefaultDamageComponent',
                'DamageEvents',
                '()'
                )
                mod.newline()
            
            mod.comment('Katagawa Jr')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_KatagawaJR',
                '/Game/Enemies/KatagawaJR/_Shared/_Design/Character/BPChar_KatagawaJR.Default__BPChar_KatagawaJR_C:DefaultDamageComponent',
                'DamageEvents',
                '()'
                )
                mod.newline()

            mod.comment('Rampager')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_Rampager',
                '/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager.Default__BPChar_Rampager_C:DefaultDamageComponent',
                'DamageEvents',
                '()'
                )
                mod.newline()

            mod.comment('Warden')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_Goliath_CageArena',
                '/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena.Default__BPChar_Goliath_CageArena_C:DefaultDamageComponent',
                'DamageEvents',
                """
                (
                    (
                        EventName=DE_RealEnrage,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary,
                        EventHealthPercent=0.999,
                        EventType=EDamageReactionEventType::Health,
                        MaxTriggerCount=1.0
                    ),
                    (
                        EventName=DE_LookToLevelUp,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary,
                        EventHealthPercent=0.5,
                        EventType=EDamageReactionEventType::Health,
                        MaxTriggerCount=1.0
                    ),
                    (
                        EventName=DE_LookToLevelUp,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary,
                        EventHealthPercent=0.0,
                        EventType=EDamageReactionEventType::Health,
                        MaxTriggerCount=1.0
                    ),
                    (
                        EventName=DE_LookToLevelUp,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary,
                        EventHealthPercent=0.5,
                        EventType=EDamageReactionEventType::Health,
                        MaxTriggerCount=3.0
                    )
                )
                """
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique',
                'CageArena',
                'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
                18.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Enemies/Goliath/_Shared/_Design/Balance/Table_Balance_Goliath_Unique.Table_Balance_Goliath_Unique',
                'CageArena',
                'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
                12.0
                )
                mod.newline()

            mod.comment('Aurelia')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_AureliaBoss',
                '/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Character/BPChar_AureliaBoss.Default__BPChar_AureliaBoss_C:DefaultDamageComponent',
                'DamageEvents',
                '()'
                )
                mod.newline()

            mod.comment('Agonizer')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_Agonizer_9k',
                '/Game/Enemies/Agonizer_9k/_Shared/Character/BPChar_Agonizer_9k.Default__BPChar_Agonizer_9k_C:DefaultDamageComponent',
                'DamageEvents',
                """
                (
                    (
                        EventName=OnReachPhase4_EridiumCore,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary
                        EventHealthPercent=0.0
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Troy')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_TroyBoss',
                '/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/BPChar_TroyBoss.Default__BPChar_TroyBoss_C:DefaultDamageComponent',
                'DamageEvents',
                '()'
                )
                mod.newline()

            mod.comment('Tyreen')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_FinalBoss',
                '/Game/Enemies/FinalBoss/_Shared/_Design/Character/BPChar_FinalBoss.Default__BPChar_FinalBoss_C:DefaultDamageComponent',
                'DamageEvents',
                """
                (
                    (
                        EventName=TooMuchDamage,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary,
                        EventHealthPercent=0.66
                    ),
                    (
                        EventName=TooMuchDamage,
                        HealthPool=/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary,
                        EventHealthPercent=0.33
                    )
                )
                """
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Enemies/FinalBoss/_Shared/_Design/Balance/Table_Balance_FinalBoss_PT1',
                'FinalBoss',
                'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
                75.0
                )
                mod.newline()

        mod.comment('Removing all the health bars from armored enemies')
        if True :

            #Mantakore

            mod.comment('Armored Jabbers')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_ApeBadass',
                '/Game/Enemies/Ape/Badass/_Design/Character/BPChar_ApeBadass.BPChar_ApeBadass_C:DefaultDamageComponent',
                'HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"',
                        HealthSectionPercentages=(0.66)
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"',
                        HealthSectionPercentages=(0.3,0.66)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Armored Hags')
            if True :

                #Tink Train

                mod.reg_hotfix(Mod.CHAR,'BPChar_GoonBadass',
                '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"',
                        HealthSectionPercentages=(0.66)
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"',
                        HealthSectionPercentages=(0.3,0.66)
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GoonBadass',
                '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"',
                        HealthSectionPercentages=(0.66)
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"',
                        HealthSectionPercentages=(0.3,0.66)
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GoonBadass',
                '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GoonBadass',
                '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

            mod.comment('Armored Goliaths')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_Goliath_CageArena',
                '/Game/Enemies/Goliath/_Unique/CageArena/_Design/Character/BPChar_Goliath_CageArena.Default__BPChar_Goliath_CageArena_C:DefaultDamageComponent',
                'HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"',
                        HealthSectionPercentages=(0.66)
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"',
                        HealthSectionPercentages=(0.3,0.66)
                    )
                )
                """
                )
                mod.newline()

            mod.comment('Armored Enforcers')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerTurnkey',
                '/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey.BPChar_EnforcerTurnkey_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerTurnkey',
                '/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey.BPChar_EnforcerTurnkey_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerTurnkey',
                '/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey.BPChar_EnforcerTurnkey_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerTurnkey',
                '/Game/Enemies/Enforcer/_Unique/TurnKey/_Design/Character/BPChar_EnforcerTurnkey.BPChar_EnforcerTurnkey_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerBadass',
                '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerBadass',
                '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerBadass',
                '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerBadass',
                '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

            mod.comment('Armored Punks')
            if True :

                mod.reg_hotfix(Mod.CHAR,'BPChar_PunkBadassArmored',
                '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadassArmored.BPChar_PunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_PunkBadassArmored',
                '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadassArmored.BPChar_PunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerBadass',
                '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadassArmored.BPChar_PunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_EnforcerBadass',
                '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadassArmored.BPChar_PunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_PunkArmored_LooterVIP',
                '/Dandelion/Enemies/Looters/Punk/ArmoredVIP/_Design/Character/BPChar_PunkArmored_LooterVIP.BPChar_PunkArmored_LooterVIP_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_PunkArmored_LooterVIP',
                '/Dandelion/Enemies/Looters/Punk/ArmoredVIP/_Design/Character/BPChar_PunkArmored_LooterVIP.BPChar_PunkArmored_LooterVIP_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_PunkArmored_LooterVIP',
                '/Dandelion/Enemies/Looters/Punk/ArmoredVIP/_Design/Character/BPChar_PunkArmored_LooterVIP.BPChar_PunkArmored_LooterVIP_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_PunkArmored_LooterVIP',
                '/Dandelion/Enemies/Looters/Punk/ArmoredVIP/_Design/Character/BPChar_PunkArmored_LooterVIP.BPChar_PunkArmored_LooterVIP_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerPunkBadassArmored',
                '/Geranium/Enemies/GerPunk_Female/Badass/_Design/Character/BPChar_GerPunkBadassArmored.BPChar_GerPunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerPunkBadassArmored',
                '/Geranium/Enemies/GerPunk_Female/Badass/_Design/Character/BPChar_GerPunkBadassArmored.BPChar_GerPunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerPunkBadassArmored',
                '/Geranium/Enemies/GerPunk_Female/Badass/_Design/Character/BPChar_GerPunkBadassArmored.BPChar_GerPunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerPunkBadassArmored',
                '/Geranium/Enemies/GerPunk_Female/Badass/_Design/Character/BPChar_GerPunkBadassArmored.BPChar_GerPunkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

            mod.comment('Armored Tinks')
            if True :

                #Big Donny

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored',
                '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored.BPChar_TinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored',
                '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored.BPChar_TinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored',
                '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored.BPChar_TinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored',
                '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored.BPChar_TinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored_Looter',
                '/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored_Looter.BPChar_TinkBadassArmored_Looter_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored_Looter',
                '/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored_Looter.BPChar_TinkBadassArmored_Looter_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored_Looter',
                '/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored_Looter.BPChar_TinkBadassArmored_Looter_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_TinkBadassArmored_Looter',
                '/Dandelion/Enemies/Looters/Tink/Badass/_Design/Character/BPChar_TinkBadassArmored_Looter.BPChar_TinkBadassArmored_Looter_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerTinkBadassArmored',
                '/Geranium/Enemies/GerTink/Badass/_Design/Character/BPChar_GerTinkBadassArmored.BPChar_GerTinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerTinkBadassArmored',
                '/Geranium/Enemies/GerTink/Badass/_Design/Character/BPChar_GerTinkBadassArmored.BPChar_GerTinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].HealthInformation',
                """
                (
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_01_Primary.ResourcePool_AI_Health_01_Primary"'
                    ),
                    (
                        HealthTypeData=HealthTypeData'"/Game/GameData/ResourcePools/HealthTypes/HealthType_Shield.HealthType_Shield"',
                        HealthPoolData=GameResourcePoolData'"/Game/GameData/ResourcePools/ResourcePool_AI_Health_02_Secondary.ResourcePool_AI_Health_02_Secondary"'
                    )
                )
                """
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerTinkBadassArmored',
                '/Geranium/Enemies/GerTink/Badass/_Design/Character/BPChar_GerTinkBadassArmored.BPChar_GerTinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[0].bOverrideHealthInformation',
                'true'
                )
                mod.newline()

                mod.reg_hotfix(Mod.CHAR,'BPChar_GerTinkBadassArmored',
                '/Geranium/Enemies/GerTink/Badass/_Design/Character/BPChar_GerTinkBadassArmored.BPChar_GerTinkBadassArmored_C:AIBalanceState_GEN_VARIABLE',
                'PlayThroughs.PlayThroughs[1].bOverrideHealthInformation',
                'true'
                )
                mod.newline()
                
        mod.comment('Health Offset (Previously 0.02)')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
            'AI_AdditionalHealthPerLevel',
            'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
            0.105
            )
            mod.newline()
                
        mod.comment('Damage Offset (Previously 0.03)')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
            'AI_AdditionalDamagePerLevel',
            'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
            0.04
            )
            mod.newline()

    mod.comment('Slaughters and Takedowns Changes')
    if True :

        mod.comment('Promethea Slaughter Changes')
        if True:

            mod.comment('Removing The Engorged Rakks From The Slaughter')
            if True:

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave4b_RatchJabbermonVarkid',
                'Options.Options[11].Factory.Object..AIActorClass',
                ''
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5b',
                'Options.Options[2].Factory.Object..AIActorClass',
                ''
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5c',
                'Options.Options[18].Factory.Object..AIActorClass',
                ''
                )
                mod.newline()
            
            mod.comment('Makes The Slaughter Available From The Start')
            if True:

                dep=Mod.get_full_cond('/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C', 'Mission')

                mod.comment('Code courtesy of Apocalyptech')
                mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                '/Game/Missions/Side/Slaughters/CreatureSlaughter/Mission_CreatureSlaughter.Default__Mission_CreatureSlaughter_C',
                'MissionDependencies',
                f'({dep})'
                )
                mod.newline()
  
        mod.comment('Reducing Slaughters and Takedowns Spawns')
        if True:

            mod.comment('Reducing Space Slaughter Spawn')
            if True:

                mod.comment('Round1')
                if True:

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1a_Trooper1',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave1b_TrooperBscShtGn',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2a_Trooper',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave2b_TrprShtMleJtpk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round1/SpawnOptions_TechSlaughter_Round1Wave3b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                mod.comment('Round2')
                if True:

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave1',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,10) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave2b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,10) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave3b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,7) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round2/SpawnOptions_TechSlaughter_Round2Wave4b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                mod.comment('Round3')
                if True:

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave1b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave2b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave3b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round3/SpawnOptions_TechSlaughter_Round3Wave4a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                mod.comment('Round4')
                if True:

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave1',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,10) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave2',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,12) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,11) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave3b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,9) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round4/SpawnOptions_TechSlaughter_Round4Wave4b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                
                mod.comment('Round5')
                if True:

                    for i in range(0,7) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave1b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,7) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,7) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave2b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,9) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,11) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave3b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                    
                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave4b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                    
                    for i in range(0,9) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/TechSlaughter/Round5/SpawnOptions_TechSlaughter_Round5Wave5',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

            mod.comment('Reducing Creature Slaughter Spawn')
            if True:

                mod.comment('Round1')
                if True:

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round1/SpawnOptions_CreatureSlaughter_Round1Wave1_SKagg',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round1/SpawnOptions_CreatureSlaughter_Round1Wave2A_Skagg_Rakk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round1/SpawnOptions_CreatureSlaughter_Round1Wave2b_Skagg_Rakk1',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round1/SpawnOptions_CreatureSlaughter_Round1Wave3_Skag_Rakk_Badass',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                mod.comment('Round2')
                if True:

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave1a_Jabbermon',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave1b_JabbermonPupAdult',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave2a_JabbermonSkagg',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave2b_JabbermonSkagg',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave3a_JabbermonSkaggRakk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave3b_JabbermonRakk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round2/SpawnOptions_CreatureSlaughter_Round2Wave4a_JabbermonRakkBadasses',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                mod.comment('Round3')
                if True:

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round3/SpawnOptions_CreatureSlaughter_Round3Wave1_SpiderAnts',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round3/SpawnOptions_CreatureSlaughter_Round3Wave2_SpiderAntsVarkid',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,7) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round3/SpawnOptions_CreatureSlaughter_Round3Wave3a_SpiderAntsVarkidRakk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round3/SpawnOptions_CreatureSlaughter_Round3Wave4_SpiderAntsVarkidRakk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                mod.comment('Round4')
                if True:

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave1_Ratch',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave2a_RatchJabbermon',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave2b_RatchJabbermon1',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave3a_RatchJabbermonVarkid',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave3b_RatchJabbermonVarkid',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave4a_RatchJabbermonVarkid',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,12) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round4/SpawnOptions_CreatureSlaughter_Round4Wave4b_RatchJabbermonVarkid',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                
                mod.comment('Round5')
                if True:

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave1a_Saurian',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,2) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave1b_Saurian',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave2a_SaurianGrog',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,6) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave2b_SaurianGrog',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,5) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave3a_SaurianRakk',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave3b_SaurianRakkNekro',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave4a_Nekro',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                    
                    for i in range(0,4) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave4b_Nekro',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                    
                    for i in range(0,16) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5a',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                    
                    for i in range(0,8) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5b',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()
                    
                    for i in range(0,24) :

                        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                        '/Game/Enemies/_Spawning/Slaughters/CreatureSlaughter/Round5/SpawnOptions_CreatureSlaughter_Round5Wave5c',
                        'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                        1.0
                        )
                        mod.newline()

            mod.comment('Reducing Slaughter Shaft Spawn')
            if True:

                for i in range(0,5) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_EnforcerMix_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,5) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_GoliathMix_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,4) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_GoonMix_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,7) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PsychoMix_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,7) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PunkMix_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,2) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PunksAndEnforcers_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,2) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PunksAndPsychos_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,2) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PunksAndTinks_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()

                for i in range(0,6) :

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_TinkMix_COVSlaughter',
                    'Options.Options[{}].AliveLimitParam.Range.Value'.format(i),
                    1.0
                    )
                    mod.newline()
        
        mod.comment('Scaling the TakeDowns to be 50% Harder Than The Base Game')
        if True:

            mod.comment('TakeDown2')
            if True:

                mod.comment('Bugs Health Takedown2')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_GroundTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_GroundTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_FlyerTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_FlyerTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0

                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_HopperTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_HopperTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassTD2',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassTD2',
                    'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassTD2',
                    'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BroodlingTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BroodlingTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.3
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BomberTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BomberTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.35
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_Flyer_FodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_Flyer_FodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.25
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_GroundTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_GroundBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_HopperTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_HopperBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BroodlingTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BroodlingBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassBossFodderTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.25
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassBossFodderTD2',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassBossFodderTD2',
                    'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Nekrobug_BadassTD2_BossAdd',
                    '/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2',
                    'Nekrobug_BadassBossFodderTD2',
                    'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',1.5*
                    3.0
                    )
                    mod.newline()

                mod.comment('Guardians Health Takedown2')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SpectreTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.7
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SpectreTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.35
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SeraTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SeraTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_HeraldTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_HeraldTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithBadassTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithBadassTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBossFodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.2
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBossFodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithBossFodderTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreBossFodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SpectreBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.2
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSpectreBossFodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SpectreBossFodderTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraBossFodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SeraBossFodderTD2',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraBossFodderTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SeraBossFodderTD2',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_Reaper',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.8
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_Reaper',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_Reaper',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianReaperTD2',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_Reaper',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithTD2_LOWXP',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithTD2_LOWXP',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'BPChar_GuardianSpectreTD2_LOWXP',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.7
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'BPChar_GuardianSpectreTD2_LOWXP',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.35
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SeraTD2_LOWXP',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianSeraTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_SeraTD2_LOWXP',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_HeraldTD2_LOWXP',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianHeraldTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_HeraldTD2_LOWXP',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithBadassTD2_LOWXP',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianWraithBadassTD2_LOWXP',
                    '/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2',
                    'Guardian_WraithBadassTD2_LOWXP',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBomber',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Bomber',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBomber_BossFodder',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_BomberFodder',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.7
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteMiniboss',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Miniboss',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    35.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteMiniboss',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Miniboss',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    35.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteMiniboss',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Miniboss',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    35.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBoss',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Boss',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    55.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBoss',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Boss',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    65.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_GuardianBruteBoss',
                    '/Game/PatchDLC/Takedown2/Enemies/GuardianBrute/_Shared/_Design/Balance/Table_Balance_GuardianBrute',
                    'GuardianBrute_Boss',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    75.0
                    )
                    mod.newline()

            mod.comment('Takedown1')
            if True:

                mod.comment('Behemoths')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothMiniWalker',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_MiniWalker',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothMiniWalker',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_MiniWalker',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothGunner',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Gunner',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    12.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothGunner',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Gunner',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRocketeer',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Rocketeer',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    15.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRocketeer',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Rocketeer',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    2.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothCarrier',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Carrier',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    12.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothCarrier',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Carrier',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    12.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRaid',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Raid',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    80.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRaid',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Raid',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    80.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_BehemothRaid',
                    '/Game/PatchDLC/Raid1/Enemies/Behemoth/_Shared/_Design/Balance/Table_Balance_Behemoth',
                    'Behemoth_Raid',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    50.0
                    )
                    mod.newline()
                
                mod.comment('FrontRunners')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerBasic_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'Frontrunner',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerBasic_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'Frontrunner',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.4
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerJammer_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'GunWolf',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerJammer_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'GunWolf',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerStriker_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'Nullhound',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    2.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_FrontrunnerStriker_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'Nullhound',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Frontrunner_Badass_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'Fronttunner_Badass',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Frontrunner_Badass_Raid1',
                    '/Game/PatchDLC/Raid1/Enemies/Frontrunner/_Shared/_Design/Balance/Table_Balance_FrontrunnerRaid1',
                    'Fronttunner_Badass',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    4.0
                    )
                    mod.newline()
                
                mod.comment('Heavies')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_GunnerDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Gunner',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Pyrotech',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Pyrotech',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_PowerhouseDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Powerhouse',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_PowerhouseDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Powerhouse',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_IcebreakerDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Icebreaker',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_IcebreakerDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Icebreaker',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_AcidrainDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Acidrain',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_AcidrainDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Acidrain',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BadassDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Badass',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    10.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_Heavy_BadassDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Heavy/_Shared/_Design/Balance/Table_Balance_HeavyRaid1',
                    'Heavy_Badass',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    2.0
                    )
                    mod.newline()
                
                mod.comment('Mechs')
                if True:
                    
                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossBar',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'Mech_Raid_BossBar',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    45.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossA',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'Mech_RaidBossA',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    15.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossA',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'Mech_RaidBossA',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    10.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossB',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'Mech_RaidBossB',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    15.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossB',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'Mech_RaidBossB',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    10.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossC',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'MechRaidBossC',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    15.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_MechRaidBossC',
                    '/Game/PatchDLC/Raid1/Enemies/Mech/_Shared/_Design/Balance/Table_Balance_Mech_Raid1',
                    'MechRaidBossC',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    10.0
                    )
                    mod.newline()
                
                mod.comment('Ratches')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Larva',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.25
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchPupRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Pup',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Basic',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Basic',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Basic',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchSpitterRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Spitter',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchSpitterRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Spitter',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchSpitterRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Spitter',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Swarm',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Birther',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    3.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Birther',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Badass',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    6.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Badass',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Badass',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Hive',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    8.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Hive',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'Ratch_Hive',
                    'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',1.5*
                    5.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchPupRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'RatchEgg_Pup',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.75
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBasicRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'RatchEgg_Basic',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.2
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_RatchBadassRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Ratch/_Shared/_Design/Balance/Table_Balance_RatchRaid1',
                    'RatchEgg_Badass',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    5.0
                    )
                    mod.newline()
                
                mod.comment('Troopers')
                if True:

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Basic',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.85
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Basic',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperMedicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Medic',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    0.9
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperMedicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Medic',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperFlashDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Flash',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperFlashDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Flash',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Melee',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.2
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Melee',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperJetpackDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Jetpack',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperJetpackDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Jetpack',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Shotgun',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    2.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBasicDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Shotgun',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBadassDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Badass',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    4.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperBadassDarkRaid1',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Badass',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    1.0
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperReflectDark',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Reflect',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.2
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperReflectDark',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Reflect',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperStealthDark',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Stealth',
                    'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',1.5*
                    1.2
                    )
                    mod.newline()

                    mod.table_hotfix(Mod.CHAR,'BPChar_TrooperStealthDark',
                    '/Game/PatchDLC/Raid1/Enemies/Trooper/_Shared/_Design/Balance/Table_Balance_TrooperRaid1',
                    'Trooper_Stealth',
                    'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',1.5*
                    0.5
                    )
                    mod.newline()

        mod.comment('Scaling the Slaughters And Trials to be 25% Harder Than The Base Game')
        if True : 
            
            regions_slaughters_trials = [
                'COVSlaughter_P',
                'CreatureSlaughter_P',
                'TechSlaughter_P',
                'ProvingGrounds_Trial1_P',
                'ProvingGrounds_Trial4_P',
                'ProvingGrounds_Trial5_P',
                'ProvingGrounds_Trial6_P',
                'ProvingGrounds_Trial7_P',
                'ProvingGrounds_Trial8_P'
            ]

            for region in regions_slaughters_trials :
                
                mod.table_hotfix(Mod.LEVEL,region,
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'AI_EnemyHealthBase',
                'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
                80*1.6*1.25
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'AI_AdditionalHealthPerLevel',
                'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
                0.05*1.25
                )
                mod.newline()

    mod.comment('NVHM scales without mayhem')
    if True:

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/GameData/Regions/RegionManagerData',
        'PlayThroughs.PlayThroughs[0].bGameStageTracksPlayerLevelAboveMinimum',
        'True'
        )
        mod.newline()
    
    mod.comment('Slam can be used while jumping')
    if True:

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/GroundSlam/GroundSlamData_Beastmaster',
        'GroundSlamGrades.GroundSlamGrades[0].MinimumHeight',
        150
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/GroundSlam/GroundSlamData_Beastmaster',
        'GroundSlamGrades.GroundSlamGrades[1].MinimumHeight',
        3500
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/GroundSlam/GroundSlamData_Gunner',
        'GroundSlamGrades.GroundSlamGrades[0].MinimumHeight',
        150
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/GroundSlam/GroundSlamData_Gunner',
        'GroundSlamGrades.GroundSlamGrades[1].MinimumHeight',
        3500
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/GroundSlam/GroundSlamData_Operative',
        'GroundSlamGrades.GroundSlamGrades[0].MinimumHeight',
        150
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/Operative/_Shared/_Design/Character/GroundSlam/GroundSlamData_Operative',
        'GroundSlamGrades.GroundSlamGrades[1].MinimumHeight',
        3500
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/GroundSlam/GroundSlamData_Siren',
        'GroundSlamGrades.GroundSlamGrades[0].MinimumHeight',
        150
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/GroundSlam/GroundSlamData_Siren',
        'GroundSlamGrades.GroundSlamGrades[1].MinimumHeight',
        3500
        )
        mod.newline()

    mod.comment('Reducing The Weight of HW For COV Badasses')
    if True:
        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_COVEnemyUse_HeavyWeapons',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY\"',
                Weight=(BaseValueConstant=0.5,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'MatchAll',
        '/Game/Enemies/Punk_Female/Badass/_Design/Weapon/ItemPools/ItemPool_BadassPunk_HeavyWeapons',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY\"',
                Weight=(BaseValueConstant=0.5,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                InventoryBalanceData=/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()
 
    mod.comment('Increasing Spawn Rate of Loot Enemies')
    if True:

        mod.comment('Increasing Spawn Rate of Jabber Thieves')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix',
            'Options.Options[4].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.04
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix_NoBadass',
            'Options.Options[3].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.04
            )
            mod.newline()

        mod.comment('Increasing Spawn Rate of Shiny Grogs')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Saurian/_Mixes/SpawnOptions_SaurianMix_Wetlands_NoTyrant',
            'Options.Options[3].WeightParam.AttributeInitializationData.BaseValueScale',
            0.3
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Saurian/_Mixes/SpawnOptions_SaurianMix_Wetlands',
            'Options.Options[6].WeightParam.AttributeInitializationData.BaseValueScale',
            0.3
            )
            mod.newline()
  
        mod.comment('Increasing Spawn Rate of Loot Tinks')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_Prologue',
            'Options.Options[5].WeightParam.Range.Value',
            0.05
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_Sacrifice',
            'Options.Options[6].WeightParam.Range.Value',
            0.05
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVault',
            'Options.Options[5].WeightParam.Range.Value',
            0.05
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_Mansion1',
            'Options.Options[9].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.25
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFields',
            'Options.Options[7].WeightParam.Range.Value',
            0.3
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_Prison1',
            'Options.Options[12].WeightParam.Range.Value',
            0.15
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeFestival_FullMix',
            'Options.Options[15].WeightParam.Range.Value',
            0.2
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeInterior_FullMix',
            'Options.Options[17].WeightParam.Range.Value',
            0.2
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/SpawnOptions_CoVMix_Desert',
            'Options.Options[10].WeightParam.Range.Value',
            0.3
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_4/Crypt/SpawnOptions_CoVMix_Crypt',
            'Options.Options[7].WeightParam.Range.Value',
            0.05
            )
            mod.newline()

        mod.comment('Increasing Spawn Rate of Loot Bots')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_City',
            'Options.Options[5].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_RiseAndGrind',
            'Options.Options[3].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_Towers',
            'Options.Options[5].WeightParam.Range.Value',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ServiceBots/_Mixes/SpawnOptions_ServiceBotMix_Watereship',
            'Options.Options[6].WeightParam.Range.Value',
            0.15
            )
            mod.newline()

        mod.comment('Increasing Spawn Rate of Chubby Skags')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Skags/_Mixes/SpawnOptions_SkagFullMix',
            'Options.Options[6].WeightParam.AttributeInitializationData.BaseValueScale',
            0.1
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Skags/_Mixes/Zone0/SpawnOptions_SkagEarlyMix',
            'Options.Options[2].WeightParam.AttributeInitializationData.BaseValueConstant',
            0.05
            )
            mod.newline()
        
        mod.comment('Increasing Spawn Rate of Engorged Rakks')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Rakk/_Mixes/SpawnOptions_Rakk_MixBadasses',
            'Options.Options[2].WeightParam.AttributeInitializationData.BaseValueScale',
            2.0
            )
            mod.newline()
    
    mod.comment('Removes The Anointed Enemies')
    if True:

        mod.comment('Removes the Anointed Goliaths')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Goliaths/Variants/SpawnOptions_GoliathAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[10].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_GoliathMix_COVSlaughter',
            'Options.Options[4].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Goliath/Badass/_Design/Character/BPChar_Goliath_Badass.BPChar_Goliath_Badass_C'
            )
            mod.newline()

        mod.comment('Removes the Anointed Pyschos')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/SpawnOptions_CoVMix_WetlandsBadasses',
            'Options.Options[5].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/WetlandsVault/SpawnOptions_CoVMix_WetlandsVaultBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/SpawnOptions_CoVMix_DesertBadasses',
            'Options.Options[3].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Psychos/Variants/SpawnOptions_PsychoAnointedMale',
            'Options.Options[0].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PsychoMix_COVSlaughter',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass_C'
            )
            mod.newline()
        
        mod.comment('Removes the Anointed Punks')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_PrologueBadass',
            'Options.Options[4].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions__CoVMix_OrbitalBadasses',
            'Options.Options[5].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/SpawnOptions_CoVMix_WetlandsBadasses',
            'Options.Options[4].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/WetlandsVault/SpawnOptions_CoVMix_WetlandsVaultBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CoVMix_MineBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/SpawnOptions_CoVMix_DesertBadasses',
            'Options.Options[2].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Punks/Variants/SpawnOptions_PunkAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_PunkMix_COVSlaughter',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Punk_Female/Badass/_Design/Character/BPChar_PunkBadass.BPChar_PunkBadass_C'
            )
            mod.newline()
        
        mod.comment('Removes the Anointed Tinks')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_0/SpawnOptions_CoVMix_PrologueBadass',
            'Options.Options[5].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions__CoVMix_OrbitalBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Mansion/SpawnOptions_CoVMix_MansionBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Marshfields/SpawnOptions_CoVMix_MarshFieldsBadassess',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Tinks/_Mixes/SpawnOptions_TinkMix',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Tinks/Variants/SpawnOptions_TinkAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/ProvingGrounds/SpawnOptions_TinkBadassMix_ProvingGrounds',
            'Options.Options[2].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_TinkMix_COVSlaughter',
            'Options.Options[5].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/MarshFields/SpawnOptions_CoVMix_MarshFieldsBadassess_MudNecks',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Tink/Badass/_Design/Character/BPChar_TinkBadass.BPChar_TinkBadass_C'
            )
            mod.newline()

        mod.comment('Removes the Anointed Enforcers')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions__CoVMix_OrbitalBadasses',
            'Options.Options[7].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_CityVaultBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_1/SpawnOptions_CoVMix_TowersBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()
            
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/Prison/SpawnOptions_CotVFullMix_PrisonBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_2/WetlandsVault/SpawnOptions_CoVMix_WetlandsVaultBadasses',
            'Options.Options[6].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[11].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CoVMix_MineBadasses',
            'Options.Options[8].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Motorcade/SpawnOptions_Cotv_MotorcadeBadasses',
            'Options.Options[10].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_EnforcerMix_COVSlaughter',
            'Options.Options[4].Factory.Object..AIActorClass',
            '/Game/Enemies/Enforcer/Badass/_Design/Character/BPChar_EnforcerBadass.BPChar_EnforcerBadass_C'
            )
            mod.newline()

        mod.comment('Removes the Anointed Goons')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/DesertVault/SpawnOptions_CoVMix_DesertVaultBadasses',
            'Options.Options[12].Factory.Object..AIActorClass',
            '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/_Mixes/Zone_3/Mine/SpawnOptions_CoVMix_MineBadasses',
            'Options.Options[9].Factory.Object..AIActorClass',
            '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/CotV/Goons/Variants/SpawnOptions_GoonAnointed',
            'Options.Options[0].Factory.Object..AIActorClass',
            '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Enemies/_Spawning/Slaughters/COVSlaughter/SpawnOptions_GoonMix_COVSlaughter',
            'Options.Options[3].Factory.Object..AIActorClass',
            '/Game/Enemies/Goon/Badass/_Design/Character/BPChar_GoonBadass.BPChar_GoonBadass_C'
            )
            mod.newline()
    
    mod.comment('Removing The Gear Level Restrictions')
    if True:

        mod.comment('Makes All Manufacturer Available From lv1')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Dahl',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Jakobs',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Hyperion',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Vladof',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Tediore',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_COV',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Torgue',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Maliwan',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Atlas',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Anshin',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_Pangolin',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

        mod.comment('Makes All Elements Available From lv1')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Fire',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Cryo',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Corrosive',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Shock',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Element_Radiation',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

        mod.comment('Makes All Gear Available From lv1')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Manufacturer_ETech',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_Pistol',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_Shotgun',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_SMG',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_AssaultRifle',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_SniperRifle',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Weapon_Heavy',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Shields',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'ClassMods',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Artifacts',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'GrenadeMods',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/LootSchedule/DataTable_GameStage_Schedule',
            'Ammo',
            'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

        mod.comment('Unlocks All The Slots at lv1')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon3',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon4',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/_Data/BPInvSlot_ClassMod',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Artifacts/_Design/_Data/BPInvSlot_Artifact',
            'InitiallyEnabled',
            'True'
            )
            mod.newline()

    mod.comment('World Drops')
    if True:

        mod.comment('Legendaries')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary',
            'ValueResolver',
            "SimpleMathValueResolver'/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary.Att_RarityWeight_05_Legendary:ValueResolver_SimpleMathValueResolver'"
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary.Att_RarityWeight_05_Legendary:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Attributes/Att_GameStage.Att_GameStage,
                BaseValueScale=1
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary.Att_RarityWeight_05_Legendary:ValueResolver_SimpleMathValueResolver',
            'ValueB',
            """
            (
                BaseValueConstant=1,
                BaseValueScale=100
            )
            """
            )
            mod.newline()  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary.Att_RarityWeight_05_Legendary:ValueResolver_SimpleMathValueResolver',
            'Operator',
            'ESimpleMathValueResolverOperatorType::Divide'
            )
            mod.newline()

        mod.comment('Purples')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare',
            'ValueResolver',
            "SimpleMathValueResolver'/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare.Att_RarityWeight_04_VeryRare:ValueResolver_SimpleMathValueResolver'"
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare.Att_RarityWeight_04_VeryRare:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Attributes/Att_GameStage.Att_GameStage,
                BaseValueScale=1
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare.Att_RarityWeight_04_VeryRare:ValueResolver_SimpleMathValueResolver',
            'ValueB',
            """
            (
                BaseValueConstant=1,
                BaseValueScale=10
            )
            """
            )
            mod.newline()  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare.Att_RarityWeight_04_VeryRare:ValueResolver_SimpleMathValueResolver',
            'Operator',
            'ESimpleMathValueResolverOperatorType::Divide'
            )
            mod.newline()

        mod.comment('Blues')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare',
            'ValueResolver',
            "SimpleMathValueResolver'/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare:ValueResolver_SimpleMathValueResolver'"
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare.Att_RarityWeight_04_VeryRare,
                BaseValueScale=50
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare:ValueResolver_SimpleMathValueResolver',
            'ValueB',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Attributes/Att_GameStage.Att_GameStage,
                BaseValueScale=0.25
            )
            """
            )
            mod.newline()  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare:ValueResolver_SimpleMathValueResolver',
            'Operator',
            'ESimpleMathValueResolverOperatorType::Divide'
            )
            mod.newline()

        mod.comment('Greens')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon',
            'ValueResolver',
            "SimpleMathValueResolver'/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon.Att_RarityWeight_02_Uncommon:ValueResolver_SimpleMathValueResolver'"
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon.Att_RarityWeight_02_Uncommon:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare,
                BaseValueScale=50
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon.Att_RarityWeight_02_Uncommon:ValueResolver_SimpleMathValueResolver',
            'ValueB',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Attributes/Att_GameStage.Att_GameStage,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon.Att_RarityWeight_02_Uncommon:ValueResolver_SimpleMathValueResolver',
            'Operator',
            'ESimpleMathValueResolverOperatorType::Divide'
            )
            mod.newline()

        mod.comment('Whites')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common',
            'ValueResolver',
            "SimpleMathValueResolver'/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common.Att_RarityWeight_01_Common:ValueResolver_SimpleMathValueResolver'"
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common.Att_RarityWeight_01_Common:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon.Att_RarityWeight_02_Uncommon,
                BaseValueScale=50
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common.Att_RarityWeight_01_Common:ValueResolver_SimpleMathValueResolver',
            'ValueB',
            """
            (
                BaseValueConstant=1,
                BaseValueAttribute=/Game/GameData/Attributes/Att_GameStage.Att_GameStage,
                BaseValueScale=5.0
            )
            """
            )
            mod.newline()  

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common.Att_RarityWeight_01_Common:ValueResolver_SimpleMathValueResolver',
            'Operator',
            'ESimpleMathValueResolverOperatorType::Divide'
            )
            mod.newline()

    mod.comment('Changed The Spawn Rate of Elements on Guns')
    if True:

        mod.comment('Common Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Common',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Common',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.125

            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Common',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.125

            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Common',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.125

            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Common',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.125

            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Common',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.125

            )
            mod.newline()

        mod.comment('UnCommon Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'UnCommon',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'UnCommon',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'UnCommon',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'UnCommon',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'UnCommon',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'UnCommon',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.25
            )
            mod.newline()

        mod.comment('Rare Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Rare',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Rare',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Rare',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Rare',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Rare',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'Rare',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.5
            )
            mod.newline()

        mod.comment('VeryRare Elemental Rarity')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'VeryRare',
            'No_Element_2_5116D4D846B4D2399C40ED8DCD2C24C1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'VeryRare',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'VeryRare',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'VeryRare',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'VeryRare',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalPartRarity/DataTable_Weapon_Elemental_Rarity',
            'VeryRare',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            1.0
            )
            mod.newline()

    mod.comment('Changed Damage based on rarity')
    if True:

        mod.comment('Common Elemental Rarity, Each rarity does 20% more damage than the previous')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
            'Common',
            'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
            1.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
            'UnCommon',
            'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
            1.0*1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
            'Rare',
            'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
            1.0*1.2*1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
            'VeryRare',
            'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
            1.0*1.2*1.2
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
            'Legendary',
            'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
            1.0*1.2*1.2*1.2
            )
            mod.newline()

    mod.comment('Elements Overhaul')
    if True:

        mod.comment('Fire')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Fire_DA',
            'StackingStrategy',
            '/Game/GameData/StackingStrategy/StackingStrategy_Capped_10.StackingStrategy_Capped_10'
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale_DOT',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.4
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale',
            'Fire_7_1FDBC8F84F8FC5AB340FF5A2F6380A54',
            0.7
            )
            mod.newline()
        
        mod.comment('Shock')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Shock_DA',
            'StackingStrategy',
            '/Game/GameData/StackingStrategy/StackingStrategy_Capped_10.StackingStrategy_Capped_10'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Shock_DA',
            'AttributeEffects',
            """
            (
                (
                    AttributeData=/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.95)
                )
            """
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale_DOT',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale',
            'Shock_8_684654654B332D94359F79BEB2DB90AA',
            0.7
            )
            mod.newline()

        mod.comment('Corrosive')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Corrosive_DA',
            'StackingStrategy',
            '/Game/GameData/StackingStrategy/StackingStrategy_Capped_10.StackingStrategy_Capped_10'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Corrosive_DA',
            'AttributeEffects',
            """
            (
                (
                    AttributeData=/Game/GameData/Attributes/Damage/Att_DamageTakenMultiplier.Att_DamageTakenMultiplier,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.028)
                )
            """
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale_DOT',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale',
            'Corrosive_9_FCB69C7740260C055C8D32B7E96603D1',
            0.7
            )
            mod.newline()

        mod.comment('Radiation')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Radiation_DA',
            'StackingStrategy',
            '/Game/GameData/StackingStrategy/StackingStrategy_Capped_10.StackingStrategy_Capped_10'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/StatusEffects/StatusEffect_Radiation_DA',
            'AttributeEffects',
            """
            (
                (
                    AttributeData=/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageReceiver_CorrosiveChance.Att_StatusEffect_DamageReceiver_CorrosiveChance,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.05)
                ),
                (
                    AttributeData=/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageReceiver_FireChance.Att_StatusEffect_DamageReceiver_FireChance,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.05)
                ),
                (
                    AttributeData=/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageReceiver_RadiationChance.Att_StatusEffect_DamageReceiver_RadiationChance,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.05)
                ),
                (
                    AttributeData=/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageReceiver_ShockChance.Att_StatusEffect_DamageReceiver_ShockChance,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.05)
                ),
                (
                    AttributeData=/Game/GameData/StatusEffects/Att_CryoRateMultiplier.Att_CryoRateMultiplier,
                    ModifierType=ScaleSimple,
                    BaseModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.05)
                )
            """
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale_DOT',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.2
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale',
            'Radiation_13_2500317646FAD2F4916D158835B29E83',
            0.65
            )
            mod.newline()

        mod.comment('Cryo')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Elemental/ElementalDamageScale/DataTable_Weapon_ElementalDamage',
            'DamageScale',
            'Cryo_10_FE2073AF44E3E00A723784B1D44C2D50',
            0.8
            )
            mod.newline()

    mod.comment('Damage And Health, NVHM And TVHM (making NVH and TVHM the same')
    if True:

        mod.comment('Miscellanious')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_IO_Balance',
            'Barrel',
            'Damage_13_560366A1463D4183F137F3AB10204686',
            1.05
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
            'Vehicle_HealthScaler',
            'Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86',
            2.5
            )
            mod.newline()

        mod.comment('Increasing The Slam, Melee And Slide Damage')
        if True:

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase',
            'PlayerMeleeDamage',
            'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
            28
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase',
            'PlayerGroundSlamDamage',
            'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
            100
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase',
            'PlayerSlideDamage',
            'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
            18
            )
            mod.newline()

        mod.comment('Flesh, Shield And Armor Damage making NVHM and TVHM the same')
        if True:

            mod.comment('NVHM')
            if True:

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh',
                'NonelementalModifier',
                1.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh',
                'CorrosiveModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh',
                'CryoModifier',
                1.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh',
                'FireModifier',
                1.5
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh',
                'ShockModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh',
                'RadiationModifier',
                1
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield',
                'NonelementalModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield',
                'CorrosiveModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield',
                'CryoModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield',
                'FireModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield',
                'ShockModifier',
                2.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield',
                'RadiationModifier',
                1.5
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor',
                'NonelementalModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor',
                'CorrosiveModifier',
                1.5
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor',
                'CryoModifier',
                1.2
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor',
                'FireModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor',
                'ShockModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor',
                'RadiationModifier',
                0.8
                )
                mod.newline()

            mod.comment('TVHM')
            if True:

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh_PT2',
                'NonelementalModifier',
                1.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh_PT2',
                'CorrosiveModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh_PT2',
                'CryoModifier',
                1.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh_PT2',
                'FireModifier',
                1.5
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh_PT2',
                'ShockModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Flesh_PT2',
                'RadiationModifier',
                1.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield_PT2',
                'NonelementalModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield_PT2',
                'CorrosiveModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield_PT2',
                'CryoModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield_PT2',
                'FireModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield_PT2',
                'ShockModifier',
                2.0
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Shield_PT2',
                'RadiationModifier',
                1.5
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor_PT2',
                'NonelementalModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor_PT2',
                'CorrosiveModifier',
                1.5
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor_PT2',
                'CryoModifier',
                1.2
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor_PT2',
                'FireModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor_PT2',
                'ShockModifier',
                0.8
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers',
                'Armor_PT2',
                'RadiationModifier',
                0.8
                )
                mod.newline()

    mod.comment('Rescaling The DLC4 Bosses')
    if True:

        mod.table_hotfix(Mod.CHAR,'BPChar_TrainBoss',
        '/Alisma/Enemies/TrainBoss/_Shared/_Design/Balance/Table_Balance_TrainBoss_PT1',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        85.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'MatchBPChar_DrBenedictAll',
        '/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        30.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_DrBenedict',
        '/Alisma/Enemies/DrBenedict/_Shared/_Design/Balance/Table_Balance_DrBenedict_PT1',
        'Basic',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        18.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
        '/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss',
        'SpongeBoss',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        45.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
        '/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss',
        'SpongeBoss',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        45.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
        '/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss',
        'SpongeBoss',
        'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
        45.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
        '/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss',
        'SpongeBoss',
        'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
        45.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_SpongeBoss',
        '/Alisma/Enemies/_Unique/SpongeBoss/_Design/Balance/Table_Balance_SpongeBoss',
        'SpongeBoss',
        'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',
        45.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_DarkBrick',
        '/Alisma/Enemies/DarkVH/DarkBrick/_Design/Balance/Table_Balance_DarkBrick_PT1',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        38.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_DarkLilith',
        '/Alisma/Enemies/DarkVH/DarkLilith/_Design/Balance/Table_Balance_DarkLilith_PT1',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        45.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_DarkMordecai',
        '/Alisma/Enemies/DarkVH/DarkMordecai/_Design/Balance/Table_Balance_DarkMordecai',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        38.0    
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_Psychodin',
        '/Alisma/Enemies/Psychodin/_Shared/_Design/Balance/Table_Balance_Psychodin',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        60.0   
        )
        mod.newline()

        mod.table_hotfix(Mod.CHAR,'BPChar_Psychodin',
        '/Alisma/Enemies/Psychodin/_Shared/_Design/Balance/Table_Balance_Psychodin',
        'Basic',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        60.0   
        )
        mod.newline()

mod.comment('Mayhem Changes')
if True:

    mod.comment('UI Edit')
    if True :

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Mayhem2/UI/MayhemMenu/BPMenu_GFxMayhemMenu',
        'MayhemDescriptionText',
        'Enable Mayhem Mode for increased challenge but better Cash and Experience reward'
        )
        mod.newline()
    
    mod.comment('Anoints drop rate')
    if True :

        mod.comment('Anoints drop rate is 0% without mayhem')
        if True :

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance',
            'PlaythroughOne.BaseValueConstant',
            0.0
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance',
            'PlaythroughTwoAndBeyond.BaseValueConstant',
            0.0
            )
            mod.newline()

        mod.comment('Anoints drop rate is 25% in mayhem 1')
        if True :

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance_Mayhem_01',
            'PlaythroughOne.BaseValueConstant',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance_Mayhem_01',
            'PlaythroughTwoAndBeyond.BaseValueConstant',
            0.0
            )
            mod.newline()

        mod.comment('Anoints drop rate is 50% in mayhem 2')
        if True :

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance_Mayhem_02',
            'PlaythroughOne.BaseValueConstant',
            0.25
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance_Mayhem_02',
            'PlaythroughTwoAndBeyond.BaseValueConstant',
            0.0
            )
            mod.newline()

        mod.comment('Anoints drop rate is 100% in mayhem 3')
        if True :

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance_Mayhem_03',
            'PlaythroughOne.BaseValueConstant',
            0.5
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DropWeight/DataTable_EndGame_DropChance',
            'NoneChance_Mayhem_03',
            'PlaythroughTwoAndBeyond.BaseValueConstant',
            0.0
            )
            mod.newline()

    mod.comment('Only 3 mayhem Levels')
    if True:

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Mayhem2/MayhemModeTwo',
        'MaxMayhemLevel',
        3
        )
        mod.newline()

    mod.comment('Removing The Mayhem Scaling on Grenade And Gear')
    if True:

        mayhem_level=[
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '07',
            '08',
            '09',
            '10'
        ]

        for i in mayhem_level:
            mod.comment('Removing mayhem {} scaling on guns and grenades'.format(i))
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_{}'.format(i),
            'MayhemLevel',
            0.0
            )
            mod.newline()

            mod.comment('Removing mayhem {} scaling on guns and grenades'.format(i))
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_{}'.format(i),
            'MonetaryValueModifier.BaseValueConstant',
            1.0
            )
            mod.newline()

            mod.comment('Removing mayhem {} scaling on guns and grenades'.format(i))
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_{}'.format(i),
            'InventoryScoreModifier.BaseValueConstant',
            1.0
            )
            mod.newline()

            mod.comment('Removing mayhem {} scaling on guns and grenades // Nexus-Mistress'.format(i))
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_{}'.format(i),
            'UIStats',
            ''
            )
            mod.newline()

            mod.comment('Removing mayhem {} scaling on guns and grenades // Nexus-Mistress'.format(i))
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_{}'.format(i),
            'MayhemLevelStat',
            ''
            )
            mod.newline()

    mod.header('Removing Anoints')
    if True:

        anoints=[
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_AccuracyHandling/GPart_All_SkillEnd_AccuracyHandling',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_EleChanceDamage/GPart_All_SkillEnd_EleChanceDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_FireRateReload/GPart_All_SkillEnd_FireRateReload',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_LifeSteal/GPart_All_SkillEnd_LifeSteal',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_ProjectileSpeed/GPart_All_SkillEnd_ProjectileSpeed',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_SplashDamage/GPart_All_SkillEnd_SplashDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_UniqueEnemyDamage/GPart_All_SkillEnd_UniqueEnemyDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillStart_AddGrenade/GPart_All_SkillEnd_AddGrenade',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandLifeSteal/GPart_Beast_AttackCmd_Lifesteal',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandMovespeed/GPart_Beast_AttackCmd_Movespeed',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/Beast_Gamma_BonusRadiationDamage/GPart_BonusRadiationDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkAttackCharge/GPart_Beast_RakkCharge',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkSlag/GPart_Beast_RakkSlag',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkUsed_CritDamage/GPart_Beast_RakkCrit',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthAccuracyHandling/GPart_Beast_Stealth_AccuracyHandling',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthNova/GPart_Beast_ExitStealthNova',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_AmmoRegen/GPart_Gunner_AutoBear_AmmoRegen',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_FireDamage/GPart_Gunner_AutoBear_FireDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/EnterExit_Nova/GPart_Gunner_EnterExit_Nova',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_KillsLowerCooldown/GPart_Gunner_KillsLowerCooldown',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFireDamage/GPart_Gunner_NextMagFireDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFirerateCrit/GPart_Gunner_NextMagFirerateCrit',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagReloadHandling/GPart_Gunner_NextMagReloadHandling',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NoAmmoConsumption/GPart_Gunner_NoAmmoConsumption',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_ShieldMaxHealth/GPart_Gunner_ShieldHealthMax',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_SplashDamageIncrease/GPart_Gunner_SplashDamageIncrease',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/IBActive_ChanceGrenade/GPart_Gunner_IBGrenadeChance',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActive_StatusEffectChance/GPart_Operative_BarrierActive_StatusEffectChance',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActiveAccuracyCrit/GPart_Operative_BarrierActive_AccuracyCrit',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierDeployShieldRecharge/GPart_Operative_BarrierDeploy_ShieldRecharge',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveHealthRegen/GPart_Operative_CloneActive_HealthRegen',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveRegenAmmo/GPart_Operative_CloneActive_AmmoRegen',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapDamage/GPart_CloneSwap_WeaponDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapInstaReload/GPart_Operative_CloneSwapInstaReload',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveBonusDamage/GPart_Operative_DroneActiveBonusDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveFireRateReload/GPart_Operative_DroneActive_FireRateReload',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveMovespeed/GPart_Operative_DroneActiveMovespeed',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_EleChance/GPart_Siren_Cast_ElementalChance',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_WeaponDamage/GPart_Siren_Cast_WeaponDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_AccuracyCrit/GPart_Siren_Grasp_AccuracyCrit',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_ChargeSpeed/GPart_Siren_Grasp_ChargeSpeed',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_ConstantNova/GPart_Siren_Grasp_ConstantNova',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/SkillEnd_AttunedEleDamage/GPart_Siren_SkillEnd_AttunedSkillDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_DamageReduction/GPart_Siren_Slam_DamageReduction',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_MeleeDamage/GPart_Siren_Slam_MeleeDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_ReturnDamage/GPart_Siren_Slam_ReturnDamage',
            '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_WeaponDamage/GPart_Siren_Slam_WeaponDamage',
            '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/ConsecutiveHits_DmgStack/GPart_EG_Generic_ConsecutiveHitsDmgStack',
            '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/KillStack_ReloadDamage/GPart_EG_Generic_KillStackReloadDamage',
            '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/LowHealth_Executor/GPart_EG_Generic_LowHealthExecutor',
            '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/ModeSwitch_WeaponDamage/GPart_EG_ModeSwitch_WeaponDamage',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/AccuracyAndHandling/GPart_EG_WhileAirborn_AccuracyHandling',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/CritDamage/GPart_EG_WhileAirborn_CritDamage',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/Damage/GPart_EG_WhileAirborn_Damage',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/FireRate/GPart_EG_WhileAirborn_FireRate',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/AccuracyAndHandling/GPart_EG_WhileSliding_AccuracyHandling',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/Damage/GPart_EG_WhileSliding_Damage',
            '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/FireRate/GPart_EG_WhileSliding_FireRate',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_All_CritStatusEffects/GPart_Passive_All_CritStatusEffect',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_ShieldBreakAmp/GPart_All_ShieldBreakAmp',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_SlideRegenShields/GPart_All_SlideRegenShields',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_CyberSpike/GPart_EG_Gen_SkillEnd_CyberSpike',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_DamageMitigation/GPart_All_DamageMitigation',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_GrenadeDamage/GPart_All_GrenadeDamage',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_PulseNova/GPart_EG_Gen_SkillActive_PulseFireNova',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_ShockFeedback/GPart_All_ShockFeedback',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_UniqueEnemyDamage/GPart_All_UniqueEnemyDamage',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillEnd_HealingPool/GPart_All_HealingPool',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillStart_ShieldRecharge/GPart_All_SkillStart_OverchargeShield',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror1/GPart_All_Passive_GenerateTerror_Melee',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror10/GPart_All_SkillEnd_GenerateTerror',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror11/GPart_All_SkillEnd_TerrorHeal',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror12/GPart_All_Passive_TerrorAccuracy',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror2/GPart_All_Passive_TerrorDamageFireRate',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror3/GPart_All_Passive_TerrorAmmoRegen',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror4/GPart_All_Passive_TerrorBonus_CryoDamage',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror5/GPart_All_Passive_TerrorBulletReflect',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror6/GPart_All_Passive_TerrorCritDamage',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror7/GPart_All_Passive_TerrorDamageMitigation',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror8/GPart_All_Passive_TerrorHealthRegen',
            '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/EndGameParts/_Generic/Terror9/GPart_All_Passive_TerrorProjectilesPerShot'
            '/Game/BloodyHarvest/Gear/Weapons/EndGameParts/Character/Beastmaster/AtkCmdTerrorFireDmg/GPart_Beast_AttackCmd_TerrorFireDMG',
            '/Game/BloodyHarvest/Gear/Weapons/EndGameParts/Character/Gunner/ReloadTerrorNova/GPart_Gunner_Reload_TerrorNova',
            '/Game/BloodyHarvest/Gear/Weapons/EndGameParts/Character/OP1/GPart_Operative_DroneActiveTerrorLifesteal',
            '/Game/BloodyHarvest/Gear/Weapons/EndGameParts/Character/Siren/Grasp_TerrorSkulls/GPart_Siren_Grasp_TerrorSkulls',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_SlideRegenShields/GPart_All_SlideRegenShields',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillEnd_HealingPool/GPart_All_HealingPool',
            '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_DamageMitigation/GPart_All_DamageMitigation',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Beast/FadeActiveWeaponDamage/GPart_Beast_FadeActiveDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Beast/GravitySnareDamage/GPart_Beast_GravitySnareActiveDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/BearFistDamage/GPart_Gunner_BearFistDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/IronCubDamage/GPart_Gunner_IronCubActiveDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/MinigunDamage/GPart_Gunner_MinigunDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/RailgunDamage/GPart_Gunner_RailgunDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/SalamanderDamage/GPart_Gunner_SalamanderDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/V35LauncherDamage/GPart_Gunner_V35LauncherDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Gunner/VanquisherDamage/GPart_Gunner_VanquisherDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/OP1/MNTISDamage/GPart_Operative_MNTISDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Siren/PhasecastDamage/GPart_Siren_PhasecastDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Siren/PhaseflareDamage/GPart_Siren_PhaseflareDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Siren/PhasegraspDamage/GPart_Siren_GraspActiveDamage',
            '/Game/PatchDLC/Ixora/Gear/Weapons/EndGameParts/Siren/PhaseslamDamage/GPart_Siren_PhaseslamDamage'
        ]

        for anoint in anoints:
            mod.comment('Removing Anoint from Pool')
            mod.reg_hotfix(Mod.PATCH,'',
            anoint,
            'MinGameStage',
            '(BaseValueConstant=100.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)'
            )
            mod.newline()

    mod.header('Scaling Anoints Down')
    if True:

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_WeaponDamage',
        'Damage_7_39142BF947B2CBE02701DBA97A4D507F',
        0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_CritDamage',
        'Damage_7_39142BF947B2CBE02701DBA97A4D507F',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_MeleeDamage',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_MoveSpeed',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.1
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_CooldownRate',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.3
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_HealthRegen',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.05
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/DataTable_EndGameParts',
        'All_ActionSkillEnd_NextMagBonusDamage',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.2
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/Gear/Anointed/DataTable_Raid1_Endgame',
        'ActionSkillStarted_BonusEleDamage',
        'Damage_7_39142BF947B2CBE02701DBA97A4D507F',
        0.1
        )
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Cryo/UIStat_EG_SkillEndBonusEleDamage_Cryo',
        'FormatText',
        "[endgame]On [endgamebold]Action Skill End[/endgamebold], gain $VALUE$ bonus Cryo Damage with Weapons for 10 seconds.[/endgame]"
        )
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Fire/UIStat_EG_SkillEndBonusEleDamage_Fire',
        'FormatText',
        "[endgame]On [endgamebold]Action Skill End[/endgamebold], gain $VALUE$ bonus Fire Damage with Weapons for 10 seconds.[/endgame]"
        )
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Shock/UIStat_EG_SkillEndBonusEleDamage_Shock',
        'FormatText',
        "[endgame]On [endgamebold]Action Skill End[/endgamebold], gain $VALUE$ bonus Shock Damage with Weapons for 10 seconds.[/endgame]"
        )
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Radiation/UIStat_EG_SkillEndBonusEleDamage_Radiation',
        'FormatText',
        "[endgame]On [endgamebold]Action Skill End[/endgamebold], gain $VALUE$ bonus Radiation Damage with Weapons for 10 seconds.[/endgame]"
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/Gear/Anointed/DataTable_Raid1_Endgame',
        'GrenadeThrow_GlobalDamage',
        'Damage_7_39142BF947B2CBE02701DBA97A4D507F',
        0.15
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/DataTable_EndGameParts_Event2',
        'All_ActionSkillActive_GrenadeDamage',
        'Damage_7_39142BF947B2CBE02701DBA97A4D507F',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/DataTable_EndGameParts_Event2',
        'All_ActionSkillActive_WeaponDamage',
        'Damage_7_39142BF947B2CBE02701DBA97A4D507F',
        0.2
        )
        mod.newline()
        
        mod.table_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/DataTable_EndGameParts_Event2',
        'Passive_HighHealthBreaker',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.5
        )
        mod.newline()

        mod.table_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/DataTable_EndGameParts_Event2',
        'Passive_UnhealthyRadDamage',
        'Custom_A_21_F62C55A14374986C5D004E94DD277B3D',
        0.3
        )
        mod.newline()

    mod.header('Mayhem Scaling')
    if True:

        set_to_0=[
        "DropNumberChanceSimpleScalar_40_115637764B3918F01E6FAFADDC005388",
        "LootQuality_56_03E220E0495C6B37CD6C7195F5EA289B"
        ]

        set_to_1=[
            "DamageScalarActionSkill_60_39AF483140740A38FC71BA897155CBFF",
            "DamageScalarMelee_67_9948929F4FF34364CED2EAB51A881946",
            "DamageScalarSlide_68_B48D0E3A4DF57196839BB58D5AE3E638",
            "DamageScalarSlam_69_15DB6EDC4CCA52620BF25398CFFD9B26",
            "DamageScalarPet_72_0DD7977D44C4A71D0A6B56B7884E023C",
            "DamageScalarEnviornmental_111_E2A582AA47FC000789FC68BBD31D2CFC",
            "DamageScalarPassive_115_6A30229E4CC04F751ED01CB64A71880F",
            "DamageDealtScalarVehicles_103_5739171948322B35CDA36487F78AF0CE",
            "DamageTakenScalarVehicles_104_B75AB4EC482624FDEAAF31B0FA369A77",
            "DamageScalarGear_119_9FC89117424C6619F2CA958FA2842FC2",
            "PetHealth_84_E5B903B4452F4310CCD13C931474E12B",
            "CompanionHealth_89_294A6BE7439072AE9F934CAA127D8D83",
            "DropWeightCommonScalar_21_59A2FB124E32B955768A7B9D93C25A99",
            "DropWeightUncommonScalar_25_809615334E7F0DB3B8712DAC221015C3",
            "DropWeightVeryRareScalar_29_F2CA570046CD50A7C514EDB0AE1BE591",
            "DropWeightLegendaryScalar_31_D9DA03C54065EA981BE218B11942C24E"
        ]

        mayhem_health = [
            "HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68",
            "ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6",
            "ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8"
        ]

        mayhem_loot = [ 
            "ExpGainScalar_39_2159F009466933AA733AE688E55B1B93",
            "CashScalar_22_B7B11DC94BBB45C94A96279146EC193E",
            "DropEridiumChanceSimpleScalar_41_E89AD7E9473FDF3CBED395BA6641FA68"
        ]


        for i in range(1,12):
            for one in set_to_1:
                mod.comment('Removing all the mayhem scalings')
                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '{}'.format(i),
                one,
                1.0
                )
                mod.newline()

            for zero in set_to_0:
                mod.comment('Removing all the mayhem scalings')
                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '{}'.format(i),
                zero,
                0.0
                )
                mod.newline()

        mod.comment('Mayhem 1')
        if True :

            for health in mayhem_health :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '1',
                health,
                1.5
                )
                mod.newline()
            
            for loot in mayhem_loot :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '1',
                loot,
                1.25
                )
                mod.newline()

        mod.comment('Mayhem 2')
        if True :

            for health in mayhem_health :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '2',
                health,
                2.0
                )
                mod.newline()
            
            for loot in mayhem_loot :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '2',
                loot,
                1.5
                )
                mod.newline()
        
        mod.comment('Mayhem 3')
        if True :

            for health in mayhem_health :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '3',
                health,
                4.0
                )
                mod.newline()
            
            for loot in mayhem_loot :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
                '3',
                loot,
                2.0
                )
                mod.newline()

    mod.header('Removing modifiers')
    if True:
        
        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_EAsy.ModSet_Mayhem2_EAsy',
        'ModifierSets',
        """
        (
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/PartyTime/Ability_Mayhem2_PartyTime.Ability_Mayhem2_PartyTime_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/AimForTheSky/Ability_Mayhem2_AimForTheSky.Ability_Mayhem2_AimForTheSky_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/RoidRage/Ability_Mayhem2_RoidRage.Ability_Mayhem2_RoidRage_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/SoulStealer/Ability_Mayhem2_SoulStealer.Ability_Mayhem2_SoulStealer_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Shared/Bighetti/Ability_Mayhem2_Bighetti.Ability_Mayhem2_Bighetti_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/FinishThem/Ability_Mayhem2_FinishThem.Ability_Mayhem2_FinishThem_C,
                Weight=(BaseValueConstant=0)
            )
        )
        """)
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Medium.ModSet_Mayhem2_Medium',
        'ModifierSets',
        """
        (
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/FloorIsLava/Ability_Mayhem2_FLoorIsLava.Ability_Mayhem2_FloorIsLava_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/FrozenPulse/Ability_Mayhem2_FrozenPulse.Ability_Mayhem2_FrozenPulse_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/Rally/Ability_Mayhem2_Rally.Ability_Mayhem2_Rally_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/OlSwitcheroo/Ability_Mayhem2_OlSwitcheroo.Ability_Mayhem2_OlSwitcheroo_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Corrosive.Ability_Mayhem2_ElementalInfusion_Corrosive_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Cryo.Ability_Mayhem2_ElementalInfusion_Cryo_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Fire.Ability_Mayhem2_ElementalInfusion_Fire_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Radiation.Ability_Mayhem2_ElementalInfusion_Radiation_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Shock.Ability_Mayhem2_ElementalInfusion_Shock_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/HealNo/Ability_Mayhem2_HealNo.Ability_Mayhem2_HealNo_C,
                Weight=(BaseValueConstant=0)
            )
        )
        """)
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Hard.ModSet_Mayhem2_Hard',
        'ModifierSets',
        """
        (
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ChainGang/Ability_Mayhem2_ChainGang.Ability_Mayhem2_ChainGang_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ArcaneEnchanter/Ability_Mayhem2_ArcaneEnchanter.Ability_Mayhem2_ArcaneEnchanter_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/DroneBuddy/Ability_Mayhem2_DroneBuddy.Ability_Mayhem2_DroneBuddy_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/EleBreaker/Ability_Mayhem2_Ele_Breaker.Ability_Mayhem2_Ele_Breaker_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/StayBack/Ability_Mayhem2_StayBack.Ability_Mayhem2_StayBack_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/BegoneDot/Ability_Mayhem2_BegoneDot.Ability_Mayhem2_BegoneDot_C,
                Weight=(BaseValueConstant=0)
            )
        )
        """)
        mod.newline()

        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard.ModSet_Mayhem2_VeryHard',
        'ModifierSets',
        """
        (
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/DeathFromBeyond/Ability_Mayhem2_DeathFromBeyond.Ability_Mayhem2_DeathFromBeyond_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/RogueLite/Ability_Mayhem2_RogueLite.Ability_Mayhem2_RogueLite_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/CriticalFailure/Ability_Mayhem2_CritFail.Ability_Mayhem2_CritFail_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/Sharpshot/Ability_Mayhem2_Sharpshot.Ability_Mayhem2_Sharpshot_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/PriorityTarget/Ability_Mayhem2_PriorityTarget.Ability_Mayhem2_PriorityTarget_C,
                Weight=(BaseValueConstant=0)
            ),
            (
                ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_All.Ability_Mayhem2_ElementalInfusion_All_C,
                Weight=(BaseValueConstant=0)
            )
        )
        """)
        mod.newline()

mod.comment('Mission Rewards')
if True:

    mod.comment('Pandora')
    if True:   

        mod.comment('1st Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Default__Mission_Ep01_ChildrenOfTheVault_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_01_Common.ItemPool_GrenadeMods_01_Common"'
            """
            )
            mod.newline()
        
        mod.comment('2nd Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep02_Sacrifice.Default__Mission_Ep02_Sacrifice_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Rare.ItemPool_Guns_Rare"'
            """
            )
            mod.newline()

        mod.comment('3rd Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep03_GetVaultMap.Default__Mission_Ep03_GetVaultMap_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()
        
        mod.comment('4th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep04_EarnSpaceship.Default__Mission_Ep04_EarnSpaceship_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_03_Rare.ItemPool_Shields_03_Rare"'
            """
            )
            mod.newline()
        
        mod.comment('17th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep17_BigChase.Default__Mission_Ep17_BigChase_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('18th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep19_MinerDetails.Default__Mission_Ep19_MinerDetails_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_03_Rare.ItemPool_GrenadeMods_03_Rare"'
            """
            )
            mod.newline()

        mod.comment('19th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep16_DesertVault.Default__Mission_Ep16_DesertVault_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_04_VeryRare.ItemPool_Shields_04_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('20th Main Mission')
        if True: 

            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep20_FirstVaultHunter.Default__Mission_Ep20_FirstVaultHunter_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_03_Rare.ItemPool_GrenadeMods_03_Rare"'
            """
            )
            mod.newline()

    mod.comment('Sanctuary')
    if True:

        mod.comment('5th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep05_Sanctuary.Default__Mission_Ep05_Sanctuary_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_03_Rare.ItemPool_GrenadeMods_03_Rare"'
            """
            )
            mod.newline()

    mod.comment('Promethea / Athenas / Skywell')
    if True:

        mod.comment('6th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep05_OvercomeHQBlockade.Default__Mission_Ep05_OvercomeHQBlockade_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('7th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep06_MeetMaya.Default__Mission_Ep06_MeetMaya_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_04_VeryRare.ItemPool_Shields_04_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('8th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep08_OrbitalPlatform.Default__Mission_Ep08_OrbitalPlatform_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_04_VeryRare.ItemPool_GrenadeMods_04_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('9th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/MIssion_Ep09_AtlasHQ.Default__MIssion_Ep09_AtlasHQ_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()
        
        mod.comment('10th Main Mission // Vault Monster')
        if True:  
            
            mod.comment('Mission reward // add unique reward here')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep10_CityVault.Default__Mission_Ep10_CityVault_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()

    mod.comment('Eden 6')
    if True:

        mod.comment('11th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep11_PrisonBreak.Default__Mission_Ep11_PrisonBreak_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_04_VeryRare.ItemPool_GrenadeMods_04_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('12th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep12_GrandTour.Default__Mission_Ep12_GrandTour_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_04_VeryRare.ItemPool_Shields_04_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('13th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep13_JakobsRebellion.Default__Mission_Ep13_JakobsRebellion_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Rare.ItemPool_Guns_Rare"'
            """
            )
            mod.newline()

        mod.comment('14th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep13_Watership.Default__Mission_Ep13_Watership_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()
        
        mod.comment('15th Main Mission')
        if True:  
            
            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep15_MarshFields.Default__Mission_Ep15_MarshFields_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_03_Rare.ItemPool_GrenadeMods_03_Rare"'
            """
            )
            mod.newline()

        mod.comment('16th Main Mission // Vault Monster')
        if True:  
            
            mod.comment('Mission reward // add unique reward here')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep16_SiblingRivalry.Default__Mission_Ep16_SiblingRivalry_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_04_VeryRare.ItemPool_Shields_04_VeryRare"'
            """
            )
            mod.newline()

    mod.comment('Nekrotafeyo')
    if True:

        mod.comment('21th Main Mission')
        if True: 

            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep21_Beachhead.Default__Mission_Ep21_Beachhead_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_VeryRare.ItemPool_Guns_VeryRare"'
            """
            )
            mod.newline()

        mod.comment('22nd Main Mission')
        if True: 

            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep22_TheMachine.Default__Mission_Ep22_TheMachine_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_03_Rare.ItemPool_GrenadeMods_03_Rare"'
            """
            )
            mod.newline()

        mod.comment('23rd Main Mission')
        if True: 

            mod.comment('Mission reward')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Missions/Plot/Mission_Ep23_TyreenFinalBoss.Default__Mission_Ep23_TyreenFinalBoss_C:RewardData_OakMissionRewardData',
            'ItemPoolReward',
            """
            ItemPoolData'"/Game/GameData/Loot/ItemPools/Eridium/ItemPool_EridiumCrystal_Large.ItemPool_EridiumCrystal_Large"'
            """
            )
            mod.newline()

COV_AR_Bateman_BALANCE=[
    [
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/EPartList_COV_AR.EPartList_COV_AR'
    ],
    [
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/InvPartSet_AR_COV_KriegeAR.InvPartSet_AR_COV_KriegeAR'
    ],
    [
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Body/Part_AR_COV_Body.Part_AR_COV_Body',
    ],
    [
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Body/Part_AR_COV_Bottle.Part_AR_COV_Bottle',
    ],
    [
        [
            2
        ],
        [
            2
        ],
        [ 
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Body/Part_AR_COV_Body_A.Part_AR_COV_Body_A',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Body/Part_AR_COV_Body_B.Part_AR_COV_Body_B'
        ]
        
    ],
    [
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage.Part_AR_COV_Barrel_HeatDamage'
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_COV_Barrel_01.Part_AR_COV_Barrel_01',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_COV_Barrel_02.Part_AR_COV_Barrel_02',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_COV_Barrel_03.Part_AR_COV_Barrel_03'
        ]
    ],
    [
        [
            1
        ],
        [
            3
        ],
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_COV_Barrel_01_A.Part_AR_COV_Barrel_01_A',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_COV_Barrel_01_B.Part_AR_COV_Barrel_01_B',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_01/Part_AR_COV_Barrel_01_C.Part_AR_COV_Barrel_01_C',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_COV_Barrel_02_A.Part_AR_COV_Barrel_02_A',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_COV_Barrel_02_B.Part_AR_COV_Barrel_02_B',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_02/Part_AR_COV_Barrel_02_C.Part_AR_COV_Barrel_02_C',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_COV_Barrel_03_A.Part_AR_COV_Barrel_03_A',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_COV_Barrel_03_B.Part_AR_COV_Barrel_03_B',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Barrel/Barrel_03/Part_AR_COV_Barrel_03_C.Part_AR_COV_Barrel_03_C'
        ]        
    ],
    [ 
        [
            1
        ],
        [
            1
        ],      
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Starter/Part_AR_COV_Starter_01.Part_AR_COV_Starter_01',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Starter/Part_AR_COV_Starter_02.Part_AR_COV_Starter_02',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Starter/Part_AR_COV_Starter_03.Part_AR_COV_Starter_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Grip/Part_AR_COV_Grip_01.Part_AR_COV_Grip_01',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Grip/Part_AR_COV_Grip_02.Part_AR_COV_Grip_02',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Grip/Part_AR_COV_Grip_03.Part_AR_COV_Grip_03',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Grip/Part_AR_COV_Grip_04.Part_AR_COV_Grip_04'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Foregrip/Part_AR_COV_Foregrip_01.Part_AR_COV_Foregrip_01',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Foregrip/Part_AR_COV_Foregrip_02.Part_AR_COV_Foregrip_02',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Foregrip/Part_AR_COV_Foregrip_03.Part_AR_COV_Foregrip_03',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Foregrip/Part_AR_COV_Foregrip_04.Part_AR_COV_Foregrip_04'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Scope/Part_AR_COV_Scope_01.Part_AR_COV_Scope_01',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Scope/Part_AR_COV_Scope_02.Part_AR_COV_Scope_02',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Scope/Part_AR_COV_Scope_03.Part_AR_COV_Scope_03',
            ''
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Elemental/Part_AR_COV_Ele_Corr.Part_AR_COV_Ele_Corr',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Elemental/Part_AR_COV_Ele_Cryo.Part_AR_COV_Ele_Cryo',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Elemental/Part_AR_COV_Ele_Fire.Part_AR_COV_Ele_Fire',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Elemental/Part_AR_COV_Ele_Radiation.Part_AR_COV_Ele_Radiation',
            '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/Parts/Elemental/Part_AR_COV_Ele_Shock.Part_AR_COV_Ele_Shock'
        ]
    ],
    [
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Part_AR_COV_Material_KriegAR.Part_AR_COV_Material_KriegAR'
    ]
]

TED_GR_Comet_BALANCE=[
    [
        '/Game/Gear/GrenadeMods/_Design/A_Data/EPartList_GrenadeMod.EPartList_GrenadeMod'
    ],
    [
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball.InvBalD_GM_TED_Fastball',
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/PartSet_GM_Fastball.PartSet_GM_Fastball'
    ],
    [
        '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Manufacturer/GM_Part_Manufacturer_07_Tediore.GM_Part_Manufacturer_07_Tediore',
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            1
        ],
        [ 
            [
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_01_Normal.GM_Part_Element_01_Normal',
                0.5
            ],
            [
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_02_Fire.GM_Part_Element_02_Fire',
                0.3
            ],
            [
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_03_Shock.GM_Part_Element_03_Shock',
                0.3
            ],
            [
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_04_Corrosive.GM_Part_Element_04_Corrosive',
                0.3
            ],
            [
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_05_Cryo.GM_Part_Element_05_Cryo',
                0.3
            ],
            [
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_06_Radiation.GM_Part_Element_06_Radiation',
                0.3
            ]  
        ] 
    ],
    [
        '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Rarity/GM_Part_Rarity_03_Rare.GM_Part_Rarity_03_Rare'
    ],
    [
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Parts/Part_GM_Aug_Fastball.Part_GM_Aug_Fastball'
    ],
    [
        [
            2
        ],
        [
            2
        ],
        [
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/GM_Part_Behavior_NONE.GM_Part_Behavior_NONE',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/GM_Part_Behavior_NONE.GM_Part_Behavior_NONE',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Roider/GM_Part_Behavior_23_Roider.GM_Part_Behavior_23_Roider',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Roider/GM_Part_Behavior_23_Roider.GM_Part_Behavior_23_Roider',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Bouncy/GM_Part_Behavior_03_Bouncy.GM_Part_Behavior_03_Bouncy',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Bouncy/GM_Part_Behavior_03_Bouncy.GM_Part_Behavior_03_Bouncy',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Spring/GM_Part_Behavior_15_Spring.GM_Part_Behavior_15_Spring',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Spring/GM_Part_Behavior_15_Spring.GM_Part_Behavior_15_Spring',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/MIRV/GM_Part_Behavior_06_MIRV.GM_Part_Behavior_06_MIRV',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/MIRV/GM_Part_Behavior_06_MIRV.GM_Part_Behavior_06_MIRV',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Divider/GM_Part_Behavior_22_Divider.GM_Part_Behavior_22_Divider',
            '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Divider/GM_Part_Behavior_22_Divider.GM_Part_Behavior_22_Divider'
        ]
    ],
    [
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Parts/Part_GM_Material_Fastball.Part_GM_Material_Fastball'
    ]
]

JAK_PS_Triolet_BALANCE=[
    [
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Pistol.EPartList_Jakobs_Pistol'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/InvPartSet_PS_JAK_DOC.InvPartSet_PS_JAK_DOC'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Body/Part_PS_JAK_Body.Part_PS_JAK_Body',
    ],
    [
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Body/Part_PS_JAK_Speedloader.Part_PS_JAK_Speedloader',
    ],
    [
        [
            2
        ],
        [
            2
        ],
        [ 
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Body/Part_PS_JAK_Body_A.Part_PS_JAK_Body_A',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Body/Part_PS_JAK_Body_B.Part_PS_JAK_Body_B',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Body/Part_PS_JAK_Body_C.Part_PS_JAK_Body_C'
        ]
        
    ],
    [
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc.Part_PS_JAK_Barrel_Doc'
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_JAK_Barrel_01.Part_PS_JAK_Barrel_01',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_JAK_Barrel_02.Part_PS_JAK_Barrel_02',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_JAK_Barrel_03.Part_PS_JAK_Barrel_03'
        ]
    ],
    [
        [
            1
        ],
        [
            3
        ],
        [
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_JAK_Barrel_01_A.Part_PS_JAK_Barrel_01_A',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_JAK_Barrel_01_B.Part_PS_JAK_Barrel_01_B',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_JAK_Barrel_01_C.Part_PS_JAK_Barrel_01_C',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_JAK_Barrel_01_D.Part_PS_JAK_Barrel_01_D',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_JAK_Barrel_02_A.Part_PS_JAK_Barrel_02_A',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_JAK_Barrel_02_B.Part_PS_JAK_Barrel_02_B',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_JAK_Barrel_02_C.Part_PS_JAK_Barrel_02_C',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_JAK_Barrel_03_A.Part_PS_JAK_Barrel_03_A',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_JAK_Barrel_03_B.Part_PS_JAK_Barrel_03_B',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_JAK_Barrel_03_C.Part_PS_JAK_Barrel_03_C',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_JAK_Barrel_03_D.Part_PS_JAK_Barrel_03_D'
        ]        
    ],
    [ 
        [
            1
        ],
        [
            1
        ], 
        [
            1
        ],      
        [
            [
                '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Grip/Part_PS_JAK_Grip_01.Part_PS_JAK_Grip_01',
                1.0
            ],
            [
                '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Grip/Part_PS_JAK_Grip_02.Part_PS_JAK_Grip_02',
                1.0
            ],
            [
                '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Grip/Part_PS_JAK_Grip_03.Part_PS_JAK_Grip_03',
                1.0
            ],
            [
                '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Grip/Part_PS_JAK_Grip_04.Part_PS_JAK_Grip_04',
                0.3
            ]
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Hammer/Part_PS_JAK_Hammer_01.Part_PS_JAK_Hammer_01',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Hammer/Part_PS_JAK_Hammer_02.Part_PS_JAK_Hammer_02',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Hammer/Part_PS_JAK_Hammer_03.Part_PS_JAK_Hammer_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Mag/Part_PS_JAK_Mag_01.Part_PS_JAK_Mag_01',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Mag/Part_PS_JAK_Mag_02.Part_PS_JAK_Mag_02',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Mag/Part_PS_JAK_Mag_03.Part_PS_JAK_Mag_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Rail/Part_PS_JAK_Rail_01.Part_PS_JAK_Rail_01',
            ''
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Scope/Part_PS_JAK_Scope_01.Part_PS_JAK_Scope_01',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Scope/Part_PS_JAK_Scope_02.Part_PS_JAK_Scope_02',
            '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Scope/Part_PS_JAK_Scope_03.Part_PS_JAK_Scope_03'
        ]
    ],
    [
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Material_Doc.Part_PS_JAK_Material_Doc'
    ]
]

TED_SG_Horn_BALANCE=[
    [
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/EPartList_SG_TED.EPartList_SG_TED'
    ],
    [
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/PartSet_SG_TED_Sludge.PartSet_SG_TED_Sludge'
    ],
    [
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Body/Part_SG_TED_Body.Part_SG_TED_Body',
    ],
    [
        [
            2
        ],
        [
            3
        ],
        [ 
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Body/Part_SG_TED_Body_A.Part_SG_TED_Body_A',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Body/Part_SG_TED_Body_B.Part_SG_TED_Body_B',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Body/Part_SG_TED_Body_C.Part_SG_TED_Body_C'
        ]
        
    ],
    [
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Barrel_Sludge.Part_SG_TED_Barrel_Sludge'
    ],
    [
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Tediore/Part_SG_TED_Barrel_ETECH_A.Part_SG_TED_Barrel_ETECH_A'
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Grip/Part_SG_TED_Grip_01.Part_SG_TED_Grip_01',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Grip/Part_SG_TED_Grip_02.Part_SG_TED_Grip_02',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Grip/Part_SG_TED_Grip_03.Part_SG_TED_Grip_03',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Grip/Part_SG_TED_Grip_04.Part_SG_TED_Grip_04',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Grip/Part_SG_TED_Grip_05.Part_SG_TED_Grip_05'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/ForeGrip/Part_SG_TED_ForeGrip_01.Part_SG_TED_ForeGrip_01',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/ForeGrip/Part_SG_TED_ForeGrip_02.Part_SG_TED_ForeGrip_02',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/ForeGrip/Part_SG_TED_ForeGrip_03.Part_SG_TED_ForeGrip_03',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/ForeGrip/Part_SG_TED_ForeGrip_04.Part_SG_TED_ForeGrip_04',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/ForeGrip/Part_SG_TED_ForeGrip_05.Part_SG_TED_ForeGrip_05'
        ]        
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Scope/Part_SG_TED_Scope_01.Part_SG_TED_Scope_01',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Scope/Part_SG_TED_Scope_02.Part_SG_TED_Scope_02',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Scope/Part_SG_TED_Scope_03.Part_SG_TED_Scope_03',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Scope/Part_SG_TED_Scope_04.Part_SG_TED_Scope_04'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/TypeMod/Part_SG_TED_TypeMod_01.Part_SG_TED_TypeMod_01',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/TypeMod/Part_SG_TED_TypeMod_02.Part_SG_TED_TypeMod_02',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/TypeMod/Part_SG_TED_TypeMod_03.Part_SG_TED_TypeMod_03',
            '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/TypeMod/Part_SG_TED_TypeMod_04.Part_SG_TED_TypeMod_04'
        ]
    ],
    [
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Parts/Elemental/Part_SG_TED_Ele_Corr.Part_SG_TED_Ele_Corr'
    ],
    [
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Material_Sludge.Part_SG_TED_Material_Sludge'
    ]
]

MAL_SR_Sun_BALANCE=[
    [
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/EPartList_MAL_SR.EPartList_MAL_SR'
    ],
    [
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/PartSet_MAL_SR_ASMD.PartSet_MAL_SR_ASMD'
    ],
    [
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Body/Part_MAL_SR_Body.Part_MAL_SR_Body',
    ],
    [
        [
            2
        ],
        [
            3
        ],
        [ 
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Body/Part_MAL_SR_Body_A.Part_MAL_SR_Body_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Body/Part_MAL_SR_Body_B.Part_MAL_SR_Body_B',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Body/Part_MAL_SR_Body_C.Part_MAL_SR_Body_C'
        ]        
    ],
    [
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD.Part_MAL_SR_Barrel_ASMD'
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03'
        ]
    ],
    [
        [
            1
        ],
        [
            3
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01_A.Part_MAL_SR_Barrel_01_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01_B.Part_MAL_SR_Barrel_01_B',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01_C.Part_MAL_SR_Barrel_01_C',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02_A.Part_MAL_SR_Barrel_02_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02_B.Part_MAL_SR_Barrel_02_B',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02_C.Part_MAL_SR_Barrel_02_C',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03_A.Part_MAL_SR_Barrel_03_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03_B.Part_MAL_SR_Barrel_03_B',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03_C.Part_MAL_SR_Barrel_03_C'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_01.Part_MAL_SR_Grip_01',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_02.Part_MAL_SR_Grip_02',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_03.Part_MAL_SR_Grip_03',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_04.Part_MAL_SR_Grip_04',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_05.Part_MAL_SR_Grip_05',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_06.Part_MAL_SR_Grip_06',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_07.Part_MAL_SR_Grip_07'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_02_A.Part_MAL_SR_Grip_02_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_03_A.Part_MAL_SR_Grip_03_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Grip/Part_MAL_SR_Grip_05_A.Part_MAL_SR_Grip_05_A'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Foregrip/Part_MAL_SR_Foregrip_01.Part_MAL_SR_Foregrip_01',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Foregrip/Part_MAL_SR_Foregrip_02.Part_MAL_SR_Foregrip_02',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Foregrip/Part_MAL_SR_Foregrip_03.Part_MAL_SR_Foregrip_03',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Foregrip/Part_MAL_SR_Foregrip_04.Part_MAL_SR_Foregrip_04',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Foregrip/Part_MAL_SR_Foregrip_05.Part_MAL_SR_Foregrip_05',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Foregrip/Part_MAL_SR_Foregrip_06.Part_MAL_SR_Foregrip_06'
        ]        
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Magazine/Part_MAL_SR_Mag_01.Part_MAL_SR_Mag_01',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Magazine/Part_MAL_SR_Mag_02.Part_MAL_SR_Mag_02',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Magazine/Part_MAL_SR_Mag_03.Part_MAL_SR_Mag_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_01/Part_MAL_SR_Scope_01.Part_MAL_SR_Scope_01',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_02/Part_MAL_SR_Scope_02.Part_MAL_SR_Scope_02',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_03/Part_MAL_SR_Scope_03.Part_MAL_SR_Scope_03'
        ]
    ],
    [
        [
            1
        ],
        [
            2
        ],
        [
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_01/Part_MAL_SR_Scope_01_A.Part_MAL_SR_Scope_01_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_01/Part_MAL_SR_Scope_01_B.Part_MAL_SR_Scope_01_B',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_02/Part_MAL_SR_Scope_02_A.Part_MAL_SR_Scope_02_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_02/Part_MAL_SR_Scope_02_B.Part_MAL_SR_Scope_02_B',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_03/Part_MAL_SR_Scope_03_A.Part_MAL_SR_Scope_03_A',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Scopes/Scope_03/Part_MAL_SR_Scope_03_B.Part_MAL_SR_Scope_03_B'
        ]
    ],
    [
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Elemental_Primary/Part_MAL_SR_Ele_Primary_Fire.Part_MAL_SR_Ele_Primary_Fire'
    ],
    [
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Material_ASMD.Part_MAL_SR_Material_ASMD'
    ]
]

TOR_PS_Vertical_BALANCE=[
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/EPartList_PS_TOR.EPartList_PS_TOR'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/PartSet_PS_TOR_Heckle.PartSet_PS_TOR_Heckle'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body.Part_PS_TOR_Body',
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_SpeedLoader.Part_PS_TOR_Body_SpeedLoader',
    ],
    [
        [
            2
        ],
        [
            2
        ],
        [ 
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_A.Part_PS_TOR_Body_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_B.Part_PS_TOR_Body_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_C.Part_PS_TOR_Body_C',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_D.Part_PS_TOR_Body_D'
        ]
        
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle'
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01.Part_PS_TOR_Barrel_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02.Part_PS_TOR_Barrel_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03.Part_PS_TOR_Barrel_03'
        ]
    ],
    [
        [
            1
        ],
        [
            3
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01_A.Part_PS_TOR_Barrel_01_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01_B.Part_PS_TOR_Barrel_01_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01_C.Part_PS_TOR_Barrel_01_C',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02_A.Part_PS_TOR_Barrel_02_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02_B.Part_PS_TOR_Barrel_02_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02_C.Part_PS_TOR_Barrel_02_C',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03_A.Part_PS_TOR_Barrel_03_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03_B.Part_PS_TOR_Barrel_03_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03_C.Part_PS_TOR_Barrel_03_C'
        ]        
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Grip/Part_PS_TOR_Grip_01.Part_PS_TOR_Grip_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Grip/Part_PS_TOR_Grip_02.Part_PS_TOR_Grip_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Grip/Part_PS_TOR_Grip_03.Part_PS_TOR_Grip_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Stock/Part_PS_TOR_Stock_02.Part_PS_TOR_Stock_02',
            ''
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Hammer/Part_PS_TOR_Hammer_01.Part_PS_TOR_Hammer_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Hammer/Part_PS_TOR_Hammer_02.Part_PS_TOR_Hammer_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Hammer/Part_PS_TOR_Hammer_03.Part_PS_TOR_Hammer_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_01.Part_PS_TOR_Mag_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_02.Part_PS_TOR_Mag_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_03.Part_PS_TOR_Mag_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_IronSight.Part_PS_TOR_IronSight',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_Scope_01.Part_PS_TOR_Scope_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_Scope_02.Part_PS_TOR_Scope_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_Scope_03.Part_PS_TOR_Scope_03'
        ]
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/FS/Part_PS_TOR_Barrel_01_B_Sight.Part_PS_TOR_Barrel_01_B_Sight'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Material_Heckle.Part_PS_TOR_Material_Heckle'
    ]
]

TOR_PS_Horizontal_BALANCE=[
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/EPartList_PS_TOR.EPartList_PS_TOR'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/PartSet_PS_TOR_Hyde.PartSet_PS_TOR_Hyde'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body.Part_PS_TOR_Body',
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_SpeedLoader.Part_PS_TOR_Body_SpeedLoader',
    ],
    [
        [
            2
        ],
        [
            2
        ],
        [ 
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_A.Part_PS_TOR_Body_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_B.Part_PS_TOR_Body_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_C.Part_PS_TOR_Body_C',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Body/Part_PS_TOR_Body_D.Part_PS_TOR_Body_D'
        ]
        
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde'
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01.Part_PS_TOR_Barrel_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02.Part_PS_TOR_Barrel_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03.Part_PS_TOR_Barrel_03'
        ]
    ],
    [
        [
            1
        ],
        [
            3
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01_A.Part_PS_TOR_Barrel_01_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01_B.Part_PS_TOR_Barrel_01_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_TOR_Barrel_01_C.Part_PS_TOR_Barrel_01_C',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02_A.Part_PS_TOR_Barrel_02_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02_B.Part_PS_TOR_Barrel_02_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_TOR_Barrel_02_C.Part_PS_TOR_Barrel_02_C',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03_A.Part_PS_TOR_Barrel_03_A',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03_B.Part_PS_TOR_Barrel_03_B',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_TOR_Barrel_03_C.Part_PS_TOR_Barrel_03_C'
        ]        
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Grip/Part_PS_TOR_Grip_01.Part_PS_TOR_Grip_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Grip/Part_PS_TOR_Grip_02.Part_PS_TOR_Grip_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Grip/Part_PS_TOR_Grip_03.Part_PS_TOR_Grip_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Stock/Part_PS_TOR_Stock_02.Part_PS_TOR_Stock_02',
            ''
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Hammer/Part_PS_TOR_Hammer_01.Part_PS_TOR_Hammer_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Hammer/Part_PS_TOR_Hammer_02.Part_PS_TOR_Hammer_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Hammer/Part_PS_TOR_Hammer_03.Part_PS_TOR_Hammer_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_01.Part_PS_TOR_Mag_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_02.Part_PS_TOR_Mag_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_03.Part_PS_TOR_Mag_03'
        ]
    ],
    [
        [
            1
        ],
        [
            1
        ],
        [
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_IronSight.Part_PS_TOR_IronSight',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_Scope_01.Part_PS_TOR_Scope_01',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_Scope_02.Part_PS_TOR_Scope_02',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Scope/Part_PS_TOR_Scope_03.Part_PS_TOR_Scope_03'
        ]
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Barrel/Barrel_01/FS/Part_PS_TOR_Barrel_01_B_Sight.Part_PS_TOR_Barrel_01_B_Sight'
    ],
    [
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Material_Heckle.Part_PS_TOR_Material_Heckle'
    ]
]

HYP_SH_Berserker_BALANCE=[
    [
        '/Game/Gear/Shields/_Design/A_Data/EPartList_Shield.EPartList_Shield'
    ],
    [
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot.InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot.InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot'
    ],
    [
        '/Game/Gear/Shields/_Design/PartSets/Part_Manufacturer/Shield_Part_Body_03_Hyperion.Shield_Part_Body_03_Hyperion'
    ],
    [
        '/Game/Gear/Shields/_Design/PartSets/Part_Rarity/Shield_Part_Rarity_Hyperion_03_Rare.Shield_Part_Rarity_Hyperion_03_Rare'
    ],
    [
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Parts/Part_Shield_Aug_ANS_LGD_WTF.Part_Shield_Aug_ANS_LGD_WTF'
    ],
    [
        '/Game/Gear/Shields/_Design/PartSets/Part_Element/Shield_Part_Element_Cryo.Shield_Part_Element_Cryo'
    ],
    [ 
        [ 
            1
        ],
        [ 
            1
        ],
        [ 
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Amp/Part_Shield_Aug_Amp.Part_Shield_Aug_Amp',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Amp/Part_Shield_Aug_Amp.Part_Shield_Aug_Amp',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Amp/Part_Shield_Aug_Amp.Part_Shield_Aug_Amp',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Roid/Part_Shield_Aug_Roid.Part_Shield_Aug_Roid',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Roid/Part_Shield_Aug_Roid.Part_Shield_Aug_Roid',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Roid/Part_Shield_Aug_Roid.Part_Shield_Aug_Roid',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Part_Shield_Aug_Nova.Part_Shield_Aug_Nova',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Part_Shield_Aug_Nova.Part_Shield_Aug_Nova',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Part_Shield_Aug_Nova.Part_Shield_Aug_Nova',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Part_Shield_Aug_Spike.Part_Shield_Aug_Spike',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Part_Shield_Aug_Spike.Part_Shield_Aug_Spike',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Part_Shield_Aug_Spike.Part_Shield_Aug_Spike',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeDelay/Part_Shield_Aug_RechargeDelay.Part_Shield_Aug_RechargeDelay',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeDelay/Part_Shield_Aug_RechargeDelay.Part_Shield_Aug_RechargeDelay',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeDelay/Part_Shield_Aug_RechargeDelay.Part_Shield_Aug_RechargeDelay',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeRate/Part_Shield_Aug_RechargeRate.Part_Shield_Aug_RechargeRate',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeRate/Part_Shield_Aug_RechargeRate.Part_Shield_Aug_RechargeRate',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeRate/Part_Shield_Aug_RechargeRate.Part_Shield_Aug_RechargeRate'
        ]
    ],
    [ 
        [ 
            1
        ],
        [ 
            1
        ],
        [ 
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Amp/Part_Shield_Aug_Amp.Part_Shield_Aug_Amp',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Amp/Part_Shield_Aug_Amp.Part_Shield_Aug_Amp',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Amp/Part_Shield_Aug_Amp.Part_Shield_Aug_Amp',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Roid/Part_Shield_Aug_Roid.Part_Shield_Aug_Roid',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Roid/Part_Shield_Aug_Roid.Part_Shield_Aug_Roid',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Roid/Part_Shield_Aug_Roid.Part_Shield_Aug_Roid',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Part_Shield_Aug_Nova.Part_Shield_Aug_Nova',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Part_Shield_Aug_Nova.Part_Shield_Aug_Nova',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Part_Shield_Aug_Nova.Part_Shield_Aug_Nova',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Part_Shield_Aug_Spike.Part_Shield_Aug_Spike',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Part_Shield_Aug_Spike.Part_Shield_Aug_Spike',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Part_Shield_Aug_Spike.Part_Shield_Aug_Spike',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeDelay/Part_Shield_Aug_RechargeDelay.Part_Shield_Aug_RechargeDelay',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeDelay/Part_Shield_Aug_RechargeDelay.Part_Shield_Aug_RechargeDelay',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeDelay/Part_Shield_Aug_RechargeDelay.Part_Shield_Aug_RechargeDelay',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeRate/Part_Shield_Aug_RechargeRate.Part_Shield_Aug_RechargeRate',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeRate/Part_Shield_Aug_RechargeRate.Part_Shield_Aug_RechargeRate',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/RechargeRate/Part_Shield_Aug_RechargeRate.Part_Shield_Aug_RechargeRate'
        ]
    ],
    [
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Parts/Part_Shield_Mat_ANS_LGD_WTF.Part_Shield_Mat_ANS_LGD_WTF'
    ]
]

BALANCE = [
    COV_AR_Bateman_BALANCE,
    TED_GR_Comet_BALANCE,
    JAK_PS_Triolet_BALANCE,
    TED_SG_Horn_BALANCE,
    MAL_SR_Sun_BALANCE,
    TOR_PS_Vertical_BALANCE,
    TOR_PS_Horizontal_BALANCE,
    HYP_SH_Berserker_BALANCE,
    JAK_SG_Beefcake_BALANCE,
    TOR_AR_Gunslinger_BALANCE,
    HYP_SG_BUL_BALANCE,
    HYP_SG_WAR_BALANCE
    ]

for balance in BALANCE:
    
    for i in range(2,len(balance)):       

        if len(balance[i]) == 1:
            int_numparts = len(balance[i])    
            if i == (len(balance)-1):
                str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][0]},Weight=(BaseValueConstant=1.0))')
                str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                int_index += int_numparts
                int_numparts = 0
            if i != (len(balance)-1):               
                str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][0]},Weight=(BaseValueConstant=1.0)),')
                str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                int_index += int_numparts
                int_numparts = 0
                
        if len(balance[i]) == 3:
            int_numparts = len(balance[i][2]) 
            if i == (len(balance)-1):
                for j in range(int_numparts-1):
                    str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0))')
                str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                int_index += int_numparts
                int_numparts = 0
            if i != (len(balance)-1):
                for j in range(int_numparts):
                    str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                int_index += int_numparts
                int_numparts = 0

        if len(balance[i]) == 4:
            int_numparts = len(balance[i][3]) 
            if i == (len(balance)-1):
                for j in range(int_numparts-1):
                    str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]})),')
                str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]}))')
                str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                int_index += int_numparts
                int_numparts = 0
            if i != (len(balance)-1):
                for j in range(int_numparts):
                    str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]})),')
                str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                int_index += int_numparts
                int_numparts = 0
        
        if len(balance[i]) > 1 and i != (len(balance)-1) and balance[i][1][0] > 1:
            str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={balance[i][0][0]},Max={balance[i][1][0]}),bEnabled=True),')     
        
        elif len(balance[i]) > 1 and i == (len(balance)-1) and balance[i][1][0] > 1: 
            str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={balance[i][0][0]},Max={balance[i][1][0]}),bEnabled=True)')
        
        elif len(balance[i]) > 1  and i != (len(balance)-1) and balance[i][1][0] == 1:
            str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
        
        elif len(balance[i]) > 1 and i == (len(balance)-1) and balance[i][1][0] == 1: 
            str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')
        
        elif len(balance[i]) == 1 and i != (len(balance)-1):
            str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
        
        elif len(balance[i]) == 1 and i == (len(balance)-1):
            str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')

    mod.comment('Partset')
    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
    balance[1][1],
    'ActorPartLists',
    f"""
    (
        {str_partset}
    )
    """
    )
    mod.newline()
    str_partset = ''
    int_numparts = 0

    mod.comment('Balance TOC')
    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
    balance[1][0],
    'RuntimePartList.PartTypeTOC',
    f"""
    (
        {str_toc}
    )
    """
    )
    mod.newline()
    str_toc = ''
    int_index = 0

    mod.comment('Balance')
    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
    balance[1][0],
    'RuntimePartList.AllParts',
    f"""
    (
        {str_invbalance}
    )
    """
    )
    mod.newline()
    str_invbalance=''

mod.comment("Class Mods Changes")
if True :

    for cm in BAL_classmods:

        mod.comment('Setting Each COM to Have its Own Balance')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        cm[1][0],
        'BaseSelectionData',
        'None'
        )
        mod.newline()

        mod.comment('Setting Each COM to Have its Own Balance')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        cm[1][1],
        'BaseSelectionData',
        'None'
        )
        mod.newline()

        for i in range(2,len(cm)):       

            if len(cm[i]) == 1:
                int_numparts = len(cm[i])    
                if i == (len(cm)-1):
                    str_invbalance=str_invbalance.__add__(f'(PartData={cm[i][0]},Weight=(BaseValueConstant=1.0))')
                    str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                    int_index += int_numparts
                    int_numparts = 0
                if i != (len(cm)-1):               
                    str_invbalance=str_invbalance.__add__(f'(PartData={cm[i][0]},Weight=(BaseValueConstant=1.0)),')
                    str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                    int_index += int_numparts
                    int_numparts = 0
                    
            if len(cm[i]) > 1:
                int_numparts = len(cm[i][2]) 
                if i == (len(cm)-1):
                    for j in range(int_numparts-1):
                        str_invbalance=str_invbalance.__add__(f'(PartData={cm[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                    str_invbalance=str_invbalance.__add__(f'(PartData={cm[i][2][j]},Weight=(BaseValueConstant=1.0))')
                    str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                    int_index += int_numparts
                    int_numparts = 0
                if i != (len(cm)-1):
                    for j in range(int_numparts):
                        str_invbalance=str_invbalance.__add__(f'(PartData={cm[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                    str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                    int_index += int_numparts
                    int_numparts = 0
            
            if len(cm[i]) > 1 and i != (len(cm)-1) and cm[i][1][0] > 1:
                str_partset=str_partset.__add__(f'(PartTypeEnum={cm[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={cm[i][0][0]},Max={cm[i][1][0]}),bEnabled=True),')     
            
            elif len(cm[i]) > 1 and i == (len(cm)-1) and cm[i][1][0] > 1: 
                str_partset=str_partset.__add__(f'(PartTypeEnum={cm[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={cm[i][0][0]},Max={cm[i][1][0]}),bEnabled=True)')
            
            elif len(cm[i]) > 1  and i != (len(cm)-1) and cm[i][1][0] == 1:
                str_partset=str_partset.__add__(f'(PartTypeEnum={cm[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
            
            elif len(cm[i]) > 1 and i == (len(cm)-1) and cm[i][1][0] == 1: 
                str_partset=str_partset.__add__(f'(PartTypeEnum={cm[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')
            
            elif len(cm[i]) == 1 and i != (len(cm)-1):
                str_partset=str_partset.__add__(f'(PartTypeEnum={cm[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
            
            elif len(cm[i]) == 1 and i == (len(cm)-1):
                str_partset=str_partset.__add__(f'(PartTypeEnum={cm[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')

        mod.comment('Partset')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        cm[1][1],
        'ActorPartLists',
        f"""
        (
            {str_partset}
        )
        """
        )
        mod.newline()
        str_partset = ''
        int_numparts = 0

        mod.comment('Balance TOC')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        cm[1][0],
        'RuntimePartList.PartTypeTOC',
        f"""
        (
            {str_toc}
        )
        """
        )
        mod.newline()
        str_toc = ''
        int_index = 0

        mod.comment('Balance')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        cm[1][0],
        'RuntimePartList.AllParts',
        f"""
        (
            {str_invbalance}
        )
        """
        )
        mod.newline()
        str_invbalance=''

    for FL4K_mod in FL4K_Class_Mods:

        for i in range(len(FL4K_mod)):
            if len(FL4K_mod[i]) == 3:
                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                FL4K_mod[i][1][0],
                FL4K_mod[i][0][0],
                FL4K_mod[i][2][0]
                )
                mod.newline()
            if len(FL4K_mod[i]) == 4:
                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                FL4K_mod[i][0][0],
                FL4K_mod[i][1][0],
                FL4K_mod[i][2][0],
                FL4K_mod[i][3][0],
                )
                mod.newline()

            if len(FL4K_mod[i]) == 5:
                mod.reg_hotfix(Mod.CHAR,FL4K_mod[i][1][0],
                FL4K_mod[i][3][0],
                FL4K_mod[i][2][0],
                FL4K_mod[i][4][0]
                )
                mod.newline()
  
    for SK in SK_BM :

        for i in range(len(SK[1])) :

            if i == len(SK[1])-1 :

                str_dep=str_dep.__add__(f'{SK[1][-1]}')

            else :

                str_dep=str_dep.__add__(f'{SK[1][i]},')
            
            
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        SK[0][0],
        'Dependencies',
        f'({str_dep})'
        )
        mod.newline()

        str_dep = ''

    mod.comment("Stats Changes")
    if True :

        for stat in STATS_ADD :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            stat[0],
            'InstigatorAttributeEffects.InstigatorAttributeEffects[0].ModifierValue.ModifierType',
            'EGbxAttributeModifierType::PreAdd'
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            stat[1],
            'Offset',
            '(BaseValueConstant=0.0)'
            )
            mod.newline()

            for j in range(len(stat[1])) :

                if j == len(stat[1])-1 : 

                    str_dep_cm=str_dep_cm.__add__(f'{stat[1][j]}')

                else :
                        
                    str_dep_cm=str_dep_cm.__add__(f'{stat[1][j]},')                

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            stat[0],
            'Dependencies',
            f'({str_dep_cm})'
            )
            mod.newline()

            str_dep_cm = ''

        for stat in STATS :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            stat[0],
            'InstigatorAttributeEffects.InstigatorAttributeEffects[0].ModifierValue.BaseValueAttribute',
            '/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            stat[0],
            'InstigatorAttributeEffects.InstigatorAttributeEffects[0].ModifierValue.ModifierType',
            'EGbxAttributeModifierType::Scale'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            stat[0],
            'InstigatorAttributeEffects.InstigatorAttributeEffects[0].ModifierValue.BaseValueScale',
            stat[2]
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            stat[1],
            'Multiplier',
            f'(BaseValueConstant={stat[2]})'.format(stat[2])
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            stat[1],
            'Level',
            '(BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel)'
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            stat[1],
            'Offset',
            '(BaseValueConstant=0.0)'
            )
            mod.newline()

            for j in range(len(stat[3])) :

                if j == len(stat[3])-1 : 

                    str_dep_cm=str_dep_cm.__add__(f'{stat[3][j]}')

                else :
                        
                    str_dep_cm=str_dep_cm.__add__(f'{stat[3][j]},')                

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            stat[0],
            'Dependencies',
            f'({str_dep_cm})'
            )
            mod.newline()

            str_dep_cm = ''

        for stat in STATS_INDEXED_5 :

            for i in range(5) :

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                stat[0],
                f'InstigatorAttributeEffects.InstigatorAttributeEffects[{i}].ModifierValue.BaseValueAttribute'.format(i),
                '/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                stat[0],
                f'InstigatorAttributeEffects.InstigatorAttributeEffects[{i}].ModifierValue.ModifierType'.format(i),
                'EGbxAttributeModifierType::Scale'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                stat[0],
                f'InstigatorAttributeEffects.InstigatorAttributeEffects[{i}].ModifierValue.BaseValueScale'.format(i),
                stat[2]
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
                stat[1],
                'Multiplier',
                f'(BaseValueConstant={stat[2]})'.format(stat[2])
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
                stat[1],
                'Level',
                '(BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel)'
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
                stat[1],
                'Offset',
                '(BaseValueConstant=0.0)'
                )
                mod.newline()

                for j in range(len(stat[3])) :

                    if j == len(stat[3])-1 : 

                        str_dep_cm=str_dep_cm.__add__(f'{stat[3][j]}')

                    else :
                            
                        str_dep_cm=str_dep_cm.__add__(f'{stat[3][j]},')                

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    stat[0],
                    'Dependencies',
                    f'({str_dep_cm})'
                    )
                    mod.newline()

                    str_dep_cm = ''

        for stat in STATS_INDEXED_4 :

            for i in range(5) :

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                stat[0],
                f'InstigatorAttributeEffects.InstigatorAttributeEffects[{i}].ModifierValue.BaseValueAttribute'.format(i),
                '/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                stat[0],
                f'InstigatorAttributeEffects.InstigatorAttributeEffects[{i}].ModifierValue.ModifierType'.format(i),
                'EGbxAttributeModifierType::Scale'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                stat[0],
                f'InstigatorAttributeEffects.InstigatorAttributeEffects[{i}].ModifierValue.BaseValueScale'.format(i),
                stat[2]
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
                stat[1],
                'Multiplier',
                f'(BaseValueConstant={stat[2]})'.format(stat[2])
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
                stat[1],
                'Level',
                '(BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel)'
                )
                mod.newline()

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
                stat[1],
                'Offset',
                '(BaseValueConstant=0.0)'
                )
                mod.newline()

                for j in range(len(stat[3])) :

                    if j == len(stat[3])-1 : 

                        str_dep_cm=str_dep_cm.__add__(f'{stat[3][j]}')

                    else :
                            
                        str_dep_cm=str_dep_cm.__add__(f'{stat[3][j]},')                

                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    stat[0],
                    'Dependencies',
                    f'({str_dep_cm})'
                    )
                    mod.newline()

                    str_dep_cm = ''

        for ui in STATS_UI :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            ui[0],
            'FormatText',
            ui[1]
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            ui[0],
            'SignStyle',
            'EUIStatValueSignStyle::Positive'
            )
            mod.newline()

        mod.comment("Dot Damage Global")
        if True :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/PartSets/Part_Stats/Part_Primary_Stat/Elemental/DOT/ClassMod_Part_Stat_Primary_Elemental_DoT_Damage_Global',
            'InstigatorAttributeEffects',
            """
                (
                    (
                        AttributeToModify=GbxAttributeData'\"/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageCauser_CorrosiveDamage.Att_StatusEffect_DamageCauser_CorrosiveDamage\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel,BaseValueScale=0.009)
                    ),
                    (
                        AttributeToModify=GbxAttributeData'\"/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageCauser_FireDamage.Att_StatusEffect_DamageCauser_FireDamage\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel,BaseValueScale=0.009)
                    ),
                    (
                        AttributeToModify=GbxAttributeData'\"/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageCauser_RadiationDamage.Att_StatusEffect_DamageCauser_RadiationDamage\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel,BaseValueScale=0.009)
                    ),
                    (
                        AttributeToModify=GbxAttributeData'\"/Game/GameData/StatusEffects/EffectModifierAttributes/Att_StatusEffect_DamageCauser_ShockDamage.Att_StatusEffect_DamageCauser_ShockDamage\"',
                        ModifierType=EGbxAttributeModifierType::Scale,
                        ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel,BaseValueScale=0.009)
                    )
                )
            """
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            'DoT_Damage_Global',
            'Multiplier',
            '(BaseValueConstant=0.009)'
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            'DoT_Damage_Global',
            'Level',
            '(BaseValueAttribute=/Game/GameData/Attributes/Att_ClassMod_ItemLevel.Att_ClassMod_ItemLevel)'
            )
            mod.newline()

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/ClassMods/_Design/Balance/Table_ClassMod_Stats2',
            'DoT_Damage_Global',
            'Offset',
            '(BaseValueConstant=0.0)'
            )
            mod.newline()

mod.comment("VHs Changes")
if True :  

    mod.comment("Fl4k Changes")
    if True :

        mod.reg_hotfix(Mod.CHAR,'BPChar_Beastmaster',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_Beastmaster.Default__BPChar_Beastmaster_C:DefaultDamageComponent',
        'HealthInformation.HealthInformation[0].HealthTypeData',
        '/Game/GameData/ResourcePools/HealthTypes/HealthType_Armor.HealthType_Armor'
        )
        mod.newline()

        mod.reg_hotfix(Mod.CHAR,'BPChar_Beastmaster',
        '/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPChar_Beastmaster.Default__BPChar_Beastmaster_C',
        'CharacterMass.Mass',
        300.0
        )
        mod.newline()

        mod.comment('Buffing global pet skill damage')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Global_Pet_SkillDamage',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        40.0
        )
        mod.newline()

        mod.comment('Buffing global pet melee damage')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Global_Pet_MeleeDamage',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        20.0
        )
        mod.newline()

        mod.comment('Buffing global pet ranged damage')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Global_Pet_RangedAttack',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        0.45
        )
        mod.newline()

        mod.comment('Buffing leap pet damage')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PlayerCharacters/_Shared/_Design/Balance/Beastmaster/DataTable_Beastmaster_SkillBalance',
        'Global_Pet_LeapAttack',
        'Scalar_5_230D633C4A306BF04AB690B7CD89D6AA',
        1.2
        )
        mod.newline()

        FL4K_Skills=[
            Attribute_Damage_Ammo,
            Fade_Away,
            Fade_Away_A1,
            Fade_Away_A2,
            Fade_Away_A3,
            Fade_Away_A4,
            Base_Jabber,
            Evo1_Jabber,
            Evo2_Jabber,
            Self_Repairing_System,
            Furious_Attack,
            Eager_To_Impress,
            All_My_BFFs,
            Round_Up,
            Lick_The_Wounds,
            Turn_Tail_And_Run,
            The_Fast_And_The_Furryous,
            Hidden_Machine,
            Rage_And_Recover,
            The_Power_Inside,
            Rakk_Attack,
            Rakk_Attack_A1,
            Rakk_Attack_A2,
            Rakk_Attack_A3,
            Rakk_Attack_A4,
            Base_Spiderant,
            Evo1_Spiderant,
            Evo2_Spiderant,
            On_The_Hunt,
            Leave_No_Trace,
            Second_Intention,
            Hunters_Eye,
            Head_Count,
            Ambush_Predator,
            Two_Fang,
            Big_Game,
            The_Most_Dangerous_Game,
            Galactic_Shadow,
            Grim_Harvest,
            Megavore,
            Gamma_Burst,
            Gamma_Burst_A1,
            Gamma_Burst_A2,
            Gamma_Burst_A3,
            Gamma_Burst_A4,
            Base_Skag,
            Evo1_Skag,
            Evo2_Skag,
            Ferocity,
            Persistence_Hunter,
            Go_For_The_Eyes,
            Who_Rescued_Who,
            He_Bites,
            Frenzy,
            Psycho_Head_on_A_Stick,
            Hive_Mind,
            Barbaric_Yawp,
            Mutated_Defense,
            Pack_Tactics,
            Shared_Spirit,
            Dominance,
            Gravity_Snare,
            Gravity_Snare_A1,
            Gravity_Snare_A2,
            Gravity_Snare_A3,
            Gravity_Snare_A4,
            Base_Loader,
            Evo1_Loader,
            Evo2_Loader,
            Gotta_Go_Fast,
            Success_Imminent,
            Agility_Training,
            Better_Toys,
            Combat_Veterinarian,
            Throatripper,
            Lethal_Force_Authorized,
            Take_This,
            Monkey_Do,
            Wooly_Armor,
            Not_Even_A_Challenge,
            Fuzzy_Math,
            Keep_Them_Safe,
            Capacitance
        ]

        for skill in FL4K_Skills:
            for i in range(len(skill)):
                if len(skill[i]) == 3:
                    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                    skill[i][1][0],
                    skill[i][0][0],
                    skill[i][2][0]
                    )
                    mod.newline()
                if len(skill[i]) == 4:
                    mod.table_hotfix(Mod.LEVEL,'MatchAll',
                    skill[i][0][0],
                    skill[i][1][0],
                    skill[i][2][0],
                    skill[i][3][0],
                    )
                    mod.newline()

                if len(skill[i]) == 5:
                    mod.reg_hotfix(Mod.CHAR,skill[i][1][0],
                    skill[i][3][0],
                    skill[i][2][0],
                    skill[i][4][0]
                    )
                    mod.newline()

mod.comment("Non unique Gun Changes")
if True :

    mod.comment('Maliwan Overhaul')
    if True:

        mod.comment('Sniper Rifles')
        if True:

            mod.comment('Barrel 01')
            if True:

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01',
                'AspectList.AspectList[2]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01',
                'AspectList.AspectList[4]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01',
                'AspectList.AspectList[5]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01:AspectList_WeaponUseModeAspectData',
                'Priority',
                'Medium'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'bUseShotStrengthFormula',
                'false'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'ShotStrengthDamageCurve',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'ShotStrengthDamageRadiusCurve',
                'None'
                )
                mod.newline()

            mod.comment('Barrel 02')
            if True:

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02',
                'AspectList.AspectList[2]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02',
                'AspectList.AspectList[3]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02',
                'AspectList.AspectList[4]',
                'None'
                )
                mod.newline()


                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'bUseShotStrengthFormula',
                'false'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'ShotStrengthDamageCurve',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'ShotStrengthDamageRadiusCurve',
                'None'
                )
                mod.newline()

            mod.comment('Barrel 03')
            if True:

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03',
                'AspectList.AspectList[2]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03',
                'AspectList.AspectList[3]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03',
                'AspectList.AspectList[4]',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'bUseShotStrengthFormula',
                'false'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'ShotStrengthDamageCurve',
                'None'
                )
                mod.newline()

                mod.reg_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
                'ShotStrengthDamageRadiusCurve',
                'None'
                )
                mod.newline()

    mod.comment('Torgue ETECH Shotgun')
    if True:

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_Rare',
        'RuntimePartList.AllParts[11].PartData',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02.Part_SG_Torgue_Magazine_02'
        )
        mod.newline()

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_Rare',
        'RuntimePartList.AllParts[13].PartData',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02.Part_SG_Torgue_Magazine_02'
        )
        mod.newline()

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_Rare',
        'RuntimePartList.AllParts[14].PartData',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02.Part_SG_Torgue_Magazine_02'
        )
        mod.newline()

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_VeryRare',
        'RuntimePartList.AllParts[12].PartData',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02.Part_SG_Torgue_Magazine_02'
        )
        mod.newline()

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_VeryRare',
        'RuntimePartList.AllParts[14].PartData',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02.Part_SG_Torgue_Magazine_02'
        )
        mod.newline()

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_VeryRare',
        'RuntimePartList.AllParts[15].PartData',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02.Part_SG_Torgue_Magazine_02'
        )
        mod.newline()

    mod.comment('Torgue Stickies Buff')
    if True:

        mod.comment('Shotgun Stickies')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_01',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.025,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_02',
            'InventoryAttributeEffects.InventoryAttributeEffects[2].ModifierValue',
            """
            (
                BaseValueConstant=0.125,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_03',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.0175,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_04',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.04,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

        mod.comment('Assault Rifle Stickies')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Magazine/Part_AR_TOR_Magazine_01',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.08,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Magazine/Part_AR_TOR_Magazine_02',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.11,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Parts/Magazine/Part_AR_TOR_Magazine_03',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.06,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

        mod.comment('Pistol Stickies')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_01',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.12,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_02',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.18,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Parts/Mag/Part_PS_TOR_Mag_03',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.24,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

        mod.comment('Heavy Stickies ')
        if True:

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_01',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.6,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_02',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=0.4,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_03',
            'InventoryAttributeEffects.InventoryAttributeEffects[1].ModifierValue',
            """
            (
                BaseValueConstant=1.0,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Magazine/Part_HW_TOR_Mag_03',
            'InventoryAttributeEffects.InventoryAttributeEffects[2].ModifierValue',
            """
            (
                BaseValueConstant=1.0,
                DataTableValue=(DataTable=None,RowName=None,ValueName=None),
                BaseValueAttribute=None,
                AttributeInitializer=None,
                BaseValueScale=1.0
            )
            """
            )
            mod.newline()

    MANUFACTURER_stats=[
        ATLAS_stats,
        COV_stats,
        DAHL_stats,
        HYPERION_stats,
        JAKOBS_stats,
        MALIWAN_stats,
        TEDIORE_stats,
        TORGUE_stats,
        VLADOF_stats
    ]

    for manufacturer in MANUFACTURER_stats:
        for i in range(1,len(manufacturer)):
            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Manufacturer_Base_Data',
            manufacturer[0][0],
            manufacturer[i][0],
            manufacturer[i][1]
            )
            mod.newline()

    WEAPON_stats=[
        AR_stats,
        SMG_stats,
        PS_stats,
        SG_stats,
        SR_stats,
        HW_stats
    ]

    for weapon in WEAPON_stats:
        for i in range(1,len(weapon)):
            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data',
            weapon[0][0],
            weapon[i][0],
            weapon[i][1]
            )
            mod.newline()

    for barrel in BARREL_stats:
        for i in range(1,len(barrel)):
            for j in range(1,len(barrel[i])):
                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                barrel[0][0],
                barrel[i][0][0],
                barrel[i][j][0],
                barrel[i][j][1]
                )
                mod.newline()

    WEAPON_manufacturer=[
        [
            'Shotgun',
            'Pistol',
            'SMG',
            'AssaultRifle',
            'Sniper',
            'Heavy'
        ],
        [
            'DAHL_59_150C89A04BB4FCF0061CAC86E39E1A39',
            'Jakobs_60_F95FBBA045F4F1899B3F7AB7A2CF0F22',
            'Hyperion_61_03553D4547FA30186E792BA391B2FFDE',
            'Vladof_63_DBDCED3C4D3A2AAE4157EEA39EAB81DB',
            'Tediore_64_177AD05C46493B9713642FA9EEDB6DDC',
            'CoV_65_A2A97C764F97EC46B630BB9F944FE44E',
            'Torgue_75_E4646A97474FA2023598DE982B960083',
            'Maliwan_76_93DF9FBB4DB223F6D5697180435918B2',
            'Atlas_78_8B8B7B8741EFF37DAC0B5D8739B6F0E4',
            'Eridi_79_33F681DA484DAC3C64282E95BFAB0872'
        ]
    ]

    for weapon in WEAPON_manufacturer[0]:
        for manufacturer in WEAPON_manufacturer[1]:
            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_DamageScale',
            weapon,
            manufacturer,
            1.0
            )
            mod.newline()
    
    for weapon in MANUFATURER_WEAPON_TYPE[0] :

        for manufacturer in MANUFATURER_WEAPON_TYPE[1] :

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_DamageScale',
            weapon,
            manufacturer[0],
            manufacturer[1]
            )
            mod.newline()

mod.comment("Shield Changes")
if True :

    mod.comment("Manufacturer Descriptions")
    if True :

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Manufacturers/_Design/Anshin',
        'Blurb',
        "“When the storm winds blow, the unyielding branches break, as gentle reeds bend.” Anshin shields have medium capacity, recharge delay and a low recharge rate ; a shield for every situation. Anshin: Unbroken."
        )
        mod.newline()

        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Manufacturers/_Design/Pangolin',
        'Blurb',
        "Bullets. Blades. Bombs. It's dangerous work, but someone's got to do it. That's why Pangolin produces the highest capacity personal shields around. Withstand everything, stop at nothin, with Pangolin."
        )
        mod.newline()

    for manufacturer in SHIELD_Manufacturer :
        for i in range(1,len(manufacturer)) :
            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/Balance/Shield_BalanceData',
            manufacturer[0][0],
            manufacturer[i][0],
            manufacturer[i][1]
            )
            mod.newline()
    
    for augment in SHIELD_AUG :
        for i in range(1,len(augment)) :
            for j in range(i) :

                mod.table_hotfix(Mod.LEVEL,'MatchAll',
                '/Game/Gear/Shields/_Design/Balance/ShieldAug_BalanceData',
                augment[0][0],
                augment[i][j][0],
                augment[i][j][1]
                )
                mod.newline()

    for excluder in SHIELD_Excluders :
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        excluder,
        'Excluders',
        'None'
        )
        mod.newline()

    mod.comment("Making Damage Shields Scale With Max Shield")
    if True :

        mod.comment("Nova")
        if True :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Attribute/Att_Calc_ShieldAug_Nova_Damage_P1.Att_Calc_ShieldAug_Nova_Damage_P1:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Attribute/Att_Calc_ShieldAug_Nova_Damage_P2.Att_Calc_ShieldAug_Nova_Damage_P2:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Nova/Attribute/Att_Calc_ShieldAug_Nova_Damage_P3.Att_Calc_ShieldAug_Nova_Damage_P3:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
            )
            mod.newline()
        
        mod.comment("Spike")
        if True :

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Attribute/Att_Calc_ShieldAug_Spike_Damage_P1.Att_Calc_ShieldAug_Spike_Damage_P1:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Attribute/Att_Calc_ShieldAug_Spike_Damage_P2.Att_Calc_ShieldAug_Spike_Damage_P2:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
            )
            mod.newline()

            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/Shields/_Design/PartSets/Part_Augment/Spike/Attribute/Att_Calc_ShieldAug_Spike_Damage_P3.Att_Calc_ShieldAug_Spike_Damage_P3:ValueResolver_SimpleMathValueResolver',
            'ValueA',
            '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
            )
            mod.newline()

    mod.comment("Changing The InvBal")
    if True :

        for balance in SH_BALANCE:
            
            for i in range(2,len(balance)):       

                if len(balance[i]) == 1:
                    int_numparts = len(balance[i])    
                    if i == (len(balance)-1):
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][0]},Weight=(BaseValueConstant=1.0))')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                        int_index += int_numparts
                        int_numparts = 0
                    if i != (len(balance)-1):               
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][0]},Weight=(BaseValueConstant=1.0)),')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                        int_index += int_numparts
                        int_numparts = 0
                        
                if len(balance[i]) == 3:
                    int_numparts = len(balance[i][2]) 
                    if i == (len(balance)-1):
                        for j in range(int_numparts-1):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0))')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                        int_index += int_numparts
                        int_numparts = 0
                    if i != (len(balance)-1):
                        for j in range(int_numparts):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                        int_index += int_numparts
                        int_numparts = 0

                if len(balance[i]) == 4:
                    int_numparts = len(balance[i][3]) 
                    if i == (len(balance)-1):
                        for j in range(int_numparts-1):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]})),')
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]}))')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                        int_index += int_numparts
                        int_numparts = 0
                    if i != (len(balance)-1):
                        for j in range(int_numparts):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]})),')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                        int_index += int_numparts
                        int_numparts = 0

                if len(balance[i]) > 1 and i != (len(balance)-1) and balance[i][1][0] > 1:
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={balance[i][0][0]},Max={balance[i][1][0]}),bEnabled=True),')     
                
                elif len(balance[i]) > 1 and i == (len(balance)-1) and balance[i][1][0] > 1: 
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={balance[i][0][0]},Max={balance[i][1][0]}),bEnabled=True)')
                
                elif len(balance[i]) > 1  and i != (len(balance)-1) and balance[i][1][0] == 1:
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
                
                elif len(balance[i]) > 1 and i == (len(balance)-1) and balance[i][1][0] == 1: 
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')
                
                elif len(balance[i]) == 1 and i != (len(balance)-1):
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
                
                elif len(balance[i]) == 1 and i == (len(balance)-1):
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')

            mod.comment('Partset')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            balance[1][1],
            'ActorPartLists',
            f"""
            (
                {str_partset}
            )
            """
            )
            mod.newline()
            str_partset = ''
            int_numparts = 0

            mod.comment('Balance TOC')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            balance[1][0],
            'RuntimePartList.PartTypeTOC',
            f"""
            (
                {str_toc}
            )
            """
            )
            mod.newline()
            str_toc = ''
            int_index = 0

            mod.comment('Balance')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            balance[1][0],
            'RuntimePartList.AllParts',
            f"""
            (
                {str_invbalance}
            )
            """
            )
            mod.newline()
            str_invbalance=''

mod.comment("Grenades Changes")
if True :

    for manufacturer in GRENADE_Manufacturer :
        for i in range(1,len(manufacturer)) :
            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/GrenadeMods/_Design/Balance/Grenade_Balance_Table',
            manufacturer[0][0],
            manufacturer[i][0],
            manufacturer[i][1]
            )
            mod.newline()
    
    for augment in GRENADE_Augment :
        for i in range(1,len(augment)) :

            mod.table_hotfix(Mod.LEVEL,'MatchAll',
            '/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Balance_Table',
            augment[0][0],
            augment[i][0],
            augment[i][1]
            )
            mod.newline()

    for excluder in GRENADE_Excluders :
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        excluder,
        'Excluders',
        'None'
        )
        mod.newline()

    mod.reg_hotfix(Mod.LEVEL,'MatchAll',
    '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Lingering/GM_Part_Behavior_07_Lingering',
    'Excluders',
    '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Element/GM_Part_Element_01_Normal.GM_Part_Element_01_Normal'
    )
    mod.newline()

    mod.comment("Changing The InvBal")
    if True :

        for balance in GR_BALANCE:
            
            for i in range(2,len(balance)):       

                if len(balance[i]) == 1:
                    int_numparts = len(balance[i])    
                    if i == (len(balance)-1):
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][0]},Weight=(BaseValueConstant=1.0))')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                        int_index += int_numparts
                        int_numparts = 0
                    if i != (len(balance)-1):               
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][0]},Weight=(BaseValueConstant=1.0)),')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                        int_index += int_numparts
                        int_numparts = 0
                        
                if len(balance[i]) == 3:
                    int_numparts = len(balance[i][2]) 
                    if i == (len(balance)-1):
                        for j in range(int_numparts-1):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0))')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                        int_index += int_numparts
                        int_numparts = 0
                    if i != (len(balance)-1):
                        for j in range(int_numparts):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][2][j]},Weight=(BaseValueConstant=1.0)),')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                        int_index += int_numparts
                        int_numparts = 0

                if len(balance[i]) == 4:
                    int_numparts = len(balance[i][3]) 
                    if i == (len(balance)-1):
                        for j in range(int_numparts-1):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]})),')
                        str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]}))')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts})')
                        int_index += int_numparts
                        int_numparts = 0
                    if i != (len(balance)-1):
                        for j in range(int_numparts):
                            str_invbalance=str_invbalance.__add__(f'(PartData={balance[i][3][j][0]},Weight=(BaseValueConstant=1.0,BaseValueScale={balance[i][3][j][1]})),')
                        str_toc=str_toc.__add__(f'(StartIndex={int_index},NumParts={int_numparts}),')
                        int_index += int_numparts
                        int_numparts = 0

                if len(balance[i]) > 1 and i != (len(balance)-1) and balance[i][1][0] > 1:
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={balance[i][0][0]},Max={balance[i][1][0]}),bEnabled=True),')     
                
                elif len(balance[i]) > 1 and i == (len(balance)-1) and balance[i][1][0] > 1: 
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=True,MultiplePartSelectionRange=(Min={balance[i][0][0]},Max={balance[i][1][0]}),bEnabled=True)')
                
                elif len(balance[i]) > 1  and i != (len(balance)-1) and balance[i][1][0] == 1:
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
                
                elif len(balance[i]) > 1 and i == (len(balance)-1) and balance[i][1][0] == 1: 
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')
                
                elif len(balance[i]) == 1 and i != (len(balance)-1):
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True),')
                
                elif len(balance[i]) == 1 and i == (len(balance)-1):
                    str_partset=str_partset.__add__(f'(PartTypeEnum={balance[0][0]},PartType={i},bCanSelectMultipleParts=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True)')

            mod.comment('Partset')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            balance[1][1],
            'ActorPartLists',
            f"""
            (
                {str_partset}
            )
            """
            )
            mod.newline()
            str_partset = ''
            int_numparts = 0

            mod.comment('Balance TOC')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            balance[1][0],
            'RuntimePartList.PartTypeTOC',
            f"""
            (
                {str_toc}
            )
            """
            )
            mod.newline()
            str_toc = ''
            int_index = 0

            mod.comment('Balance')
            mod.reg_hotfix(Mod.LEVEL,'MatchAll',
            balance[1][0],
            'RuntimePartList.AllParts',
            f"""
            (
                {str_invbalance}
            )
            """
            )
            mod.newline()
            str_invbalance=''

mod.comment("All Unique Gear Changes")
if True :

    mod.comment("Shiv's Assault Rifle")
    if True :

        mod.comment('Damage')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage',
        'InventoryAttributeEffects',
        """
        (
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0.7)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot.Att_Weapon_ProjectilesPerShot,
                ModifierType=PreAdd,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
            )  
        )
        """
        )
        mod.newline()

        mod.comment('Damage Received')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage',
        'InstigatorAttributeEffects',
        """
        (
            (
                AttributeToModify=/Game/GameData/Attributes/Damage/Att_DamageTakenMultiplier.Att_DamageTakenMultiplier,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0.7)
            ),
            (
                AttributeToModify=/Game/GameData/Attributes/Character/Att_GroundSpeedScale.Att_GroundSpeedScale,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0.9)
            )  
        )
        """
        )
        mod.newline()

        mod.comment('Removing the Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage',
        'GestaltMeshPartName',
        'None'
        )
        mod.newline()

        mod.comment('Removing the Fire Rate')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage',
        'AspectList.AspectList[0]',
        'None'
        )
        mod.newline()

        mod.comment('Ability')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Damage/Part_AR_COV_Barrel_HeatDamage.Part_AR_COV_Barrel_HeatDamage:AspectList_InventoryAbilityAspectData',
        'Abilities.Abilities[0].Ability',
        ''
        )
        mod.newline()

        mod.comment('Ability')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Parts/Part_AR_COV_Material_KriegAR.Part_AR_COV_Material_KriegAR:AspectList_InventoryAbilityAspectData',
        'Abilities',
        '()'
        )
        mod.newline()

        mod.comment('Flavor Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/UIStat_RedText_HeatDamage',
        'Text',
        "[Flavor]I'm Just A Happy Camper![/Flavor]                                               +30% [skillbold]Damage Reduction[/skillbold] but -10% [skillbold]Movement Speed[/skillbold]."
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Name_COV_AR_HeatDamage',
        'PartName',
        "The Bateman"
        )
        mod.newline()

        mod.comment('Making it a Blue')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('It Can Drop at Level 1')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR',
        'Manufacturers.Manufacturers[0].GameStageWeight.MinGameStage.BaseValueConstant',
        1.0
        )
        mod.newline()

        mod.comment('Shivs Pool')
        mod.reg_hotfix(Mod.CHAR,'BPChar_PsychoBadassPrologue',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Shiv',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )     
        )
        """
        )
        mod.newline()

        mod.comment('Shivs Pool')
        mod.reg_hotfix(Mod.CHAR,'BPChar_PsychoBadassPrologue',
        '/Game/Enemies/Psycho_Male/_Unique/BadassPrologue/_Design/Character/BPChar_PsychoBadassPrologue.BPChar_PsychoBadassPrologue_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """
        (
            ItemPools=
            (
                (
                    ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Shiv.ItemPool_Shiv\"',
                    PoolProbability=(BaseValueConstant=0.25),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1.0)
                )
            ),
            ItemPoolLists=(/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear)
        )
        """
        )
        mod.newline()
  
    mod.comment("Demoskaggon's Grenade Mod")
    if True :

        mod.comment('Damage')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Parts/Part_GM_Aug_Fastball',
        'InventoryAttributeEffects',
        """
        (
            (
                AttributeToModify=GbxAttributeData'"/Game/Gear/GrenadeMods/_Design/Attributes/Att_Grenade_IgnoreDeliveryName.Att_Grenade_IgnoreDeliveryName"',
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
            ),
            (
                AttributeToModify=GbxAttributeData'"/Game/Gear/GrenadeMods/_Design/Attributes/Att_GrenadeMod_Damage.Att_GrenadeMod_Damage"',
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=None,BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=6.0)
            ),
            (
                AttributeToModify=GbxAttributeData'"/Game/Gear/GrenadeMods/_Design/Attributes/Att_Grenade_ImpactFuseTime.Att_Grenade_ImpactFuseTime"',
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0.0)
            ),
            (
                AttributeToModify=GbxAttributeData'"/Game/Gear/GrenadeMods/_Design/Attributes/Att_GrenadeMod_ExplosionRadius.Att_GrenadeMod_ExplosionRadius"',
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=0.5)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Removing the damage buff')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Parts/Part_GM_Aug_Fastball',
        'AspectList.AspectList[1]',
        '()'
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Name/UIStat_GM_Icon_Fastball',
        'Text',
        "Comet"
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/GrenadeMods/_Design/Naming/GrenadeModNamingStrategy.GrenadeModNamingStrategy:NamePart_InventoryNamePartData_10',
        'PartName',
        "Comet"
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Name/UIStat_RedText_Fastball',
        'Text',
        "[Flavor]Unidentified Flying Object.[/Flavor]                                          Grenade launches in a straight line and has no [skillbold]Fuse Time[/skillbold]."
        )
        mod.newline()

        mod.comment('MAking it a blue')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Demoskaggon Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_DemoSkaggon',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball.InvBalD_GM_TED_Fastball,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball.InvBalD_GM_TED_Fastball\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Demoskaggon Pool')
        mod.reg_hotfix(Mod.PATCH,'',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions.CharacterExpansions_Value[61].DropOnDeathItemPools.DropOnDeathItemPools[0].PoolProbability',
        '(BaseValueConstant=1.0)'
        )
        mod.newline()

        mod.comment('Demoskaggon Pool Probability')
        mod.reg_hotfix(Mod.CHAR,'BPChar_Skag_Rare01',
        '/Game/Enemies/Skag/_Unique/Rare01/_Design/Character/BPChar_Skag_Rare01.BPChar_Skag_Rare01_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """
        (
            ItemPools=(
                (
                    ItemPool=/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_DemoSkaggon,
                    PoolProbability=(BaseValueConstant=0.25),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1.0)
                )
            )
        )
        """
        )
        mod.newline()

    mod.comment("Lavender Crawly's Pistol")
    if True :

        mod.comment('AttributeEffects')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc',
        'InventoryAttributeEffects',
        """
        (
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.85)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Spread.Att_Weapon_Spread,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.25)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_RecoilWidthScale.Att_Weapon_RecoilWidthScale,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.25)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_RecoilZoomScale.Att_Weapon_RecoilZoomScale,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.25)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo.Att_Weapon_MaxLoadedAmmo,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=3.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Removing the Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc',
        'GestaltMeshPartName',
        'None'
        )
        mod.newline()

        mod.comment('Fire Rate')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc.Part_PS_JAK_Barrel_Doc:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_JAK',
        'FireRate',
        '(Value=14.0,BaseValue=14.0)'
        )
        mod.newline()

        mod.comment('Burst Count')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc.Part_PS_JAK_Barrel_Doc:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_JAK',
        'AutomaticBurstCount',
        '(Value=3.0,BaseValue=3.0)'
        )
        mod.newline()

        mod.comment('Burst Delay')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Parts/Part_PS_JAK_Barrel_Doc.Part_PS_JAK_Barrel_Doc:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_JAK',
        'BurstFireDelay',
        '(Value=0.1,BaseValue=0.1)'
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Name_JAK_PS_Doc',
        'PartName',
        'Triolet'
        )
        mod.newline()

        mod.comment('Flavor Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/UIStat_RedText_Doc',
        'Text',
        "[Flavor]1, 2, 3.[/Flavor]                                                                          Shoots in a [skillbold]Three Round Burst[/skillbold]. Triples the [skillbold]Magazine Size[/skillbold]."
        )
        mod.newline()

        mod.comment('Rarity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Crawly Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/GameData/Loot/ItemPools/Unique/ItemPool_PredatoryLending_CrawlyFamily',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Pool Probability')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds',
        'LavenderCrawly',
        'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
        0.25
        )
        mod.newline()

        mod.comment('Removing the item expansion')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/ItemPoolExpansion_PredatoryLending_CrawlyFamily',
        'BalancedItems',
        '()'
        )
        mod.newline()

    mod.comment("Dumptruck's Shotgun")
    if True :

        mod.comment('Projectile Speed')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Projectile_TED_SG_Sludge.Projectile_TED_SG_Sludge_C:GbxProjectileMovement_GEN_VARIABLE',
        'InitialSpeed',
        4000.0
        )
        mod.newline()

        mod.comment('Projectile Velocity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Projectile_TED_SG_Sludge.Projectile_TED_SG_Sludge_C:GbxProjectileMovement_GEN_VARIABLE',
        'Velocity',
        '(X=1.0,Y=0.0,Z=0.0)'
        )
        mod.newline()

        mod.comment('Projectile Gravity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Projectile_TED_SG_Sludge.Projectile_TED_SG_Sludge_C:GbxProjectileMovement_GEN_VARIABLE',
        'ProjectileGravityScale',
        0.2
        )
        mod.newline()

        mod.comment('Projectile Explosion after the fuse time')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Projectile_TED_SG_Sludge.Default__Projectile_TED_SG_Sludge_C',
        'bExplodeAfterLifetime',
        'false'
        )
        mod.newline()

        mod.comment('AttributeEffects')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Barrel_Sludge',
        'InventoryAttributeEffects',
        """
        (
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=2.0)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_DamageRadius.Att_Weapon_DamageRadius,
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=250.0)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo.Att_Weapon_MaxLoadedAmmo,
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=12.0)
            ),
            (
                AttributeToModify=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_DamageScale.Att_TED_DamageScale,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=2.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Fire Rate')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Barrel_Sludge.Part_SG_TED_Barrel_Sludge:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
        'FireRate',
        '(Value=3.0,BaseValue=3.0)'
        )
        mod.newline()

        mod.comment('Ammo Cost')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Parts/Part_SG_TED_Barrel_Sludge.Part_SG_TED_Barrel_Sludge:AspectList_WeaponUseModeAspectData.WeaponUseComponent_WeaponFireProjectileComponent',
        'ShotAmmoCost',
        '(Value=1.0,BaseValue=1.0)'
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Name_TED_SG_SLudge',
        'PartName',
        'Horn Of Plenty'
        )
        mod.newline()

        mod.comment('Flavor Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/UIStat_RedText_Sludge',
        'Text',
        "[Flavor]Craterellus Cornucopioides.[/Flavor]                                                                          Shoots [skillbold]Grenade Blobs[/skillbold] that stick where they land. Upon reloading, the [skillbold]Grenade Blobs[/skillbold] will home to the thrown gun."
        )
        mod.newline()

        mod.comment('Rarity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Dumptruck Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_HolyDumptruck',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Dumptruck Pool Probability')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions.CharacterExpansions_Value[43].DropOnDeathItemPools.DropOnDeathItemPools[0].PoolProbability',
        '(BaseValueConstant=1.0)'
        )
        mod.newline()

        mod.comment('Dumptruck Pool Probability')
        mod.reg_hotfix(Mod.CHAR,'BPChar_Enforcer_BountyPrologue',
        '/Game/Enemies/Enforcer/_Unique/BountyPrologue/_Design/Character/BPChar_Enforcer_BountyPrologue.BPChar_Enforcer_BountyPrologue_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """
        (
            ItemPools=(
                (
                    ItemPool=/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_HolyDumptruck.ItemPool_HolyDumptruck,
                    PoolProbability=(BaseValueConstant=0.25),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=1.0)
                )
            ),
            ItemPoolLists=(/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear)
        )
        """
        )
        mod.newline()

    mod.comment("Undertaker's Sniper")
    if True :

        mod.comment('Orb Projectile Speed')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD_Orb.Projectile_MAL_SR_ASMD_Orb_C:GbxProjectileMovement_GEN_VARIABLE',
        'InitialSpeed',
        750.0
        )
        mod.newline()

        mod.comment('Orb Projectile Gravity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD_Orb.Projectile_MAL_SR_ASMD_Orb_C:GbxProjectileMovement_GEN_VARIABLE',
        'ProjectileGravityScale',
        -0.2
        )
        mod.newline()

        mod.comment('Orb Projectile Size')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD_Orb.Projectile_MAL_SR_ASMD_Orb_C:ParticleSystem_GEN_VARIABLE',
        'RelativeScale3D',
        '(X=15.0,Y=15.0,Z=15.0)'
        )
        mod.newline()

        mod.comment('Orb Projectile Effect')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD_Orb.Projectile_MAL_SR_ASMD_Orb_C:ParticleSystem_GEN_VARIABLE',
        'Template',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/Effects/Tracers/PS_MAL_SMG_Plasma_Fire.PS_MAL_SMG_Plasma_Fire'
        )
        mod.newline()

        mod.comment('Projectile Effect')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD.Projectile_MAL_SR_ASMD_C:ParticleSystem_GEN_VARIABLE',
        'Template',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/Effects/Tracers/PS_MAL_SR_Laser_Fire.PS_MAL_SR_Laser_Fire'
        )
        mod.newline()

        mod.comment('Orb Projectile Velocity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD_Orb.Projectile_MAL_SR_ASMD_Orb_C:GbxProjectileMovement_GEN_VARIABLE',
        'Velocity',
        '(X=1.0,Y=0.0,Z=0.0)'
        )
        mod.newline()

        mod.comment('Projectile Explosion after the fuse time')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Projectile_MAL_SR_ASMD_Orb.Default__Projectile_MAL_SR_ASMD_Orb_C',
        'DamageRadius',
        '(Value=3000.0,BaseValue=3000.0)'
        )
        mod.newline()

        mod.comment('Removing the Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD',
        'GestaltMeshPartName',
        'None'
        )
        mod.newline()

        mod.comment('AspectList')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD',
        'AspectList.AspectList[8]',
        'None'
        )
        mod.newline()

        mod.comment('Barrel Priority')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD.Part_MAL_SR_Barrel_ASMD:WeaponUseModeAspectData_0',
        'Priority',
        'High'
        )
        mod.newline()

        mod.comment('Fire Damage')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD.Part_MAL_SR_Barrel_ASMD:AspectList_WeaponDamageTypeAspectData',
        'DamageType',
        '/Game/GameData/DamageTypes/Fire/DmgType_Fire_Impact.DmgType_Fire_Impact_C'
        )
        mod.newline()

        mod.comment('Fire Damage')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD.Part_MAL_SR_Barrel_ASMD:AspectList_WeaponDamageTypeAspectData',
        'ImpactData',
        '/Game/GameData/Impacts/Impact_Bullet_MAL_Fire.Impact_Bullet_MAL_Fire'
        )
        mod.newline()

        mod.comment('AttributeEffects')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Parts/Part_MAL_SR_Barrel_ASMD',
        'WeaponUseModeAttributeEffects',
        """
        (
            (
                UseMode=EWeaponUseMode::EWeaponUseMode_MAX,
                UseModeBitmask=3,
                AttributeEffects=
                    (
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_SwitchModeTimeScale.Att_Weapon_SwitchModeTimeScale,
                            ModifierType=ScaleSimple,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.5)
                        ),
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ChargeTime.Att_Weapon_ChargeTime,
                            ModifierType=ScaleSimple,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.1)
                        ),
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ZoomDurationScale.Att_Weapon_ZoomDurationScale,
                            ModifierType=ScaleSimple,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.5)
                        ),
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Spread.Att_Weapon_Spread,
                            ModifierType=ScaleSimple,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.1)
                        )
                    )
            ),
            (
                UseMode=EWeaponUseMode::EWeaponUseMode_MAX,
                UseModeBitmask=1,
                AttributeEffects=
                    (
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage,
                            ModifierType=ScaleSimple,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=3.0)
                        ),
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_DamageRadius.Att_Weapon_DamageRadius,
                            ModifierType=OverrideBaseValue,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=350.0)
                        ),
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost.Att_Weapon_ShotAmmoCost,
                            ModifierType=PreAdd,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=4.0)
                        )
                    )
            ),
            (
                UseMode=EWeaponUseMode::EWeaponUseMode_MAX,
                UseModeBitmask=2,
                AttributeEffects=
                    (
                        (
                            AttributeToModify=/Game/GameData/Weapons/Att_Weapon_DamageRadius.Att_Weapon_DamageRadius,
                            ModifierType=OverrideBaseValue,
                            ModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.0)
                        )
                    )
            )
        )
        """
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Name_MAL_SR_ASMD',
        'PartName',
        'Forbidden Sun'
        )
        mod.newline()

        mod.comment('Flavor Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/UIStat_RedText_ASMD',
        'Text',
        "[Flavor]Such Excessive Destructive Power.[/Flavor]                                                                          Shoots [skillbold]Energy Orbs[/skillbold]. Shooting the [skillbold]Energy Orbs[/skillbold] will make them explode."
        )
        mod.newline()

        mod.comment('Rarity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Undertaker Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Undertaker',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Undertaker Pool Probability')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions.CharacterExpansions_Value[87].DropOnDeathItemPools.DropOnDeathItemPools[0].PoolProbability',
        '(BaseValueConstant=0.0)'
        )
        mod.newline()

        mod.comment('Undertaker Pool Probability')
        mod.reg_hotfix(Mod.CHAR,'BPChar_TinkUndertaker',
        '/Game/Enemies/Tink/_Unique/Undertaker/_Design/Character/BPChar_TinkUndertaker.BPChar_TinkUndertaker_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """
        (
            ItemPools=(
                (
                    ItemPool=/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Undertaker.ItemPool_Undertaker,
                    PoolProbability=(BaseValueConstant=1.0),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=0.25)
                )
            ),
            ItemPoolLists=(/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear)
        )
        """
        )
        mod.newline()

    mod.comment("Trufflemunch's Pitol")
    if True :

        mod.comment('Firing Pattern')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/LightProjectile_TOR_PS_HeckleHyde_Default_C.Default__LightProjectile_TOR_PS_HeckleHyde_Default_C',
        'Speed',
        4000.0
        )
        mod.newline()

        mod.comment('Firing Pattern')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/FiringPattern_Heckle',
        'bScalePattern',
        'false'
        )
        mod.newline()

        mod.comment('Firing Pattern')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/FiringPattern_Heckle',
        'Samples',
        """
        (
            (
                StartRotation=(pitch=-2.0,yaw=-1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=1
            ),
            (
                StartRotation=(pitch=-2.0,yaw=1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=2
            ),
            (
                StartRotation=(pitch=-1.0,yaw=-1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=3
            ),
            (
                StartRotation=(pitch=-1.0,yaw=1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=4
            ),
            (
                StartRotation=(pitch=0.0,yaw=-1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=5
            ),
            (
                StartRotation=(pitch=0.0,yaw=1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=6
            ),
            (
                StartRotation=(pitch=1.0,yaw=-1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=7
            ),
            (
                StartRotation=(pitch=1.0,yaw=1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=8
            ),
            (
                StartRotation=(pitch=2.0,yaw=-1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=9
            ),
            (
                StartRotation=(pitch=2.0,yaw=1.5,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=10
            )
        )
        """
        )
        mod.newline()

        mod.comment('Projectile Count')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Heckle',
        'ProjectilesPerShot',
        '(Value=10.0,BaseValue=10.0)'
        )
        mod.newline()

        mod.comment('Projectile Count')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Heckle',
        'DefaultProjectilePerShot',
        10.0
        )
        mod.newline()

        mod.comment('Auto Firing Mode')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Heckle',
        'AutomaticBurstCount',
        '(Value=0.0,BaseValue=0.0)'
        )
        mod.newline()

        mod.comment('Auto Firing Mode')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Heckle',
        'FireRate',
        '(Value=2.0,BaseValue=2.0)'
        )
        mod.newline()

        mod.comment('Element')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Heckle',
        'DefaultDamageType',
        'None'
        )
        mod.newline()

        mod.comment('Element')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle.Part_PS_TOR_Barrel_Heckle:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Heckle',
        'PowerElement',
        'None'
        )
        mod.newline()

        mod.comment('Removing The Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle',
        'GestaltMeshPartName',
        'None'
        )
        mod.newline()

        mod.comment('AttributeEffects')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Parts/Part_PS_TOR_Barrel_Heckle',
        'InventoryAttributeEffects',
        """
        (
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.4)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot.Att_Weapon_ProjectilesPerShot,
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=10.0)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost.Att_Weapon_ShotAmmoCost,
                ModifierType=PreAdd,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo.Att_Weapon_MaxLoadedAmmo,
                ModifierType=PreAdd,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=4.0)
            ),
            (
                AttributeToModify=/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_OverrideManufacturerDescription.Att_Weapon_OverrideManufacturerDescription,
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )   
        )
        """
        )
        mod.newline()

        mod.comment('Rarity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Name_TOR_PS_Heckle',
        'PartName',
        'Vertical Axis'
        )
        mod.newline()

        mod.comment('Red Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/UIStat_RedText_Heckle',
        'Text',
        "[Flavor]X^10.[/Flavor]                                                                     Shoots [skillbold]Two Vertical Lines[/skillbold]."
        )
        mod.newline()

        mod.comment('Trufflemunch Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Trufflemunch',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Trufflemunch Pool Probability')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions.CharacterExpansions_Value[89].DropOnDeathItemPools.DropOnDeathItemPools[0].PoolProbability',
        '(BaseValueConstant=0.0)'
        )
        mod.newline()

        mod.comment('Trufflemunch Pool Probability')
        mod.reg_hotfix(Mod.CHAR,'BPChar_SkagTrufflemunch',
        '/Game/Enemies/Skag/_Unique/Trufflemunch/_Design/Character/BPChar_SkagTrufflemunch.BPChar_SkagTrufflemunch_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """
        (
            ItemPools=(
                (
                    ItemPool=/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Trufflemunch.ItemPool_Trufflemunch,
                    PoolProbability=(BaseValueConstant=1.0),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=0.25)
                )
            ),
            ItemPoolLists=(/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear)
        )
        """
        )
        mod.newline()

    mod.comment("Buttmunch's Pitol")
    if True :

        mod.comment('Firing Pattern')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/FiringPattern_Hyde',
        'bScalePattern',
        'false'
        )
        mod.newline()

        mod.comment('Firing Pattern')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/FiringPattern_Hyde',
        'Samples',
        """
        (
            (
                StartRotation=(pitch=-1.5,yaw=-2.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=1
            ),
            (
                StartRotation=(pitch=1.5,yaw=-2.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=2
            ),
            (
                StartRotation=(pitch=-1.5,yaw=-1.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=3
            ),
            (
                StartRotation=(pitch=1.5,yaw=-1.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=4
            ),
            (
                StartRotation=(pitch=-1.5,yaw=0.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=5
            ),
            (
                StartRotation=(pitch=1.5,yaw=0.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=6
            ),
            (
                StartRotation=(pitch=-1.5,yaw=1.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=7
            ),
            (
                StartRotation=(pitch=1.5,yaw=1.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=8
            ),
            (
                StartRotation=(pitch=-1.5,yaw=2.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=9
            ),
            (
                StartRotation=(pitch=1.5,yaw=2.0,roll=0.0),
                bUseEndRotation=false,
                bUseID=true,
                ID=10
            )
        )
        """
        )
        mod.newline()

        mod.comment('Projectile Count')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Hyde',
        'ProjectilesPerShot',
        '(Value=10.0,BaseValue=10.0)'
        )
        mod.newline()

        mod.comment('Projectile Count')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Hyde',
        'DefaultProjectilePerShot',
        10.0
        )
        mod.newline()

        mod.comment('Auto Firing Mode')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Hyde',
        'AutomaticBurstCount',
        '(Value=0.0,BaseValue=0.0)'
        )
        mod.newline()

        mod.comment('Auto Firing Mode')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Hyde',
        'FireRate',
        '(Value=2.0,BaseValue=2.0)'
        )
        mod.newline()

        mod.comment('Element')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Hyde',
        'DefaultDamageType',
        'None'
        )
        mod.newline()

        mod.comment('Element')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde.Part_PS_TOR_Barrel_Hyde:WeaponUseModeAspectData_0.WeaponUseComponent_BPWeaponFireProjectileComponent_Hyde',
        'PowerElement',
        'None'
        )
        mod.newline()

        mod.comment('Removing The Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde',
        'GestaltMeshPartName',
        'None'
        )
        mod.newline()

        mod.comment('Removing The Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde',
        'AspectList.AspectList[2]',
        'None'
        )
        mod.newline()

        mod.comment('Removing The Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde',
        'AspectList.AspectList[3]',
        'None'
        )
        mod.newline()

        mod.comment('Removing The Mesh')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde',
        'AspectList.AspectList[5]',
        'None'
        )
        mod.newline()


        mod.comment('AttributeEffects')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Parts/Part_PS_TOR_Barrel_Hyde',
        'InventoryAttributeEffects',
        """
        (
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_Damage.Att_Weapon_Damage,
                ModifierType=ScaleSimple,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=0.4)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot.Att_Weapon_ProjectilesPerShot,
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=10.0)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost.Att_Weapon_ShotAmmoCost,
                ModifierType=PreAdd,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                AttributeToModify=/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo.Att_Weapon_MaxLoadedAmmo,
                ModifierType=PreAdd,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=4.0)
            ),
            (
                AttributeToModify=/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_OverrideManufacturerDescription.Att_Weapon_OverrideManufacturerDescription,
                ModifierType=OverrideBaseValue,
                ModifierValue=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )   
        )
        """
        )
        mod.newline()

        mod.comment('Rarity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Name_TOR_PS_Hyde',
        'PartName',
        'Horizontal Axis'
        )
        mod.newline()

        mod.comment('Red Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/UIStat_RedText_Hyde',
        'Text',
        "[Flavor]Y^10.[/Flavor]                                                                     Shoots [skillbold]Two Horizontal Lines[/skillbold]."
        )
        mod.newline()

        mod.comment('Buttmunch Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Buttmunch',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            )
        )
        """
        )
        mod.newline()

        mod.comment('Buttmunch Pool Probability')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1',
        'CharacterExpansions.CharacterExpansions_Value[88].DropOnDeathItemPools.DropOnDeathItemPools[0].PoolProbability',
        '(BaseValueConstant=0.0)'
        )
        mod.newline()

        mod.comment('Buttmunch Pool Probability')
        mod.reg_hotfix(Mod.CHAR,'BPChar_SkagButtmunch',
        '/Game/Enemies/Skag/_Unique/Buttmunch/_Design/Character/BPChar_SkagButtmunch.BPChar_SkagButtmunch_C:AIBalanceState_GEN_VARIABLE',
        'DropOnDeathItemPools',
        """
        (
            ItemPools=(
                (
                    ItemPool=/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Buttmunch.ItemPool_Buttmunch,
                    PoolProbability=(BaseValueConstant=1.0),
                    NumberOfTimesToSelectFromThisPool=(BaseValueConstant=0.25)
                )
            ),
            ItemPoolLists=(/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear)
        )
        """
        )
        mod.newline()

    mod.comment("Mincemeat's Shield")
    if True :

        mod.comment('Capacity')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/Balance/ShieldAug_Unique_BalanceData',
        'LGD_WhiskeyTangoFoxtrot',
        'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
        0.2
        )
        mod.newline()

        mod.comment('Recharge Rate')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/Balance/ShieldAug_Unique_BalanceData',
        'LGD_WhiskeyTangoFoxtrot',
        'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
        0.15
        )
        mod.newline()

        mod.comment('IED Cooldown')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/ShieldAug_WTF.Default__ShieldAug_WTF_C',
        'ReceivedDamageEventData.TriggerCooldown',
        '(BaseValueConstant=1.0,BaseValueScale=1.0)'
        )
        mod.newline()

        mod.comment('IED Fuse')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Default__Proj_WhiskeyTangoFoxtrotIED_C',
        'FuseTime',
        3.0
        )
        mod.newline()

        mod.comment('IED Radius')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Default__Proj_WhiskeyTangoFoxtrotIED_C',
        'IED_Radius',
        100.0
        )
        mod.newline()

        mod.comment('IED Speed')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Proj_WhiskeyTangoFoxtrotIED_C:GbxProjectileMovement_GEN_VARIABLE',
        'InitialSpeed',
        1000.0
        )
        mod.newline()

        mod.comment('IED Gravity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Proj_WhiskeyTangoFoxtrotIED_C:GbxProjectileMovement_GEN_VARIABLE',
        'ProjectileGravityScale',
        0.6
        )
        mod.newline()

        mod.comment('IED Velocity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Proj_WhiskeyTangoFoxtrotIED_C:GbxProjectileMovement_GEN_VARIABLE',
        'Velocity',
        '(X=1.0,Y=0.0,Z=0.0)'
        )
        mod.newline()

        mod.comment('IED Particle')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Proj_WhiskeyTangoFoxtrotIED_C:FX_Proximity_GEN_VARIABLE',
        'Template',
        '/Game/Gear/Artifacts/Effects/Systems/Slide/Cryo/PS_Snowdrift_Cryo_Iceball.PS_Snowdrift_Cryo_Iceball'
        )
        mod.newline()

        mod.comment('IED Particle')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Proj_WhiskeyTangoFoxtrotIED.Proj_WhiskeyTangoFoxtrotIED_C:FX_Proximity_GEN_VARIABLE',
        'RelativeScale3D',
        '(X=0.8,Y=0.8,Z=0.8)'
        )
        mod.newline()

        mod.comment('IED Damage')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Att_ShieldAug_WhiskeyTangoFoxtrot_Value_Damage.Att_ShieldAug_WhiskeyTangoFoxtrot_Value_Damage:ValueResolver_ShieldAugmentValueResolver',
        'ValueB',
        '(BaseValueAttribute=/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity.Att_ShieldBalance_Capacity)'
        )
        mod.newline()

        mod.comment('IED Damage')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/Balance/ShieldAug_Unique_BalanceData',
        'LGD_WhiskeyTangoFoxtrot',
        'Primary_1_56_207C26E1450330458D6C38B245C338C5',
        0.65
        )
        mod.newline()

        mod.comment('IED Chance')
        mod.table_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/Balance/ShieldAug_Unique_BalanceData',
        'LGD_WhiskeyTangoFoxtrot',
        'Secondary_1_62_F1E72F2542B441230290B388F4C494D1',
        0.5
        )
        mod.newline()

        mod.comment('Rarity')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
        'RarityData',
        '/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare'
        )
        mod.newline()

        mod.comment('Manufacturer')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
        'Manufacturers.Manufacturers[0].ManufacturerData',
        '/Game/Gear/Manufacturers/_Design/Hyperion.Hyperion'
        )
        mod.newline()

        mod.comment('Manufacturer')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
        'BaseSelectionData',
        '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion.InvBalD_Shield_Hyperion'
        )
        mod.newline()

        mod.comment('Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/Naming/ShieldNamingStrategy.ShieldNamingStrategy:NamePart_InventoryNamePartData_226',
        'PartName',
        'Snowman'
        )
        mod.newline()

        mod.comment('Augment Name')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Name/UIStat_Shield_Icon_WTF',
        'Text',
        'SNOW'
        )
        mod.newline()

        mod.comment('Red Text')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Name/UIStat_RedText_WTF',
        'Text',
        "[Flavor]Snowball Fight.[/Flavor]"
        )
        mod.newline()

        mod.comment('Description')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/UIStat_Shield_AugDescription_WhiskeyTangoFoxtrot',
        'FormatText',
        "While shielded, you have [skillbold]$VALUE$[/skillbold] chance to launch [skillbold]3 Snowballs[/skillbold] when damaged that deal"
        )
        mod.newline()

        mod.comment('Description')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Parts/Part_Shield_Aug_ANS_LGD_WTF',
        'InventoryAttributeEffects',
        '()'
        )
        mod.newline()

        mod.comment('Description')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/UIStat_Shield_AugDescription_WhiskeyTangoFoxtrot.UIStat_Shield_AugDescription_WhiskeyTangoFoxtrot:SupplementalStat_UIStatData_Attribute',
        'FormatText',
        "[skillbold]$VALUE$[/skillbold] damage."
        )
        mod.newline()

        mod.comment('Mincemeat Pool')
        mod.reg_hotfix(Mod.LEVEL,'MatchAll',
        '/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Mincemeat',
        'BalancedItems',
        """
        (
            (
                InventoryBalanceData=/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot.InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot,
                ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot.InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot\"',
                Weight=(BaseValueConstant=1.0,BaseValueScale=1.0)
            ),
            (
                ItemPoolData=/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All.ItemPool_Guns_All,
                Weight=(BaseValueConstant=1.0,BaseValueScale=0.0)
            )
        )
        """
        )
        mod.newline()

