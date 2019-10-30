#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import struct
import subprocess

# Used to grab red text entries for Legendary/Unique gear, from the extracted
# BL3 data.  This is the base extract for gen_red_text_explainer.py.
#
# Requires some manual work; titles aren't properly escaped, etc, Hunted/Hunter/Huntress
# don't match quite right, or the two Krieg ARs, etc.  A few weapons reported
# here don't actually need to be in the list, too.

name_re = re.compile('^# (.*)$')
bal_re = re.compile('^\(\'(.*?)\', [0-9\.]+(\*addition_scale)?\),$')
flavor_re = re.compile('^\[Flavor\](.*)\[\/Flavor\]$', re.I)

things = {}

# red_text_items.txt just taken from my gen_expanded_legendary_pools and massaged
# slightly
with open(os.path.join(os.path.dirname(__file__), 'red_text_items.txt')) as df:
    while True:
        name_line = df.readline()
        if name_line:
            bal_line = df.readline()

            name_match = name_re.match(name_line)
            if not name_match:
                raise Exception('unknown name line: {}'.format(name_line))
            item_name = name_match.group(1)

            bal_match = bal_re.match(bal_line)
            if not bal_match:
                raise Exception('unknown bal line: {}'.format(bal_line))
            bal_name = bal_match.group(1)

            path = os.path.dirname(bal_name)
            if not path.startswith('/Game/'):
                raise Exception('Non-/Game/ balance? {}'.format(path))
            path = path[6:]

            found_uistat = None
            for filename in os.listdir(path):
                if filename.startswith('UIStat_Red') and filename.endswith('.uexp'):
                    found_uistat = os.path.join(path, filename)
                    break

            if not found_uistat:
                path = os.path.dirname(path)
                for filename in os.listdir(path):
                    if ((filename.startswith('UIStat_Red') and filename.endswith('.uexp'))
                            or (filename.startswith('UIStat_') and filename.endswith('_Flavor.uexp'))):
                        found_uistat = os.path.join(path, filename)
                        break

            save_path = path
            if not found_uistat:
                path = os.path.join(save_path, 'UI')
                if os.path.exists(path):
                    for filename in os.listdir(path):
                        if filename.startswith('UIStat_Red') and filename.endswith('.uexp'):
                            found_uistat = os.path.join(path, filename)
                            break

            if not found_uistat:
                path = os.path.join(save_path, 'Name')
                if os.path.exists(path):
                    for filename in os.listdir(path):
                        if filename.startswith('UIStat_Red') and filename.endswith('.uexp'):
                            found_uistat = os.path.join(path, filename)
                            break

            if not found_uistat:
                things[item_name] = []
                things[item_name].append("        ('{}',".format(item_name))
                things[item_name].append("            'NO UISTAT FOUND - {}',".format(bal_name))
                things[item_name].append('            "foo",')
                things[item_name].append('            "foo"),')
                continue

            (uistat_base, uistat_file) = os.path.split(found_uistat)
            uistat_noext = uistat_file[:-5]
            uistat_obj = '/Game/{}/{}.{}'.format(uistat_base, uistat_noext, uistat_noext)

            # Get text; couldn't get `strings` binary to handle the UTF-16 text at all
            found_text = None
            with open(found_uistat, 'rb') as uidf:
                uidf.seek(0x47)
                strlen = struct.unpack('<i', uidf.read(4))[0]
                if strlen > 0:
                    data = uidf.read(strlen-1).decode('latin1')
                    flavor_match = flavor_re.match(data)
                    if flavor_match:
                        found_text = flavor_match.group(1)
                elif strlen < 0:
                    data = uidf.read(abs((strlen+1)*2))
                    data = data.decode('utf_16_le')
                    flavor_match = flavor_re.match(data)
                    if flavor_match:
                        found_text = flavor_match.group(1)
                else:
                    raise Exception('zero-length?')

            if not found_text:
                things[item_name] = []
                things[item_name].append("        ('{}',".format(item_name))
                things[item_name].append("            'NO TEXT FOUND - {}',".format(uistat_obj))
                things[item_name].append('            "NO TEXT FOUND",')
                things[item_name].append('            "foo"),')
                continue

            things[item_name] = []
            things[item_name].append("        ('{}',".format(item_name))
            things[item_name].append("            '{}',".format(uistat_obj))
            things[item_name].append('            "{}",'.format(found_text))
            things[item_name].append('            "foo"),')

        else:
            break

for (item_name, display_list) in sorted(things.items()):
    for display in display_list:
        print(display)
