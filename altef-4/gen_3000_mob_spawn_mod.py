#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

#additional or multiply bobs count, false = (src_mob_count) + (mob_count), true = (src_mob_count) * (mob_count)
mob_count_multiply = True
#mobs count
mob_count = 3
mob_alive_count = 4
#randomize spawn points (left,right,center)
random_spawn = True
from bl3hotfixmod.bl3hotfixmod import Mod
from gen_3000_Char_list import *

mod = Mod('3000_mob_spawn_mod.bl3hotfix',
        '3000 mobs count scale / spawn randomizer',
        'altef_4',
        ['increace mob count on slaughter star 3000',
        'and randomize spawn points'],
        lic=Mod.CC_BY_SA_40,
        v='1.0',
        cats='gameplay',)
        

Tech_mission = '/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel'
DC = 'SpawnMesh_DoorCargo'
DS = 'SpawnMesh_DoorSmall'
SP = 'OakSpawnPoint'
def GetSpawnPoint(idx):
    return {
        #RIGHT
        0: "{}_C'{}.{}_6'".format(DC,Tech_mission,DC),
        1: "{}_C'{}.{}_0'".format(DC,Tech_mission,DC),
        2: "{}_C'{}.{}_7'".format(DC,Tech_mission,DC),
        3: "{}'{}.{}_12'".format(SP,Tech_mission,SP),
        4: "{}'{}.{}_15'".format(SP,Tech_mission,SP),
        5: "{}'{}.{}_39'".format(SP,Tech_mission,SP),
        #LEFT
        6: "{}_C'{}.{}_5'".format(DC,Tech_mission,DC),
        7: "{}'{}.{}_41'".format(SP,Tech_mission,SP),#LBalcon Right
        8: "{}'{}.{}_20'".format(SP,Tech_mission,SP),#LBalcon Center
        9: "{}'{}.{}_49'".format(SP,Tech_mission,SP),#LBalcon Left
        10: "{}_C'{}.{}_2'".format(DC,Tech_mission,DC),
        11: "{}_C'{}.{}_1'".format(DC,Tech_mission,DC),
        12: "{}_C'{}.{}_4'".format(DC,Tech_mission,DC),
        13: "{}_C'{}.{}_3'".format(DC,Tech_mission,DC),
        14: "{}'{}.{}_8'".format(SP,Tech_mission,SP),#Lift
        15: "{}_C'{}.{}_3'".format(DC,Tech_mission,DC),
        #CENTER
        16: "{}'{}.{}_57'".format(SP,Tech_mission,SP),
        17: "{}_C'{}.{}_2'".format(DS,Tech_mission,DS),
        18: "{}_C'{}.{}_0'".format(DS,Tech_mission,DS),
        19: "{}_C'{}.{}_3'".format(DS,Tech_mission,DS),
        20: "{}_C'{}.{}_4'".format(SP,Tech_mission,SP),#boss Mech_0 Right Lift
        21: "{}_C'{}.{}_6'".format(SP,Tech_mission,SP),#boss Mech Left Lift Down
    }.get(idx, '!None')

def Get_Light(idx):
    return {#Spot_Rotating, Spot_Non_Rotating
        0: "SpawnerLight_Right",
        1: "SpawnerLight_Lower_3",
        2: "SpawnerLight_Lower_1",
        3: "SpawnerLight_Lower_0",
        4: "SpawnerLight_Lower",
        5: "SpawnerLight_Left__2",
        6: "SpawnerLight_Left__1",
        7: "SpawnerLight_Hangar_6",
        8: "SpawnerLight_Hangar_1",
        9: "SpawnerLight_Hangar_0",
        10: "SpawnerLight_Hangar_",
        11: "SpawnerLight_Hangar"
    }.get(idx, '!None')

full_Spawn_list = GetSpawnPoint(0)
for pnt in range(1,20):
    full_Spawn_list = "{},{}".format(full_Spawn_list,GetSpawnPoint(pnt))
'''for pnt in range(21,22):
    full_Spawn_list = "{},{}".format(full_Spawn_list,GetSpawnPoint(pnt))'''
print(full_Spawn_list)
'''
for ii in range(12):
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.PointLightComponent".format(Get_Light(ii)),
        'Spot_Rotating.bVisible',
        'True','',True)
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.PointLightComponent".format(Get_Light(ii)),
        'Spot_Non_Rotating.bVisible',
        'True','',True)
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.PointLightComponent".format(Get_Light(ii)),
        'Point_Area.bVisible',
        'True','',True)
K2Node_ComponentBoundEvent_0_237027
'''
for rnd in range(5):
    for wave in range(6):
        idx = 0
        for add in range(3):
            m = spawn_conf(rnd+1,wave+1,add+1,"mission")
            if "!" not in m:
                #print(m)
                if (idx == 0) and random_spawn:
                    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                        "{}.{}.SpawnerComponent".format(Tech_mission,m),
                        'SpawnPoints',
                        '({})'.format(full_Spawn_list),'',True)
                    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                        'bRandomizeSpawnPoints',
                        random_spawn,"",False)
                    for i in range(3):
                        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                            "{}.{}.SpawnerComponent".format(Tech_mission,m),
                            'SpawnPointGroups.SpawnPointGroups[{}].SpawnPoints'.format(i),
                            '({})'.format(full_Spawn_list),'',True)
                        mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                            "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                            'SpawnPointGroups.SpawnPointGroups[{}].bRandomize'.format(i),
                            random_spawn,"",True)
                if mob_count_multiply:
                    if mob_count != 1.0:
                        mvalue = spawn_conf(rnd+1,wave+1,add+1,"mobs") * mob_count
                else:
                    if mob_count != 0.0:
                        mvalue = spawn_conf(rnd+1,wave+1,add+1,"mobs") + mob_count
                mvalue = mvalue.__round__(0)
                if add == 2:
                    attr = "SpawnerComponent.Object..SpawnerStyle.Object.NumActorsParam.AttributeInitializationData.BaseValueConstant"
                else:
                    attr = "SpawnerComponent.Object..SpawnerStyle.Object.Waves.Waves[{}].SpawnerStyle.Object.NumActorsParam.AttributeInitializationData.BaseValueConstant".format(add)
                mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                    attr,
                    mvalue,"",True)
                if add == 0:
                    mvalue = spawn_conf(rnd+1,wave+1,add+1,"alive_passive")
                    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den".format(m),
                        "SpawnerComponent.Object..SpawnerStyle.Object.MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant",
                        mvalue * mob_alive_count,"",True)
                    mvalue = spawn_conf(rnd+1,wave+1,add+1,"alive_end")
                    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den".format(m),
                        "SpawnerComponent.Object..SpawnerStyle.Object.MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant",
                        mvalue,"",True)
                    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                        "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den".format(m),
                        "SpawnerComponent.Object..SpawnerStyle.Object.SpawnDelay",
                        1,"",True)
                #print(mvalue)
                mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
                    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent".format(m),
                    "SpawnerComponent.Object..SpawnerStyle.Object.Waves.Waves[{}].WarmupTimer".format(add),
                    1.0,"",True)
            idx += 1

mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
    "/Game/Maps/Slaughters/TechSlaughter/TechSlaughter_Mission.TechSlaughter_Mission:PersistentLevel.{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Single".format('OakSpawner_Mech'),
    "SpawnerComponent.Object..SpawnerStyle.Object.SpawnDelay",
    3,"",True)
mod.close()
