#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2021 Christopher J. Kucera
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
from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG_LOWER

###
### A buncha overengineered helper classees
###
### This whole generation script is simultaneously over-and-underengineered.  The
### classes are pretty good, but when it comes time for defining data, I really
### would've been better of making some Enums and generalizing that stuff a bit
### more, and ideally getting rid of all the crazy zip() stuff I'm doing, where
### multiple lists have to be the same length in order for things to work properly.
### Would've been nice for generating our sets of configurations as well (like
### automatically creating configurations which emphasize certain vehicles, etc.)
###
### Ah, well.
###

class Parts:
    """
    A full set of parts (including skins) for a vehicle type
    """

    def __init__(self, skins=None, armor=None, weap_gunner=None, weap_driver=None, boosts=None):
        self.skins = skins
        self.armor = armor
        self.weap_gunner = weap_gunner
        self.weap_driver = weap_driver
        self.boosts = boosts
        self.all_parts = []
        self.toc = []
        partset_parts = []
        for idx, part_cat in enumerate([skins, armor, weap_gunner, weap_driver, boosts]):
            if part_cat is None:
                part_cat = []
            partset_parts.append("""(
                    PartTypeEnum={},
                    PartType={},
                    bCanSelectMultipleParts=False,
                    bUseWeightWithMultiplePartSelection=False,
                    MultiplePartSelectionRange=(),
                    bEnabled=True,
                    Parts=({})
                )""".format(
                    Mod.get_full_cond('/Game/Vehicles/_Shared/Design/Parts/EPartType_Vehicle', 'UserDefinedEnum'),
                    idx,
                    ','.join([
                        '(PartData={},Weight=(BaseValueConstant=1))'.format(Mod.get_full_cond(p, 'BPVehiclePart_C')) for p in part_cat
                        ]),
                    ))
            if len(part_cat) > 0:
                self.toc.append((len(self.all_parts), len(part_cat)))
                self.all_parts.extend(part_cat)
            else:
                self.toc.append((-1, 0))
        self.hotfix_val_balance = '(AllParts=({}),PartTypeTOC=({})'.format(
                ','.join(['(PartData={},Weight=(BaseValueConstant=1))'.format(Mod.get_full_cond(p, 'BPVehiclePart_C')) for p in self.all_parts]),
                ','.join(['(StartIndex={},NumParts={})'.format(idx, size) for idx, size in self.toc]),
                )
        self.hotfix_val_partset = '({})'.format(','.join(partset_parts))

    def do_hotfixes(self, mod, level_name, obj_name):
        """
        Hotfix in our parts.  It seemed like we could theoretically point at least
        the PartSet over to an external object and save having to define this on
        *every single* SpawnOption, but it seems that the game doesn't like those
        references crossing object boundaries, so attempting to do so generally
        just results in a `None` reference.  So, we're stuck doing it this way!
        """
        # This statement *does* need to be EARLY -- if it's not, the skins/materials
        # won't actually load properly, and all spawned vehicles will just use the
        # default skin.
        mod.reg_hotfix(Mod.EARLYLEVEL, level_name,
                '{}.VehiclePartSetData_0'.format(obj_name),
                'ActorPartlists',
                self.hotfix_val_partset)

        # This one, however, can be an ordinary Level hotfix.
        mod.reg_hotfix(Mod.LEVEL, level_name,
                '{}.InventoryBalanceData_0'.format(obj_name),
                'RuntimePartList',
                self.hotfix_val_balance)

class Vehicle:
    """
    Class for a particular vehicle; should include all chassis types, the parts
    that make it up, and the number of seats available (though we really only
    use that for some checks in the Configuration class)
    """

    def __init__(self, name, base_title, chassis, chassis_labels, parts, num_seats, origin, extent):
        self.name = name
        self.base_title = base_title
        self.chassis = []
        self.chassis_labels = chassis_labels
        self.parts = parts
        self.num_seats = num_seats
        self.origin = origin
        self.extent = extent

        for base in chassis:
            last_bit = base.rsplit('/', 1)[1]
            self.chassis.append('{}.{}_C'.format(base, last_bit))

    def split_chassis(self):
        """
        Returns a list of new Vehicle objects, each with a *single* chassis defined.
        This can be used to lock specific spawns to a specific chassis.
        """
        to_ret = []
        for chassis, label in zip(self.chassis, self.chassis_labels):
            new_vehicle = Vehicle(self.name,
                    self.base_title,
                    [],
                    [],
                    self.parts,
                    self.num_seats,
                    self.origin,
                    self.extent,
                    )
            new_vehicle.chassis = [chassis]
            new_vehicle.chassis_labels = [label]
            to_ret.append(new_vehicle)
        return to_ret

class Seating:
    """
    Info about the seating on a vehicle
    """

    def __init__(self, *seats):
        self.seats = seats
        hotfix_parts = []
        for idx, seat in enumerate(seats):
            hotfix_parts.append('(SeatSlot={},SpawnOptions={})'.format(
                idx,
                Mod.get_full_cond(seat, 'SpawnOptionData'),
                ))
        self.hotfix_val = '({})'.format(','.join(hotfix_parts))

    def do_hotfixes(self, mod, level_name, obj_name):
        mod.reg_hotfix(Mod.LEVEL, level_name,
                obj_name,
                'DefaultSpawnOptions',
                mod.get_full_cond(self.seats[0], 'SpawnOptionData'))
        # This one *does* need to be EarlyLevel.  If not, a couple of things
        # happen:
        #   1) Riders other than the driver don't seem to actually attach to
        #      the vehicle
        #   2) The vehicle becomes weirdly passive, and doesn't attack unless
        #      attacked first.  Deposed drivers will even just walk away
        #      calmly if you haven't shot near the vehicle yet.
        mod.reg_hotfix(Mod.EARLYLEVEL, level_name,
                obj_name,
                'SeatList',
                self.hotfix_val)

class SeatWeights:
    """
    How many spawns are we going to *actually* seat in the vehicle?
    """

    def __init__(self, *weights):
        self.weights = weights
        hotfix_parts = []
        for idx, weight in enumerate(self.weights):
            hotfix_parts.append('(PassengerCount={},Weight={})'.format(
                idx+1,
                weight,
                ))
        self.hotfix_val = '({})'.format(','.join(hotfix_parts))

    def do_hotfixes(self, mod, level_name, obj_name):
        if len(self.weights) == 1:
            # I think this is the default, but whatever.
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    obj_name,
                    'bWeightedPassengersNum',
                    'False')
        else:
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    obj_name,
                    'bWeightedPassengersNum',
                    'True')
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    obj_name,
                    'WeightedPassengersNum',
                    self.hotfix_val)

class UIName:
    """
    GbxUIName objects that we're using as-is because they already name vehicles
    the way we want.  Ordinarily we wouldn't bother wrapping this in a class, but
    we're using BotUIName to handle custom names, and this way we can handle all
    cases the same way
    """

    def __init__(self, obj_name):
        self.obj_name = obj_name

    def __lt__(self, other):
        return self.obj_name.lower() < other.obj_name.lower()

    def get_full(self, mod):
        return mod.get_full_cond(self.obj_name, 'GbxUIName')

    def do_hotfixes(self, mod):
        # Nothing required!
        return

class OverrideUIName(UIName):
    """
    GbxUIName objects that we're using to provide some new vehicle names.  Names
    with this class will just be overridden entirely, without needing to revert
    them in specific maps.  For instance:

        /Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_Badass

    ... isn't actually used anywhere, so we can just override it and be done.
    Since the "Heavy" names don't really make a lot of sense anymore, we're also
    making use of a bunch of those names to fill in the gaps.
    """

    def __init__(self, obj_name, new_text):
        super().__init__(obj_name)
        self.new_text = new_text

    def __lt__(self, other):
        if hasattr(other, 'new_text'):
            return self.new_text.lower() < other.new_text.lower()
        else:
            return super().__lt__(other)

    def do_hotfixes(self, mod):
        mod.comment('Handling naming for {}'.format(self.new_text))
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                self.obj_name,
                'DisplayName',
                self.new_text)
        mod.newline()

class BotUIName(OverrideUIName):
    """
    GbxUIName objects that we're using to provide some new vehicle names.  These
    are all assumed to be contestants in the bot matches in the Spendopticon from
    DLC1, and thus the objects are only ever used inside Strip_P.  We're almost
    certainly overwriting some localization by doing this, but I figure nobody'll
    notice or care about it.

    (This isn't actually being used in the "live" version of this mod anymore.  My
    original plan was to continue the "<Team> <Variant> <Vehicle>" naming scheme,
    which requires a lot of UIName objects, but I've since dropped the "Team"
    component, so we have plenty without having to dip into this pool.)
    """

    def __init__(self, bot_num, orig_text, new_text):
        super().__init__('/Game/PatchDLC/Dandelion/UI/UINames/Character/RagingBot_Contestant/UIName_RagingBot_ContestantName{:03d}'.format(bot_num), new_text)
        self.orig_text = orig_text

    def do_hotfixes(self, mod):
        mod.comment('Handling naming for {}'.format(self.new_text))
        mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
                self.obj_name,
                'DisplayName',
                self.new_text)
        mod.reg_hotfix(Mod.LEVEL, 'Strip_P',
                self.obj_name,
                'DisplayName',
                self.orig_text)
        mod.newline()

class Configuration:
    """
    A specific Vehicle configuration which we're going to put into a SpawnOptions list.
    Note that there are various "transient" variables that get populated while
    processing -- make sure that a Configuration object appears only *once* in a
    single SpawnOptions edit, otherwise vars are gonna get mashed together
    """

    def __init__(self, vehicle, crew, seatweights, uinames, team):
        self.vehicle = vehicle
        self.crew = crew
        self.seatweights = seatweights
        self.uinames = uinames
        self.team = team
        self.reset_transient()

        # Various sanity checks
        if len(vehicle.chassis) != len(self.uinames):
            raise RuntimeError('Vehicle {} has {} chassis, but supplied {} UINames'.format(
                vehicle.name,
                len(vehicle.chassis),
                len(self.uinames),
                ))
        if vehicle.num_seats != len(crew.seats):
            raise RuntimeError('Vehicle {} has {} seats, but supplied a crew with {} members'.format(
                vehicle.name,
                vehicle.num_seats,
                len(crew.seats),
                ))
        for idx, seatweight in enumerate(seatweights):
            if vehicle.num_seats != len(seatweight.weights):
                raise RuntimeError('Vehicle {} has {} seats, but chassis {} was supplied weights for {}'.format(
                    vehicle.name,
                    vehicle.num_seats,
                    idx,
                    len(seatweight.weights),
                    ))

    def reset_transient(self):
        self.factory_names = []
        self.factory_weights = []
        self.factory_probabilities = []

    def get_options_hotfix_parts(self, mod):
        options_parts = []
        for factory_name, factory_weight, factory_probability in zip(
                self.factory_names,
                self.factory_weights,
                self.factory_probabilities,
                ):
            options_parts.append("""(
                    Factory={},
                    WeightParam=(
                        DisabledValueModes=110,
                        Range=(Value={:0.6f}),
                        AttributeInitializationData=(DataTableValue=(),BaseValueScale=1.000000)
                    ),
                    Probability="{:0.2f}%",
                    AliveLimitParam=(
                        ValueType=Int,
                        DisabledValueModes=110,
                        AttributeInitializationData=(DataTableValue=(),BaseValueScale=1.000000)
                    )
                )""".format(
                    mod.get_full_cond(factory_name, 'SpawnFactory_OakVehicleBuilder'),
                    factory_weight,
                    factory_probability,
                    ))
        return options_parts

    def do_hotfixes(self, mod, level_name, cur_idx, used_uinames):

        for factory_name, factory_weight, factory_probability, chassis, chassis_label, seatweight, uiname in zip(
                self.factory_names,
                self.factory_weights,
                self.factory_probabilities,
                self.vehicle.chassis,
                self.vehicle.chassis_labels,
                self.seatweights,
                self.uinames,
                ):
            mod.comment('Setting up spawn option {}: {} {}'.format(
                cur_idx,
                chassis_label,
                self.vehicle.name,
                ))

            # Parts
            self.vehicle.parts.do_hotfixes(mod, level_name, factory_name)

            # Chassis type
            chassis_full = mod.get_full_cond(chassis, 'BlueprintGeneratedClass')
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    factory_name,
                    'VehicleClass',
                    chassis_full)

            # Put the chassis type into the InvData as well
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    '{}.InventoryData_0'.format(factory_name),
                    'InventoryActorClass',
                    chassis_full)

            # Title on the InvData (I rather suspect this is unnecessary...)
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    '{}.InventoryData_0'.format(factory_name),
                    'TitlePartList',
                    '({})'.format(mod.get_full_cond(self.vehicle.base_title, 'InventoryNamePartData')))

            # Seating
            self.crew.do_hotfixes(mod, level_name, factory_name)

            # Seat Weights
            seatweight.do_hotfixes(mod, level_name, factory_name)

            # UIName
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    factory_name,
                    'UINameOverride',
                    uiname.get_full(mod))
            used_uinames.add(uiname)

            # Team
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    factory_name,
                    'CachedTeam',
                    mod.get_full_cond(self.team, 'Team'))

            # Spawn Origin/Extent
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    factory_name,
                    'SpawnOrigin',
                    '(X={},Y={},Z={})'.format(*self.vehicle.origin))
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    factory_name,
                    'SpawnExtent',
                    '(X={},Y={},Z={})'.format(*self.vehicle.extent))

            # Collision handling
            mod.reg_hotfix(Mod.LEVEL, level_name,
                    factory_name,
                    'CollisionHandling',
                    'AdjustIfPossibleButAlwaysSpawn')

            # Finish up
            mod.newline()
            cur_idx += 1

        return cur_idx

###
### Now define a whole bunch of data
###

# First up - part lists
parts_outrunner = Parts(
        skins=[
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Atlas',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Batmobile',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_COV',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Dahl',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Default',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Ellie1',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_FF',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Fire',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Forest',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_GBX',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Gold',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Grog',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Gulf',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Herbie',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Hexagon',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Houndstooth',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_HubbaBubba',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Hyp',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Hyp2',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Infection',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Jakobs',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Maliwan',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Maya',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Pirate',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Prisa',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_RedMachine',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_SDCC',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Stealth',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Torgue',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Tri',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Vladof',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_Wrap',
            ],
        armor=[
            '/Game/Vehicles/Outrunner/Design/Parts/Armor/VehiclePart_Outrunner_Armor_BasicArmor',
            '/Game/Vehicles/Outrunner/Design/Parts/Armor/VehiclePart_Outrunner_Armor_HeavyArmor',
            ],
        weap_gunner=[
            '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_MissileLauncher/HeavyMissile/VehiclePart_Weapon_HeavyMissile_Native',
            '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_MissileLauncher/SwarmerMissile/VehiclePart_Weapon_SwarmerMissile_Native',
            '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_MissileLauncher/ShotgunMissile/VehiclePart_Weapon_ShotgunMissile_Native',
            ],
        weap_driver=[
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MachineGun/OutrunnerMachineGun/VehiclePart_WeaponDriver_OutrunnerMachineGun_Native',
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_FlameThrower/FlameThrower/VehiclePart_WeaponDriver_FlameThrower_Native',
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_FlameThrower/TeslaCoil/VehiclePart_WeaponDriver_TeslaCoil_Native',
            ],
        boosts=[
            '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/BoostCanisters/VehiclePart_CoreMod_BoostCanisters',
            '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/BlazeBooster/VehiclePart_CoreMod_BlazeBooster',
            '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/EnergyCells/VehiclePart_CoreMod_EnergyCells',
            '/Game/Vehicles/Outrunner/Design/Parts/CoreMod/RazerWings/VehiclePart_CoreMod_RazerWings',
            ],
        )

parts_cyclone = Parts(
        skins=[
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Atlas',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Chopper',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Chups',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_COV',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Dahl',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Dark',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Default',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Ellie1',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Forest',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_GBX',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_GC',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_HubbaBubba',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Hyp',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Hyp2',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Jakobs',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_LifeSaver',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Maliwan',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Mask',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Maya',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Ninja',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Pepto',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Police',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Stealth',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Torgue',
            '/Game/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Vladof',
            '/Game/PatchDLC/Hibiscus/Vehicles/Revolver/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Revolver_Fish',
            ],
        armor=[
            '/Game/Vehicles/Revolver/Design/Parts/Armor/VehiclePart_Revolver_Armor_BasicArmor',
            '/Game/Vehicles/Revolver/Design/Parts/Armor/VehiclePart_Revolver_Armor_HeavyArmor',
            ],
        weap_gunner=[],
        weap_driver=[
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MechanicalLauncher/SawBladeLancer/VehiclePart_WeaponDriver_SawBladeLauncher_Native',
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MechanicalLauncher/RevolverMachineGun/VehiclePart_WeaponDriver_RevolverMachineGun_Native',
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MechanicalLauncher/BlazeRodLancer/VehiclePart_WeaponDriver_BlazeRodLauncher_Native',
            ],
        boosts=[
            '/Game/Vehicles/Revolver/Design/Parts/CoreMod/HeavyBooster/VehiclePart_HeavyBooster',
            '/Game/Vehicles/Revolver/Design/Parts/CoreMod/Firestarter/VehiclePart_FireStarter',
            '/Game/Vehicles/Revolver/Design/Parts/CoreMod/DigiThruster/VehiclePart_DigiThruster',
            '/Game/Vehicles/Revolver/Design/Parts/CoreMod/CryoBooster/VehiclePart_CryoBooster',
            ],
        )

parts_technical = Parts(
        skins=[
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Atlas',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Bling',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_BlueAngel',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Bubblegum',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Camo',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Checker',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Cov',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Dahl',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Default',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Dino',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_E3',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Ellie1',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Festi',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Forest',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_GBX',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_GoldenTicket',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Halftone',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_HYP',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_JAK',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_MAL',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Maya',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Plaid',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Roadkill',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Sand',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Skag',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Stealth',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Thunderbird',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Torgue',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Vaughn',
            '/Game/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Vladof',
            '/Game/PatchDLC/Hibiscus/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Tentacle',
            '/Game/PatchDLC/Hibiscus/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Fish',
            '/Game/PatchDLC/Hibiscus/Vehicles/Technical/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Technical_Frost',
            ],
        armor=[
            '/Game/Vehicles/Technical/Design/Parts/Armor/VehiclePart_Techincal_Armor_BasicArmor',
            '/Game/Vehicles/Technical/Design/Parts/Armor/VehiclePart_Technical_Armor_HeavyArmor',
            '/Game/Vehicles/Technical/Design/Parts/Armor/VehiclePart_Technical_Armor_MeatGrinder',
            ],
        weap_gunner=[
            '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_Catapult/BarrelLauncher/VehiclePart_Weapon_BarrelLauncher_Native',
            '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_Catapult/PropelledBombsLauncher/VehiclePart_Weapon_PropelledBombsLauncher_Native',
            '/Game/Vehicles/VehicleWeapons/GunnerWeapons/Type_Catapult/StickyBombLauncher/VehiclePart_Weapon_StickyBombs_Native',
            ],
        weap_driver=[
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MachineGun/MachineGun/VehiclePart_WeaponDriver_MachineGun_Native',
            '/Game/Vehicles/VehicleWeapons/DriverWeapons/Type_MachineGun/FlakCannon/VehiclePart_WeaponDriver_FlakCannon_Native',
            ],
        boosts=[
            '/Game/Vehicles/Technical/Design/Parts/Accessory/ToxicBooster/VehiclePart_CoreMod_ToxicBooster',
            '/Game/Vehicles/Technical/Design/Parts/Accessory/FuelBarrels/VehiclePart_CoreMod_FuelBarrels',
            '/Game/Vehicles/Technical/Design/Parts/Accessory/FlatBed/VehiclePart_CoreMod_Flatbed',
            '/Game/Vehicles/Technical/Design/Parts/Accessory/JetBooster/VehiclePart_CoreMod_JetBooster',
            ],
        )

# Special-case Technical parts for forcing a flatbed
parts_technical_flatbed = Parts(
        skins=parts_technical.skins,
        armor=parts_technical.armor,
        weap_gunner=parts_technical.weap_gunner,
        weap_driver=parts_technical.weap_driver,
        boosts=[
            '/Game/Vehicles/Technical/Design/Parts/Accessory/FlatBed/VehiclePart_CoreMod_Flatbed',
            ],
        )

parts_jetbeast = Parts(
        skins=[
            '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Default',
            '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin1',
            '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin2',
            '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin3',
            '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin4',
            '/Geranium/Vehicles/Horse/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Horse_Skin5',
            ],
        armor=[
            '/Geranium/Vehicles/Horse/Design/Parts/Armor/VehiclePart_Horse_Armor_HardSaddleBags',
            '/Geranium/Vehicles/Horse/Design/Parts/Armor/VehiclePart_Horse_Armor_SoftSaddleBags',
            ],
        weap_gunner=[],
        weap_driver=[
            '/Geranium/Vehicles/VehicleWeapons/Type_DualMachineGun/VehiclePart_WeaponDriver_Horse_DualMachineGun',
            '/Geranium/Vehicles/VehicleWeapons/Type_Cannon/VehiclePart_WeaponDriver_Horse_Cannon',
            '/Geranium/Vehicles/VehicleWeapons/Type_Mortar/VehiclePart_Weapon_Horse_Mortar',
            ],
        boosts=[
            '/Geranium/Vehicles/Horse/Design/Parts/CoreMod/TwinEngine/VehiclePart_TwinEngine_Horse',
            '/Geranium/Vehicles/Horse/Design/Parts/CoreMod/SingleEngine/VehiclePart_SingleBooster_Horse',
            ],
        )

# Basic Vehicle Definitions
outrunner = Vehicle('Outrunner',
        base_title='/Game/Vehicles/Outrunner/Design/Name_Outrunner',
        chassis=[
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_TwitchyWheels',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_ZipWheels',
            '/Game/Vehicles/Outrunner/Vehicle/Vehicle_Outrunner_HoverWheels',
            ],
        chassis_labels=[
            'Dune Buggy',
            'Twitch',
            'Zip',
            'Hover',
            ],
        parts=parts_outrunner,
        num_seats=2,
        origin=(-4.2730255, 0.0, -1.4607391),
        extent=(218.57593, 126.6194, 106.6422),
        )

technical = Vehicle('Technical',
        base_title='/Game/Vehicles/Technical/Design/Name_Technical',
        chassis=[
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical',
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_HoverWheels',
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BarbedWheels',
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BigWheels',
            ],
        chassis_labels=[
            'All-Terrain',
            'Hover',
            'Barbed',
            'Monster',
            ],
        parts=parts_technical,
        num_seats=4,
        origin=(5.056488, 0.0, 17.908813),
        extent=(349.4303, 161.26369, 129.8378),
        )
# We want a hover-specific spawn for a single spawn
technical_reg, technical_hover, technical_barbed, technical_monster = technical.split_chassis()

# We also want a flatbed-only technical for joke "stolen" vehicles
technical_flatbed = Vehicle('Flatbed Technical',
        base_title='/Game/Vehicles/Technical/Design/Name_Technical',
        chassis=[
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical',
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_HoverWheels',
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BarbedWheels',
            '/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BigWheels',
            ],
        chassis_labels=[
            'All-Terrain',
            'Hover',
            'Barbed',
            'Monster',
            ],
        parts=parts_technical_flatbed,
        num_seats=4,
        origin=(5.056488, 0.0, 17.908813),
        extent=(349.4303, 161.26369, 129.8378),
        )

cyclone = Vehicle('Cyclone',
        base_title='/Game/Vehicles/Revolver/Design/Name_Revolver',
        chassis=[
            '/Game/Vehicles/Revolver/Vehicle/Vehicle_Revolver',
            '/Game/Vehicles/Revolver/Vehicle/Vehicle_Revolver_DualWheel',
            '/Game/Vehicles/Revolver/Vehicle/Vehicle_Revolver_HoverWheels',
            '/Game/Vehicles/Revolver/Vehicle/Vehicle_Revolver_WideWheel',
            ],
        chassis_labels=[
            'Monowheel',
            'Blade',
            'Hover',
            'Wide',
            ],
        parts=parts_cyclone,
        num_seats=1,
        origin=(8.040237, 0.23180771, -48.234562),
        extent=(100.19306, 61.77092, 56.96728),
        )

jetbeast = Vehicle('Jetbeast',
        base_title='/Geranium/Vehicles/Horse/Design/Name_Horse',
        chassis=[
            '/Geranium/Vehicles/Horse/Vehicle/Vehicle_Horse_Tyrant',
            '/Geranium/Vehicles/Horse/Vehicle/Vehicle_Horse_Predator',
            '/Geranium/Vehicles/Horse/Vehicle/Vehicle_Horse_Biobeast',
            ],
        chassis_labels=[
            'Lucivore Bloodhauler',
            'Hellion Quickmaw',
            'Bellik Skiff',
            ],
        parts=parts_jetbeast,
        num_seats=1,
        origin=(8.040237, 0.23180771, -48.234562),
        extent=(100.19306, 61.77092, 56.96728),
        )

# Opted not to do this, after all.
if False:

    # UINames for vehicles
    # We *do* have plenty of UINames from that bot-fighting pool to play around with here, so
    # at the moment I've retained the base-game convention of labelling vehicles as
    # "<Team> [<Chassis>] <Vehicle>", which means five separate titles for each chassis variant.
    # For the added "joke" vehicles I'm planning on (like Jabber vehicles and such) I'm just
    # going to use a single name regardless of chassis, but I honestly sort of wonder if I should
    # do the same for everything else, too.  Either get rid of the Chassis indicator, or even the
    # Team.

    # Outrunner - Regular
    uiname_outrunner_reg_cov = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_COV')
    uiname_outrunner_reg_mal = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_Maliwan1')
    uiname_outrunner_reg_dark = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_DarkMaliwan')
    uiname_outrunner_reg_dr = BotUIName(13, "Ze-Freluquet", "Devil Rider Outrunner")
    uiname_outrunner_reg_dlc2 = BotUIName(14, "BananeFromHell", "Mumblers Outrunner")

    # Outrunner - Hover
    uiname_outrunner_hover_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_COV_Badass', 'COV Hover Runner')
    uiname_outrunner_hover_mal = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_Maliwan')
    uiname_outrunner_hover_dark = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_DarkMaliwan')
    uiname_outrunner_hover_dr = BotUIName(15, "SAB1NG92", "Devil Rider Hover Runner")
    uiname_outrunner_hover_dlc2 = BotUIName(16, "Valeon", "Mumblers Outrunner")

    # Outrunner - Twitch
    uiname_outrunner_twitch_cov = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Twitchrunner_COV')
    uiname_outrunner_twitch_mal = UIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_TwitchRunner_Maliwan')
    uiname_outrunner_twitch_dark = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_TwitchRunner_Maliwan_Badass', 'Dark Maliwan Twitch Runner')
    uiname_outrunner_twitch_dr = BotUIName(17, "Warwill", "Devil Rider Twitch Runner")
    uiname_outrunner_twitch_dlc2 = BotUIName(18, "KIAMaker", "Mumblers Twitch Runner")

    # Outrunner - Zip
    uiname_outrunner_zip_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_twitchRunner_COV_Badass', 'COV Zip Runner')
    uiname_outrunner_zip_mal = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_Maliwan_Badass', 'Maliwan Zip Runner')
    uiname_outrunner_zip_dark = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_DarkMaliwan_Badass', 'Dark Maliwan Zip Runner')
    uiname_outrunner_zip_dr = BotUIName(19, "Serge-1", "Devil Rider Zip Runner")
    uiname_outrunner_zip_dlc2 = BotUIName(20, "Serge-2", "Mumblers Zip Runner")

    # Outrunner UIName lists
    uiname_list_outrunner_cov = [uiname_outrunner_reg_cov, uiname_outrunner_twitch_cov, uiname_outrunner_zip_cov, uiname_outrunner_hover_cov]
    uiname_list_outrunner_mal = [uiname_outrunner_reg_mal, uiname_outrunner_twitch_mal, uiname_outrunner_zip_mal, uiname_outrunner_hover_mal]
    uiname_list_outrunner_dark = [uiname_outrunner_reg_dark, uiname_outrunner_twitch_dark, uiname_outrunner_zip_dark, uiname_outrunner_hover_dark]
    uiname_list_outrunner_dr = [uiname_outrunner_reg_dr, uiname_outrunner_twitch_dr, uiname_outrunner_zip_dr, uiname_outrunner_hover_dr]
    uiname_list_outrunner_dlc2 = [uiname_outrunner_reg_dlc2, uiname_outrunner_twitch_dlc2, uiname_outrunner_zip_dlc2, uiname_outrunner_hover_dlc2]

    # Technical - Regular
    uiname_technical_reg_cov = UIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_COV')
    uiname_technical_reg_mal = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_Maliwan_Badass', 'Maliwan Technical')
    uiname_technical_reg_dark = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_COV_Badass', 'Dark Maliwan Technical')
    uiname_technical_reg_dr = BotUIName(21, "CapitaineStar", "Devil Rider Technical")
    uiname_technical_reg_dlc2 = UIName('/Game/PatchDLC/Hibiscus/UI/UINames/Missions/Side/UIName_Technical_Hibiscus')

    # Technical - Hover
    uiname_technical_hover_cov = UIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_HoverTechnical_COV')
    uiname_technical_hover_mal = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_Badass', 'Maliwan Hover Technical')
    uiname_technical_hover_dark = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_DarkMaliwan_Badass', 'Dark Maliwan Hover Technical')
    uiname_technical_hover_dr = BotUIName(22, "Thebetter22", "Devil Rider Hover Technical")
    uiname_technical_hover_dlc2 = BotUIName(23, "CorporateDiva", "Mumblers Hover Technical")

    # Technical - Barbed
    uiname_technical_barbed_cov = BotUIName(1, "AwfulGamer", "COV Barbed Technical")
    uiname_technical_barbed_mal = BotUIName(3, "D.V.L.", "Maliwan Barbed Technical")
    uiname_technical_barbed_dark = BotUIName(2, "Khul'Trag", "Dark Maliwan Barbed Technical")
    uiname_technical_barbed_dr = BotUIName(24, "Zaiuskhan", "Devil Rider Barbed Technical")
    uiname_technical_barbed_dlc2 = BotUIName(25, "Akiosabt", "Mumblers Barbed Technical")

    # Technical - Monster
    uiname_technical_monster_cov = BotUIName(4, "MainGuy", "COV Monster Technical")
    uiname_technical_monster_mal = BotUIName(6, "Monsieur Pepui", "Maliwan Monster Technical")
    uiname_technical_monster_dark = BotUIName(5, "Francking", "Dark Maliwan Monster Technical")
    uiname_technical_monster_dr = BotUIName(26, "Grenzerk", "Devil Rider Monster Technical")
    uiname_technical_monster_dlc2 = BotUIName(27, "D4T0U", "Mumblers Monster Technical")

    # Technical UIName lists
    uiname_list_technical_cov = [uiname_technical_reg_cov, uiname_technical_hover_cov, uiname_technical_barbed_cov, uiname_technical_monster_cov]
    uiname_list_technical_mal = [uiname_technical_reg_mal, uiname_technical_hover_mal, uiname_technical_barbed_mal, uiname_technical_monster_mal]
    uiname_list_technical_dark = [uiname_technical_reg_dark, uiname_technical_hover_dark, uiname_technical_barbed_dark, uiname_technical_monster_dark]
    uiname_list_technical_dr = [uiname_technical_reg_dr, uiname_technical_hover_dr, uiname_technical_barbed_dr, uiname_technical_monster_dr]
    uiname_list_technical_dlc2 = [uiname_technical_reg_dlc2, uiname_technical_hover_dlc2, uiname_technical_barbed_dlc2, uiname_technical_monster_dlc2]

    # Cyclone - Regular
    uiname_cyclone_reg_cov = UIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_COV')
    uiname_cyclone_reg_mal = UIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_Maliwan')
    uiname_cyclone_reg_dark = UIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_DarkMaliwan')
    uiname_cyclone_reg_dr = BotUIName(28, "Sercort", "Devil Rider Cyclone")
    uiname_cyclone_reg_dlc2 = BotUIName(29, "T-WIN", "Mumblers Cyclone")

    # Cyclone - Blade
    uiname_cyclone_blade_cov = UIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_BladeRevolver_COV')
    uiname_cyclone_blade_mal = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_Maliwan_Badass', 'Maliwan Blade Cyclone')
    uiname_cyclone_blade_dark = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_BladeRevolver_COV_Badass', 'Dark Maliwan Blade Cyclone')
    uiname_cyclone_blade_dr = BotUIName(30, "Xiirka", "Devil Rider Blade Cyclone")
    uiname_cyclone_blade_dlc2 = BotUIName(31, "Demeryk", "Mumblers Blade Cyclone")

    # Cyclone - Hover
    uiname_cyclone_hover_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_COV_Badass', 'COV Hover Cyclone')
    uiname_cyclone_hover_mal = UIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_Maliwan')
    uiname_cyclone_hover_dark = UIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_DarkMaliwan')
    uiname_cyclone_hover_dr = BotUIName(32, "RealReal", "Devil Rider Hover Cyclone")
    uiname_cyclone_hover_dlc2 = BotUIName(33, "ACleverPony", "Mumblers Hover Cyclone")

    # Cyclone - Wide
    uiname_cyclone_wide_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_DarkMaliwan_Badass', 'COV Wide Cyclone')
    uiname_cyclone_wide_mal = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_Maliwan_Badass', 'Maliwan Wide Cyclone')
    uiname_cyclone_wide_dark = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_DarkMaliwan_Badass', 'Dark Maliwan Wide Cyclone')
    uiname_cyclone_wide_dr = BotUIName(34, "Maximus Primus", "Devil Rider Wide Cyclone")
    uiname_cyclone_wide_dlc2 = BotUIName(35, "Egagj035", "Mumblers Wide Cyclone")

    # Cyclone UIName lists
    uiname_list_cyclone_cov = [uiname_cyclone_reg_cov, uiname_cyclone_blade_cov, uiname_cyclone_hover_cov, uiname_cyclone_wide_cov]
    uiname_list_cyclone_mal = [uiname_cyclone_reg_mal, uiname_cyclone_blade_mal, uiname_cyclone_hover_mal, uiname_cyclone_wide_mal]
    uiname_list_cyclone_dark = [uiname_cyclone_reg_dark, uiname_cyclone_blade_dark, uiname_cyclone_hover_dark, uiname_cyclone_wide_dark]
    uiname_list_cyclone_dr = [uiname_cyclone_reg_dr, uiname_cyclone_blade_dr, uiname_cyclone_hover_dr, uiname_cyclone_wide_dr]
    uiname_list_cyclone_dlc2 = [uiname_cyclone_reg_dlc2, uiname_cyclone_blade_dlc2, uiname_cyclone_hover_dlc2, uiname_cyclone_wide_dlc2]

    # Jetbeast - Lucivore Bloodhauler
    # Jetbeast names, in general, are getting completely overhauled here.  The default names
    # reference weapons, not chassis, which makes things awkward given how we're randomizing
    # things.  So basically no Jetbeast naming object remains intact.  (To be fair, the
    # majority of the stock UINames weren't ever actually *used*, anyway).
    uiname_jetbeast_bloodhauler_cov = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Empty_DMG', 'COV Lucivore Bloodhauler')
    uiname_jetbeast_bloodhauler_mal = BotUIName(7, "Vapeur Chaude", "Maliwan Lucivore Bloodhauler")
    uiname_jetbeast_bloodhauler_dark = BotUIName(10, "DjyDjy", "Dark Maliwan Lucivore Bloodhauler")
    uiname_jetbeast_bloodhauler_dr = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Punks_DMG', 'Devil Rider Lucivore Bloodhauler')
    uiname_jetbeast_bloodhauler_dlc2 = BotUIName(36, "Rulio Estebane", "Mumblers Lucivore Bloodhauler")

    # Jetbeast - Hellion Quickmaw
    uiname_jetbeast_quickmaw_cov = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Empty_Mortar', 'COV Hellion Quickmaw')
    uiname_jetbeast_quickmaw_mal = BotUIName(8, "Gwigre", "Maliwan Hellion Quickmaw")
    uiname_jetbeast_quickmaw_dark = BotUIName(11, "Babinator", "Dark Maliwan Hellion Quickmaw")
    uiname_jetbeast_quickmaw_dr = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Punks_Cannon', 'Devil Rider Hellion Quickmaw')
    uiname_jetbeast_quickmaw_dlc2 = BotUIName(37, "MarcAttack", "Mumblers Hellion Quickmaw")

    # Jetbeast - Bellik Skiff
    uiname_jetbeast_skiff_cov = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Punks_Mortar', 'COV Bellik Skiff')
    uiname_jetbeast_skiff_mal = BotUIName(9, "Khal Robo", "Maliwan Bellik Skiff")
    uiname_jetbeast_skiff_dark = BotUIName(12, "Poliiikooo", "Dark Maliwan Bellik Skiff")
    uiname_jetbeast_skiff_dr = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Empty_Cannon', 'Devil Rider Bellik Skiff')
    uiname_jetbeast_skiff_dlc2 = BotUIName(38, "PurpleLove", "Mumblers Bellik Skiff")

    # Jetbeast UIName lists
    uiname_list_jetbeast_cov = [uiname_jetbeast_bloodhauler_cov, uiname_jetbeast_quickmaw_cov, uiname_jetbeast_skiff_cov]
    uiname_list_jetbeast_mal = [uiname_jetbeast_bloodhauler_mal, uiname_jetbeast_quickmaw_mal, uiname_jetbeast_skiff_mal]
    uiname_list_jetbeast_dark = [uiname_jetbeast_bloodhauler_dark, uiname_jetbeast_quickmaw_dark, uiname_jetbeast_skiff_dark]
    uiname_list_jetbeast_dr = [uiname_jetbeast_bloodhauler_dr, uiname_jetbeast_quickmaw_dr, uiname_jetbeast_skiff_dr]
    uiname_list_jetbeast_dlc2 = [uiname_jetbeast_bloodhauler_dlc2, uiname_jetbeast_quickmaw_dlc2, uiname_jetbeast_skiff_dlc2]

    # UINames - Bot Overrides (just here for easy copy+pasting, while building this out)
    # These ones have been used, so far:
    #uiname_01 = BotUIName(1, "AwfulGamer", "foo")
    #uiname_02 = BotUIName(2, "Khul'Trag", "foo")
    #uiname_03 = BotUIName(3, "D.V.L.", "foo")
    #uiname_04 = BotUIName(4, "MainGuy", "foo")
    #uiname_05 = BotUIName(5, "Francking", "foo")
    #uiname_06 = BotUIName(6, "Monsieur Pepui", "foo")
    #uiname_07 = BotUIName(7, "Vapeur Chaude", "foo")
    #uiname_08 = BotUIName(8, "Gwigre", "foo")
    #uiname_09 = BotUIName(9, "Khal Robo", "foo")
    #uiname_10 = BotUIName(10, "DjyDjy", "foo")
    #uiname_11 = BotUIName(11, "Babinator", "foo")
    #uiname_12 = BotUIName(12, "Poliiikooo", "foo")
    #uiname_13 = BotUIName(13, "Ze-Freluquet", "foo")
    #uiname_14 = BotUIName(14, "BananeFromHell", "foo")
    #uiname_15 = BotUIName(15, "SAB1NG92", "foo")
    #uiname_16 = BotUIName(16, "Valeon", "foo")
    #uiname_17 = BotUIName(17, "Warwill", "foo")
    #uiname_18 = BotUIName(18, "KIAMaker", "foo")
    #uiname_19 = BotUIName(19, "Serge-1", "foo")
    #uiname_20 = BotUIName(20, "Serge-2", "foo")
    #uiname_21 = BotUIName(21, "CapitaineStar", "foo")
    #uiname_22 = BotUIName(22, "Thebetter22", "foo")
    #uiname_23 = BotUIName(23, "CorporateDiva", "foo")
    #uiname_24 = BotUIName(24, "Zaiuskhan", "foo")
    #uiname_25 = BotUIName(25, "Akiosabt", "foo")
    #uiname_26 = BotUIName(26, "Grenzerk", "foo")
    #uiname_27 = BotUIName(27, "D4T0U", "foo")
    #uiname_28 = BotUIName(28, "Sercort", "foo")
    #uiname_29 = BotUIName(29, "T-WIN", "foo")
    #uiname_30 = BotUIName(30, "Xiirka", "foo")
    #uiname_31 = BotUIName(31, "Demeryk", "foo")
    #uiname_32 = BotUIName(32, "RealReal", "foo")
    #uiname_33 = BotUIName(33, "ACleverPony", "foo")
    #uiname_34 = BotUIName(34, "Maximus Primus", "foo")
    #uiname_35 = BotUIName(35, "Egagj035", "foo")
    #uiname_36 = BotUIName(36, "Rulio Estebane", "foo")
    #uiname_37 = BotUIName(37, "MarcAttack", "foo")
    #uiname_38 = BotUIName(38, "PurpleLove", "foo")

    # These are currently available for the taking:
    #uiname_39 = BotUIName(39, "Fred Wallet", "foo")
    #uiname_40 = BotUIName(40, "Prelart", "foo")
    #uiname_41 = BotUIName(41, "John4", "foo")
    #uiname_42 = BotUIName(42, "Hybrid E.T.", "foo")
    #uiname_43 = BotUIName(43, "NeoTrack-A", "foo")
    #uiname_44 = BotUIName(44, "Derebiru", "foo")
    #uiname_45 = BotUIName(45, "Aragar", "foo")
    #uiname_46 = BotUIName(46, "Ahiyan", "foo")

# This is the one we're now doing for real.
if True:

    # UINames for vehicles
    # In this version, we're actually gonna omit the team/faction entirely.  Doing so seemed
    # popular enough in a quick little Discord poll, and this way we've got a lot more room
    # for expansion, and also don't have to yank UINames from that bot-fighting pool.  (Though
    # I'll leave that stuff in, in case I decide I want it after all.)  I'm going to keep
    # separate vars for each team, though, just so's I can easily switch back at any point,
    # if need be.

    # Outrunner - Regular
    uiname_outrunner_reg_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_COV', 'Dune Buggy Runner')
    uiname_outrunner_reg_mal = uiname_outrunner_reg_cov
    uiname_outrunner_reg_dark = uiname_outrunner_reg_cov
    uiname_outrunner_reg_dr = uiname_outrunner_reg_cov
    uiname_outrunner_reg_dlc2 = uiname_outrunner_reg_cov

    # Outrunner - Hover
    uiname_outrunner_hover_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_Maliwan', 'Hover Runner')
    uiname_outrunner_hover_mal = uiname_outrunner_hover_cov
    uiname_outrunner_hover_dark = uiname_outrunner_hover_cov
    uiname_outrunner_hover_dr = uiname_outrunner_hover_cov
    uiname_outrunner_hover_dlc2 = uiname_outrunner_hover_cov

    # Outrunner - Twitch
    uiname_outrunner_twitch_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Twitchrunner_COV', 'Twitch Runner')
    uiname_outrunner_twitch_mal = uiname_outrunner_twitch_cov
    uiname_outrunner_twitch_dark = uiname_outrunner_twitch_cov
    uiname_outrunner_twitch_dr = uiname_outrunner_twitch_cov
    uiname_outrunner_twitch_dlc2 = uiname_outrunner_twitch_cov

    # Outrunner - Zip
    uiname_outrunner_zip_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_twitchRunner_COV_Badass', 'Zip Runner')
    uiname_outrunner_zip_mal = uiname_outrunner_zip_cov
    uiname_outrunner_zip_dark = uiname_outrunner_zip_cov
    uiname_outrunner_zip_dr = uiname_outrunner_zip_cov
    uiname_outrunner_zip_dlc2 = uiname_outrunner_zip_cov

    # Outrunner UIName lists
    uiname_list_outrunner_cov = [uiname_outrunner_reg_cov, uiname_outrunner_twitch_cov, uiname_outrunner_zip_cov, uiname_outrunner_hover_cov]
    uiname_list_outrunner_mal = [uiname_outrunner_reg_mal, uiname_outrunner_twitch_mal, uiname_outrunner_zip_mal, uiname_outrunner_hover_mal]
    uiname_list_outrunner_dark = [uiname_outrunner_reg_dark, uiname_outrunner_twitch_dark, uiname_outrunner_zip_dark, uiname_outrunner_hover_dark]
    uiname_list_outrunner_dr = [uiname_outrunner_reg_dr, uiname_outrunner_twitch_dr, uiname_outrunner_zip_dr, uiname_outrunner_hover_dr]
    uiname_list_outrunner_dlc2 = [uiname_outrunner_reg_dlc2, uiname_outrunner_twitch_dlc2, uiname_outrunner_zip_dlc2, uiname_outrunner_hover_dlc2]

    # Technical - Regular
    uiname_technical_reg_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_COV', 'All-Terrain Technical')
    uiname_technical_reg_mal = uiname_technical_reg_cov
    uiname_technical_reg_dark = uiname_technical_reg_cov
    uiname_technical_reg_dr = uiname_technical_reg_cov
    uiname_technical_reg_dlc2 = uiname_technical_reg_cov

    # Technical - Hover
    uiname_technical_hover_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_HoverTechnical_COV', 'Hover Technical')
    uiname_technical_hover_mal = uiname_technical_hover_cov
    uiname_technical_hover_dark = uiname_technical_hover_cov
    uiname_technical_hover_dr = uiname_technical_hover_cov
    uiname_technical_hover_dlc2 = uiname_technical_hover_cov

    # Technical - Barbed
    uiname_technical_barbed_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_COV_Badass', 'Barbed Technical')
    uiname_technical_barbed_mal = uiname_technical_barbed_cov
    uiname_technical_barbed_dark = uiname_technical_barbed_cov
    uiname_technical_barbed_dr = uiname_technical_barbed_cov
    uiname_technical_barbed_dlc2 = uiname_technical_barbed_cov

    # Technical - Monster
    uiname_technical_monster_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Technical/UIName_Technical_Badass', 'Monster Technical')
    uiname_technical_monster_mal = uiname_technical_monster_cov
    uiname_technical_monster_dark = uiname_technical_monster_cov
    uiname_technical_monster_dr = uiname_technical_monster_cov
    uiname_technical_monster_dlc2 = uiname_technical_monster_cov

    # Technical UIName lists
    uiname_list_technical_cov = [uiname_technical_reg_cov, uiname_technical_hover_cov, uiname_technical_barbed_cov, uiname_technical_monster_cov]
    uiname_list_technical_mal = [uiname_technical_reg_mal, uiname_technical_hover_mal, uiname_technical_barbed_mal, uiname_technical_monster_mal]
    uiname_list_technical_dark = [uiname_technical_reg_dark, uiname_technical_hover_dark, uiname_technical_barbed_dark, uiname_technical_monster_dark]
    uiname_list_technical_dr = [uiname_technical_reg_dr, uiname_technical_hover_dr, uiname_technical_barbed_dr, uiname_technical_monster_dr]
    uiname_list_technical_dlc2 = [uiname_technical_reg_dlc2, uiname_technical_hover_dlc2, uiname_technical_barbed_dlc2, uiname_technical_monster_dlc2]

    # Cyclone - Regular
    uiname_cyclone_reg_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_COV', 'Monowheel Cyclone')
    uiname_cyclone_reg_mal = uiname_cyclone_reg_cov
    uiname_cyclone_reg_dark = uiname_cyclone_reg_cov
    uiname_cyclone_reg_dr = uiname_cyclone_reg_cov
    uiname_cyclone_reg_dlc2 = uiname_cyclone_reg_cov

    # Cyclone - Blade
    uiname_cyclone_blade_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_BladeRevolver_COV', 'Blade Cyclone')
    uiname_cyclone_blade_mal = uiname_cyclone_blade_cov
    uiname_cyclone_blade_dark = uiname_cyclone_blade_cov
    uiname_cyclone_blade_dr = uiname_cyclone_blade_cov
    uiname_cyclone_blade_dlc2 = uiname_cyclone_blade_cov

    # Cyclone - Hover
    uiname_cyclone_hover_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_Maliwan', 'Hover Cyclone')
    uiname_cyclone_hover_mal = uiname_cyclone_hover_cov
    uiname_cyclone_hover_dark = uiname_cyclone_hover_cov
    uiname_cyclone_hover_dr = uiname_cyclone_hover_cov
    uiname_cyclone_hover_dlc2 = uiname_cyclone_hover_cov

    # Cyclone - Wide
    uiname_cyclone_wide_cov = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_DarkMaliwan_Badass', 'Wide Cyclone')
    uiname_cyclone_wide_mal = uiname_cyclone_wide_cov
    uiname_cyclone_wide_dark = uiname_cyclone_wide_cov
    uiname_cyclone_wide_dr = uiname_cyclone_wide_cov
    uiname_cyclone_wide_dlc2 = uiname_cyclone_wide_cov

    # Cyclone UIName lists
    uiname_list_cyclone_cov = [uiname_cyclone_reg_cov, uiname_cyclone_blade_cov, uiname_cyclone_hover_cov, uiname_cyclone_wide_cov]
    uiname_list_cyclone_mal = [uiname_cyclone_reg_mal, uiname_cyclone_blade_mal, uiname_cyclone_hover_mal, uiname_cyclone_wide_mal]
    uiname_list_cyclone_dark = [uiname_cyclone_reg_dark, uiname_cyclone_blade_dark, uiname_cyclone_hover_dark, uiname_cyclone_wide_dark]
    uiname_list_cyclone_dr = [uiname_cyclone_reg_dr, uiname_cyclone_blade_dr, uiname_cyclone_hover_dr, uiname_cyclone_wide_dr]
    uiname_list_cyclone_dlc2 = [uiname_cyclone_reg_dlc2, uiname_cyclone_blade_dlc2, uiname_cyclone_hover_dlc2, uiname_cyclone_wide_dlc2]

    # Jetbeast - Lucivore Bloodhauler
    uiname_jetbeast_bloodhauler_cov = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Empty_DMG', 'Lucivore Bloodhauler')
    uiname_jetbeast_bloodhauler_mal = uiname_jetbeast_bloodhauler_cov
    uiname_jetbeast_bloodhauler_dark = uiname_jetbeast_bloodhauler_cov
    uiname_jetbeast_bloodhauler_dr = uiname_jetbeast_bloodhauler_cov
    uiname_jetbeast_bloodhauler_dlc2 = uiname_jetbeast_bloodhauler_cov

    # Jetbeast - Hellion Quickmaw
    uiname_jetbeast_quickmaw_cov = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Empty_Mortar', 'Hellion Quickmaw')
    uiname_jetbeast_quickmaw_mal = uiname_jetbeast_quickmaw_cov
    uiname_jetbeast_quickmaw_dark = uiname_jetbeast_quickmaw_cov
    uiname_jetbeast_quickmaw_dr = uiname_jetbeast_quickmaw_cov
    uiname_jetbeast_quickmaw_dlc2 = uiname_jetbeast_quickmaw_cov

    # Jetbeast - Bellik Skiff
    uiname_jetbeast_skiff_cov = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Punks_Mortar', 'Bellik Skiff')
    uiname_jetbeast_skiff_mal = uiname_jetbeast_skiff_cov
    uiname_jetbeast_skiff_dark = uiname_jetbeast_skiff_cov
    uiname_jetbeast_skiff_dr = uiname_jetbeast_skiff_cov
    uiname_jetbeast_skiff_dlc2 = uiname_jetbeast_skiff_cov

    # Jetbeast UIName lists
    uiname_list_jetbeast_cov = [uiname_jetbeast_bloodhauler_cov, uiname_jetbeast_quickmaw_cov, uiname_jetbeast_skiff_cov]
    uiname_list_jetbeast_mal = [uiname_jetbeast_bloodhauler_mal, uiname_jetbeast_quickmaw_mal, uiname_jetbeast_skiff_mal]
    uiname_list_jetbeast_dark = [uiname_jetbeast_bloodhauler_dark, uiname_jetbeast_quickmaw_dark, uiname_jetbeast_skiff_dark]
    uiname_list_jetbeast_dr = [uiname_jetbeast_bloodhauler_dr, uiname_jetbeast_quickmaw_dr, uiname_jetbeast_skiff_dr]
    uiname_list_jetbeast_dlc2 = [uiname_jetbeast_bloodhauler_dlc2, uiname_jetbeast_quickmaw_dlc2, uiname_jetbeast_skiff_dlc2]

    # Some joke UINames
    uiname_outrunner_stolen = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_Maliwan1', "Stolen Outrunner")
    uiname_technical_stolen = OverrideUIName('/Game/PatchDLC/Hibiscus/UI/UINames/Missions/Side/UIName_Technical_Hibiscus', "Stolen Technical")
    uiname_cyclone_stolen = OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_Maliwan', "Stolen Cyclone")
    uiname_jetbeast_stolen = OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Punks_Cannon', "Stolen Jetbeast")

    # Leftover vehicle UINames we can use for other shenanigans:
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_DarkMaliwan', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_COV_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_DarkMaliwan', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_TwitchRunner_Maliwan', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_TwitchRunner_Maliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_Maliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_HoverRunner_DarkMaliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_Maliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Outrunner/UIName_Outrunner_DarkMaliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_DarkMaliwan', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_Maliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_BladeRevolver_COV_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_Revolver_COV_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_DarkMaliwan', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_Maliwan_Badass', "foo")
    #OverrideUIName('/Game/Vehicles/_Shared/Design/UINames/Revolver/UIName_HoverRevolver_DarkMaliwan_Badass', "foo")
    #OverrideUIName('/Geranium/Enemies/_Spawning/Vehicles/Horse/UINames/UIName_Vehicle_Horse_Empty_Cannon', "foo")

# Teams
team_cov = '/Game/Common/_Design/Teams/Team_CotV'
team_mal = '/Game/Common/_Design/Teams/Team_Maliwan'
team_dlc2 = '/Game/PatchDLC/Hibiscus/Teams/Team_FrostBiter'
team_jabber = '/Game/Common/_Design/Teams/Team_Ape'
team_cult = '/Game/PatchDLC/Hibiscus/Teams/Team_Cultist'

# Riders
rider_cov = '/Game/Enemies/_Spawning/CotV/Punks/Variants/SpawnOptions_PunkBasic'
rider_cov_badass = '/Game/Enemies/_Spawning/CotV/Punks/Variants/SpawnOptions_PunkBadass'
rider_mal = '/Game/Enemies/_Spawning/Maliwan/Troopers/Variants/SpawnOptions_TrooperBasic'
rider_mal_badass = '/Game/Enemies/_Spawning/Maliwan/Troopers/Variants/SpawnOptions_TrooperBadass'
rider_mal_heavy = '/Game/Enemies/_Spawning/Maliwan/Heavies/Variants/SpawnOptions_HeavyBasic'
rider_dark = '/Game/Enemies/_Spawning/Maliwan/Troopers/Variants/SpawnOptions_TrooperBasicDark'
rider_dark_badass = '/Game/Enemies/_Spawning/Maliwan/Troopers/Variants/SpawnOptions_TrooperBadassDark'
rider_dark_heavy = '/Game/Enemies/_Spawning/Maliwan/Heavies/Variants/SpawnOptions_HeavyBadassDark_Random'
rider_passenger = '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/SpawnOptions_CotV_PassengerMix'
rider_ep05 = '/Game/Missions/Plot/Ep05_OvercomeHQBlockade/EchoTechnical/SpawnOptions_OvercomeBlockade_PunkWithEchoLog'
rider_dlc2 = '/Hibiscus/Enemies/_Spawning/FrostBiter/Variants/SpawnOptions_FrostBiter_Punk'
rider_dr = '/Geranium/Enemies/_Spawning/COV/Punks/Variants/SpawnOptions_GerPunkBasic'

# "Joke" Riders
rider_jabber = '/Game/Enemies/_Spawning/Ape/Variants/SpawnOptions_ApeBasic'
rider_jabber_badass = '/Game/Enemies/_Spawning/Ape/Variants/SpawnOptions_ApeBadass'
rider_nog = '/Game/Enemies/_Spawning/Maliwan/Nog/Variants/SpawnOptions_NogBasic'
rider_nog_badass = '/Game/Enemies/_Spawning/Maliwan/Nog/Variants/SpawnOptions_NogBadass'
rider_tink = '/Game/Enemies/_Spawning/CotV/Tinks/Variants/SpawnOptions_TinkBasic'
rider_tink_badass = '/Game/Enemies/_Spawning/CotV/Tinks/Variants/SpawnOptions_TinkBadass'
rider_skag = '/Game/Enemies/_Spawning/Skags/Variants/SpawnOptions_SkagAdult'
rider_skrit = '/Hibiscus/Enemies/_Spawning/Cultist/Minion/Variants/SpawnOptions_MinionBasic'
rider_skrit_badass = '/Hibiscus/Enemies/_Spawning/Cultist/Minion/Variants/SpawnOptions_MinionBadass'
rider_wolven = '/Hibiscus/Enemies/_Spawning/Wolf/Variants/SpawnOptions_Wolven_Basic'
rider_rustler = '/Geranium/Enemies/_Spawning/COV/Tinks/Variants/SpawnOptions_GerTinkBasic'
rider_rustler_badass = '/Geranium/Enemies/_Spawning/COV/Tinks/Variants/SpawnOptions_GerTinkBadass'
rider_bellik = '/Geranium/Enemies/_Spawning/Biobeast/Variants/SpawnOption_Biobeast_Fodder'

# Crews.  One per available seat.
crew_cov_1 = Seating(rider_cov)
crew_cov_badass_1 = Seating(rider_cov_badass)
crew_cov_2 = Seating(rider_cov, rider_cov)
crew_cov_badass_2 = Seating(rider_cov, rider_cov_badass)
crew_cov_4 = Seating(rider_cov, rider_cov, rider_passenger, rider_passenger)
crew_cov_badass_4 = Seating(rider_cov, rider_cov_badass, rider_cov, rider_cov_badass)
crew_ep05 = Seating(rider_ep05, rider_cov, rider_passenger, rider_passenger)
crew_mal_1 = Seating(rider_mal)
crew_mal_badass_1 = Seating(rider_mal_badass)
crew_mal_2 = Seating(rider_mal, rider_mal)
crew_mal_badass_2 = Seating(rider_mal, rider_mal_badass)
crew_mal_4 = Seating(rider_mal, rider_mal, rider_mal, rider_mal)
crew_mal_badass_4 = Seating(rider_mal, rider_mal_badass, rider_mal, rider_mal_heavy)
crew_dark_1 = Seating(rider_dark)
crew_dark_badass_1 = Seating(rider_dark_badass)
crew_dark_2 = Seating(rider_dark, rider_dark)
crew_dark_badass_2 = Seating(rider_dark, rider_dark_badass)
crew_dark_4 = Seating(rider_dark, rider_dark, rider_dark, rider_dark)
crew_dark_badass_4 = Seating(rider_dark, rider_dark_badass, rider_dark, rider_dark_heavy)
crew_dlc2_1 = Seating(rider_dlc2)
crew_dlc2_2 = Seating(rider_dlc2, rider_dlc2)
crew_dlc2_4 = Seating(rider_dlc2, rider_dlc2, rider_dlc2, rider_dlc2)
crew_dr_1 = Seating(rider_dr)
crew_dr_2 = Seating(rider_dr, rider_dr)
crew_dr_4 = Seating(rider_dr, rider_dr, rider_dr, rider_dr)

# "Joke" crews
crew_jabber_1 = Seating(rider_jabber)
crew_jabber_2 = Seating(rider_jabber, rider_jabber)
crew_jabber_4 = Seating(rider_jabber, rider_jabber, rider_jabber, rider_jabber_badass)
crew_nog_1 = Seating(rider_nog)
crew_nog_2 = Seating(rider_nog, rider_nog)
crew_nog_4 = Seating(rider_nog, rider_nog, rider_nog, rider_nog_badass)
crew_tink_1 = Seating(rider_tink)
crew_tink_2 = Seating(rider_tink, rider_tink)
crew_tink_4 = Seating(rider_tink, rider_tink, rider_tink_badass, rider_skag)
crew_skrit_1 = Seating(rider_skrit)
crew_skrit_2 = Seating(rider_skrit, rider_skrit)
crew_skrit_4 = Seating(rider_skrit, rider_skrit, rider_skrit_badass, rider_wolven)
crew_rustler_1 = Seating(rider_rustler)
crew_rustler_2 = Seating(rider_rustler, rider_rustler)
crew_rustler_4 = Seating(rider_rustler, rider_rustler, rider_rustler_badass, rider_bellik)

# Seat distributions -- how likely it is to have that number of riders
seatweights_1 = SeatWeights(1)
seatweights_2_70 = SeatWeights(0.3, 0.7)
seatweights_2_76 = SeatWeights(0.3, 1.0)
seatweights_2_80 = SeatWeights(0.25, 1.0)
seatweights_2_100 = SeatWeights(0, 0.7)
seatweights_4_rising = SeatWeights(0.2, 1.0, 0.8, 1.0)
seatweights_4_even = SeatWeights(0.0, 0.001, 0.1, 0.1)
seatweights_4_high = SeatWeights(0, 0, 1.0, 3.0)

# Seatweight collections, one per chassis -- this way, different chassis
# configs can have different probabilities for how many riders there are.
outrunner_seatweights_less_on_fancy = [seatweights_2_100, seatweights_2_70, seatweights_2_70, seatweights_2_70]
outrunner_seatweights_less_on_fancy_76 = [seatweights_2_100, seatweights_2_76, seatweights_2_76, seatweights_2_76]
outrunner_seatweights_80pct_2 = [seatweights_2_80, seatweights_2_80, seatweights_2_80, seatweights_2_80]
outrunner_seatweights_always_2 = [seatweights_2_100, seatweights_2_100, seatweights_2_100, seatweights_2_100]
technical_seatweights_rising = [seatweights_4_even, seatweights_4_rising, seatweights_4_rising, seatweights_4_rising]
technical_seatweights_even = [seatweights_4_even, seatweights_4_even, seatweights_4_even, seatweights_4_even]
technical_seatweights_high = [seatweights_4_high, seatweights_4_high, seatweights_4_high, seatweights_4_high]
cyclone_seatweights = [seatweights_1, seatweights_1, seatweights_1, seatweights_1]
jetbeast_seatweights = [seatweights_1, seatweights_1, seatweights_1]

# Some common Configurations we're going to use
#
# "Badass" SpawnOptions have historically just meant Heavy armor, and those
# vehicles got their own name.  Since we're just randomizing all that anyway,
# the "badass/heavy" distinction doesn't really exist anymore.  (We could
# certainly figure out a way to break those out to continue having heavy-armor
# vehicles named differently, but we've already got too much naming going on.)
# In lieu of having a meaningful vehicle-level distinction between regular and
# "badass" spawns, we're going to instead make sure that some badasses spawn as
# riders in there.

# Outrunners
conf_outrunner_cov = Configuration(vehicle=outrunner,
        crew=crew_cov_2,
        seatweights=outrunner_seatweights_less_on_fancy,
        uinames=uiname_list_outrunner_cov, 
        team=team_cov,
        )
conf_outrunner_cov_badass = Configuration(vehicle=outrunner,
        crew=crew_cov_badass_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=uiname_list_outrunner_cov, 
        team=team_cov,
        )
conf_outrunner_mal = Configuration(vehicle=outrunner,
        crew=crew_mal_2,
        seatweights=outrunner_seatweights_less_on_fancy_76,
        uinames=uiname_list_outrunner_mal, 
        team=team_mal,
        )
conf_outrunner_mal_badass = Configuration(vehicle=outrunner,
        crew=crew_mal_badass_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=uiname_list_outrunner_mal, 
        team=team_mal,
        )
conf_outrunner_dark = Configuration(vehicle=outrunner,
        crew=crew_dark_2,
        seatweights=outrunner_seatweights_80pct_2,
        uinames=uiname_list_outrunner_dark, 
        team=team_mal,
        )
conf_outrunner_dark_badass = Configuration(vehicle=outrunner,
        crew=crew_dark_badass_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=uiname_list_outrunner_dark, 
        team=team_mal,
        )
conf_outrunner_dlc2 = Configuration(vehicle=outrunner,
        crew=crew_dlc2_2,
        seatweights=outrunner_seatweights_less_on_fancy,
        uinames=uiname_list_outrunner_dlc2, 
        team=team_dlc2,
        )
conf_outrunner_dr = Configuration(vehicle=outrunner,
        crew=crew_dr_2,
        seatweights=outrunner_seatweights_less_on_fancy,
        uinames=uiname_list_outrunner_dr, 
        team=team_cov,
        )
conf_outrunner_jabber = Configuration(vehicle=outrunner,
        crew=crew_jabber_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=[uiname_outrunner_stolen]*4, 
        team=team_jabber,
        )
conf_outrunner_nog = Configuration(vehicle=outrunner,
        crew=crew_nog_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=[uiname_outrunner_stolen]*4, 
        team=team_mal,
        )
conf_outrunner_tink = Configuration(vehicle=outrunner,
        crew=crew_tink_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=[uiname_outrunner_stolen]*4, 
        team=team_cov,
        )
conf_outrunner_skrit = Configuration(vehicle=outrunner,
        crew=crew_skrit_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=[uiname_outrunner_stolen]*4, 
        team=team_cult,
        )
conf_outrunner_rustler = Configuration(vehicle=outrunner,
        crew=crew_rustler_2,
        seatweights=outrunner_seatweights_always_2,
        uinames=[uiname_outrunner_stolen]*4, 
        team=team_cov,
        )

# Technicals
conf_technical_cov = Configuration(vehicle=technical,
        crew=crew_cov_4,
        seatweights=technical_seatweights_even,
        uinames=uiname_list_technical_cov, 
        team=team_cov,
        )
conf_technical_cov_badass = Configuration(vehicle=technical,
        crew=crew_cov_badass_4,
        seatweights=technical_seatweights_rising,
        uinames=uiname_list_technical_cov, 
        team=team_cov,
        )
conf_technical_mal = Configuration(vehicle=technical,
        crew=crew_mal_4,
        seatweights=technical_seatweights_rising,
        uinames=uiname_list_technical_mal, 
        team=team_mal,
        )
conf_technical_mal_badass = Configuration(vehicle=technical,
        crew=crew_mal_badass_4,
        seatweights=technical_seatweights_high,
        uinames=uiname_list_technical_mal, 
        team=team_mal,
        )
conf_technical_dark = Configuration(vehicle=technical,
        crew=crew_dark_4,
        seatweights=technical_seatweights_rising,
        uinames=uiname_list_technical_dark, 
        team=team_mal,
        )
conf_technical_dark_badass = Configuration(vehicle=technical,
        crew=crew_dark_badass_4,
        seatweights=technical_seatweights_high,
        uinames=uiname_list_technical_dark, 
        team=team_mal,
        )
conf_technical_ep05 = Configuration(vehicle=technical_hover,
        crew=crew_ep05,
        seatweights=[seatweights_4_high],
        uinames=[uiname_technical_hover_cov],
        team=team_cov,
        )
conf_technical_dlc2 = Configuration(vehicle=technical,
        crew=crew_dlc2_4,
        seatweights=technical_seatweights_even,
        uinames=uiname_list_technical_dlc2, 
        team=team_dlc2,
        )
conf_technical_dr = Configuration(vehicle=technical,
        crew=crew_dr_4,
        seatweights=technical_seatweights_even,
        uinames=uiname_list_technical_dr, 
        team=team_cov,
        )
conf_technical_jabber = Configuration(vehicle=technical_flatbed,
        crew=crew_jabber_4,
        seatweights=technical_seatweights_high,
        uinames=[uiname_technical_stolen]*4, 
        team=team_jabber,
        )
conf_technical_nog = Configuration(vehicle=technical_flatbed,
        crew=crew_nog_4,
        seatweights=technical_seatweights_high,
        uinames=[uiname_technical_stolen]*4, 
        team=team_mal,
        )
conf_technical_tink = Configuration(vehicle=technical_flatbed,
        crew=crew_tink_4,
        seatweights=technical_seatweights_high,
        uinames=[uiname_technical_stolen]*4, 
        team=team_cov,
        )
conf_technical_skrit = Configuration(vehicle=technical_flatbed,
        crew=crew_skrit_4,
        seatweights=technical_seatweights_high,
        uinames=[uiname_technical_stolen]*4, 
        team=team_cult,
        )
conf_technical_rustler = Configuration(vehicle=technical_flatbed,
        crew=crew_rustler_4,
        seatweights=technical_seatweights_high,
        uinames=[uiname_technical_stolen]*4, 
        team=team_cov,
        )

# Cyclones
conf_cyclone_cov = Configuration(vehicle=cyclone,
        crew=crew_cov_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_cov, 
        team=team_cov,
        )
conf_cyclone_cov_badass = Configuration(vehicle=cyclone,
        crew=crew_cov_badass_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_cov, 
        team=team_cov,
        )
conf_cyclone_mal = Configuration(vehicle=cyclone,
        crew=crew_mal_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_mal, 
        team=team_mal,
        )
conf_cyclone_mal_badass = Configuration(vehicle=cyclone,
        crew=crew_mal_badass_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_mal, 
        team=team_mal,
        )
conf_cyclone_dark = Configuration(vehicle=cyclone,
        crew=crew_dark_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_dark, 
        team=team_mal,
        )
conf_cyclone_dark_badass = Configuration(vehicle=cyclone,
        crew=crew_dark_badass_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_dark, 
        team=team_mal,
        )
conf_cyclone_dlc2 = Configuration(vehicle=cyclone,
        crew=crew_dlc2_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_dlc2, 
        team=team_dlc2,
        )
conf_cyclone_dr = Configuration(vehicle=cyclone,
        crew=crew_dr_1,
        seatweights=cyclone_seatweights,
        uinames=uiname_list_cyclone_dr, 
        team=team_cov,
        )
conf_cyclone_jabber = Configuration(vehicle=cyclone,
        crew=crew_jabber_1,
        seatweights=cyclone_seatweights,
        uinames=[uiname_cyclone_stolen]*4, 
        team=team_jabber,
        )
conf_cyclone_nog = Configuration(vehicle=cyclone,
        crew=crew_nog_1,
        seatweights=cyclone_seatweights,
        uinames=[uiname_cyclone_stolen]*4, 
        team=team_mal,
        )
conf_cyclone_tink = Configuration(vehicle=cyclone,
        crew=crew_tink_1,
        seatweights=cyclone_seatweights,
        uinames=[uiname_cyclone_stolen]*4, 
        team=team_cov,
        )
conf_cyclone_skrit = Configuration(vehicle=cyclone,
        crew=crew_skrit_1,
        seatweights=cyclone_seatweights,
        uinames=[uiname_cyclone_stolen]*4, 
        team=team_cult,
        )
conf_cyclone_rustler = Configuration(vehicle=cyclone,
        crew=crew_rustler_1,
        seatweights=cyclone_seatweights,
        uinames=[uiname_cyclone_stolen]*4, 
        team=team_cov,
        )

# Jetbeasts
conf_jetbeast_cov = Configuration(vehicle=jetbeast,
        crew=crew_cov_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_cov, 
        team=team_cov,
        )
conf_jetbeast_cov_badass = Configuration(vehicle=jetbeast,
        crew=crew_cov_badass_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_cov, 
        team=team_cov,
        )
conf_jetbeast_mal = Configuration(vehicle=jetbeast,
        crew=crew_mal_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_mal, 
        team=team_mal,
        )
conf_jetbeast_mal_badass = Configuration(vehicle=jetbeast,
        crew=crew_mal_badass_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_mal, 
        team=team_mal,
        )
conf_jetbeast_dark = Configuration(vehicle=jetbeast,
        crew=crew_dark_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_dark, 
        team=team_mal,
        )
conf_jetbeast_dark_badass = Configuration(vehicle=jetbeast,
        crew=crew_dark_badass_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_dark, 
        team=team_mal,
        )
conf_jetbeast_dlc2 = Configuration(vehicle=jetbeast,
        crew=crew_dlc2_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_dlc2, 
        team=team_dlc2,
        )
conf_jetbeast_dr = Configuration(vehicle=jetbeast,
        crew=crew_dr_1,
        seatweights=jetbeast_seatweights,
        uinames=uiname_list_jetbeast_dr, 
        team=team_cov,
        )
conf_jetbeast_jabber = Configuration(vehicle=jetbeast,
        crew=crew_jabber_1,
        seatweights=jetbeast_seatweights,
        uinames=[uiname_jetbeast_stolen]*3,
        team=team_jabber,
        )
conf_jetbeast_nog = Configuration(vehicle=jetbeast,
        crew=crew_nog_1,
        seatweights=jetbeast_seatweights,
        uinames=[uiname_jetbeast_stolen]*3,
        team=team_mal,
        )
conf_jetbeast_tink = Configuration(vehicle=jetbeast,
        crew=crew_tink_1,
        seatweights=jetbeast_seatweights,
        uinames=[uiname_jetbeast_stolen]*3,
        team=team_cov,
        )
conf_jetbeast_skrit = Configuration(vehicle=jetbeast,
        crew=crew_skrit_1,
        seatweights=jetbeast_seatweights,
        uinames=[uiname_jetbeast_stolen]*3,
        team=team_cult,
        )
conf_jetbeast_rustler = Configuration(vehicle=jetbeast,
        crew=crew_rustler_1,
        seatweights=jetbeast_seatweights,
        uinames=[uiname_jetbeast_stolen]*3,
        team=team_cov,
        )

# And some common configuration profiles (did not use a separate class for this,
# since all we really want is a configuration and its weight

original_bias_weight = 2

p_outrunner_cov = [(conf_outrunner_cov, 1)]
p_technical_cov = [(conf_technical_cov, 1)]
p_cyclone_cov = [(conf_cyclone_cov, 1)]
p_jetbeast_cov = [(conf_jetbeast_cov, 1)]
p_cov_all = p_outrunner_cov + p_technical_cov + p_cyclone_cov + p_jetbeast_cov
# Actually not really using the base *_all vars anywhere; instead I've moved
# to having the original vehicle types be weighted a bit higher, so we need
# separate profiles for each of those cases.  This is where having all this
# stuff wrapped up with various Enums would be especially nice; could just
# do this automatically in a loop.
p_cov_all_outrunner = [
        (conf_outrunner_cov, original_bias_weight),
        (conf_technical_cov, 1),
        (conf_cyclone_cov, 1),
        (conf_jetbeast_cov, 1),
        ]
p_cov_all_technical = [
        (conf_outrunner_cov, 1),
        (conf_technical_cov, original_bias_weight),
        (conf_cyclone_cov, 1),
        (conf_jetbeast_cov, 1),
        ]
p_cov_all_cyclone = [
        (conf_outrunner_cov, 1),
        (conf_technical_cov, 1),
        (conf_cyclone_cov, original_bias_weight),
        (conf_jetbeast_cov, 1),
        ]

p_outrunner_cov_badass = [(conf_outrunner_cov_badass, 1)]
p_technical_cov_badass = [(conf_technical_cov_badass, 1)]
p_cyclone_cov_badass = [(conf_cyclone_cov_badass, 1)]
p_jetbeast_cov_badass = [(conf_jetbeast_cov_badass, 1)]
p_cov_all_badass = p_outrunner_cov_badass + p_technical_cov_badass + p_cyclone_cov_badass + p_jetbeast_cov_badass
p_cov_all_badass_outrunner = [
        (conf_outrunner_cov_badass, original_bias_weight),
        (conf_technical_cov_badass, 1),
        (conf_cyclone_cov_badass, 1),
        (conf_jetbeast_cov_badass, 1),
        ]
p_cov_all_badass_technical = [
        (conf_outrunner_cov_badass, 1),
        (conf_technical_cov_badass, original_bias_weight),
        (conf_cyclone_cov_badass, 1),
        (conf_jetbeast_cov_badass, 1),
        ]
p_cov_all_badass_cyclone = [
        (conf_outrunner_cov_badass, 1),
        (conf_technical_cov_badass, 1),
        (conf_cyclone_cov_badass, original_bias_weight),
        (conf_jetbeast_cov_badass, 1),
        ]

p_outrunner_mal = [(conf_outrunner_mal, 1)]
p_technical_mal = [(conf_technical_mal, 1)]
p_cyclone_mal = [(conf_cyclone_mal, 1)]
p_jetbeast_mal = [(conf_jetbeast_mal, 1)]
p_mal_all = p_outrunner_mal + p_technical_mal + p_cyclone_mal + p_jetbeast_mal
p_mal_all_outrunner = [
        (conf_outrunner_mal, original_bias_weight),
        (conf_technical_mal, 1),
        (conf_cyclone_mal, 1),
        (conf_jetbeast_mal, 1),
        ]
p_mal_all_cyclone = [
        (conf_outrunner_mal, 1),
        (conf_technical_mal, 1),
        (conf_cyclone_mal, original_bias_weight),
        (conf_jetbeast_mal, 1),
        ]

p_outrunner_mal_badass = [(conf_outrunner_mal_badass, 1)]
p_technical_mal_badass = [(conf_technical_mal_badass, 1)]
p_cyclone_mal_badass = [(conf_cyclone_mal_badass, 1)]
p_jetbeast_mal_badass = [(conf_jetbeast_mal_badass, 1)]
p_mal_all_badass = p_outrunner_mal_badass + p_technical_mal_badass + p_cyclone_mal_badass + p_jetbeast_mal_badass
p_mal_all_badass_outrunner = [
        (conf_outrunner_mal_badass, original_bias_weight),
        (conf_technical_mal_badass, 1),
        (conf_cyclone_mal_badass, 1),
        (conf_jetbeast_mal_badass, 1),
        ]
p_mal_all_badass_cyclone = [
        (conf_outrunner_mal_badass, 1),
        (conf_technical_mal_badass, 1),
        (conf_cyclone_mal_badass, original_bias_weight),
        (conf_jetbeast_mal_badass, 1),
        ]

p_outrunner_dark = [(conf_outrunner_dark, 1)]
p_technical_dark = [(conf_technical_dark, 1)]
p_cyclone_dark = [(conf_cyclone_dark, 1)]
p_jetbeast_dark = [(conf_jetbeast_dark, 1)]
p_dark_all = p_outrunner_dark + p_technical_dark + p_cyclone_dark + p_jetbeast_dark
p_dark_all_outrunner = [
        (conf_outrunner_dark, original_bias_weight),
        (conf_technical_dark, 1),
        (conf_cyclone_dark, 1),
        (conf_jetbeast_dark, 1),
        ]
p_dark_all_cyclone = [
        (conf_outrunner_dark, 1),
        (conf_technical_dark, 1),
        (conf_cyclone_dark, original_bias_weight),
        (conf_jetbeast_dark, 1),
        ]

p_outrunner_dark_badass = [(conf_outrunner_dark_badass, 1)]
p_technical_dark_badass = [(conf_technical_dark_badass, 1)]
p_cyclone_dark_badass = [(conf_cyclone_dark_badass, 1)]
p_jetbeast_dark_badass = [(conf_jetbeast_dark_badass, 1)]
p_dark_all_badass = p_outrunner_dark_badass + p_technical_dark_badass + p_cyclone_dark_badass + p_jetbeast_dark_badass
p_dark_all_badass_outrunner = [
        (conf_outrunner_dark_badass, original_bias_weight),
        (conf_technical_dark_badass, 1),
        (conf_cyclone_dark_badass, 1),
        (conf_jetbeast_dark_badass, 1),
        ]
p_dark_all_badass_cyclone = [
        (conf_outrunner_dark_badass, 1),
        (conf_technical_dark_badass, 1),
        (conf_cyclone_dark_badass, original_bias_weight),
        (conf_jetbeast_dark_badass, 1),
        ]

p_outrunner_dlc2 = [(conf_outrunner_dlc2, 1)]
p_technical_dlc2 = [(conf_technical_dlc2, 1)]
p_cyclone_dlc2 = [(conf_cyclone_dlc2, 1)]
p_jetbeast_dlc2 = [(conf_jetbeast_dlc2, 1)]
p_dlc2_all = p_outrunner_dlc2 + p_technical_dlc2 + p_cyclone_dlc2 + p_jetbeast_dlc2
p_dlc2_all_technical = [
        (conf_outrunner_dlc2, 1),
        (conf_technical_dlc2, original_bias_weight),
        (conf_cyclone_dlc2, 1),
        (conf_jetbeast_dlc2, 1),
        ]

p_outrunner_dr = [(conf_outrunner_dr, 1)]
p_technical_dr = [(conf_technical_dr, 1)]
p_cyclone_dr = [(conf_cyclone_dr, 1)]
p_jetbeast_dr = [(conf_jetbeast_dr, 1)]
p_dr_all = p_outrunner_dr + p_technical_dr + p_cyclone_dr + p_jetbeast_dr
p_dr_all_jetbeast = [
        (conf_outrunner_dr, 1),
        (conf_technical_dr, 1),
        (conf_cyclone_dr, 1),
        (conf_jetbeast_dr, original_bias_weight),
        ]

# Joke profiles

joke_scaling = 0.1
#joke_scaling = 1000

p_outrunner_nog = [(conf_outrunner_nog, joke_scaling)]
p_outrunner_nog_all = [
        (conf_outrunner_nog, joke_scaling*original_bias_weight),
        (conf_technical_nog, joke_scaling),
        (conf_cyclone_nog, joke_scaling),
        (conf_jetbeast_nog, joke_scaling),
        ]
p_cyclone_nog = [(conf_cyclone_nog, joke_scaling)]
p_cyclone_nog_all = [
        (conf_outrunner_nog, joke_scaling),
        (conf_technical_nog, joke_scaling),
        (conf_cyclone_nog, joke_scaling*original_bias_weight),
        (conf_jetbeast_nog, joke_scaling),
        ]
p_technical_jabber = [(conf_technical_jabber, joke_scaling)]
p_technical_jabber_all = [
        (conf_outrunner_jabber, joke_scaling),
        (conf_technical_jabber, joke_scaling*original_bias_weight),
        (conf_cyclone_jabber, joke_scaling),
        (conf_jetbeast_jabber, joke_scaling),
        ]
p_cyclone_jabber = [(conf_cyclone_jabber, joke_scaling)]
p_cyclone_jabber_all = [
        (conf_outrunner_jabber, joke_scaling),
        (conf_technical_jabber, joke_scaling),
        (conf_cyclone_jabber, joke_scaling*original_bias_weight),
        (conf_jetbeast_jabber, joke_scaling),
        ]
p_outrunner_tink = [(conf_outrunner_tink, joke_scaling)]
p_outrunner_tink_all = [
        (conf_outrunner_tink, joke_scaling*original_bias_weight),
        (conf_technical_tink, joke_scaling),
        (conf_cyclone_tink, joke_scaling),
        (conf_jetbeast_tink, joke_scaling),
        ]
p_cyclone_tink = [(conf_cyclone_tink, joke_scaling)]
p_cyclone_tink_all = [
        (conf_outrunner_tink, joke_scaling),
        (conf_technical_tink, joke_scaling),
        (conf_cyclone_tink, joke_scaling*original_bias_weight),
        (conf_jetbeast_tink, joke_scaling),
        ]
p_technical_tink = [(conf_technical_tink, joke_scaling)]
p_technical_tink_all = [
        (conf_outrunner_tink, joke_scaling),
        (conf_technical_tink, joke_scaling*original_bias_weight),
        (conf_cyclone_tink, joke_scaling),
        (conf_jetbeast_tink, joke_scaling),
        ]
p_technical_skrit = [(conf_technical_skrit, joke_scaling)]
p_technical_skrit_all = [
        (conf_outrunner_skrit, joke_scaling),
        (conf_technical_skrit, joke_scaling*original_bias_weight),
        (conf_cyclone_skrit, joke_scaling),
        (conf_jetbeast_skrit, joke_scaling),
        ]
p_jetbeast_rustler = [(conf_jetbeast_rustler, joke_scaling)]
p_jetbeast_rustler_all = [
        (conf_outrunner_rustler, joke_scaling),
        (conf_technical_rustler, joke_scaling),
        (conf_cyclone_rustler, joke_scaling),
        (conf_jetbeast_rustler, joke_scaling*original_bias_weight),
        ]

###
### Start the mod(s)!
###

for filename, mod_title, profile_idx, extra_description in [
        ('', 'Vehicle Unlocks', 0, [
            "This variant maintains the types of vehicles which spawn in any given",
            "level.  For instance, a map which ordinarily only spawns Outrunners",
            "will still only spawn Outrunners.",
            ]),
        ('_plus', 'Vehicle Unlocks+', 1, [
            "This variant completely unlocks vehicle types, too, so every level which",
            "has enemy vehicle spawns will be able to spawn Outrunners, Cyclones,",
            "Technicals, and Jetbeasts.  The spawning will retain a slight bias",
            "towards the original vehicle type(s), though.",
            ]),
        ]:

    # Build up our description
    desc = [
            "Sets enemy vehicle spawns to use all vehicle parts/skins/chassis from",
            "the beginning of the game, both to make part collection easier, and to",
            "provide a more interesting set of vehicles to fight against throughout",
            "the game.",
            ]
    if extra_description:
        desc.append('')
        desc.extend(extra_description)
    desc.extend([
        "",
        "Enemy vehicle names have been standardized across the board to only",
        "report on the chassis/wheel type (and vehicle type, of course), rather",
        "than also including the faction/team.  So instead of 'COV Twitch",
        "Runner', you'll now see 'Twitch Runner'.  This change has been applied",
        "to Jetbeasts as well.",
        "",
        "This mod also converts Clever Girl, Festive Flesh-Eater, and Skagzilla",
        "to use Monster Wheels.  It also adds in some rare 'Stolen' variants in",
        "some maps, which have driver/rider types not ordinarily encountered in",
        "the base game."
        ])

    # Start the mod object
    mod = Mod('vehicle_unlocks{}.bl3hotfix'.format(filename),
            mod_title,
            'Apocalyptech',
            desc,
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='2.0.0',
            cats='gameplay, vehicle',
            )

    mod.header('Remove level restrictions for parts')

    for (label, table, col_name, rows) in [
            ('Vehicle Parts (table 1)',
                '/Game/Vehicles/_Shared/Design/Balance/Data/DataTable_VehiclePartsData',
                'MinGameStage_15_D986BDE142AA94D9995403BC41D5DA70',
                [
                    'Technical_StickyBombs',
                    'Technical_FlakCannon',
                    'Technical_ToxicBooster',
                    'Technical_FuelBarrels',
                    'Outrunner_TwitchyWheels',
                    'Outrunner_HoverWheels',
                    'Outrunner_TeslaCoil',
                    'Outrunner_FlameThrower',
                    'Outrunner_ShotgunMissile',
                    'Outrunner_SwarmerMissile',
                    'Outrunner_BlazeBooster',
                    'Revolver_DualWheel',
                    'Revolver_HoverWheels',
                    'Revolver_HeavyArmor',
                    'Revolver_FireStarter',
                    'Revolver_SpikeLauncher',
                    'Revolver_SawBladeLauncher',
                    ]),
            ('Vehicle Parts (table 2)',
                '/Game/Vehicles/_Shared/Design/Balance/Data/DataTable_VehiclePartsSchedule',
                'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
                [
                    'Technical_Mod_ToxicBoost',
                    'Technical_Mod_FuelBarrels',
                    'Technical_Armor_Heavy',
                    'Technical_Wep_FlakCannon',
                    'Outrunner_Wheels_Twitchy',
                    'Outrunner_Wheels_Hover',
                    'Outrunner_Mod_BlazeBoost',
                    'Outrunner_Wep_Flamethrower',
                    'Outrunner_Wep_TeslaCoil',
                    'Outrunner_Wep_SwarmerMissile',
                    'Outrunner_Wep_ShotgunMissile',
                    'Revolver_Wheel_Dual',
                    'Revolver_Wheel_Hover',
                    'Revolver_Mod_FireStarter',
                    'Revolver_Armor_Heavy',
                    'Revolver_Wep_SpikeLauncher',
                    'Revolver_Wep_Sawblades',
                    ]),
            ('Vehicle Skins',
                '/Game/Vehicles/_Shared/Design/Balance/Data/DataTable_VehicleSkinSchedule',
                'MinGameStage_17_2500317646FAD2F4916D158835B29E83',
                [
                    'Outrunner_PsychoMobile',
                    'Outrunner_Houndstooth',
                    'Outrunner_Forest',
                    'Outrunner_GoldenHog',
                    'Outrunner_Borderlandstton',
                    'Outrunner_HistoricRacing',
                    'Outrunner_Bubblegum',
                    'Outrunner_RageCage',
                    'Outrunner_Pirate',
                    'Outrunner_RedMachine',
                    'Technical_Bubblegum',
                    'Technical_Desert',
                    'Technical_Blueangels',
                    'Technical_Halftone',
                    'Technical_Forest',
                    'Technical_Leather',
                    'Technical_Stealth',
                    'Technical_Thunderbird',
                    'Revolver_Chopper',
                    'Revolver_Lollipop',
                    'Revolver_Dark',
                    'Revolver_Forest',
                    'Revolver_Bubblegum',
                    'Revolver_Golden',
                    'Revolver_Lifeline',
                    'Revolver_Maliwan',
                    'Revolver_Stealth',
                    ]),
            ]:
        mod.comment(label)
        for row in rows:
            mod.table_hotfix(Mod.LEVEL, 'MatchAll',
                    table,
                    row,
                    col_name,
                    0)
        mod.newline()

    # Fix any skin errors
    mod.header('Fixes/Tweaks')

    mod.comment('Fix Outrunner Red Machine Skin MaxGameStage')
    mod.reg_hotfix(Mod.LEVEL, 'MatchAll',
            '/Game/Vehicles/Outrunner/Design/Parts/Materials/VehiclePart_Mat_VehiclePart_Outrunner_RedMachine',
            'MaxGameStage.DataTableValue.ValueName',
            'MaxGameStage_18_5DDD0AF343807440C74B37A083027F1C')
    mod.newline()

    for (label, levels, spawn_obj) in [
            ('Clever Girl (in Floodmoor Basin)',
                ['Wetlands_P'],
                '/Game/Enemies/_Spawning/Vehicles/RareSpawns/SpawnOptions_RareVehicle_Technical_CleverGirl'),
            ('Festive Flesh-Eater (in Splinterlands and Carnivora)',
                ['Motorcade_P', 'MotorcadeFestival_P'],
                '/Game/Enemies/_Spawning/Vehicles/RareSpawns/SpawnOptions_RareVehicle_Technical_Princess'),
            ('Skagzilla (in The Droughts)',
                ['Prologue_P'],
                '/Game/Enemies/_Spawning/Vehicles/RareSpawns/SpawnOptions_RareVehicle_Technical_Skagzilla'),
            ]:
        mod.comment('Make {} use Monster Wheels'.format(label))
        for level in levels:
            mod.reg_hotfix(Mod.LEVEL, level,
                    spawn_obj,
                    'Options[0].Factory.Object..VehicleClass',
                    mod.get_full_cond('/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BigWheels', 'Vehicle_Technical_BigWheels_C'))
            mod.reg_hotfix(Mod.LEVEL, level,
                    spawn_obj,
                    'Options[0].Factory.Object..CustomInventoryData.Object..InventoryActorClass',
                    mod.get_full_cond('/Game/Vehicles/Technical/Vehicle/Vehicle_Technical_BigWheels', 'Vehicle_Technical_BigWheels_C'))
        mod.newline()

    # Now the real "meat" of the mod
    used_uinames = set()
    for label, obj_name, levels, profiles in [
            ('COV Outrunner',
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner', [
                    'Prologue_P',
                    ],
                (p_outrunner_cov + p_outrunner_tink, p_cov_all_outrunner + p_outrunner_tink_all),
                ),
            ('COV Outrunner',
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner', [
                    'Outskirts_P',
                    ],
                (p_outrunner_cov, p_cov_all_outrunner),
                ),
            ("COV Badass Outrunner",
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Outrunner_Badass', [
                    'Desert_P',
                    'MotorcadeFestival_P',
                    'Convoy_P',
                    ],
                (p_outrunner_cov_badass, p_cov_all_badass_outrunner),
                ),
            ('COV Outrunner',
                '/Game/Missions/Plot/Ep02_Sacrifice/SpawnOptions_CotV_Outrunner_Basic', [
                    'Sacrifice_P',
                    ],
                (p_outrunner_cov, p_cov_all_outrunner),
                ),
            ('COV Outrunner',
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Outrunner_CotV_Convoy', [
                    'Convoy_P',
                    ],
                (p_outrunner_cov, p_cov_all_outrunner),
                ),
            ('COV Outrunner',
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Carnivora/SpawnOptions_Outrunner_CotV_Carnivora', [
                    'MotorcadeFestival_P',
                    ],
                (p_outrunner_cov, p_cov_all_outrunner),
                ),
            ("COV Outrunner",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Desert/SpawnOptions_Outrunner_CotV_Desert', [
                    'Desert_P',
                    ],
                (p_outrunner_cov + p_outrunner_tink, p_cov_all_outrunner + p_outrunner_tink_all),
                ),
            ("Maliwan Outrunner",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Outrunner', [
                    'City_P',
                    ],
                (p_outrunner_mal + p_outrunner_nog, p_mal_all_outrunner + p_outrunner_nog_all),
                ),
            ("Maliwan Badass Outrunner",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Outrunner_Badass', [
                    'City_P',
                    ],
                (p_outrunner_mal_badass, p_mal_all_badass_outrunner),
                ),
            ("Dark Maliwan Outrunner",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Outrunner', [
                    'Desolate_P',
                    ],
                (p_outrunner_dark, p_dark_all_outrunner),
                ),
            ("Dark Maliwan Badass Outrunner",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Outrunner_Badass', [
                    'Desolate_P',
                    ],
                (p_outrunner_dark_badass, p_dark_all_badass_outrunner),
                ),
            ("COV Technical",
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Technical', [
                    'Outskirts_P',
                    'CityVault_P',
                    ],
                (p_technical_cov, p_cov_all_technical),
                ),
            ("COV Badass Technical",
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Technical_Badass', [
                    'Outskirts_P',
                    'Wetlands_P',
                    'Convoy_P',
                    'Motorcade_P',
                    'MotorcadeFestival_P',
                    ],
                (p_technical_cov_badass, p_cov_all_badass_technical),
                ),
            ("COV Technical",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Technical_CotV_Convoy', [
                    'Convoy_P',
                    ],
                (p_technical_cov, p_cov_all_technical),
                ),
            ("COV Technical",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Motorcade/SpawnOptions_Technical_CotV_Motorcade', [
                    'Motorcade_P',
                    # Looks like this can get called from Carnivora, too
                    'MotorcadeFestival_P',
                    ],
                (p_technical_cov + p_technical_tink, p_cov_all_technical + p_technical_tink_all),
                ),
            ("COV Technical",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_1/CityVault/SpawnOptions_Technical_CotV_CityVault', [
                    'CityVault_P',
                    ],
                (p_technical_cov, p_cov_all_technical),
                ),
            ("COV Technical",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_2/Wetlands/SpawnOptions_Technical_CotV_Wetlands', [
                    'Wetlands_P',
                    ],
                (p_technical_cov + p_technical_jabber, p_cov_all_technical + p_technical_jabber_all),
                ),
            ("Special Hover Technical (mission-specific but continues to spawn)",
                '/Game/Enemies/_Spawning/Vehicles/Technical/SpawnOptions_Vehicle_EP05_HoverTechnical', [
                    'Outskirts_P',
                    ],
                ([(conf_technical_ep05, 1)], [(conf_technical_ep05, 1)]),
                ),
            ("Mumblers Technical",
                '/Hibiscus/Enemies/_Spawning/Vehicles/SpawnOptions_Vehicle_Frostbiter_Lake_FullMix', [
                    'Lake_P',
                    ],
                (p_technical_dlc2 + p_technical_skrit, p_dlc2_all_technical + p_technical_skrit_all),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Revolver', [
                    'Convoy_P',
                    ],
                (p_cyclone_cov, p_cov_all_cyclone),
                ),
            ("COV Badass Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/SpawnOptions_CotV_Revolver_Badass', [
                    'Wetlands_P',
                    'MotorcadeFestival_P',
                    'Convoy_P',
                    'Desert_P',
                    'Motorcade_P',
                    ],
                (p_cyclone_cov_badass, p_cov_all_badass_cyclone),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Convoy/SpawnOptions_Revolver_CotV_Convoy', [
                    'Convoy_P',
                    ],
                (p_cyclone_cov, p_cov_all_cyclone),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Carnivora/SpawnOptions_Revolver_CotV_Carnivora', [
                    'MotorcadeFestival_P',
                    ],
                (p_cyclone_cov, p_cov_all_cyclone),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Desert/SpawnOptions_Revolver_CotV_Desert', [
                    'Desert_P',
                    ],
                (p_cyclone_cov + p_cyclone_tink, p_cov_all_cyclone + p_cyclone_tink_all),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_3/Motorcade/SpawnOptions_Revolver_CotV_Motorcade', [
                    'Motorcade_P',
                    # Looks like this can probably get called from Canivora as well.
                    'MotorcadeFestival_P',
                    ],
                (p_cyclone_cov + p_cyclone_tink, p_cov_all_cyclone + p_cyclone_tink_all),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/_Mixes/Zone_2/Wetlands/SpawnOptions_Revolver_CotV_Wetlands', [
                    'Wetlands_P',
                    ],
                (p_cyclone_cov + p_cyclone_jabber, p_cov_all_cyclone + p_cyclone_jabber_all),
                ),
            ("COV Cyclone",
                '/Game/Enemies/_Spawning/CotV/Vehicles/Zone_1/CityVault/SpawnOptions_Revolver_CotV_CityVault', [
                    'CityVault_P',
                    ],
                (p_cyclone_cov, p_cov_all_cyclone),
                ),
            ("Maliwan Cyclone",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Revolver', [
                    'City_P',
                    ],
                (p_cyclone_mal + p_cyclone_nog, p_mal_all_cyclone + p_cyclone_nog_all),
                ),
            ("Maliwan Badass Cyclone",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_Maliwan_Revolver_Badass', [
                    'City_P',
                    ],
                (p_cyclone_mal_badass, p_mal_all_badass_cyclone),
                ),
            ("Dark Maliwan Cyclone",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Revolver', [
                    'Desolate_P',
                    ],
                (p_cyclone_dark, p_dark_all_cyclone),
                ),
            ("Dark Maliwan Badass Cyclone",
                '/Game/Enemies/_Spawning/Maliwan/Vehicles/SpawnOptions_DarkMaliwan_Revolver_Badass', [
                    'Desolate_P',
                    ],
                (p_cyclone_dark_badass, p_dark_all_badass_cyclone),
                ),
            ("Devil Rider Jetbeasts",
                '/Geranium/Enemies/_Spawning/Vehicles/Horse/SpawnOptions_Vehicle_Horse_ALL', [
                    'Frontier_P',
                    ],
                (p_jetbeast_dr + p_jetbeast_rustler, p_dr_all_jetbeast + p_jetbeast_rustler_all),
                ),
            ]:

        profile = profiles[profile_idx]

        # First up, so we're only doing it once: Loop through our whole
        # configuration/vehicle structure to figure out what our factory
        # object names will be, and what weights to report in the "Probability"
        # attr.  (That attr doesn't actually matter, but it's nice to have for
        # human readability purposes.)
        #
        # This whole section is quite inefficient; we're looping through the same
        # objects a number of times here.  Alas.

        obj_name_last = obj_name.rsplit('/', 1)[1]

        # Assign transient variables; object names and raw weights first
        num_factories = 0
        total_weight = 0
        for config, weight in profile:
            config.reset_transient()
            individual_weight = float(weight)/len(config.vehicle.chassis)
            total_weight += weight
            for idx in range(len(config.vehicle.chassis)):
                config.factory_names.append('{}.{}:Apoc_Factory_{}'.format(obj_name, obj_name_last, num_factories))
                config.factory_weights.append(individual_weight)
                num_factories += 1

        # Now that "Probability" attr info
        for config, _ in profile:
            for idx in range(len(config.vehicle.chassis)):
                config.factory_probabilities.append(config.factory_weights[idx]/total_weight*100)

        # Construct the main Factory-creation hotfix
        options_parts = []
        for config, _ in profile:
            options_parts.extend(config.get_options_hotfix_parts(mod))
        options_hotfix_value = '({})'.format(','.join(options_parts))

        for level in levels:

            mod.header('{} @ {} ({})'.format(label, LVL_TO_ENG_LOWER[level.lower()], level))

            # Set up the main Options list, which is what ends up creating all our new Factory
            # objects.  This statement itself doesn't really have to be EarlyLevel *itself*,
            # but for materials/skins to load in properly, the PartSet objects *do* have to
            # be EarlyLevel, and those won't exist until we do this.  So, EarlyLevel it is.
            mod.comment('Setting up all options for this spawn')
            mod.reg_hotfix(Mod.EARLYLEVEL, level,
                    obj_name,
                    'Options',
                    options_hotfix_value)
            mod.newline()

            # Now loop through and handle each Configuration
            cur_idx = 0
            for config, _ in profile:
                cur_idx = config.do_hotfixes(mod, level, cur_idx, used_uinames)

    # Set up any UINames which need fixing
    if used_uinames:
        mod.header('Processing UIName Changes')
        for uiname in sorted(used_uinames):
            uiname.do_hotfixes(mod)
        mod.newline()

    mod.close()
