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

mod = Mod('photo_mode_unlock.txt',
        'Photo Mode Unlock',
        'Apocalyptech',
        [
            "Unlocks the camera in Photo Mode to be able to go extremely far.  Possibly",
            "not to the full extent of every level -- I've not tested thoroughly -- but",
            "enough to take you from the Highway FT in Droughts back to the main FT in",
            "that area, at least.  Also buffs up the camera move speed so that it's not",
            "agonizing having to go over so much terrain.  That might make lining up",
            "precise angles a bit harder, but c'est la vie!",
        ],
        lic=Mod.CC_BY_SA_40,
        )

# Default: 200
camera_range = 30000

# Default: 100
speed = 800

mod.comment('Extending camera range')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Camera/CameraMode_PhotoMode_Offset.CameraMode_PhotoMode_Offset:Behaviors_CameraBehavior_OffsetCameraRelativeFromInputs',
        'MoveLimit',
        f"""(
            Min=(X=-{camera_range},Y=-{camera_range},Z=-{camera_range}),
            Max=(X={camera_range},Y={camera_range},Z={camera_range}),
            IsValid=1
        )""")
mod.newline()

mod.comment('Increasing camera move speed')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Camera/CameraMode_PhotoMode_Offset.CameraMode_PhotoMode_Offset:Behaviors_CameraBehavior_OffsetCameraRelativeFromInputs',
        'MoveSpeed',
        speed)
mod.newline()

mod.close()
