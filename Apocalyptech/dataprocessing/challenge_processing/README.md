Some scripts to grab challenge data out of map object dumps that I use
to generate the data used by `gen_always_visible_challenge_icons.py`.
These have been living in a dir which doesn't actually get backed up
by my backup system, so I realized I should pull 'em in here for
safekeeping.

I use UUU's `Ctrl-<numpad-/>` to generate `UE4Tools_NamesDump.txt`
and `UE4Tools_ObjectsDump.txt` files for each map, then compress
the files using `xz`/lzma.  I've got them sorted in dirs by DLC,
then by map.  Top-level dirs are stuff like `basegame`, `dlc1`,
and `dlc1`, and then under there I have `City_P`, `Towers_P`, etc.
Each of those dirs just has the two compressed data files.

Then I can use `get_challenges.sh` to loop through the dumps to
find the challenge objects, which calls out to `process_challenges.py`
to *actually* do the work.

Note that the things that are found for DLC1 don't seem to work,
alas, and putting them in my modfile even causes weird problems.  DLC2
has not yet been tested.
