from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('Grenade.bl3hotfix',
'Grenade Changes',
'Grimm',
[
    'Complete rebalance for all grenades.',
    'Grenades are now more powerfull.',
    'Having the same parts on the grenade boost the effect even further than before',
    'Two parts is twice as good as one part, and three parts is twice as good as two parts.',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'

],
lic=Mod.CC_BY_SA_40,
)

grenadetype='/Game/Gear/GrenadeMods/_Design/Balance/Grenade_Balance_Table'
grenademods='/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Balance_Table'
grenademodsunique='/Game/Gear/GrenadeMods/_Design/Balance/GrenadeMod_Unique_Balance_Table'
jackpot='/Game/PatchDLC/Dandelion/Gear/Grenade/GrenadeMod_Dandelion_Table'
bounty='/Game/PatchDLC/Geranium/Gear/Grenade/GrenadeMod_Geranium_Table'
tk2='/Game/PatchDLC/Takedown2/Gear/GrenadeMods/GrenadeMod_Unique_BalanceTable_Takedown2'

###DLCS

mod.comment('AcidBurn damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'AcidBurn',
'Damage_12_F33DA0994756D761207677A51A156787',
0.5
)
mod.newline()

mod.comment('Slider damage')
mod.table_hotfix(Mod.PATCH, '',
jackpot,
'Slider',
'Damage_12_F33DA0994756D761207677A51A156787',
0.55
)
mod.newline()

mod.comment('CoreBurst damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'CoreBurst',
'Damage_12_F33DA0994756D761207677A51A156787',
1.3
)
mod.newline()

mod.comment('SkagOil damage')
mod.table_hotfix(Mod.PATCH, '',
bounty,
'SkagOil',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.1
)
mod.newline()

mod.comment('DAF_Lightspeed damage')
mod.table_hotfix(Mod.PATCH, '',
tk2,
'DAF_Lightspeed',
'Damage_12_F33DA0994756D761207677A51A156787',
0.25
)
mod.newline()

###UNIQUES

mod.comment('LGD_BouncingBosom damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_BouncingBosom',
'Damage_12_F33DA0994756D761207677A51A156787',
0.3
)
mod.newline()

mod.comment('LGD_Firestorm damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Firestorm',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.5
)
mod.newline()

mod.comment('LGD_Fastball damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Fastball',
'Damage_12_F33DA0994756D761207677A51A156787',
4.0
)
mod.newline()

mod.comment('LGD_EMP damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_EMP',
'Damage_12_F33DA0994756D761207677A51A156787',
0.5
)
mod.newline()

mod.comment('LGD_HipHop damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_HipHop',
'Damage_12_F33DA0994756D761207677A51A156787',
0.3
)
mod.newline()

mod.comment('LGD_WidowMaker damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_WidowMaker',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.5
)
mod.newline()

mod.comment('LGD_Surge damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Surge',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.25
)
mod.newline()

mod.comment('LGD_Nagate damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Nagate',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.8
)
mod.newline()

mod.comment('LGD_Quasar damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Quasar',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.7
)
mod.newline()

mod.comment('LGD_StormFront damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_StormFront',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.5
)
mod.newline()

mod.comment('LGD_HunterSeeker damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_HunterSeeker',
'Damage_12_F33DA0994756D761207677A51A156787',
-1.5
)
mod.newline()

mod.comment('LGD_Kryll damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Kryll',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.8
)
mod.newline()

mod.comment('MSN_Shroom damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'MSN_Shroom',
'Damage_12_F33DA0994756D761207677A51A156787',
0.5
)
mod.newline()

mod.comment('LGD_RedQueen damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_RedQueen',
'Damage_12_F33DA0994756D761207677A51A156787',
0.2
)
mod.newline()

mod.comment('LGD_Epicenter damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Epicenter',
'Damage_12_F33DA0994756D761207677A51A156787',
-1.0
)
mod.newline()

mod.comment('LGD_WizardOfNOG damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_WizardOfNOG',
'Damage_12_F33DA0994756D761207677A51A156787',
0.2
)
mod.newline()

mod.comment('LGD_ECHO2 damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_ECHO2',
'Damage_12_F33DA0994756D761207677A51A156787',
0.8
)
mod.newline()

mod.comment('LGD_Chupa damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_Chupa',
'Damage_12_F33DA0994756D761207677A51A156787',
0
)
mod.newline()

mod.comment('LGD_TranFusion damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'LGD_TranFusion',
'Damage_12_F33DA0994756D761207677A51A156787',
0.4
)
mod.newline()

mod.comment('Piss damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'Piss',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.45
)
mod.newline()

mod.comment('ObviousTrap damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'ObviousTrap',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.2
)
mod.newline()

mod.comment('BirthdaySuprise damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'BirthdaySuprise',
'Damage_12_F33DA0994756D761207677A51A156787',
1.0
)
mod.newline()

mod.comment('Cupcake damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'Cupcake',
'Damage_12_F33DA0994756D761207677A51A156787',
1.8
)
mod.newline()

mod.comment('Toiletbombs damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'Toiletbombs',
'Damage_12_F33DA0994756D761207677A51A156787',
0.3
)
mod.newline()

mod.comment('Seeker damage')
mod.table_hotfix(Mod.PATCH, '',
grenademodsunique,
'Seeker',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.4
)
mod.newline()

###GRENADE MODS

mod.comment('MIRV damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.8
)
mod.newline()

mod.comment('MIRV one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
2.0
)
mod.newline()

mod.comment('MIRV double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
4.0
)
mod.newline()

mod.comment('MIRV triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
8.0
)
mod.newline()

mod.comment('Lingering damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.4
)
mod.newline()

mod.comment('Lingering one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
3.0
)
mod.newline()

mod.comment('Lingering double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
6.0
)
mod.newline()

mod.comment('Lingering triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
12.0
)
mod.newline()

mod.comment('Lingering one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Secondary_1_17_518A093F48377625749592BEC8275DC6',
3.0
)
mod.newline()

mod.comment('Lingering double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Secondary_2_18_AB999387440701CC75633C917E78FD7B',
6.0
)
mod.newline()

mod.comment('Lingering triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Lingering',
'Secondary_3_19_ACA59F5242FD94CFBAB2418760866307',
12.0
)
mod.newline()

mod.comment('Sticky damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Sticky',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.1
)
mod.newline()

mod.comment('Sticky one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Sticky',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
1.0
)
mod.newline()

mod.comment('Sticky double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Sticky',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
2.0
)
mod.newline()

mod.comment('Sticky triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Sticky',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
4.0
)
mod.newline()

mod.comment('Bouncy damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Bouncy',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.15
)
mod.newline()

mod.comment('Bouncy one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Bouncy',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
3.0
)
mod.newline()

mod.comment('Bouncy double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Bouncy',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
6.0
)
mod.newline()

mod.comment('Bouncy triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Bouncy',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
12.0
)
mod.newline()

mod.comment('Singularity damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Singularity',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.3
)
mod.newline()

mod.comment('Singularity radius')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Singularity',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
0.5
)
mod.newline()

mod.comment('Singularity one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Singularity',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
1.0
)
mod.newline()

mod.comment('Singularity double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Singularity',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
2.0
)
mod.newline()

mod.comment('Singularity triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Singularity',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
4.0
)
mod.newline()

mod.comment('Transfusion damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Transfusion',
'Damage_12_F33DA0994756D761207677A51A156787',
0.2
)
mod.newline()

mod.comment('Transfusion one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Transfusion',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.3
)
mod.newline()

mod.comment('Transfusion double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Transfusion',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.6
)
mod.newline()

mod.comment('Transfusion triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Transfusion',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
1.2
)
mod.newline()

mod.comment('Large damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Large',
'Damage_12_F33DA0994756D761207677A51A156787',
0.2
)
mod.newline()

mod.comment('Large one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Large',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.4
)
mod.newline()

mod.comment('Large double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Large',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.8
)
mod.newline()

mod.comment('Large triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Large',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
1.6
)
mod.newline()

mod.comment('Spring damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.4
)
mod.newline()

mod.comment('Spring one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
1.0
)
mod.newline()

mod.comment('Spring double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
2.0
)
mod.newline()

mod.comment('Spring triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
4.0
)
mod.newline()

mod.comment('Spring one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Secondary_1_17_518A093F48377625749592BEC8275DC6',
1.1
)
mod.newline()

mod.comment('Spring double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Secondary_2_18_AB999387440701CC75633C917E78FD7B',
1.2
)
mod.newline()

mod.comment('Spring triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Spring',
'Secondary_3_19_ACA59F5242FD94CFBAB2418760866307',
1.4
)
mod.newline()

mod.comment('MIRV_MIRV damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV_MIRV',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.3
)
mod.newline()

mod.comment('MIRV_MIRV one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV_MIRV',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
3.0
)
mod.newline()

mod.comment('MIRV_MIRV double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV_MIRV',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
6.0
)
mod.newline()

mod.comment('MIRV_MIRV triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'MIRV_MIRV',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
12.0
)
mod.newline()

mod.comment('Money damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Money',
'Damage_12_F33DA0994756D761207677A51A156787',
0.8
)
mod.newline()

mod.comment('Money one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Money',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
3.0
)
mod.newline()

mod.comment('Money double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Money',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
6.0
)
mod.newline()

mod.comment('Money triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Money',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
12.0
)
mod.newline()

mod.comment('Generator damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Generator',
'Damage_12_F33DA0994756D761207677A51A156787',
0.15
)
mod.newline()

mod.comment('Generator one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Generator',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.3
)
mod.newline()

mod.comment('Generator double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Generator',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.6
)
mod.newline()

mod.comment('Generator triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Generator',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
1.2
)
mod.newline()

mod.comment('Nuke damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Nuke',
'Damage_12_F33DA0994756D761207677A51A156787',
0.6
)
mod.newline()

mod.comment('Nuke one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Nuke',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
1.0
)
mod.newline()

mod.comment('Nuke double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Nuke',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
2.0
)
mod.newline()

mod.comment('Nuke triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Nuke',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
3.0
)
mod.newline()

mod.comment('Artillery damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Artillery',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.4
)
mod.newline()

mod.comment('Artillery one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Artillery',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.15
)
mod.newline()

mod.comment('Artillery double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Artillery',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.3
)
mod.newline()

mod.comment('Artillery triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Artillery',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
0.6
)
mod.newline()

mod.comment('Link damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Link',
'Damage_12_F33DA0994756D761207677A51A156787',
0.3
)
mod.newline()

mod.comment('Link one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Link',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.15
)
mod.newline()

mod.comment('Link double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Link',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.25
)
mod.newline()

mod.comment('Link triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Link',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
0.5
)
mod.newline()

mod.comment('Divider damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Divider',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.4
)
mod.newline()

mod.comment('Divider one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Divider',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
1.0
)
mod.newline()

mod.comment('Divider double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Divider',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
2.0
)
mod.newline()

mod.comment('Divider triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Divider',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
4.0
)
mod.newline()

mod.comment('Roider damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Roider',
'Damage_12_F33DA0994756D761207677A51A156787',
0.25
)
mod.newline()

mod.comment('Roider one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Roider',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.3
)
mod.newline()

mod.comment('Roider double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Roider',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.6
)
mod.newline()

mod.comment('Roider triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Roider',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
1.2
)
mod.newline()

mod.comment('ElementalDamage damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Damage_12_F33DA0994756D761207677A51A156787',
0.15
)
mod.newline()

mod.comment('ElementalDamage one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
0.2
)
mod.newline()

mod.comment('ElementalDamage double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
0.4
)
mod.newline()

mod.comment('ElementalDamage triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
0.8
)
mod.newline()

mod.comment('ElementalDamage one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Secondary_1_17_518A093F48377625749592BEC8275DC6',
0.2
)
mod.newline()

mod.comment('ElementalDamage double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Secondary_2_18_AB999387440701CC75633C917E78FD7B',
0.4
)
mod.newline()

mod.comment('ElementalDamage triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'ElementalDamage',
'Secondary_3_19_ACA59F5242FD94CFBAB2418760866307',
0.8
)
mod.newline()

mod.comment('Rain damage')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Rain',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.5
)
mod.newline()

mod.comment('Rain one part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Rain',
'Primary_1_14_785154D64AF8EEEA12E3F1A63A0B04B6',
2.0
)
mod.newline()

mod.comment('Rain double part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Rain',
'Primary_2_15_2B2EF17E422835A6F855B0B351652BD4',
4.0
)
mod.newline()

mod.comment('Rain triple part')
mod.table_hotfix(Mod.PATCH, '',
grenademods,
'Rain',
'Primary_3_16_1E6ADA3B4212CC38E1A4E59C9B29BBE2',
8.0
)
mod.newline()

###GRENADE TYPE

mod.comment('Exploder damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_Heavy',
'Damage_12_F33DA0994756D761207677A51A156787',
0.3
)
mod.newline()

mod.comment('Exploder radius')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_Heavy',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
0.0
)
mod.newline()

mod.comment('Homing damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_Homing',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.8
)
mod.newline()

mod.comment('Longbow damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_Longbow',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.4
)
mod.newline()

mod.comment('Airboosted damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_AirBoosted',
'Damage_12_F33DA0994756D761207677A51A156787',
0.
)
mod.newline()

mod.comment('Rubberized damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_Rubberized',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.2
)
mod.newline()

mod.comment('Impact damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Manufacturer_Impact',
'Damage_12_F33DA0994756D761207677A51A156787',
-0.1
)
mod.newline()

###RARITY DAMAGE

mod.comment('White damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Common',
'Damage_12_F33DA0994756D761207677A51A156787',
0
)
mod.newline()

mod.comment('White radius')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Common',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
0
)
mod.newline()

mod.comment('White ele chance')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Common',
'ElementalChance_27_7937D4CF4A8DD22697D5E4B2D4C91A2C',
0
)
mod.newline()

mod.comment('White ele damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Common',
'ElementalDamage_29_5B61CFB144632591AA0579A20584A549',
0
)
mod.newline()

mod.comment('Green damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Uncommon',
'Damage_12_F33DA0994756D761207677A51A156787',
0.2
)
mod.newline()

mod.comment('Green radius')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Uncommon',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
0.2
)
mod.newline()

mod.comment('Green ele chance')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Uncommon',
'ElementalChance_27_7937D4CF4A8DD22697D5E4B2D4C91A2C',
0.1
)
mod.newline()

mod.comment('Green ele damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Uncommon',
'ElementalDamage_29_5B61CFB144632591AA0579A20584A549',
0.1
)
mod.newline()

mod.comment('Blue damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Rare',
'Damage_12_F33DA0994756D761207677A51A156787',
0.44
)
mod.newline()

mod.comment('Blue radius')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Rare',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
0.44
)
mod.newline()

mod.comment('Blue ele chance')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Rare',
'ElementalChance_27_7937D4CF4A8DD22697D5E4B2D4C91A2C',
0.2
)
mod.newline()

mod.comment('Blue ele damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Rare',
'ElementalDamage_29_5B61CFB144632591AA0579A20584A549',
0.2
)
mod.newline()

mod.comment('Purple damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_VeryRare',
'Damage_12_F33DA0994756D761207677A51A156787',
0.728
)
mod.newline()

mod.comment('Purple radius')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_VeryRare',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
0.728
)
mod.newline()

mod.comment('Purple ele chance')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_VeryRare',
'ElementalChance_27_7937D4CF4A8DD22697D5E4B2D4C91A2C',
0.3
)
mod.newline()

mod.comment('Purple ele damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_VeryRare',
'ElementalDamage_29_5B61CFB144632591AA0579A20584A549',
0.3
)
mod.newline()

mod.comment('Orange damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Legendary',
'Damage_12_F33DA0994756D761207677A51A156787',
1.037
)
mod.newline()

mod.comment('Orange radius')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Legendary',
'Radius_13_9DDB780D4981106D3843E19FAC0856D3',
1.037
)
mod.newline()

mod.comment('Orange ele chance')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Legendary',
'ElementalChance_27_7937D4CF4A8DD22697D5E4B2D4C91A2C',
0.4
)
mod.newline()

mod.comment('Orange ele damage')
mod.table_hotfix(Mod.PATCH, '',
grenadetype,
'Rarity_Legendary',
'ElementalDamage_29_5B61CFB144632591AA0579A20584A549',
0.4
)
mod.newline()

