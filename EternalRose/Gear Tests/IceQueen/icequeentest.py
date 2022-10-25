import sys
import collections
sys.path.append('../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, Balance

mod = Mod('icequeenweaponbalancefix.bl3hotfix',
        'Ice Queen Weapon Balance Fix',
        'Eternal Rose',
        [
            "Making The Ice Queen sniper drop without a scope for better visibility",
        ],
        contact='https://github.com/RoseEternal',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gear-general',
        )

icequeen_bal_name = '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen'
parts = [
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Scope',
        ]
category = [
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Scope/None'
        ]

# Add the parts
data = BL3Data()
icequeen_bal = Balance.from_data(data, icequeen_bal_name)
cat = icequeen_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
icequeen_bal.hotfix_full(mod)

mod.close()