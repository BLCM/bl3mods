Arbitrary Partlocks
===================

This isn't actually a mod itself.  Rather, it's an interactive script which can
*create* a mod for you, which will allow you to partlock specific balances
however you like.  For instance, if you always want to have a specific scope
on sniper rifles, or a particular barrel on ARs, you'd be able to do so in
here.

The UI is a bit weird, and I'm not going to go into detail here (sorry, perhaps
later when I don't have a million READMEs to write), but hopefully it's
self-explanatory enough.

You *will* need to install the `colorama` Python module in order to run this,
and it requires a working `bl3data` installation with access to extracted BL3
data (see the `python_mod_helpers` directory at the top of this repo).

Changelog
=========

**v1.1.0** - Jan 10, 2021
 * Improved accuracy of part lists, which fixes some off-by-one errors (mostly
   just related to COMs)
 * Allowed specifying ranges of parts to act on (using dashes), and specifying
   multiple parts/ranges with commas
 * Doesn't quit automatically after saving out to a file
 * Use `d` to toggle showing dependencies/excluders
 * Displays which Anointments no longer spawn when using GBX Hotfixes

**v1.0.0** - Sep 26, 2020
 * First versioned release
 
Licenses
========

This code is licensed under the [GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

