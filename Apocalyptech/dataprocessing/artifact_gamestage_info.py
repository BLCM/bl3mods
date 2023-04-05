#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
# <cj@apocalyptech.com>
# <https://apocalyptech.com/contact.php>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import math
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import BVC

# Finds Artifacts without a proper MinGameStage

data = BL3Data()

# This stuff yoinked from gen_item_balances.py
artifact_balances = [
        ('Common', '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_01_Common'),
        ('Uncommon', '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_02_Uncommon'),
        ('Rare', '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_03_Rare'),
        ('Very Rare', '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_04_VeryRare'),
        ('Legendary', '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact_05_Legendary'),
        ("Company Man (Atlas)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Atlas/Balance/InvBalD_Artifact_CompanyMan_Atlas'),
        ("Company Man (CoV)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/CoV/Balance/InvBalD_Artifact_CompanyMan_CoV'),
        ("Company Man (Dahl)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Dahl/Balance/InvBalD_Artifact_CompanyMan_Dahl'),
        ("Company Man (Hyperion)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Hyperion/Balance/InvBalD_Artifact_CompanyMan_Hyperion'),
        ("Company Man (Jakobs)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Jakobs/Balance/InvBalD_Artifact_CompanyMan_Jakobs'),
        ("Company Man (Maliwan)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Maliwan/Balance/InvBalD_Artifact_CompanyMan_Maliwan'),
        ("Company Man (Tediore)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Tediore/Balance/InvBalD_Artifact_CompanyMan_Tediore'),
        ("Company Man (Torgue)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Torgue/Balance/InvBalD_Artifact_CompanyMan_Torgue'),
        ("Company Man (Vladof)", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/CompanyMan/Vladof/Balance/InvBalD_Artifact_CompanyMan_Vladof'),
        ("Deathrattle", '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Deathrattle/Balance/InvBalD_Artifact_Deathrattle'),
        ("Electric Banjo", '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElectricBanjo/Balance/InvBalD_Artifact_ElectricBanjo'),
        ("Grave", '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave'),
        ("Holy Grail", '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/HolyGrail/Balance/InvBalD_Artifact_HolyGrail'),
        ("Lunacy", '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy'),
        ("Mysterious Amulet", '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet'),
        ("Mysterious Artifact", '/Game/PatchDLC/Ixora2/Gear/Artifacts/_Unique/MysteriousAmulet/Balance/InvBalD_Artifact_MysteriousAmulet'),
        ("Pearl of Ineffable Knowledge", '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK'),
        ("Phoenix Tears", '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/PhoenixTears/Balance/InvBalD_Artifact_PhoenixTears'),
        ("Road Warrior", '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/RoadWarrior/Balance/InvBalD_Artifact_RoadWarrior'),
        ("Shlooter", '/Game/PatchDLC/VaultCard2/Gear/Artifacts/Unique/Shlooter/Balance/InvBalD_Artifact_Shlooter'),
        ("Toboggan", '/Game/PatchDLC/Ixora/Gear/Artifacts/_Design/_Unique/Toboggan/Balance/InvBalD_Artifact_Toboggan'),
        ("Unleash the Dragon", '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElDragonJr/Balance/InvBalD_Artifact_ElDragonJr'),
        ("Vault Hunter's Relic", '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/VaultHunterRelic/Balance/InvBalD_Artifact_Relic'),
        ("Vendetta", '/Game/PatchDLC/Geranium/Gear/Artifacts/_Design/_Unique/Vengeance/Balance/InvBalD_Artifact_Vengeance'),
        ("Commander Planetoid", '/Game/PatchDLC/Raid1/Gear/Artifacts/CommanderPlanetoid/InvBalD_Artifact_CommanderPlanetoid'),
        ("Cosmic Crater", '/Game/PatchDLC/Raid1/Gear/Artifacts/CosmicCrater/InvBalD_Artifact_CosmicCrater'),
        ("Deathless", '/Game/PatchDLC/Raid1/Gear/Artifacts/Deathless/InvBalD_Artifact_Deathless'),
        ("Launch Pad", '/Game/PatchDLC/Raid1/Gear/Artifacts/Salvo/InvBalD_Artifact_Salvo'),
        ("Loaded Dice", '/Game/PatchDLC/Raid1/Gear/Artifacts/LoadedDice/InvBalD_Artifact_LoadedDice'),
        ("Moxxi's Endowment", '/Game/PatchDLC/Raid1/Gear/Artifacts/MoxxisEndowment/InvBalD_Artifact_MoxxisEndowment'),
        ("Otto Idol", '/Game/PatchDLC/Raid1/Gear/Artifacts/OttoIdol/InvBalD_Artifact_OttoIdol'),
        ("Pull Out Method", '/Game/PatchDLC/Raid1/Gear/Artifacts/PullOutMethod/InvBalD_Artifact_PullOutMethod'),
        ("Rocket Boots", '/Game/PatchDLC/Raid1/Gear/Artifacts/RocketBoots/InvBalD_Artifact_RocketBoots'),
        ("Safeguard", '/Game/PatchDLC/Raid1/Gear/Artifacts/Safegaurd/InvBalD_Artifact_Safegaurd'),
        ("Splatter Gun", '/Game/PatchDLC/Raid1/Gear/Artifacts/SplatterGun/InvBalD_Artifact_SplatterGun'),
        ("Static Charge", '/Game/PatchDLC/Raid1/Gear/Artifacts/StaticTouch/InvBalD_Artifact_StaticTouch'),
        ("Victory Rush", '/Game/PatchDLC/Raid1/Gear/Artifacts/VictoryRush/InvBalD_Artifact_VictoryRush'),
        ("White Elephant", '/Game/PatchDLC/Raid1/Gear/Artifacts/WhiteElephant/InvBalD_Artifact_WhiteElephant'),
        ]
artifact_balances.sort()

for name, bal_name in artifact_balances:
    bal_data = data.get_data(bal_name)
    found_main = False
    mingamestage = None
    for export in bal_data:
        if export['export_type'] == 'InventoryBalanceData':
            found_main = True
            if 'Manufacturers' in export and type(export['Manufacturers']) == list:
                if len(export['Manufacturers']) != 1:
                    print('WARNING: {} manufacturers in {} | {}'.format(
                        len(export['Manufacturers']),
                        name,
                        bal_name,
                        ))
                    continue
                man = export['Manufacturers'][0]
                if 'GameStageWeight' in man and 'MinGameStage' in man['GameStageWeight']:
                    mingamestage = data.process_bvc(BVC.from_data_struct(man['GameStageWeight']['MinGameStage']))
            break
    if not found_main:
        print(f'WARNING: Could not find main export for {name} | {bal_name}')
    else:
        if name == 'Deathrattle':
            # Hardcoded hotfix
            mingamestage = 27
        if mingamestage != 27:
            print(name)
            print(bal_name)
            print(mingamestage)
            print('')

