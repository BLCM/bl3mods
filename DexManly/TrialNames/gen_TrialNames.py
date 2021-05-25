import sys
sys.path.append('..\python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('TrialNames.bl3hotfix',
        'Trial Names',
        'DexManly',
        [
            "Add trial names to the galaxy map proving grounds."
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol',
        )

mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-1.PlanetMapData_ProvingGround-1', 'SubHeader', 'Proving Grounds - Survival')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-4.PlanetMapData_ProvingGround-4', 'SubHeader', 'Proving Grounds - Fervor')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-5.PlanetMapData_ProvingGround-5', 'SubHeader', 'Proving Grounds - Cunning')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-6.PlanetMapData_ProvingGround-6', 'SubHeader', 'Proving Grounds - Supremacy')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-7.PlanetMapData_ProvingGround-7', 'SubHeader', 'Proving Grounds - Discipline')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-8.PlanetMapData_ProvingGround-8', 'SubHeader', 'Proving Grounds - Instinct')
mod.newline()
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-1.PlanetMapData_ProvingGround-1', 'DisplayName', 'Gradient of Dawn (Survival)')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-4.PlanetMapData_ProvingGround-4', 'DisplayName', 'The Skydrowned Pulpit (Fervor)')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-5.PlanetMapData_ProvingGround-5', 'DisplayName', 'Ghostlight Beacon (Cunning)')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-6.PlanetMapData_ProvingGround-6', 'DisplayName', 'The Hall Obsidian (Supremacy)')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-7.PlanetMapData_ProvingGround-7', 'DisplayName', 'Precipice Anchor (Discipline)')
mod.reg_hotfix(Mod.LEVEL, 'MatchAll', '/Game/GameData/ZoneMap/PlanetMapData/PlanetMapData_ProvingGround-8.PlanetMapData_ProvingGround-8', 'DisplayName', 'Wayward Tether (Instinct)')

mod.close()
