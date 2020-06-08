#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
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

from bl3hotfixmod.bl3hotfixmod import Mod, BVC

for event, menunum in [
        ('normal', 0),
        ('halloween', 3),
        ('christmas', 4),
        ('cartels', 5),
        ]:

    mod_filename = 'main_menu_{}.txt'.format(event)
    event_cap = event.capitalize()

    mod = Mod(mod_filename,
            'Main Menu: {}'.format(event_cap),
            'Apocalyptech',
            [
                "Sets the main menu to have the {} visuals.  No actual effect on".format(event_cap),
                "gameplay or anything (use the `eventname_enable.txt` mods to actually",
                "turn timed events back on).",
            ],
            lic=Mod.CC_BY_SA_40,
            )

    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Common/_Design/Table_MicropatchSwitches',
            'MainMenuAltBackground',
            'Value',
            BVC(bvc=menunum))

    mod.close()


