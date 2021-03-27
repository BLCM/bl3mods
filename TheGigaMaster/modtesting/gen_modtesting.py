import sys
sys.path.append('../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('varkid.bl3hotfix',
	'Varkid Evolution Increase',
	'TheGigaMaster',
	[
		'testing'
	],
	lic=Mod.CC_BY_SA_40,
	v='0.2',
	cats='enemy','scaling',
	)

mod.comment('increase varkid to adult to 100 chance')
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
    """)
mod.comment('adult to badass 100 chance')
mod.newline()

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
    """)
mod.comment('badass to superbadass 100 chance')
mod.newline()

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
    """)

mod.comment('badass to superbadass 100 chance')
mod.newline()
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
    """)
