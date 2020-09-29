from bl3hotfixmod import Mod  

#Boom Enhance buff?

mod=Mod('god_clone.bl3hotfix',
'God Clone',
'SSpyR',
[
    'Makes Clone actually do some good Damage.',
    'Also why have a swap cooldown?',
    'And making Doppelbanger ridic cause why not.'
],
lic=Mod.CC_BY_SA_40,
cats='cheat, joke'
)

mod.comment('Reducing Clone cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'DigiClone_Cooldown',
'Value',
'(BaseValueConstant=0.00)'
)
mod.newline()

mod.comment('Increasing Clone duration')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'DigiClone_Duration',
'Value',
'(BaseValueConstant=75.00)'
)
mod.newline()

mod.comment('Increasing Clone health')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'DigiClone_HealthScalar',
'Value',
'(BaseValueConstant=180.00)'
)
mod.newline()

mod.comment('Adjusting swap cooldown')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'DigiClone_SwapPlacesCooldown',
'Value',
'(BaseValueConstant=0.10)'
)
mod.newline()

mod.comment('Buffing Double Barrel damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'DoubleBarrel_GunDamage',
'Value',
'(BaseValueConstant=700.00)'
)
mod.newline()

mod.comment('Decreasing time to proc Doppelbanger')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'PanicButton_FuseTime',
'Value',
'(BaseValueConstant=0.50)'
)
mod.newline()

mod.comment('Buffing minimum damage of Doppelbanger')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'PanicButton_MinDamage',
'Value',
'(BaseValueConstant=999.00)'
)
mod.newline()

mod.comment('Buffing maximum damage of Doppelbanger')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Operative/DataTable_Operative_ConstantValues',
'PanicButton_MaxDamage',
'Value',
'(BaseValueConstant=9999.00)'
)
mod.newline()

mod.comment('Buffing Clone damage')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_Player_Scalar_Constants',
'SkillDamage_Operative',
'Scaler_6_5C32556442B4DA4D7EAE1A8610E0A950',
9999.00
)
mod.newline()

mod.close()