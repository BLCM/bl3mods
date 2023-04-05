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
import argparse
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

# Args (just for --verbose)
parser = argparse.ArgumentParser(
        description="Creates the Atlas HQ Fast Travel mods",
        )

parser.add_argument('-v', '--verbose',
        action='store_true',
        help='Show verbose information as we read data',
        )

args = parser.parse_args()
verbose = args.verbose

# Define some classes...
class Location:
    """
    All the seemingly-relevant data about positioning, etc, for a fast travel
    station (basically, all the values we'll need to set when we move them around).
    """

    def __init__(self, sm_export_idx=-1, x=0, y=0, z=0, pitch=0, yaw=0, roll=0,
            aa_export_idx=-1, act_x=0, act_y=0, act_z=0, radius=1000, halfheight=300,
            res_export_idx=-1, activate_on_enter_area=True, res_x=0, res_y=0, res_z=0,
            ):

        self.sm_export_idx = sm_export_idx
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        self.aa_export_idx = aa_export_idx
        self.act_x = act_x
        self.act_y = act_y
        self.act_z = act_z
        self.radius = radius
        self.halfheight = halfheight
        self.res_export_idx = res_export_idx
        self.activate_on_enter_area = activate_on_enter_area
        self.res_x = res_x
        self.res_y = res_y
        self.res_z = res_z

        # Does this location have an Ubergraph reference which would need to be
        # updated, if a different machine was swapped in-place?  This is not
        # autodetected in any way -- it must be set manually.  This value, if set,
        # should be a tuple where the first element is the object name, and the
        # second element is the attribute name.
        self.ubergraph_ref = None

    @staticmethod
    def from_data(map_data, export):

        kwargs = {}

        # Get the skeletal mesh, and associated attrs
        skeletalmesh = map_data[export['SkeletalMesh']['export']-1]
        kwargs['sm_export_idx'] = skeletalmesh['_jwp_export_idx']
        kwargs['x'] = skeletalmesh['RelativeLocation']['x']
        kwargs['y'] = skeletalmesh['RelativeLocation']['y']
        kwargs['z'] = skeletalmesh['RelativeLocation']['z']
        if 'RelativeRotation' in skeletalmesh:
            kwargs['pitch'] = skeletalmesh['RelativeRotation']['pitch']
            kwargs['yaw'] = skeletalmesh['RelativeRotation']['yaw']
            kwargs['roll'] = skeletalmesh['RelativeRotation']['roll']

        # Get the ActivationArea, and associated attrs
        aa = map_data[export['ActivationArea']['export']-1]
        kwargs['aa_export_idx'] = aa['_jwp_export_idx']
        if 'RelativeLocation' in aa:
            kwargs['act_x'] = aa['RelativeLocation']['x']
            kwargs['act_y'] = aa['RelativeLocation']['y']
            kwargs['act_z'] = aa['RelativeLocation']['z']
        if 'DetectionRadius' in aa:
            kwargs['radius'] = aa['DetectionRadius']
        if 'DetectionHalfHeight' in aa:
            kwargs['halfheight'] = aa['DetectionHalfHeight']

        # resurrection component
        res = map_data[export['OakTravelStationResurrectComponent']['export']-1]
        kwargs['res_export_idx'] = res['_jwp_export_idx']
        if 'bActivateOnEnterArea' in res:
            kwargs['activate_on_enter_area'] = res['bActivateOnEnterArea']
        else:
            kwargs['activate_on_enter_area'] = True
        if 'RelativeLocation' in res:
            kwargs['res_x'] = res['RelativeLocation']['x']
            kwargs['res_y'] = res['RelativeLocation']['y']
            kwargs['res_z'] = res['RelativeLocation']['z']

        # Now make an object from all this.
        return Location(**kwargs)

    def report(self):

        print('  Position: {}, {}, {}'.format(
            self.x,
            self.y,
            self.z,
            ))
        print('  Rotation: {}, {}, {}'.format(
            self.pitch,
            self.yaw,
            self.roll,
            ))
        print('  Activation Location: {}, {}, {}'.format(
            self.act_x,
            self.act_y,
            self.act_z,
            ))
        print('  Activation Params: radius {}, halfheight {}'.format(
            self.radius,
            self.halfheight,
            ))
        if not self.activate_on_enter_area:
            print('  WARNING: bActivateOnEnterArea is set to False on the OakTravelStationResurrectComponent')
        print('  Resurrection Location: {}, {}, {}'.format(
            self.res_x,
            self.res_y,
            self.res_z,
            ))

class Station:

    def __init__(self, obj_name_last, map_name, map_obj_name, map_data, export):

        # Our passed-in info
        self.obj_name_last = obj_name_last
        self.map_name = map_name
        self.map_obj_name = map_obj_name
        self.map_data = map_data
        self.export = export
        self.export_idx = export['_jwp_export_idx']
        self.export_type = export['export_type']

        # Does this object have the *minimum* detection radius we're willing
        # to accept on reassignments?  (Basically just using this for the
        # fast travel, so it's always got a wide radius.)  This isn't autodetected
        # in any way -- it must be set manually.
        self.has_min_radius = False

        # Figure out our actual object name
        self.obj_name = '{}.{}:PersistentLevel.{}'.format(
                self.map_obj_name,
                self.map_obj_name.split('/')[-1],
                self.obj_name_last)

        # Grab our location information
        self.loc = Location.from_data(map_data, export)

    def report(self):
        print(self.obj_name)
        print('Main Export {}, SM Export {}, AA Export {}, RES Export {}'.format(
            self.export_idx,
            self.loc.sm_export_idx,
            self.loc.aa_export_idx,
            self.loc.res_export_idx,
            ))
        self.loc.report()

    def move_to(self, mod, loc):
        """
        Moves ourselves to the specified `loc`, to the given `mod` modfile.
        Bit of bleedthrough here; this should maybe be in Location, though
        we're doing a few checks against our own location data, so it's easier
        to leave it in here.
        """

        # TODO: So one problem with this mod is that when you fast-travel into the
        # map from outside, you end up getting dumped into the original Fast Travel
        # spot first.  You can then do an in-map fast travel over to the real
        # station, at least, which is pretty quick.  I'm honestly not sure if there's
        # anything we can do about that at the moment -- I assume that the player's
        # location must be set real early on in the level-loading process, before
        # hotfixes have been processed.  I did try converting all these to EARLYLEVEL
        # instead, but that didn't change anything.  So yeah, might be something
        # that requires a hypothetical SDK.  Still, better than nothing!

        # Sub-objects we'll be touching
        sm_obj_name = f'{self.obj_name}.SkeletalMesh'
        aa_obj_name = f'{self.obj_name}.ActivationArea'
        res_obj_name = f'{self.obj_name}.OakTravelStationResurrectComponent'

        # Location
        mod.reg_hotfix(Mod.LEVEL, self.map_name,
                sm_obj_name,
                'RelativeLocation',
                f'(x={loc.x},y={loc.y},z={loc.z})',
                notify=True,
                )

        # Rotation
        mod.reg_hotfix(Mod.LEVEL, self.map_name,
                sm_obj_name,
                'RelativeRotation',
                f'(pitch={loc.pitch},yaw={loc.yaw},roll={loc.roll})',
                notify=True,
                )

        # Activation Location
        mod.reg_hotfix(Mod.LEVEL, self.map_name,
                aa_obj_name,
                'RelativeLocation',
                f'(x={loc.act_x},y={loc.act_y},z={loc.act_z})',
                notify=True,
                )

        # Detection Radius
        if self.has_min_radius and loc.radius < self.loc.radius:
            radius = self.loc.radius
        else:
            radius = loc.radius
        mod.reg_hotfix(Mod.LEVEL, self.map_name,
                aa_obj_name,
                'DetectionRadius',
                radius,
                notify=True,
                )

        # Detection halfheight, whatever that is.
        mod.reg_hotfix(Mod.LEVEL, self.map_name,
                aa_obj_name,
                'DetectionHalfHeight',
                loc.halfheight,
                notify=True,
                )

        # Resurrection Location
        mod.reg_hotfix(Mod.LEVEL, self.map_name,
                res_obj_name,
                'RelativeLocation',
                f'(x={loc.res_x},y={loc.res_y},z={loc.res_z})',
                notify=True,
                )

        # Activate on entering its area?  Only going to set this if it's
        # changing, since we expect it to be True
        if self.loc.activate_on_enter_area != loc.activate_on_enter_area:
            mod.reg_hotfix(Mod.LEVEL, self.map_name,
                    res_obj_name,
                    'bActivateOnEnterArea',
                    loc.activate_on_enter_area,
                    notify=True,
                    )

        # Finally -- any Ubergraph references to update?
        if loc.ubergraph_ref is not None:
            obj_name, attr_name = loc.ubergraph_ref
            mod.reg_hotfix(Mod.LEVEL, self.map_name,
                    obj_name,
                    attr_name,
                    Mod.get_full_cond(self.obj_name, self.export_type))

class StationMap:

    def __init__(self, data, verbose=False):
        self.station_exports = {}
        for map_name, map_obj_name in [
                ('AtlasHQ_P', '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Courtyard_Dynamic'),
                ('AtlasHQ_P', '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_P'),
                # This one doesn't currently serialize
                #('AtlasHQ_P', '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Labs'),
                ]:
            map_data = data.get_data(map_obj_name)
            for export in map_data:
                if export['export_type'] == 'FastTravelStationObject_C' \
                        or export['export_type'] == 'ResurrectTravelStationObject_C' \
                        or export['export_type'] == 'FastTravelStationObject_OneWay_C':
                    station = Station(export['_jwp_object_name'], map_name, map_obj_name, map_data, export)
                    self.station_exports[export['_jwp_object_name']] = station

                    # Report, if we've been told to.
                    if verbose:
                        station.report()
                        print('')

    def __getitem__(self, name):
        return self.station_exports[name]

# Load all our data
data = BL3Data()
sm = StationMap(data, verbose)

# Fast Travel (level entrance)
station_ft_main = sm['FastTravelStationObject_1547']
station_ft_main.has_min_radius = True

# Rhys's office
station_rhys = sm['Checkpoint_Office']

# Maintenance Access (dogleg during battle around the perimiter)
station_maint = sm['Checkpoint_Maintenance']

# Outside control room (near the end of the dogleg)
station_control1 = sm['Checkpoint_ControlRoomOne']

# Office area to the right, inside HQ building
station_offices = sm['Checkpoint_Lounge']

# Skunkworks Lab (Terry + friend)
# Skipping this one since AtlasHQ_Labs isn't currently serializable.  Position, for
# reference, is: -7100, 3514, 1500, and rotation is 0, 179.999939, 0.  (Haven't looked
# up the other stats 'cause we're not using it anyway.)
# station_lab = sm['ResurrectTravelStationObject_2']

# Bottom of Elevator
station_elevator = sm['Checkpoint_ControlRoomTwo']
station_elevator.loc.ubergraph_ref = (
        '/Game/Maps/Zone_1/AtlasHQ/AtlasHQ_Courtyard_Dynamic.AtlasHQ_Courtyard_Dynamic:PersistentLevel.AtlasHQ_Courtyard_Dynamic_C_0',
        'Checkpoint_ControlRoomTwo_ExecuteUbergraph_AtlasHQ_Courtyard_Dynamic_RefProperty',
        )

# One-way Fast Travel (level end)
station_ft_oneway = sm['FastTravelStationObject_OneWay_2']

# Seaside arena, by the radio challenge
station_radio = sm['ResurrectTravelStationObject_2']

###
### My own invented locations
###

# Upper courtyard, outside Atlas HQ
loc_courtyard = Location(x=6400, y=-2509, z=-605,
        pitch=0, yaw=158, roll=0,
        )

###
### Now do stuff
###

for title, filename, moves, desc in [
        ("Rhys' Office", 'rhys_office', [
            (station_ft_main, station_rhys.loc),
            (station_rhys, station_ft_main.loc),
            ],
            [
                "Moves the Atlas HQ Fast Travel machine into Rhys' Office,",
                "swapping places with the New-U station ordinarily found there.",
            ]),
        ("Base of Elevator", 'elevator_base', [
            (station_ft_main, station_elevator.loc),
            (station_elevator, station_ft_main.loc),
            ],
            [
                "Moves the Atlas HQ Fast Travel machine to the bottom of the",
                "long elevator, swapping places with the New-U station",
                "ordinarily found there.",
            ]),
        ("Upper Courtyard", 'courtyard', [
            (station_ft_main, loc_courtyard),
            (station_offices, station_ft_main.loc),
            ],
            [
                "Moves the Atlas HQ Fast Travel machine to the upper courtyard,",
                "just outside the Atlas HQ entrance.  The New-U station tucked",
                "away in the offices to the right, inside Atlas HQ, is moved over",
                "to replace the Fast Travel station's original location.  Also,",
                "the New-U in the bank spawns you over by one of the exits,",
                "practically outside the building.  Go figure.",
            ]),
        ]:

    # Open the mod
    mod = Mod(f'atlas_hq_fast_travel_{filename}.bl3hotfix',
            f'Atlas HQ Fast Travel: {title}',
            'Apocalyptech',
            desc,
            contact='https://apocalyptech.com/contact.php',
            lic=Mod.CC_BY_SA_40,
            v='1.0.1',
            cats='qol, maps',
            ss=[f'https://raw.githubusercontent.com/BLCM/bl3mods/master/Apocalyptech/qol/atlas_hq_fast_travel/screenshot_{filename}.jpg'],
            )

    # Process the moves
    for station, location in moves:
        mod.comment(station.obj_name_last)
        station.move_to(mod, location)
        mod.newline()

    # Update the location for the station when we're *not* already at Atlas HQ
    # We're assuming here that the first entry in the `moves` list is the one
    # describing where the FT station itself is going.
    loc = moves[0][1]
    mod.header('Update global game map FT location')
    mod.reg_hotfix(Mod.PATCH, '',
            '/Game/GameData/ZoneMap/ZoneMapData/ZoneMapData_AtlasHQ',
            'ZoneMapPOIList.ZoneMapPOIList[3].PointOfInterestTransform.Translation',
            f'(x={loc.x},y={loc.y},z={loc.z})')
    mod.newline()

    # Close
    mod.close()
