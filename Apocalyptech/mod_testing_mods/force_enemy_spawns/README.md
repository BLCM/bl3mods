Force Enemy Spawns
==================

Resource mod which attemps to alter SpawnOptions objects so that wherever
the configured character *can* spawn, they *will* spawn 100% of the time.

Does not attempt to touch SpawnOptions objects which don't involve the
specified char, since BL3/WL spawning points are often a bit touchy about
which chars are allowed to spawn from them.

The on-disk version here is hardcoded to Anointed Tinks.  To make it
operate on some other enemy, you'll have to edit the generation script
and re-generate it.

Changelog
=========

**v1.0.0** - Jan 24, 2023
 * Initial release, based on v1.0.1 of
   [WL's Force Enemy Spawns](https://github.com/BLCM/wlmods/wiki/Force%20Enemy%20Spawns%3A%20BPchar_GoblinBarrel)
 
Licenses
========

This mod is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

