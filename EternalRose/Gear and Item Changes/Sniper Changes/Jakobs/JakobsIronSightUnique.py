import sys
import collections
sys.path.append('../../../../python_mod_helpers')
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod, Balance

mod = Mod('jakobsironsightunique.bl3hotfix',
        'Jakobs Snipers Iron Sight Change',
        'Eternal Rose',
        [
            "Allowing all Unique Jakobs to drop without a scope, thus being Iron Sighted.",
        ],
        contact='https://github.com/RoseEternal',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gear-general',
        )
        
# These are the Unique Snipers that Jakobs have in-game. The Monocle is absent since it's Barrel is the scope for the weapon.
# So getting rid of the scope will still present to a visible scope while ADS'ing with the Monocle. 
        
icequeen_bal_name = '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen'
        
headsplosion_bal_name = '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion'
        
birdofprey_bal_name = '/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/BirdofPrey/Balance/Balance_SR_JAK_BirdofPrey'
        
fixedbirdofprey_bal_name = '/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/BirdofPrey/Balance/Balance_SR_JAK_BirdofPrey_FixedParts'
        
disruptor_bal_name = '/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Disruptor/Balance/Balance_SR_JAK_Disruptor'

wedding_bal_name = '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite'

# Parts is for directing the game "here's where I want the part" and the Category makes a new "None" sniper scope. 
        
parts = [
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Scope',
        ]
        
category = [
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Parts/Scope/None'
        ]

# Add the parts one by one

data = BL3Data()
icequeen_bal = Balance.from_data(data, icequeen_bal_name)
cat = icequeen_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
icequeen_bal.hotfix_full(mod)

headsplosion_bal = Balance.from_data(data, headsplosion_bal_name)
cat = headsplosion_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
headsplosion_bal.hotfix_full(mod)

birdofprey_bal = Balance.from_data(data, birdofprey_bal_name)
cat = birdofprey_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
birdofprey_bal.hotfix_full(mod)

fixedbirdofprey_bal = Balance.from_data(data, fixedbirdofprey_bal_name)
cat = fixedbirdofprey_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
fixedbirdofprey_bal.hotfix_full(mod)

disruptor_bal = Balance.from_data(data, disruptor_bal_name)
cat = disruptor_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
disruptor_bal.hotfix_full(mod)

wedding_bal = Balance.from_data(data, wedding_bal_name)
cat = wedding_bal.categories[6]
cat.enabled = True
for parts in category:
    cat.add_part_name(parts)
wedding_bal.hotfix_full(mod)

mod.close()