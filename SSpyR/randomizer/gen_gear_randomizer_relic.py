from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

# Finally better randomize some items (looking at you COMs and Artifacts)
# Had to remove randomization of weapon materials in order to play with other randomizers

mod=Mod('gear_randomizer_relic.bl3hotfix',
'Gear Randomizer: Artifacts',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
cats='gear-general, randomizer'
)

data=BL3Data()

#Try to Adjust to Make More Random Combinations?

#List the Balances
abal_name=[
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_01_Common',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_02_Uncommon',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_03_Rare',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_04_VeryRare',
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_05_Legendary',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElDragonJr/Balance/InvBalD_Artifact_ElDragonJr',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElectricBanjo/Balance/InvBalD_Artifact_ElectricBanjo',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/PhoenixTears/Balance/InvBalD_Artifact_PhoenixTears',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/RoadWarrior/Balance/InvBalD_Artifact_RoadWarrior',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/VaultHunterRelic/Balance/InvBalD_Artifact_Relic',
    '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK',
    '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy',
    '/Game/PatchDLC/Geranium/Gear/Artifacts/_Design/_Unique/Vengeance/Balance/InvBalD_Artifact_Vengeance',
    '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Deathrattle/Balance/InvBalD_Artifact_Deathrattle',
    '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/HolyGrail/Balance/InvBalD_Artifact_HolyGrail',
    '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet'
]

for bal in abal_name:
    abals=Balance.from_data(data, bal)
    mat_type=len(abals.categories)
    for cat in abals.categories:
        if cat.index==1:
            for bals in abal_name:
                abalslist=Balance.from_data(data, bals)
                for cats in abalslist.categories:
                    if (cats.index==2) & (len(cats)!=0):
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
            if cat.enabled is False:
                cat.enabled=True
        if cat.index==2:
            for bals2 in abal_name:
                abalslist2=Balance.from_data(data, bals2)
                for cats2 in abalslist2.categories:
                    if (cats2.index==1) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
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
            break
    abals.hotfix_full(mod)

mod.close()