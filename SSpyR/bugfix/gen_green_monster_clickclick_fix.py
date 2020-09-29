from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data


mod = Mod('green_monster_clickclick_fix.bl3hotfix',
        'Green Monster Click Click Points Fix',
        'SSpyR',
        [
            'Green Monster can only get 1 point in Click Click.',
            'This mod adds 2 other Click Click parts to fix that.'
        ],
        lic=Mod.CC_BY_SA_40,
        cats='bugfix, gear-com'
        )

gm_bal_name='/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1'
clickclick_part='/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/Skills/ClassMod_Part_Skill_Gunner_ClickClikc_DLC1' 

data = BL3Data()
gm_bal = Balance.from_data(data, gm_bal_name)
for cat in gm_bal.categories:
    if cat.index == 5 & cat.num_max == 5:
        cat.add_part_name(clickclick_part, 1)
        cat.add_part_name(clickclick_part, 1)
        break
gm_bal.hotfix_full(mod)

mod.close()