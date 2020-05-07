#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('mayhem2_modifier_nerfs.txt',
        'Mayhem 2.0: Various Modifier Nerfs',
        [
            "Applying some nerfs to Mayhem 2.0 modifiers that I enjoy, but wish",
            "were a little less intrusive.  Cheaty!  Though the Lootsplosion",
            "modifier change is technically *against* the player rather than for.",
        ])

mod.header('Actual Stat Changes')

infusion_pct = 0.25
infusion_rpt = int(infusion_pct*100)

switcheroo_scale = -0.02
switcheroo_rpt = int(abs(switcheroo_scale*100))

ticked_scale = 0.3
ticked_rpt = int((1-ticked_scale)*100)

critfail_scale = 0.5
critfail_rpt = int((1-critfail_scale)*100)

holycrit_noncrit_scale = 0.65
holycrit_noncrit_rpt = int((1-holycrit_noncrit_scale)*100)
holycrit_crit_scale = 1.35
holycrit_crit_rpt = int((holycrit_crit_scale-1)*100)

for label, values in sorted([
        ('Lootspolosion - Cut lootsplosion item quantity in half', [
            # Default value: 15 - there's just too much loot at default levels!
            ('PartyTime_Quantity', 8),
            ]),
        ('Post Mortem - Reduce DEATH health a bit', [
            # Default value: 5
            ('DeathFromBeyond_Health', 3.5),
            ]),
        ('Dazed and Infused / Charred Mode / High Voltage / Acid Reign / Chilling Them Softly / Totally Radical - damage reduction instead of total invuln.', [
            # Default value: 0
            ('ElementalInfusionDamageTaken', infusion_pct),
            ]),
        ('Floor is Lava - add a bit more wiggle room to the timing', [
            # Default value: 0.25
            ('FloorIsLava_CheckTime', 0.5),
            ]),
        ('Pain Tolerance - reduce damage reduction a bit', [
            # Default value: -0.03
            ('OlSwitcheroo_Resistance', switcheroo_scale),
            ]),
        ('Boundary Issues - nerf beam damage a bit', [
            # Default value: 0.025
            ('StayBack_BeamDamage', 0.015),
            ]),
        ('Ticked Off - reduce damage resistance', [
            # Default value: 0.1
            ('BegoneDot_Resistance', ticked_scale),
            ]),
        ('Not the Face - reduce crit damage reduction', [
            # Default value: 0.25
            ('CriticalFailure_Resistance', 0.5),
            ]),
        ('Holy Crit - reduce non-crit nerf, buff crit a bit further', [
            # Default value: 0.5
            ('Sharpshot_NonCrit_Penalty', holycrit_noncrit_scale),
            # Default value: 1.25
            ('Sharpshot_CritBonus', holycrit_crit_scale),
            ]),
        ]):
    mod.comment(label)
    for (row, value) in values:
        mod.table_hotfix(Mod.EARLYLEVEL, 'MatchAll',
                '/Game/PatchDLC/Mayhem2/Abilities/_Shared/Balance/Table_Mayhem2Abilities_ConstantValues',
                row,
                'Base_17_28B25EC8493D1EB6C2138A962F659BCD',
                value)
    mod.newline()

# These *could* be coupled in with the stat changes above, but for the Elemental
# Infusion ones we'd have multiple objects, and it hardly seems worth it.
mod.header('Text Updates')

for obj_name, desc in [
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_All',
            'Enemies may be infused with a random element. Infused enemies only take {}% damage from that element and release a Nova when killed.'.format(infusion_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_Corrosive',
            'Enemies may be infused with Corrosive. Infused enemies only take {}% damage from Corrosive damage and release a Corrosive Nova when killed.'.format(infusion_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_Cryo',
            'Enemies may be infused with Cryo. Infused enemies only take {}% damage from Cryo damage and release a Cryo Nova when killed.'.format(infusion_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_Fire',
            'Enemies may be infused with Incendiary. Infused enemies only take {}% damage from Incendiary damage and release an Incendiary Nova when killed.'.format(infusion_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_Radiation',
            'Enemies may be infused with Radiation. Infused enemies only take {}% damage from Radiation damage and release a Radiation Nova when killed.'.format(infusion_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_ElementalInfusion_Shock',
            'Enemies may be infused with Shock. Infused enemies only take {}% damage from Shock damage and release a Shock Nova when killed.'.format(infusion_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_OlSwitcheroo',
            'When damaged, enemies gain {}% Damage Reduction against the type of damage received for 3 seconds. This effect can stack up to 20 times.'.format(switcheroo_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Enemies/ModUiStat_Mayhem2_Enemies_BegoneDot',
            'Status Effect Damage against enemies is reduced by {}%. Maliwan\'s not gonna like this...'.format(ticked_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Players/ModUiStat_Mayhem2_Players_CriticalFailure',
            'Critical Hit Damage is reduced by {}%. Some people are just hard-headed...'.format(critfail_rpt)),
        ('/Game/PatchDLC/Mayhem2/ModifierSets/UI/Players/ModUiStat_Mayhem2_Players_Sharpshot',
            'I can dance all day! Critical Hit Damage is increased by {}%, but Non-Critical Hit Damage is reduced by {}%.'.format(holycrit_crit_rpt, holycrit_noncrit_rpt)),
        ]:
    mod.reg_hotfix(Mod.PATCH, '',
            obj_name,
            'Description',
            desc)

mod.close()
