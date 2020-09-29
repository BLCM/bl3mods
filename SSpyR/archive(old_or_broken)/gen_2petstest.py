from bl3hotfixmod import Mod 

mod=Mod('2petstest.txt',
'FL4K 2 Pets',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Test')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPBeastmasterComponent.BPBeastmasterComponent_C',
'CharacterSlots',
"""
(
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/PlayerSlot_Pet.PlayerSlot_Pet
    ),
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/PlayerSlot_Pet.PlayerSlot_Pet
    )
)
"""
)
mod.newline()

mod.comment('Test')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPBeastmasterComponent.BPBeastmasterComponent_C',
'PetSlotData',
"""
(
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/PlayerSlot_Pet.PlayerSlot_Pet
    ),
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/PlayerSlot_Pet.PlayerSlot_Pet
    )
)
"""
)
mod.newline()

mod.comment('Test')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/ActionSkill/ActionSkill_RakkAttack.ActionSkill_RakkAttack',
'SupportedAugmentSlots',
"""
(
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Slots/AugmentSlot_Skill1_Mod1.AugmentSlot_Skill1_Mod1
    ),
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Slots/AugmentSlot_Skill1_Mod2.AugmentSlot_Skill1_Mod2
    ),
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill1_RakkAttack/Slots/AugmentSlot_Skill1_Mod1.AugmentSlot_Skill1_Mod1
    )
)
"""
)
mod.newline()