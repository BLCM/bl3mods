from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('Shield.bl3hotfix',
'Shield Changes',
'Grimm',
[
    'Complete rebalance for all shields.',
    'Having the same parts on the shield boost the effect even further than before',
    'Two parts is twice as good as one part, and three parts is twice as good as two parts.',
    'Thanks to CodyCode, SsPyR, Apocalyptech, 10 FPS, HackerSmasher, FromDarkHell, Apple1417'
],
lic=Mod.CC_BY_SA_40,
)

shield='/Game/Gear/Shields/_Design/Balance/Shield_BalanceData'
shieldmods='/Game/Gear/Shields/_Design/Balance/ShieldAug_BalanceData'
uniques='/Game/Gear/Shields/_Design/Balance/ShieldAug_Unique_BalanceData'

###MODS BALANCE

mod.comment('Nova capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Nova',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.15
)
mod.newline()

mod.comment('Nova rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Nova',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.1
)
mod.newline()

mod.comment('Nova delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Nova',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.05
)
mod.newline()

mod.comment('Nova one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Nova',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
1.0
)
mod.newline()

mod.comment('Nova double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Nova',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
2.0
)
mod.newline()

mod.comment('Nova triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Nova',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
4.0
)
mod.newline()

mod.comment('Spike capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Spike',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.08
)
mod.newline()

mod.comment('Spike rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Spike',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
-0.05
)
mod.newline()

mod.comment('Spike delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Spike',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.02
)
mod.newline()

mod.comment('Spike one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Spike',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.5
)
mod.newline()

mod.comment('Spike double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Spike',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
1.0
)
mod.newline()

mod.comment('Spike triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Spike',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
2.0
)
mod.newline()

mod.comment('Roid capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Roid',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.15
)
mod.newline()

mod.comment('Roid rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Roid',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
-0.1
)
mod.newline()

mod.comment('Roid delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Roid',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.25
)
mod.newline()

mod.comment('Roid one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Roid',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
1.0
)
mod.newline()

mod.comment('Roid double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Roid',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
2.0
)
mod.newline()

mod.comment('Roid triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Roid',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
4.0
)
mod.newline()

mod.comment('TriggerHappy capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'TriggerHappy',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.15
)
mod.newline()

mod.comment('TriggerHappy rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'TriggerHappy',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
-0.1
)
mod.newline()

mod.comment('TriggerHappy delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'TriggerHappy',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.15
)
mod.newline()

mod.comment('TriggerHappy one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'TriggerHappy',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.1
)
mod.newline()

mod.comment('TriggerHappy double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'TriggerHappy',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.2
)
mod.newline()

mod.comment('TriggerHappy triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'TriggerHappy',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.4
)
mod.newline()

mod.comment('Fleeting capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Fleeting',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.1
)
mod.newline()

mod.comment('Fleeting rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Fleeting',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.05
)
mod.newline()

mod.comment('Fleeting delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Fleeting',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.15
)
mod.newline()

mod.comment('Fleeting one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Fleeting',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.1
)
mod.newline()

mod.comment('Fleeting double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Fleeting',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.2
)
mod.newline()

mod.comment('Fleeting triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Fleeting',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.4
)
mod.newline()

mod.comment('Adrenaline capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adrenaline',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.05
)
mod.newline()

mod.comment('Adrenaline rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adrenaline',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.05
)
mod.newline()

mod.comment('Adrenaline delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adrenaline',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.15
)
mod.newline()

mod.comment('Adrenaline one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adrenaline',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
-0.5
)
mod.newline()

mod.comment('Adrenaline double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adrenaline',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
-1.0
)
mod.newline()

mod.comment('Adrenaline triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adrenaline',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
-2.0
)
mod.newline()

mod.comment('Projected capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Projected',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.25
)
mod.newline()

mod.comment('Projected rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Projected',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
-0.1
)
mod.newline()

mod.comment('Projected delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Projected',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.05
)
mod.newline()

mod.comment('Projected one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Projected',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
1.0
)
mod.newline()

mod.comment('Projected double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Projected',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.5
)
mod.newline()

mod.comment('Projected triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Projected',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.25
)
mod.newline()

mod.comment('Amp capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Amp',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.25
)
mod.newline()

mod.comment('Amp rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Amp',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.2
)
mod.newline()

mod.comment('Amp delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Amp',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.2
)
mod.newline()

mod.comment('Amp one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Amp',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.3
)
mod.newline()

mod.comment('Amp double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Amp',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.6
)
mod.newline()

mod.comment('Amp triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Amp',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
1.2
)
mod.newline()

mod.comment('SafeSpace capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'SafeSpace',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.05
)
mod.newline()

mod.comment('Reflection capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Reflection',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.2
)
mod.newline()

mod.comment('Reflection rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Reflection',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.05
)
mod.newline()

mod.comment('Reflection delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Reflection',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.15
)
mod.newline()

mod.comment('Reflection one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Reflection',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.2
)
mod.newline()

mod.comment('Reflection double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Reflection',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.4
)
mod.newline()

mod.comment('Reflection triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Reflection',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.8
)
mod.newline()

mod.comment('Adaptive capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adaptive',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.1
)
mod.newline()

mod.comment('Adaptive rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adaptive',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.05
)
mod.newline()

mod.comment('Adaptive delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adaptive',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.1
)
mod.newline()

mod.comment('Adaptive one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adaptive',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
-0.2
)
mod.newline()

mod.comment('Adaptive double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adaptive',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
-0.4
)
mod.newline()

mod.comment('Adaptive triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Adaptive',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
-0.8
)
mod.newline()

mod.comment('Absorb capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Absorb',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.25
)
mod.newline()

mod.comment('Absorb rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Absorb',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.2
)
mod.newline()

mod.comment('Absorb delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Absorb',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.15
)
mod.newline()

mod.comment('Absorb one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Absorb',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.2
)
mod.newline()

mod.comment('Absorb double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Absorb',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.4
)
mod.newline()

mod.comment('Absorb triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Absorb',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.8
)
mod.newline()

mod.comment('Turtle capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Turtle',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.5
)
mod.newline()

mod.comment('Turtle rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Turtle',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
-0.2
)
mod.newline()

mod.comment('Turtle delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Turtle',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.25
)
mod.newline()

mod.comment('Turtle one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Turtle',
'Secondary_1_62_F1E72F2542B441230290B388F4C494D1',
-0.1
)
mod.newline()

mod.comment('Turtle double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Turtle',
'Secondary_2_63_5492A1134C687D18D386DAA6A8FF185E',
-0.15
)
mod.newline()

mod.comment('Turtle triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Turtle',
'Secondary_3_64_A3C5C0EC446950EEEEC7E9B3776271B7',
-0.2
)
mod.newline()

mod.comment('Health capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Health',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.25
)
mod.newline()

mod.comment('Health rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Health',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0
)
mod.newline()

mod.comment('Health delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Health',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0
)
mod.newline()

mod.comment('Health one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Health',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.2
)
mod.newline()

mod.comment('Health double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Health',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.4
)
mod.newline()

mod.comment('Health triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Health',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.8
)
mod.newline()

mod.comment('Booster capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Booster',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.05
)
mod.newline()

mod.comment('Booster rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Booster',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0
)
mod.newline()

mod.comment('Booster delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Booster',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0
)
mod.newline()

mod.comment('Booster one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Booster',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.15
)
mod.newline()

mod.comment('Booster double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Booster',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.3
)
mod.newline()

mod.comment('Booster triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Booster',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.6
)
mod.newline()

mod.comment('HealthCharge capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'HealthCharge',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.05
)
mod.newline()

mod.comment('HealthCharge rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'HealthCharge',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.05
)
mod.newline()

mod.comment('HealthCharge delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'HealthCharge',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.05
)
mod.newline()

mod.comment('HealthCharge one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'HealthCharge',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.1
)
mod.newline()

mod.comment('HealthCharge double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'HealthCharge',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.2
)
mod.newline()

mod.comment('HealthCharge triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'HealthCharge',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.4
)
mod.newline()

mod.comment('PowerCharge capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'PowerCharge',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.3
)
mod.newline()

mod.comment('PowerCharge rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'PowerCharge',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.1
)
mod.newline()

mod.comment('PowerCharge delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'PowerCharge',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.1
)
mod.newline()

mod.comment('PowerCharge one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'PowerCharge',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.2
)
mod.newline()

mod.comment('PowerCharge double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'PowerCharge',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.4
)
mod.newline()

mod.comment('PowerCharge triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'PowerCharge',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.8
)
mod.newline()

mod.comment('FortifyCharge capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'FortifyCharge',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.2
)
mod.newline()

mod.comment('FortifyCharge rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'FortifyCharge',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.1
)
mod.newline()

mod.comment('FortifyCharge delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'FortifyCharge',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.1
)
mod.newline()

mod.comment('FortifyCharge one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'FortifyCharge',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.85
)
mod.newline()

mod.comment('FortifyCharge double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'FortifyCharge',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.7
)
mod.newline()

mod.comment('FortifyCharge triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'FortifyCharge',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.4
)
mod.newline()

mod.comment('Vagabond capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Vagabond',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0
)
mod.newline()

mod.comment('Vagabond rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Vagabond',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0
)
mod.newline()

mod.comment('Vagabond delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Vagabond',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0
)
mod.newline()

mod.comment('Vagabond one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Vagabond',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.0725
)
mod.newline()

mod.comment('Vagabond double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Vagabond',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.15
)
mod.newline()

mod.comment('Vagabond triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Vagabond',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.3
)
mod.newline()

mod.comment('Brimming capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Brimming',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.1
)
mod.newline()

mod.comment('Brimming rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Brimming',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0
)
mod.newline()

mod.comment('Brimming delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Brimming',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.1
)
mod.newline()

mod.comment('Brimming one part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Brimming',
'Primary_1_56_207C26E1450330458D6C38B245C338C5',
0.05
)
mod.newline()

mod.comment('Brimming double part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Brimming',
'Primary_2_57_B75F9DB543F7963A15ECCBAC5D036A8E',
0.1
)
mod.newline()

mod.comment('Brimming triple part')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Brimming',
'Primary_3_58_12AFE8834560F575F1813591F715BCE1',
0.2
)
mod.newline()

mod.comment('RechargeRate capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'RechargeRate',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.2
)
mod.newline()

mod.comment('RechargeRate rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'RechargeRate',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0.3
)
mod.newline()

mod.comment('RechargeRate delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'RechargeRate',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0
)
mod.newline()

mod.comment('RechargeDelay capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'RechargeDelay',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
-0.2
)
mod.newline()

mod.comment('RechargeDelay rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'RechargeDelay',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
0
)
mod.newline()

mod.comment('RechargeDelay delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'RechargeDelay',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
-0.3
)
mod.newline()

mod.comment('Capacity capacity')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Capacity',
'Capacity_26_1F88EEE04E890908FB52AE9442E35CE3',
0.35
)
mod.newline()

mod.comment('Capacity rate')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Capacity',
'RechargeRate_27_8A47A06C426C0A244C25068F9B363075',
-0.1
)
mod.newline()

mod.comment('Capacity delay')
mod.table_hotfix(Mod.PATCH, '',
shieldmods,
'Capacity',
'RechargeDelay_28_56D5148C458B7E0E4C3DEB8437889B8E',
0.1
)
mod.newline()