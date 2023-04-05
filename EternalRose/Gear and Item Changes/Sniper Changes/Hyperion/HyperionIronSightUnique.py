import sys
import collections
sys.path.append('../../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, Balance

mod = Mod('hyperionironsightunique.bl3hotfix',
        'Hyperion Snipers Iron Sight Change',
        'Eternal Rose',
        [
            "Allowing all Unique Hyperion snipers to drop without a scope, thus being Iron Sighted.",
        ],
        contact='https://github.com/RoseEternal',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gear-general',
        )
        
# These are the Unique Snipers that Hyperion have in-game.
        
crossbow_bal_name = '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork'
        
woodblocks_bal_name = '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks'

nulpoint_bal_name = '/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer'

# Parts is for directing the game "here's where I want the part" and the Category makes a new "None" sniper scope. 
        
parts = [
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Parts/Scope',
        ]
        
category = [
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Parts/Scope/None'
        ]

# Add the parts one by one

data = BL3Data()
crossbow_bal = Balance.from_data(data, crossbow_bal_name)
cat = crossbow_bal.categories[7]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
crossbow_bal.hotfix_full(mod)

woodblocks_bal = Balance.from_data(data, woodblocks_bal_name)
cat = woodblocks_bal.categories[7]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
woodblocks_bal.hotfix_full(mod)

nulpoint_bal = Balance.from_data(data, nulpoint_bal_name)
cat = nulpoint_bal.categories[7]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
nulpoint_bal.hotfix_full(mod)

mod.close()