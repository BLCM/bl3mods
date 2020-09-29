from bl3hotfixmod import Mod 


mod=Mod('skill_replacement_test.txt',
'Skill Replacement Test',
'SSpyR',
[
    'Test mod to see if I can rearrange skills.'
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Test')
mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..Items.Items[0].Object..AbilityClass',
            Mod.get_full_cond('/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/MatchedSet/Passive_Gunner_MatchedSet.Passive_Gunner_MatchedSet_C', 'BlueprintGeneratedClass'))

#mod.reg_hotfix(Mod.PATCH, '',
#            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
#            'Tiers.Tiers[1].Object..Items.Items[0].Object..ItemFrameName',
#            'matchingSet')

mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..Items.Items[1].Object..AbilityClass',
            Mod.get_full_cond('/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/MatchedSet/Passive_Gunner_MatchedSet.Passive_Gunner_MatchedSet_C', 'BlueprintGeneratedClass'))

#mod.reg_hotfix(Mod.PATCH, '',
#            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
#            'Tiers.Tiers[1].Object..Items.Items[1].Object..ItemFrameName',
#            'matchingSet')

mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
            'Tiers.Tiers[1].Object..Items.Items[1].Object..AbilityClass',
            Mod.get_full_cond('/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/RootToRise/PassiveSkill_Siren_RootToRise.PassiveSkill_Siren_RootToRise_C', 'BlueprintGeneratedClass'))

#mod.reg_hotfix(Mod.PATCH, '',
#            '/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag',
#            'Tiers.Tiers[1].Object..Items.Items[1].Object..ItemFrameName',
#            'rootsToRise')

mod.reg_hotfix(Mod.PATCH, '',
            '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
            'Tiers.Tiers[1].Object..Items.Items[1].Object..ItemFrameName',
            '(/Game/PlayerCharacters/Gunner/_Shared/_Design/Character/Inventory/AbilityTree_Branch_BottomlessMag.Tiers.Tiers[1].Object..Items.Items[1].Object..ItemFrameName)')

mod.close()


mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl',
'Tiers.Tiers[0].Object..Items.Items[0].Object..AugmentData',
Mod.get_full_cond('/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill2_Cloak/ActionSkill/ActionSkill_Cloak.ActionSkill_C', 'BlueprintGeneratedClass')
)
mod.newline()

mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Phasetrance/ActionSkill/ActionSkillSlot_Siren_AttackComponent',
'SupportedAugments.SupportedAugments[0]',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/ActionSkills/Skill2_Cloak/ActionSkill/ActionSkill_Cloak.ActionSkill_C'
)