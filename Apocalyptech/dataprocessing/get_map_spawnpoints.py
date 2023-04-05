#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import sys
sys.path.append('../../python_mod_helpers')
sys.path.append('map_objects')
from mapobjlib.mapobjlib import MapObjects
from bl3data.bl3data import BL3Data

mo = MapObjects()
for level, object_path in mo.get_by_type('SpawnPoint_IO_C', 'Prologue_P'):
    print(object_path)

