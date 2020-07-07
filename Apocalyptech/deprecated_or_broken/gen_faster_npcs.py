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

from bl3hotfixmod.bl3hotfixmod import Mod, BVCF

mod = Mod('faster_npcs.txt',
        'Faster NPCs',
        'Apocalyptech',
        [
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Pretty sure this is the right var to go after, to get Oletta to speed up.
# Haven't yet found a hotfix syntax that'll alter it, though.  And of course
# I could be wrong about the var, too...

# getall gbxcharacteraniminstance maxwalkspeed
# BPAnim_Granny_C /Geranium/Maps/Forest/Forest_P.Forest_P:PersistentLevel.BPChar_Granny_C_0.CharacterMesh0.BPAnim_Granny_C_0.MaxWalkSpeed = 120
#
# getall gbxskeletalmeshcomponent animscriptinstance name=charactermesh0

if False:
    # Attempts at a "direct" set.
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Granny',
            #'/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.Default__BPChar_Granny_C:CharacterMesh0.BPAnim_Granny_C',
            #'/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.Default__BPAnim_Granny_C',
            #'/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.Default__BPChar_Granny_C:CharacterMesh0.Default__BPAnim_Granny_C',
            '/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.BPChar_Granny_C:CharacterMesh0.Default__BPAnim_Granny_C',
            'MaxWalkSpeed',
            600)

if False:
    # Attempts at fancy object redirection
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Granny',
            '/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.Default__BPChar_Granny_C:CharacterMesh0',
            #'AnimScriptInstance.Object..MaxWalkSpeed',
            'Default__BPAnim_Granny_C.Object..MaxWalkSpeed',
            600)

if False:
    # Attempts direct at what I assume is the BPAnim object which gets loaded in
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Granny',
            '/Geranium/NonPlayerCharacters/Granny/Animation/BPAnim_Granny.Default__BPAnim_Granny_C',
            'MaxWalkSpeed',
            600)
    # Super longshots here
    for hf_type in [Mod.CHAR, Mod.PACKAGE, Mod.POST]:
        mod.reg_hotfix(hf_type, 'BPAnim_Granny',
                '/Geranium/NonPlayerCharacters/Granny/Animation/BPAnim_Granny.Default__BPAnim_Granny_C',
                'MaxWalkSpeed',
                600)

if False:
    # Had about zero hopes for this one, but figured I should try anyway.  Attempt
    # to go right at the level-specific obj
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Granny',
            #'/Geranium/Maps/Forest/Forest_P.Forest_P:PersistentLevel.BPChar_Granny_C_0.CharacterMesh0.BPAnim_Granny_C_0',
            '/Geranium/Maps/Forest/Forest_P.Forest_P:PersistentLevel.BPChar_Granny_C_0.CharacterMesh0.Default__BPAnim_Granny_C',
            'MaxWalkSpeed',
            600)

if True:
    # Huh, have I been going after the wrong var all this time?
    # Edit: nah, I can't seem to edit this one either, alas.  ><
    mod.reg_hotfix(Mod.CHAR, 'BPChar_Granny',
            '/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.Default__BPChar_Granny_C:CharMoveComp',
            'MaxWalkSpeed',
            '(Value=600,BaseValue=600)')
    mod.reg_hotfix(Mod.LEVEL, 'Forest_P',
            '/Geranium/NonPlayerCharacters/Granny/_Design/Character/BPChar_Granny.Default__BPChar_Granny_C:CharMoveComp',
            'MaxWalkSpeed',
            '(Value=600,BaseValue=600)')

mod.close()
