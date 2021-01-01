from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

# Finally better randomize some items (looking at you COMs and Artifacts)
# Had to remove randomization of weapon materials in order to play with other randomizers

mod=Mod('gear_randomizer_nade.bl3hotfix',
'Gear Randomizer: Grenades',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
cats='gear-general, randomizer'
)

data=BL3Data()

#List the Balances
gbal_name=[
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/_Unique/BirthdaySuprise/Balance/InvBalD_GM_BirthdaySuprise',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ButtStallion/Balance/InvBalD_GM_ButtStallion',
    '/Game/Gear/GrenadeMods/_Design/_Unique/CashMoneyPreorder/Balance/InvBalD_GM_CashMoneyPreorder',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Chupa/Balance/InvBalD_GM_Chupa',
    '/Game/Gear/GrenadeMods/_Design/_Unique/EchoV2/Balance/InvBalD_GM_EchoV2',
    '/Game/Gear/GrenadeMods/_Design/_Unique/EMP/Balance/InvBalD_GM_EMP',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Epicenter/Balance/InvBalD_GM_Epicenter',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball',
    '/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm',
    '/Game/Gear/GrenadeMods/_Design/_Unique/HipHop/Balance/InvBalD_GM_TOR_HipHop',
    '/Game/Gear/GrenadeMods/_Design/_Unique/HunterSeeker/Balance/InvBalD_GM_HunterSeeker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/JustDeserts/Balance/InvBalD_GM_JustDeserts',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Kryll/Balance/InvBalD_GM_Kryll',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Mogwai/Balance/InvBalD_GM_Mogwai',
    '/Game/Gear/GrenadeMods/_Design/_Unique/MoxiesBosom/Balance/InvBalD_GM_PAN_MoxiesBosom',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Mushroom/Balance/InvBalD_GM_Shroom',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Nagate/Balance/InvBalD_GM_Nagate',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Quasar/Balance/InvBalD_GM_Quasar',
    '/Game/Gear/GrenadeMods/_Design/_Unique/RedQueen/Balance/InvBalD_GM_RedQueen',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Seeker/Balance/InvBalD_GM_Seeker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/StormFront/Balance/InvBalD_GM_StormFront',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Summit/Balance/InvBalD_GM_Summit',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Surge/Balance/InvBalD_GM_Surge',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ToiletBombs/Balance/InvBalD_GM_TOR_ToiletBombs',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ToyGrenade/Balance/InvBalD_GM_ToyGrenade',
    '/Game/Gear/GrenadeMods/_Design/_Unique/TranFusion/Balance/InvBalD_GM_TranFusion',
    '/Game/Gear/GrenadeMods/_Design/_Unique/WidowMaker/Balance/InvBalD_GM_WidowMaker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/WizardOfNOG/Balance/InvBalD_GM_WizardOfNOG',
    '/Game/PatchDLC/BloodyHarvest/Gear/GrenadeMods/_Design/_Unique/FontOfDarkness/Balance/InvBalD_GM_TOR_FontOfDarkness',
    '/Game/PatchDLC/Dandelion/Gear/Grenade/Slider/Balance/InvBalD_GM_TED_Slider',
    '/Game/PatchDLC/Dandelion/Gear/Grenade/AcidBurn/Balance/InvBalD_GM_AcidBurn',
    '/Game/PatchDLC/Event2/Gear/GrenadeMods/FishSlap/Balance/InvBalD_GM_FishSlap',
    '/Game/PatchDLC/Takedown2/Gear/GrenadeMods/Lightspeed/Balance/InvBalD_GM_HYP_Lightspeed',
    '/Game/PatchDLC/Geranium/Gear/Grenade/CoreBurst/Balance/InvBalD_GM_CoreBurst',
    '/Game/PatchDLC/Geranium/Gear/Grenade/SkagOil/Balance/InvBalD_GM_SkagOil',
    '/Game/PatchDLC/Ixora/Gear/GrenadeMods/HOTSpring/Balance/InvBalD_GM_HOTSpring'
]

for bal in gbal_name:
    gbals=Balance.from_data(data, bal)
    mat_type=len(gbals.categories)
    for cat in gbals.categories:
        if cat.index==1:
            for bals in gbal_name:
                gbalslist=Balance.from_data(data, bals)
                for cats in gbalslist.categories:
                    if (cats.index==1) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
        if cat.index==2:
            for bals2 in gbal_name:
                gbalslist2=Balance.from_data(data, bals2)
                for cats2 in gbalslist2.categories:
                    if (cats2.index==2) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
        if cat.index==3:
            for bals3 in gbal_name:
                gbalslist3=Balance.from_data(data, bals3)
                for cats3 in gbalslist3.categories:
                    if (cats3.index==3) & (len(cats3)!=0):
                        parts=cats3.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            cat.num_min=0
            cat.num_max=1
        if cat.index==4:
            for bals4 in gbal_name:
                gbalslist4=Balance.from_data(data, bals4)
                for cats4 in gbalslist4.categories:
                    if (cats4.index==4) & (len(cats4)!=0):
                        parts=cats4.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            cat.select_multiple=True
            cat.num_min=2
            cat.num_max=3
        if cat.index==mat_type-1:
            for bals5 in gbal_name:
                gbalslist5=Balance.from_data(data, bals5)
                for cats5 in gbalslist5.categories:
                    if len(cats5)!=0:
                        parts=cats5.str_partlist()
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
    gbals.hotfix_full(mod)

mod.close()