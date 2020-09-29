Borderlands 3 Mods
==================

This is the github home to a collection of Bordlerlands 3 Mods.  At the
moment, all the mods stored here are made using the hotfix injection
method of BL3 modding, which basically just adds custom hotfixes to the
ones sent to the game by Gearbox.

Running Mods
------------

Currently, there is currently only one publicly-available method for
running hotfix-based mods, and it's not an especially easy one.  It's
based on the network tool [mitmproxy](https://mitmproxy.org/) and
requires a nontrivial amount of setup.  Information on that method
can be found a [Apocalyptech's bl3hotfixmodding repo](https://github.com/apocalyptech/bl3hotfixmodding).
Users who use this method will maintain a `modlist.txt` file (you can
see an example here at `modlist_example.txt`) which defines all the
active mods, and then the mitmproxy process will inject them into
the network stream.

Other methods are forthcoming, including some more user-friendly GUIs
which let you just choose mods from a list, but there is currently no
release date scheduled for those tools.  Those tools are unlikely to
make use of the `modlist.txt` format that Apocalyptech's mitmproxy-based
solution does.

The Python utility `modlist_to_json.py` can be used to convert a
`modlist.txt` file to a format capable with one such unreleased utility.

Finding Mods
------------

Obviously you can just browse around this github repo to find mods that
you like, but since the mods are arranged by author, it might be difficult
to know exactly what's available.  Like for BL2/TPS mods, we've created a
[Borderlands 3 ModCabinet Wiki](https://github.com/BLCM/BL3ModCabinet/wiki)
which categorizes mods by what they do, and will probably be much easier
to work with.

Some mod authors might decide to store their BL3 mods somewhere other than
here, of course.  If any major hubs of BL3 mod distribution ever becomes
popular, we'll link it in here.  The
[Borderlands 3 section of Nexus Mods](https://www.nexusmods.com/borderlands3)
is likely to start accumulating these kinds of mods, once friendlier tools
are developed to make use of them.

For Mod Authors
===============

See [README-authors.md](README-authors.md) for information on both
writing BL3 mods, and contributing to this github (and associated
wiki).

