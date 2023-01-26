Digby's Smooth Tube Audio Fix
=============================

Fixes the broken audio for Digby's Smooth Tube by reverting its custom
soundbank back to its original state, after it had gotten broken by the
2020-06-11 Guardian Takedown patch.  Note that there is *no* hotfix
component to this mod!  No OHL or B3HM required.  The actual fix is
contained in the associated pakfile.  Get that installed along with your
existing pakfiles, and you'll be good to go.

Building The Pakfile
====================

You can construct the replacement pakfile yourself pretty easily if you've
got `UnrealPak.exe` handy.  The soundbank in question is
[`3471258537.bnk`](https://apocalyptech.com/games/bl3-pakfile/index.php?name=3471258537).
Its original version was contained inside `pakchunk2-WindowsNoEditor_2_P.pak`.
Then on the Guardian Takedown patch, it was replaced by a version in
`pakchunk2-WindowsNoEditor_6_P.pak`.  The original version includes all the
saxophone noises embedded in the soundbank itself, but the new one appears
to try and use external `.wem`s for the sounds, instead.  Clearly that
linking didn't work properly.

Anyway, creating the fix is easy -- simply unpack the original `3471258537.bnk`
from `pakchunk2-WindowsNoEditor_2_P.pak`, and then re-pack it into a new
pakfile.  Make sure that new pakfile's loaded *after* all the other
`pakchunk2-*` files, and you should be good to go!  Note that the replacement
pakfile does *not* need to be encrypted, or to have its index encrypted, though
for the version distributed here, I've used the usual BL3 key for the pakfile.
Getting the internal structure correct was a bit tricky for me.  What I did
was create an `export` directory, with `3471258537.bnk` sitting inside, and
created a `contents.txt` file (outside the `export` dir) with the following
contents:

    "export/*" "../../../OakGame/Content/WwiseAudio/"

Then I used the argument `-Create=contents.txt` with UnrealPak, which read in
the bank from the `export` dir, and set up the prefixes properly in the pak.

Changelog
=========

**v1.0.0** - Jan 25, 2023
 * Initial release
 
Licenses
========

The mod itself can't really be usefully licensed by a modder like myself.
The pakfile contents themselves are owned/copyrighted/whatever by Gearbox,
2K, or whoever else technically owns all that stuff.

The generation script for the mod is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](../../COPYING.txt) for the full text of the license.

