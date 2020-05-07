#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

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
            [
                "Sets the main menu to have the {} visuals.  No actual effect on".format(event_cap),
                "gameplay or anything (use the `eventname_enable.txt` mods to actually",
                "turn timed events back on).",
            ])

    mod.table_hotfix(Mod.PATCH, '',
            '/Game/Common/_Design/Table_MicropatchSwitches',
            'MainMenuAltBackground',
            'Value',
            BVC(bvc=menunum))

    mod.close()
    print('Generated {}'.format(mod_filename))


