import sys
from bl3hotfixmod import Mod
	  
mod = Mod('whereismyfile.bl3hotfix',
        'Varkid Testing',
        'TheGigaMaster',
        [
            "testing shit here"
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gameplay, qol',
        )

mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_LarvaToAdult.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
		DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """),

mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_AdultToBadass.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
			DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """),

mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_BadassToSuper.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
			DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """),

mod.reg_hotfix(Mod.CHAR, 'MatchAll',
    '/Game/Enemies/Varkid/_Shared/_Design/Attributes/Table_VarkidShared_EvolutionChance',
    'EvolveChance_SuperToRaid.OnePlayer_PT1',
    """
    (
    	BaseValueConstant=1,
			DataTableValue=(
			DataTable=None,
			RowName="",
			ValueName=""),
		BaseValueAttribute=None,
		AttributeInitializer=None,
		BaseValueScale=1
    )
    """),
mod.close()
