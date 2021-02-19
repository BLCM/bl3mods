import sys
sys.path.append('..\python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('BetterSanctuary3Floors.bl3hotfix',
        'Better Sanctuary 3 Floors',
        'DexManly',
        [
            "Sanctuary 3 should be a safe place for users to",
			"drop loot, trade, examine, and sort your loot. ",
			"but too often you end up with loot falling through",
			"the floors. This mod adds square objects under the",
			"floors of Sanctuary 3 so that your loot never is lost!",
			"If you see the giant cheeseburger (mmmm) on the middle",
			"table, then you know you are safte to drop items!"
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='maps','qol',
        )

level_Sanctuary3 = '/Game/Maps/Sanctuary3/Sanctuary3_P'
basicCube = '/Engine/BasicShapes/Cube'
burger = '/Game/InteractiveObjects/MissionSpecificObjects/DynastyDiner/Burger/Model/Meshes/SM_DynastyDiner_Burger'
transparent = False

mod.comment("Burger AKA hotfix indicator")
mod.mesh_hotfix(level_Sanctuary3,
            	burger,
            	location=(14700,8269,-685),
            	scale=(3,3,3))
mod.newline()

mod.comment("Floor Under Spawn and Character Quarters")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(14670,7240,-840),
            	scale=(60,50,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Left Hallway")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(13730,3090,-840),
            	scale=(9.1,33,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Moxxis")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(12570,1250,-840),
            	scale=(33,30,0.5),
				transparent=transparent)
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(11559,-529,-840),
            	scale=(9,10,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Right Hallway")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(15650,1890,-840),
            	scale=(9.1,57,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Marcus")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(17100,2042.5,-840),
            	scale=(23,30,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Hall to left-handed gun switch")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(15668.5,2400,-1460),
            	scale=(40,42,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Shooting Range")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(17200,-1580,-1460),
            	scale=(20,38,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Zero Room")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(13180,1000,-1560),
            	scale=(10,10,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Cargo Room")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(13850,-477,-2200),
            	scale=(35,50,0.5),
				transparent=transparent)
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(15906,-605,-2200),
            	scale=(7,23,0.5),
				transparent=transparent)
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(15906,-2586,-2200),
            	scale=(7,7,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under DropPod Room")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(16709,-2120,-2400),
            	scale=(20,7,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Bridge")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(14707,-8623,-720),
            	scale=(20,22,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Hall To Bridge")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(14697,-4413,-140),
            	scale=(12,54,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Lilith Room")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(12400,-4044,-360),
            	scale=(20,9,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Ava Room")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(17000,-4044,-360),
            	scale=(20,9,0.5),
				transparent=transparent)
mod.newline()

mod.comment("Floor Under Tannis Room")
mod.mesh_hotfix(level_Sanctuary3,
            	basicCube,
            	location=(12500,-968,-130),
            	scale=(33,45,0.5),
				transparent=transparent)
mod.newline()

mod.close()
