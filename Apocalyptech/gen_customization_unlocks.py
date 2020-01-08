#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('customization_unlocks.txt',
        'Customization Unlocks',
        [
            "Various cosmetic items are locked to specific DLC-like requirements,",
            "such as preordering the game, or buying one of the deluxe or super",
            "deluxe editions of the game.  This removes those restrictions so the",
            "related skins are usable.",
            "",
            "Note that this isn't at all helpful unless you get the relevant",
            "customization items to spawn in your game, so you can add them to",
            "your profile.  Either add them in to my expanded_customization_pools",
            "mod, or spawn them directly using testing_loot_drops (you'll have to",
            "edit the Python generation scripts, in either case).",
            "",
            "Once activated in your profile, the cosmetics will remain there even",
            "if you launch the game without this mod enabled, but you won't have",
            "access to them until you re-enable this mod.  You don't have to worry",
            "about re-dropping them, though, because they remain in the profile.",
        ],
        'CustomPools',
        )

for (label, locked_bals) in sorted([

        ('Retro Pack (Deluxe Edition)', [
            # Skins, Heads, Weapon Skin, ECHO Skin
            '/Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_34.InvBal_CustomSkin_Beastmaster_34',
            '/Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_34.InvBal_CustomSkin_Gunner_34',
            '/Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_34.InvBal_CustomSkin_Operative_34',
            '/Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_34.InvBal_CustomSkin_Siren_34',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_28.InvBal_CustomHead_Beastmaster_28',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_28.InvBal_CustomHead_Gunner_28',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_28.InvBal_CustomHead_Operative_28',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_28.InvBal_CustomHead_Siren_28',
            '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_23.InvBal_WeaponSkin_23',
            '/Game/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_12.InvBal_ECHOTheme_12',
            ]),

        ('Neon Pack (Deluxe Edition)', [
            # Skins, Heads, Trinket, ECHO Skin
            '/Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_35.InvBal_CustomSkin_Beastmaster_35',
            '/Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_35.InvBal_CustomSkin_Gunner_35',
            '/Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_35.InvBal_CustomSkin_Operative_35',
            '/Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_35.InvBal_CustomSkin_Siren_35',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/Beastmaster/Heads/CustomHead_Beastmaster_29.InvBal_CustomHead_Beastmaster_29',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/Gunner/Heads/CustomHead_Gunner_29.InvBal_CustomHead_Gunner_29',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/Operative/Heads/CustomHead_Operative_29.InvBal_CustomHead_Operative_29',
            '/Game/PatchDLC/Customizations/PlayerCharacters/_Customizations/SirenBrawler/Heads/CustomHead_Siren_29.InvBal_CustomHead_Siren_29',
            '/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_52.InvBal_WeaponTrinket_52',
            '/Game/PlayerCharacters/_Customizations/EchoDevice/ECHOTheme_13.InvBal_ECHOTheme_13',
            ]),

        ('Gold Pack (Preorders)', [
            # Weapon Skin, Trinket
            '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_21.InvBal_WeaponSkin_21',
            '/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_51.InvBal_WeaponTrinket_51',
            ]),

        ('Gearbox Pack (Deluxe Edition)', [
            # Weapon Skin, Trinket
            '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_22.InvBal_WeaponSkin_22',
            '/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_54.InvBal_WeaponTrinket_54',
            ]),

        ('Butt Stallion Pack (Super Deluxe Edition)', [
            # Weapon Skin, Trinket
            '/Game/Gear/WeaponSkins/_Design/SkinParts/WeaponSkin_24.InvBal_WeaponSkin_24',
            '/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_53.InvBal_WeaponTrinket_53',
            ]),

        ('Toy Box Pack (Deluxe Edition)', [
            # Trinket
            '/Game/Gear/WeaponTrinkets/_Design/TrinketParts/WeaponTrinket_58.InvBal_WeaponTrinket_58',
            ]),

        ]):

    mod.comment(label)
    for locked_bal in locked_bals:
        mod.reg_hotfix(Mod.PATCH, '',
                locked_bal,
                'DlcInventorySetData',
                'None')
    mod.newline()

mod.close()
