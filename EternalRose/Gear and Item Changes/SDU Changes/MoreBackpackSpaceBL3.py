import sys
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod


mod = Mod('MoreBackpackSpaceBL3.bl3hotfix',
        'More Backpack Space for Borderlands 3',
        'Eternal Rose',
        [
            "Ever feel you don't have enough space? Not enough loot to scratch that itch?",
            "Worry no more, this mod allows you to buy more for the same price! Think of it",
            "as a discount from Marcus! And don't you tell anyone he hasn't done anything for",
            "you.",
            "This mod will increase the slots obtained per each tier of SDU you buy from Marcus.",
        ],
        contact='https://github.com/RoseEternal',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='inventory'
        )
        
row_hardcodes = {
        'Table_SDU_Bank': {
            23: 'NewRow',
            24: 'NewRow_0',
            25: 'NewRow_1',
            26: 'NewRow_2',
            27: 'NewRow_3',
            },
        }
        
for table, levels in [
        ('Table_SDU_Backpack', 13),
        ]:
    mod.comment(table)
    for level in range(levels):
        if table in row_hardcodes and level in row_hardcodes[table]:
            row_name = row_hardcodes[table][level]
        else:
            row_name = 'Lv{}'.format(level+1)    
        mod.table_hotfix(Mod.PATCH,'',
            '/Game/Pickups/SDU/{}'.format(table),
            row_name,
            'AttributeModifyInfo',
            (ModifierValue:='(AttributeToModify=/Game/GameData/Attributes/Character/Att_PlayerInventoryMax.Att_PlayerInventoryMax,ModifierType=PreAdd,ModifierValue=(BaseValueConstant=28.0)')
            )
        mod.newline()
    mod.newline()
mod.close()