#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

scale_pistol = 0.5
scale_shotgun = 0.4
scale_smg = 0.5
scale_sniper = 0
scale_heavy = 0.5

mod = Mod('maliwan_charge_time.txt',
        'Buffed Maliwan Charge Times',
        [
            'Reduces the charge time for most Maliwan guns.  Notable exceptions at the moment',
            'are all pistols: the unique gun "Starkiller," and the generic Maliwan Atomizers',
            'and Melters.  Those seem to use unique timing mechanisms which nothing else uses.',
            '',
            "Note that it's possible that any gun whose damage depends on charge time could",
            '*possibly* be nerfed by this, if the damage is based on time and not charge',
            "percent.  I think they're probably fine but have not tested it.",
            '',
            'Pistol Scaling: {:d}% (except Starkiller, Atomizers, and Melters)'.format(int(scale_pistol*100)),
            'Shotgun Scaling: {:d}%'.format(int(scale_shotgun*100)),
            'SMG Scaling: {:d}%'.format(int(scale_smg*100)),
            'Sniper Scaling: {:d}%'.format(int(scale_sniper*100)),
            #'',
            #"Also (possibly) buffs the charge time for the ION CANNON, even though it's a Vladof gun.",
        ],
        'MaliwanCharge',
        )

def charge_time(mod,
        obj_name,
        new_val,
        final_attr='ChargeTime',
        prev_val=None,
        aspect_list=1,
        aspect_attr='Component_BPWeaponChargeComponent_MAL',
        ):
    if prev_val is None:
        prev_val = ''
    else:
        prev_val = '(BaseValue={:.6f})'.format(prev_val)
    mod.reg_hotfix(Mod.PATCH, '',
            '{}:AspectList_WeaponUseModeSecondaryAspectData.{}'.format(obj_name, aspect_attr),
            'AspectList.AspectList[{}].Object..Component.Object..{}'.format(aspect_list, final_attr),
            '(BaseValue={:.6f})'.format(new_val),
            prev_val=prev_val)

# Put in our improvements
mod.header('Generic Weapons')
for (label, obj_name, default, scale) in [
        ('Pistol: Blaster',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_MAL_Barrel_03.Part_PS_MAL_Barrel_03',
            0.7,
            scale_pistol),
        ('Shotgun: Terminator',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_MAL_Barrel_01.Part_SG_MAL_Barrel_01',
            0.7,
            scale_shotgun),
        ('Shotgun: Shockwave',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_MAL_Barrel_02.Part_SG_MAL_Barrel_02',
            1.05,
            scale_shotgun),
        ('Shotgun: Cyclotron',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_MAL_Barrel_03.Part_SG_MAL_Barrel_03',
            0.9,
            scale_shotgun),
        ('SMG: Pulsar',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_MAL_Barrel_01.Part_SM_MAL_Barrel_01',
            0.75,
            scale_smg),
        ('SMG: Nebula',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SM_MAL_Barrel_02.Part_SM_MAL_Barrel_02',
            0.85,
            scale_smg),
        ('SMG: Quasar',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SM_MAL_Barrel_03.Part_SM_MAL_Barrel_03',
            1.0,
            scale_smg),
        ('Sniper Rifle: Multiplex',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01',
            1.1,
            scale_sniper),
        ('Sniper Rifle: Particle Rifle',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02',
            0.9,
            scale_sniper),
        ('Sniper Rifle: Proton Rifle',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03',
            1.75,
            scale_sniper),
        ]:
    mod.comment('{} (default: {})'.format(label, default))
    charge_time(mod, obj_name, default*scale)
    mod.newline()

mod.header('Legendaries/Uniques')
for label, obj_name, default, scale in [
        ('Cloud Kill',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill.Part_SM_MAL_Barrel_CloudKill',
            0.8,
            scale_smg),
        ('Crit',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Barrel_Crit.Part_SM_MAL_Barrel_Crit',
            0.75,
            scale_smg),
        ('Cutsman',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Barrel_Cutsman.Part_SM_MAL_Barrel_Cutsman',
            1.0,
            scale_smg),
        ('Destructo Spinner',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Barrel_DestructoSpin.Part_SM_MAL_Barrel_DestructoSpin',
            0.5,
            scale_smg),
        ('E-Gone',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Barrel_Egon.Part_SM_MAL_Barrel_Egon',
            0.85,
            scale_smg),
        ("Ember's Purge",
            '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Parts/Part_SM_MAL_Barrel_EmbersPurge.Part_SM_MAL_Barrel_EmbersPurge',
            0.75,
            scale_smg),
        ("The Emperor's Condiment",
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer.Part_SM_MAL_Barrel_Emporer',
            0.85,
            scale_smg),
        ('Firestorm',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_FireStorm.Part_MAL_SR_Barrel_FireStorm',
            1.0, # pre-GBX-hotfix value: 1.75
            scale_sniper),
        ('Hellshock',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock.Part_PS_MAL_Barrel_HellShock',
            0.8,
            scale_pistol),
        ('ION LASER',
            '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Parts/Part_SM_MAL_Barrel_IonLaser.Part_SM_MAL_Barrel_IonLaser',
            0.45,
            scale_smg),
        ("Kill-o'-the-Wisp",
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Barrel_Wisp.Part_SG_MAL_Barrel_Wisp',
            1.0,
            scale_shotgun),
        ('Krakatoa',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Parts/Part_MAL_SR_Barrel_Krakatoa.Part_MAL_SR_Barrel_Krakatoa',
            1.0,
            scale_sniper),
        ("Kyb's Worth",
            '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Parts/Part_SM_MAL_Barrel_KybsWorth.Part_SM_MAL_Barrel_KybsWorth',
            0.85,
            scale_smg),
        ("Miss Moxxi's Vibra-Pulse",
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Barrel_VibraPulse.Part_SM_MAL_Barrel_VibraPulse',
            1.15,
            scale_smg),
        ('P2P Networker',
            '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Parts/Part_SM_MAL_Barrel_Link.Part_SM_MAL_Barrel_Link',
            0.85,
            scale_smg),
        ('Projectile Recursion',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Parts/Part_SG_MAL_Barrel_Recursion.Part_SG_MAL_Barrel_Recursion',
            1.0,
            scale_shotgun),
        ('Shrieking Devil',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Parts/Part_SG_MAL_Barrel_Shriek.Part_SG_MAL_Barrel_Shriek',
            2.0,
            scale_shotgun),
        ('Soleki Protocol',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Parts/Part_MAL_SR_Barrel_Soleki.Part_MAL_SR_Barrel_Soleki',
            1.25,
            scale_sniper),
        ('Storm',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_Storm.Part_MAL_SR_Barrel_Storm',
            1.0, # pre-GBX-hotfix value: 2.0
            scale_sniper),
        ('Tsunami',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Barrel_Tsunami.Part_SM_MAL_Barrel_Tsunami',
            0.8,
            scale_smg),
        ("Vosk's Deathgrip",
            '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Barrel_DeathGrip.Part_SG_MAL_Barrel_DeathGrip',
            0.9,
            scale_shotgun),
        ]:
    mod.comment('{} (default: {})'.format(label, default))
    charge_time(mod, obj_name, default*scale)
    mod.newline()

# This doesn't seem to actually do the trick, and I don't care enough to track
# it down.  Was technically out-of-place anyway.
#mod.header('Non-Maliwan Weapons')
#for label, obj_name, aspect_attr, aspect_idx, default, scale in [
#        ('ION CANNON (Vladof Heavy Weapon)',
#            '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Parts/Part_HW_VLA_Barrel_IonCannon.Part_HW_VLA_Barrel_IonCannon',
#            'Component_WeaponChargeComponent',
#            7,
#            2,
#            scale_heavy),
#        ]:
#    mod.comment('{} (default: {})'.format(label, default))
#    charge_time(mod, obj_name, default*scale, aspect_list=aspect_idx, aspect_attr=aspect_attr)
#    mod.newline()

# No idea why these don't work...
#mod.comment('Pistol Tests...')
#for obj_name, new_val in [
#        ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_MAL_Barrel_01.Part_PS_MAL_Barrel_01', 5),
#        ('/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_MAL_Barrel_02.Part_PS_MAL_Barrel_02', 10),
#        ]:
#    charge_time(mod, obj_name, new_val)
#mod.newline()

# Read below for a very labor-intensive way to glean the default values, in the
# absence of an in-game console, or other introspection methods!  It's... fun?
#
# (no, it's not, really)
#
# This method is quite obsolete now that we've discovered JohnWickParse, which
# doesn't serialize *all* the Barrel part data, but does serialize enough that
# you can get the value right from the JSON file.  Leaving it in just out of
# some weird nostalgia, but JWP is the way to go.

# Figuring out defaults by basically doing set_cmp on a wide range of possible values,
# setting the new value to some obviously-distinct times.  I used 3-second intervals
# so that any timing errors or whatever would be entirely negligible.  I'd done
# initial manual times for the vanilla guns, so I had a pretty reasonable idea about
# the start range to try, though in the end I had to do a second pass to widen up
# the "from" values a bit more, for half of 'em.
#for (label, part, start) in [
#        # First pass...
#        #('pistol3', '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_MAL_Barrel_03.Part_PS_MAL_Barrel_03', 0.5),
#        #('shotty1', '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_MAL_Barrel_01.Part_SG_MAL_Barrel_01', 0.9),
#        #('shotty2', '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_MAL_Barrel_02.Part_SG_MAL_Barrel_02', 1.15),
#        #('shotty3', '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_MAL_Barrel_03.Part_SG_MAL_Barrel_03', 1.0),
#        #('smg1', '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_MAL_Barrel_01.Part_SM_MAL_Barrel_01', 0.7),
#        #('smg2', '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SM_MAL_Barrel_02.Part_SM_MAL_Barrel_02', 0.9),
#        #('smg3', '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SM_MAL_Barrel_03.Part_SM_MAL_Barrel_03', 0.9),
#        #('sniper1', '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01', 1.2),
#        #('sniper2', '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02', 0.8),
#        #('sniper3', '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03', 1.7),
#
#        # Second pass... (got 'em!)
#        #('shotty1', '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_MAL_Barrel_01.Part_SG_MAL_Barrel_01', 0.7),
#        #('shotty2', '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_MAL_Barrel_02.Part_SG_MAL_Barrel_02', 1.0),
#        #('shotty3', '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_MAL_Barrel_03.Part_SG_MAL_Barrel_03', 0.8),
#        #('smg2', '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SM_MAL_Barrel_02.Part_SM_MAL_Barrel_02', 0.7),
#        #('sniper1', '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01', 1.0),
#
#        # Legendaries/Uniques pass 1
#        #('Cloud Kill',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill.Part_SM_MAL_Barrel_CloudKill', 0.85),
#        #('Crit',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Barrel_Crit.Part_SM_MAL_Barrel_Crit', 0.70),
#        #('Cutsman',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Barrel_Cutsman.Part_SM_MAL_Barrel_Cutsman', 1.0),
#        #('Destructo Spinner',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Barrel_DestructoSpin.Part_SM_MAL_Barrel_DestructoSpin', 0.5),
#        #('E-Gone',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Barrel_Egon.Part_SM_MAL_Barrel_Egon', 0.70),
#        #("The Emperor's Condiment",
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer.Part_SM_MAL_Barrel_Emporer', 0.8),
#        #('Hellshock',
#        #    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock.Part_PS_MAL_Barrel_HellShock', 1.15),
#        #("Kill-o'-the-Wisp",
#        #    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Barrel_Wisp.Part_SG_MAL_Barrel_Wisp', 1.15),
#        #('Krakatoa',
#        #    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Parts/Part_MAL_SR_Barrel_Krakatoa.Part_MAL_SR_Barrel_Krakatoa', 0.8),
#        #("Miss Moxxi's Vibra-Pulse",
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Barrel_VibraPulse.Part_SM_MAL_Barrel_VibraPulse', 1.0),
#        #('Projectile Recursion',
#        #    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Parts/Part_SG_MAL_Barrel_Recursion.Part_SG_MAL_Barrel_Recursion', 0.9),
#        #('Shrieking Devil',
#        #    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Parts/Part_SG_MAL_Barrel_Shriek.Part_SG_MAL_Barrel_Shriek', 1.95),
#        #('Soleki Protocol',
#        #    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Parts/Part_MAL_SR_Barrel_Soleki.Part_MAL_SR_Barrel_Soleki', 1.2),
#        #('Tsunami',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Barrel_Tsunami.Part_SM_MAL_Barrel_Tsunami', 0.75),
#
#        # Legendaries/Uniques pass 2
#        #('Hellshock',
#        #    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock.Part_PS_MAL_Barrel_HellShock', 0.85),
#        #('Cloud Kill',
#        #    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill.Part_SM_MAL_Barrel_CloudKill', 0.7),
#        #("Kill-o'-the-Wisp",
#        #    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Barrel_Wisp.Part_SG_MAL_Barrel_Wisp', 0.95),
#
#        # Legendaries/Uniques pass 3
#        #('Hellshock',
#        #    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock.Part_PS_MAL_Barrel_HellShock', 0.7),
#
#        ### Maliwan Takedown / Mayhem 4 Gear
#        #("Kyb's Worth",
#        #    '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Parts/Part_SM_MAL_Barrel_KybsWorth.Part_SM_MAL_Barrel_KybsWorth', 0.6),
#        #('P2P Networker',
#        #    '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Parts/Part_SM_MAL_Barrel_Link.Part_SM_MAL_Barrel_Link', 0.8),
#        #("Vosk's Deathgrip",
#        #    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Barrel_DeathGrip.Part_SG_MAL_Barrel_DeathGrip', 0.5),
#
#        # Take 2.
#        ("Vosk's Deathgrip",
#            '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Barrel_DeathGrip.Part_SG_MAL_Barrel_DeathGrip', 0.8),
#        ]:
#    mod.comment(label)
#    prev_val = start
#    new_val = 3
#    steps = 0
#    while steps < 7:
#        charge_time(mod,
#                part,
#                new_val,
#                prev_val=prev_val,
#                )
#        steps += 1
#        new_val += 3
#        prev_val += 0.05
#    mod.newline()

mod.close()
