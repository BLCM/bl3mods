#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2022 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
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
from bl3data.bl3data import BL3Data

# An attempt to see if we could standardize on `RootComponent` for the positioning
# of type-11-injected objects.  Basically loops through all map objects looking
# for exports which link to *other* exports which have `RelativeLocation` or
# `RelativeRotation` attrs, and keeping track of the attr names which link to those
# other exports.
#
# (Was actually originally gonna be an attempt to just find out *which* attr was
# appropriate for positioning, but I don't think this approach would ever give
# me the confidence in results necessary to consider that problem solved.)
#
# Turns out practically everything *does* have `RootComponent`, but after some
# testing, not everything can actually use it for repositioning.  My CAR platforms
# for Jetbeasts Everywhere, for instance, or the Easy Entry To Fort Sunshine switch.
# So, in the end, not super useful.
#
# The output, btw, showing the very few objects which *don't* have `RootComponent`:
#
#    Found 155,961 objects
#    Found 2,724 map objects
#    Found 2554 object mappings
#    /dandelion/mapspecific/strip/peepshow/blueprint/_shared/io_switch_hyp_button_v1_peepshow: {'SM_Button_Generic_Cylindrical_V1'}
#    /game/destructibles/eden6/_mansion/wall_500/_design/pd_wall_mansion_500_unbroken: {'ParentComponent'}
#    /game/destructibles/missionspecific/cityvault/blockade_bandit/_design/pd_blockade_bandit: {'ParentComponent'}
#    /game/destructibles/missionspecific/prison/wall_prison/_design/pd_wall_prison: {'ParentComponent'}
#    /game/destructibles/missionspecific/prologue/bridge_foot/_design/pd_bridge_foot: {'ParentComponent'}
#    /game/destructibles/missionspecific/wetlandsvault/icewall_tc/_design/pd_icewall_figures_tc: {'ParentComponent'}
#    /game/destructibles/missionspecific/wetlandsvault/icewall_tc/_design/pd_icewall_tc: {'ParentComponent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_collection: {'AttachParent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_collectiondeaddrop: {'AttachParent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_hijack_spawner: {'AttachParent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_hunt_spawner: {'AttachParent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_killtarget_spawner: {'AttachParent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_sabotage: {'AttachParent'}
#    /game/gamedata/challenges/components/bp_crewchallengecomponent_salvage: {'AttachParent'}
#    /game/gamedata/challenges/eridianwriting/bp_challengecomponent_iconeridian: {'AttachParent'}
#    /game/interactiveobjects/doors/atlas/_design/io_door_atlashq_elevator_interior_short: {'Door_L', 'Door_R'}
#    /game/interactiveobjects/doors/atlas/_design/io_door_atlashq_elevator_interior_tall: {'Door_L', 'Door_R'}
#    /game/interactiveobjects/gamesystemmachines/fasttravelstation/leveltravelstationbillboard: {'AttachParent'}
#    /game/interactiveobjects/gamesystemmachines/fasttravelstation/oaktravelstationresurrectcomponent: {'AttachParent'}
#    /game/interactiveobjects/missiondamageable/_design/io_missiondamageable_lock_cage: {'ParentComponent'}
#    /game/missions/side/zone_3/desert/bufffilmbuff/io_missionplaceable_bufffilmbuff_projectorbulb: {'Placeable Mesh', 'PlaceableMeshComponent'}
#    /game/patchdlc/dandelion/gamedata/challenges/components/bp_crewchallengecomp_killtarget_dlc1: {'AttachParent'}
#    /game/patchdlc/dandelion/gamedata/challenges/components/bp_crewchallengecomp_sabotage_dlc1: {'AttachParent'}
#    /game/patchdlc/geranium/gamedata/challenges/components/bp_crewchallengecomponent_jakobsvault: {'AttachParent'}
#    /game/patchdlc/geranium/gamedata/challenges/components/bp_crewchallengecomponent_treasuremap: {'AttachParent'}
#    /geranium/levelart/destructibles/mission_specific/glass_case/_design/pd_glass_case: {'ParentComponent'}
#    /hibiscus/interactiveobjects/missionspecific/crew/gifts/component/bp_crewchallengecomp_gifts_dlc2: {'AttachParent'}
#    /hibiscus/interactiveobjects/missionspecific/crew/hunt/component/bp_crewchallengecomp_hunt_dlc2: {'AttachParent'}
#    /hibiscus/interactiveobjects/missionspecific/crew/mancubus/component/bp_crewchallengecomp_mancubus_dlc2: {'AttachParent'}

print("Eh, didn't work out.  See the source if you're interested.")
sys.exit(0)

data = BL3Data()

mapref_blocklist = set()
mapref_mapping = {}
obj_dir_base = '/home/pez/bl3_decrypt/extracted'
obj_dir_base_len = len(obj_dir_base)
for dirpath, dirnames, filenames in os.walk(obj_dir_base):
    for filename in filenames:
        if filename.endswith('.umap') or filename.endswith('.uasset'):
            base_filename = filename.rsplit('.', 1)[0]
            base_filename_c = f'{base_filename}_C'
            if base_filename_c not in mapref_blocklist:
                if base_filename_c in mapref_mapping:
                    mapref_blocklist.add(base_filename_c)
                    del mapref_mapping[base_filename_c]
                else:
                    base_pathname = os.path.join(dirpath[obj_dir_base_len:], base_filename)
                    mapref_mapping[base_filename_c] = base_pathname.lower()
print('Found {:,} objects'.format(len(mapref_mapping)))

map_objects = []
for pattern in [
        #'/Game/Maps/Zone_1/City/*',
        '/Game/Maps/MenuMap/*',
        '/Game/Maps/ProvingGrounds/*/*',
        '/Game/Maps/Sanctuary3/*',
        '/Game/Maps/Slaughters/*/*',
        '/Game/Maps/Zone_0/*/*',
        '/Game/Maps/Zone_1/*/*',
        '/Game/Maps/Zone_2/*/*',
        '/Game/Maps/Zone_3/*/*',
        '/Game/Maps/Zone_4/*/*',
        '/Dandelion/Maps/*/*',
        '/Hibiscus/Maps/*/*',
        '/Geranium/Maps/*/*',
        '/Alisma/Maps/*/*',
        '/Ixora/Maps/*/*',
        '/Ixora2/Maps/Boss/*',
        '/Ixora2/Maps/Cabin/*',
        '/Ixora2/Maps/Noir/*',
        '/Ixora2/Maps/Mystery/*/*',
        ]:
    map_objects.extend(data.glob(pattern))
print('Found {:,} map objects'.format(len(map_objects)))
if False:
    for map_obj in map_objects:
        print(map_obj)
    sys.exit(0)

found_maps = {}
obj_blocklist = {
        '/Game/Maps/Zone_1/Towers/Mat_KillaVoltBlack',
        }
export_blocklist = {
        'export_type',
        '_jwp_export_idx',
        '_jwp_is_asset',
        '_jwp_object_name',
        }
for obj_name in sorted(map_objects):
    if obj_name in obj_blocklist:
        continue
    obj_data = data.get_data(obj_name)
    #print(f'Processing {obj_name}')
    for export in obj_data:
        export_type = export['export_type']
        if export_type in mapref_mapping:
            #print(f' - {export_type}')
            matched_export_nums = set()
            for k, v in export.items():
                if k not in export_blocklist:
                    if type(v) == dict:
                        if 'export' in v and v['export'] != 0:
                            reference = obj_data[v['export']-1]
                            if 'RelativeLocation' in reference or 'RelativeRotation' in reference:
                                matched_export_nums.add(v['export'])
                                type_obj_path = mapref_mapping[export_type]
                                if type_obj_path not in found_maps:
                                    found_maps[type_obj_path] = set()
                                found_maps[type_obj_path].add(k)
                                #print('{}: {}'.format(
                                #    mapref_mapping[export_type],
                                #    k,
                                #    ))
            #if len(matched_export_nums) > 1:
            #    print(f'WARNING: Matched more than one export for {export_type}: {matched_export_nums}')

#print(found_maps)
print('Found {} object mappings'.format(len(found_maps)))
for k, v in sorted(found_maps.items()):
    if 'RootComponent' in v:
        pass
        #print(f'{k}: RootComponent')
    else:
        print(f'{k}: {v}')

