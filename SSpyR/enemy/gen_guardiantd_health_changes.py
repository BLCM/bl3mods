from bl3hotfixmod import Mod

mod=Mod('guardiantd_health_changes.bl3hotfix',
'Guardian Takedown Health Balancing',
'SSpyR',
[
    'Buff health of mobs.'
],
lic=Mod.CC_BY_SA_40,
cats='scaling, enemy'
)

#Iterate through lists, make duplicates and check for them if they use anything past primary

healthprimary='HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12'
healthseconndary='HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49'
healthtert='HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2'
healthquart='HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863'
healthquin='HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113'

nekrobugtable='/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2'
guardiantable='/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2'

#write all values for each in between commas
nekrobug_chars=[
    'Nekrobug_GroundTD2,15.0',
    'Nekrobug_FlyerTD2,10.0',
    'Nekrobug_HopperTD2,15.0',
    'Nekrobug_BadassTD2,30.0,5.0,3.0,3.0,3.0', #5 values 
]

#write all values for each in between commas, 2 values for all except Reaper which is 3
guardian_chars=[
    'GuardianWraithTD2,20.0,8.0',
    'GuardianSpectreTD2,20.0,8.0',
    'GuardianSeraTD2,12.0,6.0',
    'GuardianHeraldTD2,18.0,16.0',
    'GuardianWraithBadassTD2,24.0,12.0',
    'GuardianReaperTD2,25.0,25.0,25.0',
    'GuardianWraithTD2_LOWXP,20.0,8.0',
    'GuardianSpectreTD2_LOWXP,20.0,8.0',
    'GuardianSeraTD2_LOWXP,12.0,6.0',
    'GuardianHeraldTD2_LOWXP,18.0,16.0',
    'GuardianWraithBadassTD2_LOWXP,24.0,12.0'
]

mod.comment('Nekrobug Adjustments')
for nasset in nekrobug_chars:
    nasset=nasset.split(',')
    name=nasset[0]
    value=nasset[1]
    mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
        nekrobugtable,
        name,
        healthprimary,
        value
    )
    if name=='Nekrobug_BadassTD2':
        mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
            nekrobugtable,
            name,
            healthseconndary,
            nasset[2]
        )
        mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
            nekrobugtable,
            name,
            healthtert,
            nasset[3]
        )
        mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
            nekrobugtable,
            name,
            healthquart,
            nasset[4]
        )
        mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
            nekrobugtable,
            name,
            healthquin,
            nasset[5]
        )
mod.newline()

mod.comment('Guardian Adjustments')
for gasset in guardian_chars:
    gasset=gasset.split(',')
    name=gasset[0]
    value=gasset[1]
    mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
        guardiantable,
        name,
        healthprimary,
        value
    )
    mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
        guardiantable,
        name,
        healthseconndary,
        gasset[2]
    )
    if name=='GuardianReaperTD2':
        mod.table_hotfix(Mod.CHAR, 'BP_Char_'+name,
        guardiantable,
        name,
        healthtert,
        gasset[3]
    )
mod.newline()

mod.close()
