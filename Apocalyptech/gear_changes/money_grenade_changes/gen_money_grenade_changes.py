#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, ItemPool, BVC, BVCF

class ModConfig:
    """
    Class to encapsulate the various bits of data that we're changing, mostly just
    so that we can provide some easy defaults, and avoid having a huge-ass tuple
    for our loop, instead.
    """

    pool1 = '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/ItemPool_GrenadeMod_Money_1'
    pool2 = '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/ItemPool_GrenadeMod_Money_2'
    pool3 = '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/ItemPool_GrenadeMod_Money_3'

    uistat1 = ('/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/UIStat_Grenade_Money_Description_Single',
            'Enemies drop [skill]some[/skill] {} when damaged.')
    uistat2 = ('/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/UIStat_Grenade_Money_Description_Double',
            'Enemies drop [skill]lots[/skill] of {} when damaged.')
    uistat3 = ('/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/UIStat_Grenade_Money_Description_Triple',
            'Enemies drop [skill]a buttload[/skill] of {} when damaged.')

    def __init__(self, mod_label, mod_filename,
            desc_text,
            card_text,
            part_text,
            rewards1,
            rewards2,
            rewards3,
            single_name='Money',
            triple_name='Trust Fund',
            combo_name_mirv='Diversifying',
            combo_name_rain='Make It Rain',
            combo_name_nuke='Investing',
            combo_name_large='Big Spender',
            combo_name_bouncy='Bullish',
            combo_name_spring='Depreciating',
            combo_name_sticky='Price Fixing',
            combo_name_artillery='Windfall',
            combo_name_lingering='Jackpot',
            combo_name_divide='Compounding',
            combo_name_singularity='Moneysink',
            combo_name_roider='ROI Rage',
            combo_name_link='Pyramid Scheme',
            combo_name_transfusion='Cash Infusion',
            combo_name_generator='Taxing',
            combo_name_elemental='Cash Infusion',
            combo_name_force='Bailout',
            combo_name_money='Greed',
            ):
        """
        rewards1, rewards2, and rewards3 should be a list of tuples, with the first
        element being a balance name (or `None`), the second being a pool name
        (or `None`), and the third being a weighting value (either a number or a
        `BVC` object).
        """
        self.mod_label = mod_label
        self.mod_filename = mod_filename
        self.desc_text = desc_text
        self.card_text = card_text
        self.part_text = part_text
        self.single_name = single_name
        self.triple_name = triple_name
        self.combo_name_mirv = combo_name_mirv
        self.combo_name_rain = combo_name_rain
        self.combo_name_nuke = combo_name_nuke
        self.combo_name_large = combo_name_large
        self.combo_name_bouncy = combo_name_bouncy
        self.combo_name_spring = combo_name_spring
        self.combo_name_sticky = combo_name_sticky
        self.combo_name_artillery = combo_name_artillery
        self.combo_name_lingering = combo_name_lingering
        self.combo_name_divide = combo_name_divide
        self.combo_name_singularity = combo_name_singularity
        self.combo_name_roider = combo_name_roider
        self.combo_name_link = combo_name_link
        self.combo_name_transfusion = combo_name_transfusion
        self.combo_name_generator = combo_name_generator
        self.combo_name_elemental = combo_name_elemental
        self.combo_name_force = combo_name_force
        self.combo_name_money = combo_name_money

        # Construct our ItemPools right away
        self.rewards1 = ItemPool(self.pool1)
        self.rewards2 = ItemPool(self.pool2)
        self.rewards3 = ItemPool(self.pool3)
        for pool_obj, rewards in [
                (self.rewards1, rewards1),
                (self.rewards2, rewards2),
                (self.rewards3, rewards3),
                ]:
            for balance_name, pool_name, weight in rewards:
                if balance_name:
                    pool_obj.add_balance(balance_name, weight)
                else:
                    pool_obj.add_pool(pool_name, weight)

    def _combo_name(self, mod, index, new_name):

        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Gear/GrenadeMods/_Design/Naming/GrenadeModNamingStrategy',
                f'ExtractedCombinationNames.ExtractedCombinationNames[{index}].NamePart.Object..PartName',
                new_name)

    def write_mod(self):

        mod = Mod(f'money_grenade_changes_{self.mod_filename}.bl3hotfix',
                f'Money Grenade Changes: {self.mod_label}',
                'Apocalyptech',
                [
                    f"Changes the 'Money' grenade part to drop {self.desc_text} instead of money.",
                ],
                lic=Mod.CC_BY_SA_40,
                v='1.0.0',
                cats='joke, gear-grenade, cheat',
                ss=f'https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/gear_changes/money_grenade_changes/screenshot_{self.mod_filename}.png',
                )

        mod.header('Update item prefixes')
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Gear/GrenadeMods/_Design/Naming/GrenadeModNamingStrategy',
                'SingleNames.SingleNames[20].NamePart.Object..PartName',
                self.single_name)
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Gear/GrenadeMods/_Design/Naming/GrenadeModNamingStrategy',
                'TripleNames.TripleNames[11].NamePart.Object..PartName',
                self.triple_name)
        self._combo_name(mod, 19, self.combo_name_mirv)
        self._combo_name(mod, 36, self.combo_name_rain)
        self._combo_name(mod, 52, self.combo_name_nuke)
        self._combo_name(mod, 67, self.combo_name_large)
        self._combo_name(mod, 81, self.combo_name_bouncy)
        self._combo_name(mod, 94, self.combo_name_spring)
        self._combo_name(mod, 106, self.combo_name_sticky)
        self._combo_name(mod, 117, self.combo_name_artillery)
        self._combo_name(mod, 127, self.combo_name_lingering)
        self._combo_name(mod, 136, self.combo_name_divide)
        self._combo_name(mod, 144, self.combo_name_singularity)
        self._combo_name(mod, 151, self.combo_name_roider)
        self._combo_name(mod, 157, self.combo_name_link)
        self._combo_name(mod, 162, self.combo_name_transfusion)
        self._combo_name(mod, 166, self.combo_name_generator)
        self._combo_name(mod, 169, self.combo_name_elemental)
        self._combo_name(mod, 171, self.combo_name_force)
        self._combo_name(mod, 172, self.combo_name_money)
        mod.newline()

        mod.header('Update part name')
        mod.reg_hotfix(Mod.PATCH, '',
                '/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/UIStat_Grenade_Money_Icon',
                'Text',
                self.part_text.upper())
        mod.newline()

        mod.header('Update drop pools and card descriptions')
        for pool_label, rewards, (uistat_name, uistat_text) in [
                ('Single-part grenade', self.rewards1, self.uistat1),
                ('Double-part grenade', self.rewards2, self.uistat2),
                ('Triple-part grenade', self.rewards3, self.uistat3),
                ]:
            mod.comment(pool_label)
            mod.reg_hotfix(Mod.PATCH, '',
                    rewards.pool_name,
                    'BalancedItems',
                    str(rewards))
            mod.reg_hotfix(Mod.PATCH, '',
                    uistat_name,
                    'FormatText',
                    uistat_text.format(self.card_text))
            mod.newline()

        # Special-case hardcodes for some mod types
        if self.mod_label == 'Diamond Keys':

            # Fix up the diamond key item so that it looks better when dropped
            # (by default it just looks like eridium, and also doesn't auto-pickup)

            mod.header_lines([
                "Fixing up droppable Diamond Key object",
                "",
                "We're making a few changes here which affect the item card specifically,",
                "though the item card will basically never be seen since we're enabling",
                "auto-pickup as well.  If you *do* get a glimpse of the card (using Photo",
                "Mode or the like) you'll see a bit of weirdness still -- the card might",
                "inherit the visual price of whatever card was last looked at, and the",
                "loot beam icon might inherit the last-looked-at item as well.  In the",
                "end I'm not bothering to track that down, though, since you've gotta",
                "work hard to see the card anyway.",
                ])

            mod.comment('Use an actual key mesh')
            mod.reg_hotfix(Mod.PATCH, '',
                    '/Game/PatchDLC/VaultCard/Data/Currency/BP_DiamondKey_Single.Default__BP_DiamondKey_Single_C',
                    'ItemMeshComponent.Object..StaticMesh',

                    # Tried lots of various meshes here; I'm tempted to go with one of the keyring ones,
                    # but in the end I just went with one of the smaller single-key ones.  Would be nice
                    # if I could get that Geranium Key-to-City ones to interact with physics, though
                    # that might cause weird problems with the key during the plot (or on Decoration),
                    # so eh.  We'll just stick with the tiny key for now.

                    # A bit much, though it's a nice big size.  Is definitely a keyring, though.
                    #Mod.get_full_cond('/Dandelion/Missions/Plot/Ep04_Trashtown/Janitor_Keyring/Model/Meshes/SM_Janitor_Keyring', 'StaticMesh'),

                    # Definitely a keyring; probably better than SM_Janitor_Keyring if I feel okay with that...
                    #Mod.get_full_cond('/Ixora2/Missions/02_Eden6/Keyring/Model/Meshes/SM_Key_Ring', 'StaticMesh'),

                    # Hah, just a rusty sphere basically
                    #Mod.get_full_cond('/Geranium/LevelArt/Lodge/Props/Model/Meshes/SM_Apple_Key', 'StaticMesh'),

                    # Very nice (and rightly-sized!) key, but it weirdly doesn't seem to actually interact with physics
                    # at all?  Just hangs there in midair.
                    #Mod.get_full_cond('/Geranium/InteractiveObjects/MissionAssets/Plot_5/Model/Meshes/SM_Key_to_City', 'StaticMesh'),
                    # Same story here; and seemingly identical to the other one.  Almost certainly a copied object.
                    #Mod.get_full_cond('/Game/PatchDLC/Geranium/InteractiveObjects/PlayerQuarters/RoomDecoMeshes/Meshes/SM_Key_to_City_RoomDeco', 'StaticMesh'),

                    # Perfectly serviceable key, but quite small
                    #Mod.get_full_cond('/Hibiscus/InteractiveObjects/MissionSpecific/Plot/EP03/Pickups/SM_Key_GateKey', 'StaticMesh'),
                    # Perfectly serviceable key, but quite small
                    Mod.get_full_cond('/Game/LevelArt/Environments/_Global/Props/Keys/Key_Scooters/Model/Meshes/SM_Key_Scooters', 'StaticMesh'),
                    )
            mod.newline()

            mod.comment('Set a different item card type')
            mod.reg_hotfix(Mod.PATCH, '',
                    '/Game/PatchDLC/VaultCard/Data/Currency/InvData_DiamondKey',
                    'ItemCardTypeFrameName',
                    #'currencyEridium',
                    # Mission is nice; has a diamondy icon, even!
                    'Mission',
                    # Cash works well
                    #'Cash',
                    )
            mod.newline()

            mod.comment('Set monetary value to 1; might prevent currency from inheriting from previously-viewed items')
            mod.reg_hotfix(Mod.PATCH, '',
                    '/Game/PatchDLC/VaultCard/Data/Currency/InvData_DiamondKey',
                    'MonetaryValue',
                    BVCF(bvc=1))
            mod.newline()

            mod.comment('Assign Legendary rarity (instead of Eridium), for loot bar + frame color')
            mod.reg_hotfix(Mod.PATCH, '',
                    '/Game/PatchDLC/VaultCard/Data/Currency/InventoryBalance_DiamondKey',
                    'RarityData',
                    Mod.get_full_cond('/Game/GameData/Loot/RarityData/RarityData_05_Legendary', 'RarityData'))
            mod.newline()

            mod.comment('Auto-pickup Diamond Keys')
            mod.reg_hotfix(Mod.PATCH, '',
                    '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_DiamondKey',
                    'PickupActionType',
                    #'OnUseOnly',
                    'OnUseOrTouch',
                    )
            mod.newline()

        mod.close()

# For our "gear" preset, how much to scale the non-gun drops relative to gun drops,
# since BL3 doesn't really have that in an item pool.  Based on the BL2 drop rates.
# 80% will give you about equal guns+not-guns; doing 60% for now.
non_gun_scale = .6

# Now loop through and generate a bunch of mods
for modconf in [
        ModConfig(mod_label='Eridium',
            mod_filename='eridium',
            desc_text='eridium',
            card_text='eridium',
            part_text='ERIDIUM',
            single_name='Eridium',
            combo_name_money='Hoarding',
            triple_name="Earl's Choice",
            # Honestly *most* of the combo names still work all right for the Eridium
            # variant, so I'm basically happy with where this one ended up.
            combo_name_singularity='Sunk Cost',
            combo_name_transfusion='Infusion',
            combo_name_elemental='Infusion',
            rewards1=[
                ('/Game/Pickups/Eridium/InvBal_Eridium_Single', None, BVC(bvc=.75)),
                ('/Game/Pickups/Eridium/InvBal_Eridium_Stack', None, BVC(bvc=.25)),
                ],
            rewards2=[
                ('/Game/Pickups/Eridium/InvBal_Eridium_Single', None, BVC(bvc=.5)),
                ('/Game/Pickups/Eridium/InvBal_Eridium_Stack', None, BVC(bvc=.5)),
                ],
            rewards3=[
                ('/Game/Pickups/Eridium/InvBal_Eridium_Single', None, BVC(bvc=.25)),
                ('/Game/Pickups/Eridium/InvBal_Eridium_Stack', None, BVC(bvc=.75)),
                ],
            ),
        ModConfig(mod_label='Grenades',
            mod_filename='grenades',
            desc_text='replacement grenade ammo',
            card_text='replacement grenade ammo',
            part_text='GRENADES',
            single_name='Replenishment',
            combo_name_money='Excess',
            triple_name='Gray Goo',
            # Names for the combos here?  I have no idea; this one's difficult because
            # the grenade ammo effect is so ridiculous and specific.  Something TODO
            # later, I guesss.
            #combo_name_mirv='Gremlin',
            #combo_name_nuke='Overwhelming
            #combo_name_large='???',
            #combo_name_sticky='???',
            combo_name_transfusion='Infusion',
            combo_name_elemental='Infusion',
            rewards1=[
                ('/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Grenade', None, BVC(bvc=1)),
                ],
            rewards2=[
                ('/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Grenade', None, BVC(bvc=1)),
                ],
            rewards3=[
                ('/Game/Pickups/Ammo/DA_InventoryBalance_Ammo_Grenade', None, BVC(bvc=1)),
                ],
            ),
        ModConfig(mod_label='Diamond Keys',
            mod_filename='diamondkeys',
            desc_text='Diamond Keys',
            card_text='diamond keys',
            part_text='DIAMOND KEYS',
            single_name='Diamond',
            combo_name_money='Engagement',
            triple_name='Mr. Shine',
            # Like with Eridium, most of the vanilla combo names work out pretty well,
            # though I'm sure that there's some fun I could have here if I were willing
            # to let this sit and brainstorm for a bit.
            combo_name_transfusion='Infusion',
            combo_name_elemental='Infusion',
            rewards1=[
                ('/Game/PatchDLC/VaultCard/Data/Currency/InventoryBalance_DiamondKey', None, BVC(bvc=1)),
                ],
            rewards2=[
                ('/Game/PatchDLC/VaultCard/Data/Currency/InventoryBalance_DiamondKey', None, BVC(bvc=1)),
                ],
            rewards3=[
                ('/Game/PatchDLC/VaultCard/Data/Currency/InventoryBalance_DiamondKey', None, BVC(bvc=1)),
                ],
            ),
        ModConfig(mod_label='Loot',
            mod_filename='loot',
            desc_text='loot',
            card_text='loot',
            part_text='LOOT',
            single_name='Loot',
            combo_name_money='Lootful',
            triple_name='Lootsplosion',
            # As with the grenade-ammo variant, I don't really know for here.  If I let
            # this sit for awhile I could probably come up with some stuff, but for a
            # joke mod, I'd rather just let it get out there.  So whatever, this is it.
            combo_name_transfusion='Infusion',
            combo_name_elemental='Infusion',
            rewards1=[
				(None, '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All', BVC(bvc=1, bvs=1)),
				(None, '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All', BVC(bvc=1, bvs=.45*non_gun_scale)),
				(None, '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All', BVC(bvc=1, bvs=.35*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts', BVC(bvc=1, bvs=.20*non_gun_scale)),
                ],
            rewards2=[
				(None, '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All', BVC(bvc=1, bvs=1)),
				(None, '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All', BVC(bvc=1, bvs=.45*non_gun_scale)),
				(None, '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All', BVC(bvc=1, bvs=.35*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts', BVC(bvc=1, bvs=.20*non_gun_scale)),
                ],
            rewards3=[
				(None, '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All', BVC(bvc=1, bvs=1)),
				(None, '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All', BVC(bvc=1, bvs=.45*non_gun_scale)),
				(None, '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All', BVC(bvc=1, bvs=.35*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Beastmaster', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Gunner', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Operative', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods_Siren', BVC(
					bva='/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren', bvs=.25*non_gun_scale)),
				(None, '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts', BVC(bvc=1, bvs=.20*non_gun_scale)),
                ],
            ),
        ]:

    modconf.write_mod()

