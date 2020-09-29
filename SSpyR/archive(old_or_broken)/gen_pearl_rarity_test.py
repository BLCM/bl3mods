from bl3hotfixmod import Mod
from bl3data import BL3Data

#Doesn't Work Well

mod=Mod('pearl_rarity_test.txt',
		'Testing Making Pearl Rarity',
		'SSpyR',
		[
			''
		],
		lic=Mod.CC_BY_SA_40
		)

data=BL3Data()

mod.comment('Testing')
mod.reg_hotfix(Mod.PATCH, '',
			   '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber',
			   'RarityData',
			   '/Game/GameData/Loot/RarityData/RarityData_00_Mission')
mod.newline()

mod.close()