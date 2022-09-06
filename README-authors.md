Writing Mods
============

Right now, the only available method of modding Borderlands 3 in a way that
resembles BL2/TPS modding is through hotfix injection.  This poses a number
of challenges to even get it working, and once you've gotten that far, it's
not nearly as mature as BLCMM-based BL2/TPS modding is.

For the modder who's already familiar with modding BL2/TPS, there *are* many
similarities between the two.  BLCMM abstracts a lot of the details when
writing mods, but in the end you can think of BL3 hotfixes as just a collection
of weird-looking `set` statements (though you'll never actually see the word
`set` in the hotfixes).  But past experience in dealing with BL2/TPS arrays,
and knowing how to dive into attributes using hotfix syntax, etc, will definitely
make the transition to BL3 hotfix modding much easier.

The main resource for getting used to writing these kind of hotfix mods is
the main [BLCMods Wiki](https://github.com/BLCM/BLCMods/wiki).  The Borderlands 3
links are near the bottom of the main page.  Here's some of the main pages
you'll want to look into:

- [Accessing BL3 Data](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data) -
  Since we don't have something like BLCMM for BL3 modding, one of the bigger
  challenges is having game data to work with.  This page details all of our
  currently-known ways of pulling information from the game, which will be
  a great help in figuring out what to change in the game.
- [Borderlands 3 Hotfixes](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfixes) -
  For this style of modding, you're basically writing raw hotfixes, so knowing how
  they're laid out and how to read them is extremely useful.
- [Borderlands 3 Hotfix Modding](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfix-Modding) -
  This page is a primer for getting used to writing BL3 hotfixes.  This page is,
  unfortunately, written mostly from the perspective of someone who's already
  familiar with BL2/TPS modding.  This page goes into some detail about some of
  the differences between modding in BL2/TPS and BL3.

One invaluable resource to look at, of course, is existing hotfixes.  There's a few
places to look to take a look at those:

- This repository contains a lot of known-working examples
- Gearbox's official hotfixes have been being collected since very shortly after the
  game launch, at [the bl3hotfixes repo](https://github.com/BLCM/bl3hotfixes/).
- A Google Sheets of the combined set of Gearbox-provided hotfixes is also available,
  in a nice spreadsheet format:
  [https://docs.google.com/spreadsheets/d/1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ/](https://docs.google.com/spreadsheets/d/1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ/)

Constructing Mods With Code
===========================

BL2/TPS modding is able to make use of BLCMM to simplify things and catch common
errors, but we don't have something like that for BL3 Hotfix Modding yet.  One
way to make modding easier is to use programming languages to help you construct
the mod files.  This repo includes some Python-based scripts which serves to do
that.  Practically all of Apocalyptech's mods in here were constructed using these
modules.

Using them does require that you install Python on your system, and get used to
working in the language, but it avoids having to worry about fiddly hotfix syntax
and lets you focus on just writing the hotfixes.  Take, for example, this hotfix
from Apocalyptech's Better Loot, which increases eridium drop chances from
standard enemies:

    SparkCharacterLoadedEntry,(1,1,0,MatchAll),/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear,ItemPools[10].PoolProbability,0,,(BaseValueConstant=0.8,DataTableValue=(DataTable=None,RowName="",ValueName=""),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1)

There's a lot going on there, with weird syntax, parentheses you have to keep
track of, and for it to be a valid hotfix you can't make use of whitespace to
make it any clearer.  Writing the hotfix with code, however, lets you do this,
instead:

```python
mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear',
    'ItemPools[10].PoolProbability',
    """
    (
        BaseValueConstant=0.8,
        DataTableValue=(
            DataTable=None,
            RowName="",
            ValueName=""),
        BaseValueAttribute=None,
        AttributeInitializer=None,
        BaseValueScale=1
    )
    """)
```

And then the mod-helper framework will convert that into a proper hotfix for
you, and you can edit it in a much more intuitive way.

These helpers (and a few more examples of how to use them) can be found in
the [python_mod_helpers](https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers)
directory, and plenty of examples of using it in "real life" can be found
throughout Apocalyptech's mod directory.

The code in `python_mod_helpers` dir is licensed under the GNU GPLv3 or later.

Contributing
============

If you've ever submitted mods to the BL2/TPS github area, you already know
how to do so for this repo, because the procedure is identical.  You can find
instructions for how to do so
[at the BLCMods Wiki](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Contribution).

If you want your mods to show up on the
[Borderlands 3 ModCabinet wiki](https://github.com/BLCM/bl3mods/wiki), which
is the easiest way for users to find mods through github, you'll want to make sure
to follow the [ModCabinet wiki guidelines](https://github.com/BLCM/bl3mods/wiki/Contributing-to-BL3-ModCabinet)
as well.  The most important parts are to make sure your mod file has a `.bl3hotfix`
extension, and contain `@title` and `@categories` headers at the top of the mod file.

