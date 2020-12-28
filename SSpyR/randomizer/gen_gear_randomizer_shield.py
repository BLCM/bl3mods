from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

# Finally better randomize some items (looking at you COMs and Artifacts)
# Had to remove randomization of weapon materials in order to play with other randomizers

mod=Mod('gear_randomizer_shield.bl3hotfix',
'Gear Randomizer: Shields',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
cats='gear-general'
)

data=BL3Data()

#List the Balances
sbal_name=[
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_01_Common',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_02_Uncommon',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_03_Rare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_04_VeryRare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_01_Common',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_02_Uncommon',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_03_Rare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_04_VeryRare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_01_Common',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_02_Uncommon',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_03_Rare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_04_VeryRare',
    '/Game/Gear/Shields/_Design/_Uniques/Aurelia/Balance/InvBalD_Shield_LGD_Aurelia',
    '/Game/Gear/Shields/_Design/_Uniques/BackHam/Balance/InvBalD_Shield_BackHam',
    '/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/Balance/InvBalD_Shield_LGD_BigBoomBlaster',
    '/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole',
    '/Game/Gear/Shields/_Design/_Uniques/BuriedAlive/Balance/InvBalD_Shield_BuriedAlive',
    '/Game/Gear/Shields/_Design/_Uniques/Cyttorak/bALANCE/InvBalD_Shield_Cyttorak',
    '/Game/Gear/Shields/_Design/_Uniques/Dispensary/Balance/InvBalD_Shield_LGD_Dispensary',
    '/Game/Gear/Shields/_Design/_Uniques/FrontLoader/Balance/InvBalD_Shield_LGD_FrontLoader',
    '/Game/Gear/Shields/_Design/_Uniques/GoldenTouch/Balance/InvBalD_Shield_GoldenTouch',
    '/Game/Gear/Shields/_Design/_Uniques/Impaler/Balance/InvBalD_Shield_LGD_Impaler',
    '/Game/Gear/Shields/_Design/_Uniques/LoopOf4N631/Balance/InvBalD_Shield_HYP_LoopOf4N631',
    '/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup',
    '/Game/Gear/Shields/_Design/_Uniques/MoxxisEmbrace/Balance/InvBalD_Shield_MoxxisEmbrace',
    '/Game/Gear/Shields/_Design/_Uniques/MrCaffeine/Balance/InvBalD_Shield_PAN_MrCaffeine',
    '/Game/Gear/Shields/_Design/_Uniques/NovaBurner/Balance/InvBalD_Shield_LGD_NovaBurner',
    '/Game/Gear/Shields/_Design/_Uniques/Radiate/Balance/InvBalD_Shield_LGD_Radiate',
    '/Game/Gear/Shields/_Design/_Uniques/Re-Charger/Balance/InvBalD_Shield_LGD_ReCharger',
    '/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier',
    '/Game/Gear/Shields/_Design/_Uniques/Revengenader/Balance/InvBalD_Shield_LGD_Revengenader',
    '/Game/Gear/Shields/_Design/_Uniques/RoughRider/Balance/InvBalD_Shield_LGD_RoughRider',
    '/Game/Gear/Shields/_Design/_Uniques/ShootingStar/Balance/InvBalD_Shield_LGD_ShootingStar',
    '/Game/Gear/Shields/_Design/_Uniques/SlideKick/Balance/InvBalD_Shield_LGD_SlideKick',
    '/Game/Gear/Shields/_Design/_Uniques/StopGap/Balance/InvBalD_Shield_LGD_StopGap',
    '/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer',
    '/Game/Gear/Shields/_Design/_Uniques/Unpaler/Balance/InvBalD_Shield_LGD_Unpaler',
    '/Game/Gear/Shields/_Design/_Uniques/Vamp/Balance/InvBalD_Shield_Legendary_Vamp',
    '/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward',
    '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
    '/Game/PatchDLC/BloodyHarvest/Gear/Shields/_Design/_Unique/ScreamOfPain/Balance/InvBalD_Shield_ScreamOfTerror',
    '/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Balance/InvBalD_Shield_Clover',
    '/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Ember/Balance/InvBalD_Shield_Ember',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Rico/Balance/InvBalD_Shield_Rico',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Initiative/Balance/InvBalD_Shield_Initiative',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/VoidRift/Balance/InvBalD_Shield_LGD_VoidRift',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/Firewall/Balance/InvBalD_Shield_Legendary_Firewall',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/MEAT/Balance/InvBalD_Shield_Legendary_MEAT',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/Wattson/Balance/InvBalD_Shield_Legendary_Wattson',
    '/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Balance/InvBalD_Shield_LGD_Stinger',
    '/Game/PatchDLC/Takedown2/Gear/Shields/Aesclepius/Balance/InvBalD_Shield_LGD_Aesclepius',
    '/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/FaultyStar/Balance/InvBalD_Shield_Legendary_FaultyStar',
    '/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/FaultyStar/Balance/InvBalD_Shield_Legendary_FaultyStar_Epic',
    '/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/PlusUltra/Balance/InvBalD_Shield_Legendary_PlusUltra',
    '/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/PlusUltra/Balance/InvBalD_Shield_Legendary_PlusUltra_Epic',
    '/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Beskar/Balance/InvBalD_Shield_Beskar',
    '/Game/PatchDLC/Ixora/Gear/Shields/_Unique/MadCap/Balance/InvBalD_Shield_LGD_Madcap',
    '/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Ventilator/Balance/InvBalD_Shield_Ventilator'
]

for bal in sbal_name:
    sbals=Balance.from_data(data, bal)
    mat_type=len(sbals.categories)
    for cat in sbals.categories:
        if cat.index==2:
            for bals in sbal_name:
                sbalslist=Balance.from_data(data, bals)
                for cats in sbalslist.categories:
                    if (cats.index==2) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
            cat.select_multiple=True
            cat.num_min=0
            cat.num_max=3
        if cat.index==3:
            for bals2 in sbal_name:
                sbalslist2=Balance.from_data(data, bals2)
                for cats2 in sbalslist2.categories:
                    if (cats2.index==3) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        #check=len(partsplit)-1
                        #i=0
                        #while i < check:
                            #if '/Game' in partsplit[i]:
                        parts_adj=partsplit[1].replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
                            #i=i+1
            cat.select_multiple=True
            cat.num_min=2
            cat.num_max=3
        if cat.index==mat_type-1:
            for bals3 in sbal_name:
                sbalslist3=Balance.from_data(data, bals3)
                for cats3 in sbalslist3.categories:
                    if len(cats3)!=0:
                        parts=cats3.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        if 'material' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
                        if '_mat_' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
            break
    sbals.hotfix_full(mod)

mod.close()