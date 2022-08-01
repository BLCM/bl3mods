#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import math
import enum
import argparse
from bl3data.bl3data import BL3Data

# Known TODO:
#  - Have not figured out how to get to sniper zoom levels
#  - Reload times!  For instance the three Jakobs Magazines Part_PS_JAK_Mag_01 through 03...
#    01 + 02 use the default (which is apparently ~2.5) but 03 specifies 1.75.  Would need
#    to know the defaults.
#  - Jakobs ricochet stats; for instance WeaponUseComponent_BPWeaponFireProjectileComponent_JAK in Part_PS_JAK_Barrel_GodMother
#  - Non-weapon parts haven't even been tried yet

# Also, I kind of just stopped working on this after awhile, so now that I'm
# checking it in, I'm not really sure how well it was working or not.  Use
# at your own risk!  (Not that it'd break anything, might just not work very
# well.)

data = BL3Data()

class ModType(enum.Enum):
    OverrideBaseValue = 'OverrideBaseValue'
    PreAdd = 'PreAdd'
    PostAdd = 'PostAdd'
    Scale = 'Scale'
    ScaleSimple = 'ScaleSimple'
    # This one's a bit of tomfoolery I'm putting in myself, for Reasons.
    Report = 'Report'

class BaseAttribute:
    """
    Basic class to hold info about an attribute modification.  Just the attr path and
    modification method (which should be Simple, ScaleSimple, etc...)
    """

    def __init__(self, attribute, mod_type):
        self.attribute = attribute
        if type(mod_type) == str:
            self.mod_type = ModType[mod_type]
        else:
            self.mod_type = mod_type
        self.reset_attrs = False
        self.use_mode = None

class WBCAttribute(BaseAttribute):
    """
    An Attribute modification which comes from a WBC object.  These have a bunch of info
    read in while we process the WBC, and then we later read out the exact values based
    on info we're getting elsewhere (so no "value" ever gets stored in here, since it's
    more of a general-purpose window into getting attributes from a source, rather than
    a specific attribute itself).
    """

    def __init__(self, wbc, data, table):
        super().__init__(data['Attribute'][1], data['ModifierType'].split('::')[-1])
        self.wbc = wbc
        self.data = data
        self.table = table
        self.name = data['ColumnName']
        self.resolver_export = data['DataTableAttributeValueResolver']['export']
        self.resolver = self.wbc.obj[self.resolver_export-1]
        assert(self.resolver['DataTableRow']['DataTable'][1] == self.wbc.table_name)
        self.parent_column = self.resolver['DataTableColumn']
        if 'ParsedPath' in self.resolver['Property']:
            self.column = self.resolver['Property']['ParsedPath']['PropertyName']
        else:
            self.column = None

class RegularAttribute(BaseAttribute):
    """
    A "regular" attribute which contains all the info about values and stuff, inside
    a BVC struct.
    """

    def __init__(self, bl3data, data, reset_attrs=False, use_mode=None):
        super().__init__(data['AttributeToModify'][1], data['ModifierType'].split('::')[-1])
        self.reset_attrs = reset_attrs
        self.use_mode = use_mode
        self.data = data
        # Hardcoding a special-case here - Dahl Burst-Fire Rate attribute
        # modifications alter the current firerate, which is looked up via
        # a BVC struct which contains an `AttributePropertyValueResolver`,
        # which our BVC processing can't cope with (since it relies heavily
        # on context).  But we'll go ahead and process it "manually" here,
        # since the important bit in these cases is the BaseValueScale.
        if ((self.attribute == '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_BurstFireRate' 
                or self.attribute == '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_SemiFireRate')
                and self.mod_type == ModType.OverrideBaseValue):
            self.mod_type = ModType.ScaleSimple
            self.value = data['ModifierValue']['BaseValueScale']
        else:
            self.value = bl3data.process_bvc_struct(data['ModifierValue'])

class ReportAttribute(BaseAttribute):
    """
    A "report" attribute that we're sort of making up ourselves.  This is for
    cases where we don't have an actual *number* to report, but rather some
    text that we've hardcoded here in the app.
    """

    def __init__(self, attr_name, value, reset_attrs=False, use_mode=None):
        super().__init__(attr_name, ModType.Report)
        self.value = value
        self.reset_attrs = reset_attrs
        self.use_mode = None

class ModifiedAttr:
    """
    Class to store an aggregate amount of info about a single attribute, which
    might be getting modified by any number of WBCAttributes or RegularAttributes
    """

    def __init__(self, name, use_mode=None):
        self.name = name
        self.use_mode = use_mode
        self.bases = []
        self.preadds = []
        self.postadds = []
        self.scales = []
        self.scalesimples = []
        self.reports = []
        self.has_reset = False
        self.modes = {}
        self.map = {
                ModType.OverrideBaseValue: self.bases,
                ModType.PreAdd: self.preadds,
                ModType.PostAdd: self.postadds,
                ModType.Scale: self.scales,
                ModType.ScaleSimple: self.scalesimples,
                ModType.Report: self.reports,
                }

    def add(self, new_attr, value=None):

        # Create a sub-attr for the specific use mode, if applicable
        if self.use_mode is None and new_attr.use_mode is not None:
            if new_attr.use_mode not in self.modes:
                self.modes[new_attr.use_mode] = ModifiedAttr(self.name, use_mode=new_attr.use_mode)
            self.modes[new_attr.use_mode].add(new_attr, value)
            return

        # Attributes which come in with bResetAttributes=True don't seem to pay
        # attention to order; or at least if there's a bResetAttributes=True in
        # an earlier AspectList entry, it seems to overwrite attribute
        # modifications even if they appear *later* in the AspectList.  It
        # could be that there's cases where this isn't true, but ehhh..
        # TODO: Figure out if that's the case.  :D
        if self.has_reset:
            return

        # If the new attr is resetting, do that.
        if new_attr.reset_attrs:
            self.has_reset = True
            self.bases.clear()
            self.preadds.clear()
            self.postadds.clear()
            self.scales.clear()
            self.scalesimples.clear()
            self.reports.clear()

        # Finally, store the value
        mod_type = new_attr.mod_type
        if value is None:
            if type(new_attr) != WBCAttribute:
                value = new_attr.value
            else:
                return
        self.map[new_attr.mod_type].append(value)

    def get_reports(self):
        """
        Get the total processed reports for this part.  Returns a list of tuples, where
        the first element is the mode number (might be `None`) and the second is the
        text to report.
        """
        # FINAL = (BASE + [sum of PreAdd]) × (1 + [sum of positive Scale])÷(1 - [sum of negative Scale]) × [product of ScaleSimple] + [sum of PostAdd]
        to_ret = []
        for base in self.bases:
            # no idea what precedence would be if more than one base override happened
            to_ret.append('{:g}'.format(base))
        if self.preadds:
            to_ret.append('+{} (pre)'.format(sum(self.preadds)))
        if self.postadds:
            to_ret.append('+{} (post)'.format(sum(self.postadds)))
        if self.scales or self.scalesimples:
            end_val = 1
            if self.scales:
                # for positive val, Scale is: *(1+x)
                # for negative val, Scale is: /(1-x)
                total_top = 0
                total_bottom = 0
                for scale in self.scales:
                    if val >= 0:
                        total_top += scale
                    else:
                        total_bottom += scale
                end_val *= ((1.0+total_top)/(1.0-total_bottom))
            if self.scalesimples:
                end_val *= math.prod(self.scalesimples)
            if end_val > 1:
                to_ret.append('+{:g}%'.format((end_val-1)*100))
            elif end_val < 1:
                to_ret.append('-{:g}%'.format(abs(end_val-1)*100))
            else:
                # Don't bother reporting if nothing's actually changed; this is
                # pretty common with initializations, etc.
                pass
        for report in self.reports:
            to_ret.append(report)

        if self.has_reset:
            # Just had this for debugging; for weapon parts, it looks like bResetAttributes
            # never actually affects the reported numbers, FWIW.
            #to_ret.append('bResetAttributes=True')
            # ... but it actually *might* make sense to include it in the report, regardless,
            # since the part might be in "conflict" with other parts.
            for idx in range(len(to_ret)):
                to_ret[idx] += ' (hard reset)'

        # This is dumb but whatever
        for idx in range(len(to_ret)):
            to_ret[idx] = (self.use_mode, to_ret[idx])

        # Report on child modes
        for use_mode, child in sorted(self.modes.items()):
            to_ret.extend(child.get_reports())

        return to_ret

class AttrCollection:
    """
    A collection of ModifiedAttr objects; also includes the code necessary
    to report on them.
    """

    # Keep in mind that after converting to english, entirely-identical report lines
    # will get "combined."  For instance, when seen together, it looks like
    # Att_Weapon_ReloadTime and Att_Weapon_TapedReloadTime are always equal -- if
    # both have the name `Reload Speed`, and the values are the same, it'll only
    # get reported once, even though the actual attribute is different.  (If the
    # values ever *diverge* with in a single part, though, both values would show
    # up.)
    attr_to_eng = {
            # More straightforward ones
            '/Game/GameData/Accuracy/Att_AccuracyOnIdleRegenerationRate': 'Idle Accuracy Regen',
            '/Game/GameData/Attributes/Character/Att_WeaponSwapSpeedScale': 'Weapon Swap Speed Timescale ????',
            '/Game/GameData/Attributes/DamageMultipliers/Att_DamageSourceInstigatorMultiplier_Melee': 'Melee Damage',
            '/Game/GameData/Weapons/Att_CriticalHitDamageBonus': 'Crit Damage',
            '/Game/GameData/Weapons/Att_Weapon_AutomaticBurstCount': 'Automatic Burst Count ????',
            '/Game/GameData/Weapons/Att_Weapon_ChargeTime': 'Charge Time',
            '/Game/GameData/Weapons/Att_Weapon_Damage': 'Damage',
            '/Game/GameData/Weapons/Att_Weapon_DamageRadius': 'Damage Radius',
            '/Game/GameData/Weapons/Att_Weapon_FireRate': 'Fire Rate',
            '/Game/GameData/Weapons/Att_Weapon_FireRateAccelDuration': 'Fire Rate Acceleration Duration',
            '/Game/GameData/Weapons/Att_Weapon_FireRateDecelDuration': 'Fire Rate Deceleration Duration',
            '/Game/GameData/Weapons/Att_Weapon_FireSequenceLength': 'Fire Sequence Length ????',
            '/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo': 'Max Loaded Ammo ????',
            '/Game/GameData/Weapons/Att_Weapon_MinFireRatePercentToFire': 'Min firerate percent to fire ????',
            '/Game/GameData/Weapons/Att_Weapon_ProjectileSpeedScale': 'Projectile Speed',
            '/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot': 'Projectiles',
            '/Game/GameData/Weapons/Att_Weapon_RecoilZoomScale': 'Zoom Recoil Scale ????',
            '/Game/GameData/Weapons/Att_Weapon_ResetFireSequenceCompletePercentage': 'Reset Fire Seq Complete Pct ????',
            '/Game/GameData/Weapons/Att_Weapon_ResetFireSequenceTime': 'Reset Fire Sequence Time ????',
            '/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost': 'Ammo Shot Cost',
            '/Game/GameData/Weapons/Att_Weapon_StatusEffectChance': 'Status Effect Chance',
            '/Game/GameData/Weapons/Att_Weapon_StatusEffectDamage': 'Status Effect Damage',
            '/Game/GameData/Weapons/Att_Weapon_SwitchModeTimeScale': 'Mode Switch Timescale ????',
            '/Game/GameData/Weapons/Att_Weapon_UseHeatImpulse': 'Heat Impulse',
            '/Game/GameData/Weapons/Att_Weapon_ZoomDOFNearRegion': 'Scope Zoom DOF',
            '/Game/GameData/Weapons/Att_Weapon_ZoomDurationScale': 'Zoom Duration Scale ????',
            '/Game/GameData/Weapons/Att_Weapon_ZoomFOVScale': 'Zoom FOV Scale ????',
            '/Game/GameData/Weapons/WeaponShield/Att_WeaponShield_Component_MaxValue': 'Weap. Shield Capacity',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Atlas/Attributes/Att_ATL_TrackerLifetime': 'Tracker Lifetime',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/COV/Attributes/Att_Cov_JankinessPerShot': 'Jankiness per Shot',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_RefundBullet': 'Refund Bullet',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_Ricochet': 'Ricochet',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_DamageRadius': 'Tediore Damage Radius ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Attributes/Att_TOR_ProjectileDamageScale': 'Projectile Damage',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Attributes/Att_TOR_ProjectilePerShot': 'Torgue Projectiles per Shot',

            # These two seen on Hellwalker...
            '/Game/GameData/Weapons/Att_Weapon_ActiveHeatRate': 'Active Heat Rate ????',
            '/Game/GameData/Weapons/Att_Weapon_GoreModifier': 'Gore Modifier ????',

            # Two separate reload ones?  What's up w/ "Taped" in there?
            '/Game/GameData/Weapons/Att_Weapon_ReloadTime': 'Reload Speed',
            '/Game/GameData/Weapons/Att_Weapon_TapedReloadTime': 'Reload Speed (taped) ????',

            # Burst Stuff
            '/Game/GameData/Weapons/Att_Weapon_BurstFireDelay': 'Burst Fire Delay',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_BurstFireRate': 'Burst Fire Rate',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_BurstSize': 'Burst Size',

            # Some Tediore stuff; have no idea what this might be
            # I suspect they must relate to the reload modes
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_TargetCombo': 'Tediore Target Combo ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_DamageScale': 'Tediore Damage Scale ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_Shooting': 'Tediore Shooting ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_MIRV': 'Tediore MIRV ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_NumMirvProjectiles': 'MIRV Projectiles',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_Stabilizer': 'Tediore Stabilizer ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_Homing': 'Tediore Homing ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_Sticky': 'Tediore Sticky ????',
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_Bouncy': 'Tediore Bouncy ????',
            # I suspect this one should be set to ignore, actually
            '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_CanTalk': 'Tediore Can Talk ????',

            # Torgue things; this one shows up on Echo and Hyde
            #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Attributes/Att_TOR_OverrideForcedDetonation': 'Override Forced Detonation ???',
            # This on Alchemist
            #'/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Attributes/Att_TOR_OverrideStickyDetonationMode': 'Override Sticky Detonation Mode',

            # Recoil
            '/Game/GameData/Weapons/Att_Weapon_RecoilWidthScale': 'Recoil Width',
            '/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale': 'Recoil Height',

            # Accuracy / Spread
            '/Game/GameData/Weapons/Att_Weapon_Spread': 'Weapon Spread',
            '/Game/GameData/Weapons/Att_Weapon_AccuracyImpulse': 'Accuracy Impulse',
            '/Game/GameData/Accuracy/Att_AccuracyMaxValue': 'Accuracy Max',

            # Sway
            '/Game/GameData/Weapons/Att_Weapon_SwayAccuracyScale': 'Firing Weapon Sway',
            '/Game/GameData/Weapons/Att_Weapon_SwayZoomAccuracyScale': 'ADS Firing Weapon Sway',
            '/Game/GameData/Weapons/Att_Weapon_SwayScale': 'Idle Sway',
            '/Game/GameData/Weapons/Att_Weapon_SwayZoomScale': 'ADS Idle Sway',
            '/Game/GameData/Weapons/Att_Weapon_SwaySpeed': 'Sway Speed',
            '/Game/GameData/Weapons/Att_Weapon_SwayDiscHeight': 'Sway Area Height',
            '/Game/GameData/Weapons/Att_Weapon_SwayDiscWidth': 'Sway Area Width',
            '/Game/GameData/Weapons/Att_Weapon_SwayMaxAccuracyPercent': 'Sway Max Accuracy Percent ????',
            }

    attr_to_ignore = set([
        # I think that these maybe just go into the whole NamingStrategy stuff?
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_CritDamage',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_ReloadSpeed',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_Damage',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_Handling',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_Accuracy',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_FireRate',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_ProjectileSpeed',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_HeatImpulse',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_ChargeTime',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/NameStats/Att_WeaponName_AreaDamage',

        # ???
        '/Game/GameData/Weapons/Att_Weapon_FireAnimationBlendSpace',

        # I thinks this might just be visual, related to reload?
        # Both show up in Part_SG_JAK_Barrel_01_B
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_BreakLoadShellAmount',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_UsesSequence',

        # This from Part_SG_JAK_Foregrip_01
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_PumpAction',

        # This from Part_SG_JAK_Mag_01
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_BreakAction',

        # Just denotes that something's E-tech?
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Tediore/Attributes/Att_TED_ETech',

        # Doesn't really matter; I think these are just internal housekeeping things?
        # Some of these might be nice to report on, honestly, like Jakobs pump/lever actions, CoV repair
        # style, etc...
        '/Game/GameData/Weapons/Att_Weapon_CustomSightColorScheme',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_MagType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_CustomA_PartType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_OverrideManufacturerDescription',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Grips/Att_Weapon_ForegripType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Grips/Att_Weapon_GripType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Grips/Att_Weapon_PistolStock',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Melee/Att_Weapon_MeleeStyle',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Reload/Att_Weapon_ReloadType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Scope/Att_ScopeType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_BarrelType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_CustomB_PartType',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/COV/Attributes/Att_Cov_StarterType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_HolsteredSizeType',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Projectiles/PS/Att_TOR_PS_HammerType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_ModeType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_BoltType',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_Weapon_TriggerType',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_LeverAction',
        '/Game/Gear/Weapons/_Shared/_Design/WeaponAttributes/Att_ModeSwitchType',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_PumpAction_Type',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Attributes/Att_TOR_ProjectileType',
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/COV/Attributes/Att_Cov_RepairStyle',
        ])

    def __init__(self):
        self.attrs = {}

    def add(self, new_attr, value=None):
        attr = new_attr.attribute
        if attr not in self.attrs:
            self.attrs[attr] = ModifiedAttr(attr)
        self.attrs[attr].add(new_attr, value)

    def report_to(self, reports):
        for attr_name, attr in self.attrs.items():
            if attr_name in self.attr_to_ignore:
                continue
            if attr_name in self.attr_to_eng:
                eng_name = self.attr_to_eng[attr_name]
            else:
                eng_name = attr_name
            for mode, report in attr.get_reports():
                if mode is None:
                    mode_prefix = ''
                    sort_prefix = 0
                elif mode == 1:
                    mode_prefix = '(Primary) '
                    sort_prefix = mode
                elif mode == 2:
                    mode_prefix = '(Secondary) '
                    sort_prefix = mode
                else:
                    raise RuntimeError('Unknown use mode: {}'.format(mode))
                reports.add((sort_prefix, '{}{}: {}'.format(mode_prefix, eng_name, report)))

# Attributes which show up in RegularAttribute BVC structs which our BVC-struct parsing doesn't
# know how to deal with, on account of it relying on other dynamic engine info.  Keys here are
# the attributes in question (found in `BaseValueAttribute` in the BVC struct).  The values are
# tuples where the first value is the report string we'll use, and the second value is a set of
# `AttributeToModify` attributes where we've seen these.  There's sort of no reason to be checking
# on those, honestly, but this way I've got a pretty good description in here of exactly how
# these things are used in the data.
reg_attr_unparseable_bva = {
        # Shows up in /Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Magazine/Part_SG_JAK_Mag_01
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Jakobs/Attributes/Att_JAK_BreakLoadShellAmount': (
            'BreakLoadShellAmount',
            set([
                '/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo',
                ]),
            ),
        # Shows up in /Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Part_PS_TOR_Barrel_ETech
        '/Game/GameData/Weapons/Att_Weapon_MaxLoadedAmmo': (
            'Max Loaded Ammo',
            set([
                '/Game/GameData/Weapons/Att_Weapon_ShotAmmoCost',
                '/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot',
                ]),
            ),
        # Shows up in /Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/Parts/FiringMode/Part_DAL_AR_Auto_Burst
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_BurstSize': (
            'Burst Size',
            set([
                '/Game/GameData/Weapons/Att_Weapon_AutomaticBurstCount',
                ]),
            ),
        # Shows up in /Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/Parts/FiringMode/Part_DAL_AR_Auto_Burst
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_BurstFireRate': (
            'Burst Fire Rate',
            set([
                '/Game/GameData/Weapons/Att_Weapon_FireRate',
                ]),
            ),
        # Shows up in /Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/Parts/FiringMode/Part_DAL_AR_Auto_Single
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Dahl/Att_Dahl_SemiFireRate': (
            'Semiauto Fire Rate',
            set([
                '/Game/GameData/Weapons/Att_Weapon_FireRate',
                ]),
            ),
        # Shows up in /Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/Parts/Underbarrel/Part_PS_VLA_Underbarrel_01
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Vladof/Attributes/Att_Vlad_PS_UnderbarrelFireRateBonus': (
            'Underbarrel Firerate Bonus',
            set([
                '/Game/GameData/Weapons/Att_Weapon_FireRate',
                ]),
            ),
        }
reg_attr_unparseable_ai = {
        # Shows up in /Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/Parts/Mag/Part_SG_Torgue_Magazine_01
        '/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/Torgue/Attributes/Init_TOR_ProjPerMagBarrel': (
            'unknown',
            set([
                '/Game/GameData/Weapons/Att_Weapon_ProjectilesPerShot',
                ]),
            ),
        }

def get_regular_attribute(bl3data, data, reset_attrs=True, use_mode=None):
    """
    Turns a "standard" attribute into a RegularAttribute object, if we can, or
    a ReportAttribute if we have known exceptions.  `bl3data` should be a
    BL3Data struct, and `data` should be the attribute data itself, containing
    attrs like AttributeToModify and ModifierValue.  Will return `None` if the
    structure can't be turned into an object (due to a missing AttributeToModify
    parameter, mostly).
    """
    global reg_attr_unparseable_bva
    global reg_attr_unparseable_ai
    if 'export' not in data['AttributeToModify']:
        for bvc_attr, unparseables in [
                ('BaseValueAttribute', reg_attr_unparseable_bva),
                ('AttributeInitializer', reg_attr_unparseable_ai),
                ]:
            if 'export' not in data['ModifierValue'][bvc_attr]:
                possibly_unparseable = data['ModifierValue'][bvc_attr][1]
                attr_to_modify = data['AttributeToModify'][1]
                if possibly_unparseable in unparseables and attr_to_modify in unparseables[possibly_unparseable][1]:
                    return ReportAttribute(attr_to_modify, '({})'.format(unparseables[possibly_unparseable][0]), reset_attrs, use_mode)
        return RegularAttribute(bl3data, data, reset_attrs, use_mode)
    return None

def process_common_attrs(bl3data, data):
    """
    This attempts to process some attributes which we *might* find in a variety
    of places.  This will certainly end up looking for atttributes which will
    never exist, under some circumstances, but it should do all right.
    """
    tmp_ret = []
    reset_attrs = ('bResetAttributes' in data and data['bResetAttributes'])
    if 'InventoryAttributeEffects' in data:
        for effect_entry in data['InventoryAttributeEffects']:
            tmp_ret.append(get_regular_attribute(bl3data, effect_entry, reset_attrs))
    if 'InstigatorAttributeEffects' in data:
        for effect_entry in data['InstigatorAttributeEffects']:
            tmp_ret.append(get_regular_attribute(bl3data, effect_entry, reset_attrs))
    if 'WeaponUseModeAttributeEffects' in data:
        for wuae in data['WeaponUseModeAttributeEffects']:
            # This is a bitmask, but in BL3 there's only ever two total modes, so
            # if the value is 1 or 2, that's the mode that it applies to; if it's
            # 3, it'll apply to both modes (which we can consider "global").  So
            # we'll just check for 1 or 2 and be done with it.
            use_mode = wuae['UseModeBitmask']
            assert(use_mode > 0 and use_mode <= 3)
            if use_mode == 3:
                use_mode = None
            for effect_entry in wuae['AttributeEffects']:
                tmp_ret.append(get_regular_attribute(bl3data, effect_entry, reset_attrs, use_mode=use_mode))
    # Filter out `None`s.  I know there are better ways to do this.
    to_ret = []
    for item in tmp_ret:
        if item is not None:
            to_ret.append(item)
    return to_ret

class Bonus:

    def __init__(self, bl3data, data):
        self.data = data
        self.attributes = process_common_attrs(bl3data, data)

class WBC:

    def __init__(self, path_name, data):
        #print('NOTICE: Reading WBC {}'.format(path_name))
        self.path_name = path_name
        self.data = data
        self.obj = self.data.get_data(path_name)
        self.table_name = None
        self.table = None
        self.attributes = {}
        self.collections = {}
        self.bonuses = {}
        for export in self.obj:
            if export['export_type'] == 'WeaponBonusDataTableData':
                self.table_name = export['DataTable'][1]
                self.table = self.data.get_data(self.table_name)[0]
                for attribute in export['AttributeMapping']:
                    if attribute['ColumnName'] in self.attributes:
                        # This is known to happen sometimes, for instance a dual `SwayAccuracyScale` inside
                        # /Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Barrel/Bonus_Weapon_PS_Barrel
                        # Confirmed by changing the relevant attributes to some really-noticeable ones
                        # (pellet count and reload speed): only the first gets applied.
                        #print('NOTE: {} has a duplicate "{}" entry in AttributeMapping'.format(
                        #    self.path_name,
                        #    attribute['ColumnName'],
                        #    ))
                        pass
                    else:
                        self.attributes[attribute['ColumnName']] = WBCAttribute(self, attribute, self.table)
                for collection in export['ColumnCollections']:
                    assert(collection['CollectionName'] not in self.collections)
                    self.collections[collection['CollectionName']] = set(collection['ColumnNames'])
            elif export['export_type'] == 'WeaponBonusCollectionData':
                if 'Bonuses' not in export:
                    print('No Bonuses found in: {}'.format(self.path_name))
                    continue
                for bonus in export['Bonuses']:
                    bonus_name = bonus['Name']
                    assert(bonus_name not in self.bonuses)
                    self.bonuses[bonus_name] = Bonus(data, bonus)

        assert(self.table or self.bonuses)

    def get_columns(self, collection_name):
        if collection_name in self.collections:
            return self.collections[collection_name]
        else:
            return set()

    def get_mod(self, row, column):
        if column not in self.attributes:
            return (None, None)
        attr = self.attributes[column]
        if attr.column is None:
            value = None
        else:
            value = attr.table[row][attr.column]
        return (attr, value)

    def get_bonus_attrs(self, bonus_name):
        if bonus_name not in self.bonuses:
            return []
        return self.bonuses[bonus_name].attributes

wbcs = {}

aspect_type_skips = set([
    #'WeaponUseModeSecondaryAspectData',
    'BP_ATL_Emissive_Common_C',
    'BP_ATL_Emissive_Epic_C',
    'BP_ATL_Emissive_Rare_C',
    'BP_ATL_Emissive_UnCommon_C',
    'BP_ElementalEmissives_Corrosive_C',
    'BP_ElementalEmissives_Cryo_C',
    'BP_ElementalEmissives_Fire_C',
    'BP_ElementalEmissives_Radiation_C',
    'BP_ElementalEmissives_Shock_C',
    'BP_MAL_ElemPrimary_01_Fire_C',
    'BP_MAL_ElemPrimary_02_Cryo_C',
    'BP_MAL_ElemPrimary_03_Shock_C',
    'BP_MAL_ElemPrimary_04_Slag_C',
    'BP_MAL_ElemPrimary_05_Corrosive_C',
    'BP_MAL_ElemSecondary_01_Fire_C',
    'BP_MAL_ElemSecondary_02_Cryo_C',
    'BP_MAL_ElemSecondary_03_Shock_C',
    'BP_MAL_ElemSecondary_04_Slag_C',
    'BP_MAL_ElemSecondary_05_Corrosive_C',
    'BP_WeaponMaterialWear_01_Common_C',
    'BP_WeaponMaterialWear_02_Uncommon_C',
    'BP_WeaponMaterialWear_03_Rare_C',
    'BP_WeaponMaterialWear_04_VeryRare_C',
    'BP_WeaponMaterialWear_05_Legendary_C',
    'InventoryAbilityAspectData',
    'InventoryConditionalDamageAspectData',
    'InventoryMaterialAspectData',
    'InventoryMeshAttachmentAspectData',
    'TedioreProjectileClassAspect',
    'TedioreWeaponAspectData',
    'WeaponAttachmentEffectAspectData',
    'WeaponAudioAspectData',
    'WeaponAudioStreamingAspectData',
    'WeaponFoleyAspectData',
    'WeaponMaterialEffectAspectData',
    'WeaponPlayerMeleeOverrideAspectData',
    'WeaponSkeletalControlAspectData',
    'WeaponUseModeAspectData',
    'WeaponUseModeCrosshairAspectData',
    'WeaponUseModeNameAspectData',
    ])
wbc_skips = set([
    # The attrs this links to includes some that I have no idea how to parse properly
    # (namely `WeaponTypeDataTableAttributeValueResolver` from, for instance,
    # /Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/Weapon_Damage/Att_DamageScale_Vladof)
    # so we're skipping it; this is just "base" guntype stats anyway, I think, and not
    # something I'd care much about reporting on.
    '/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Bonus/WBC_WeaponBaseInitialization',
    ])
secondary_aspects = {
        'WeaponAmmoComponent': ('Ammo Count', 'LoadedAmmo'),
        'WeaponZoomComponent': ('Scope Zoom', '----bleh----'),
        }
damage_types = {
        '/Game/GameData/DamageTypes/Corrosive/DmgType_Corrosive_Impact': 'Corrosive',
        '/Game/GameData/DamageTypes/Cryo/DmgType_Cryo_Impact': 'Cryo',
        '/Game/GameData/DamageTypes/Fire/DmgType_Fire_Impact': 'Fire',
        '/Game/GameData/DamageTypes/Impact/DmgType_Normal': 'Normal',
        '/Game/GameData/DamageTypes/Radiation/DmgType_Radiation_Impact': 'Radiation',
        '/Game/GameData/DamageTypes/Shock/DmgType_Shock_Impact': 'Shock',
        }
part_skips = set([
    '/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Parts/Part_Eridian_Fabricator',
    ])

#for part_name in ['/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Part_MAL_SR_Barrel_ETech']:
#for part_name in sorted(data.find('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts/Grip', 'Part_')):
#for part_name in sorted(data.find('/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/Parts', 'Part_')):
#for part_name in sorted(data.find('/Game/Gear/Weapons/Pistols/Jakobs', 'Part_')):
#for part_name in sorted(data.find('/Game/Gear/Weapons/Pistols', 'Part_')):
for part_name in sorted(data.find('/Game/Gear/Weapons', 'Part_')):
    if part_name in part_skips:
        continue
    part = data.get_data(part_name)
    found_main_export = False
    for export in part:
        if export['_jwp_object_name'].startswith('Part_') and export['export_type'].startswith('BPInvPart_'):
            found_main_export = True
            reports = set()
            report_attrs = AttrCollection()

            # Kick off the display of the part
            print(part_name)

            # Process "common" attrs
            for attr in process_common_attrs(data, export):
                report_attrs.add(attr)

            # Check for AspectList
            if 'AspectList' not in export:
                # This happens not infrequently; see for instance Part_PS_JAK_Speedloader and Part_PS_JAK_Rail_01
                #print('No AspectList found: {}'.format(part_name))
                print('')
                continue

            # Loop through the AspectList
            for aspect_idx, aspect_entry in enumerate(export['AspectList']):
                if 'export' not in aspect_entry:
                    print('No AspectList subobject found on idx {}: {}'.format(
                        aspect_idx,
                        part_name,
                        ))
                    continue

                # Make sure we've got an object to jump to
                if '_jwp_export_dst_type' not in aspect_entry or aspect_entry['_jwp_export_dst_type'] in aspect_type_skips:
                    continue

                # Grab the aspect and continue if we think we've got data for it
                # Honestly we should probably not bother with this check, but I sort of wanted to
                # be notified when we encountered aspects we don't yet understand.
                aspect = part[aspect_entry['export']-1]
                if 'DataTableBonuses' not in aspect \
                        and 'BonusCollection' not in aspect \
                        and 'ComparisonClass' not in aspect \
                        and 'DamageType' not in aspect \
                        and 'InventoryAttributeEffects' not in aspect \
                        and 'InstigatorAttributeEffects' not in aspect \
                        and 'WeaponUseModeAttributeEffects' not in aspect:
                    # Hardcode when we expect to see this
                    if part_name == '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Parts/Tails/Tail_01/Part_HW_TOR_Tail_01_B' and aspect_idx == 0:
                        pass
                    else:
                        print('No DataTableBonuses/BonusCollection/etc on aspect {}: {}'.format(
                            aspect_idx,
                            part_name
                            ))
                    continue

                # Check for DataTableBonuses (WBC stuff)
                if 'DataTableBonuses' in aspect:
                    for dtbonus in aspect['DataTableBonuses']:
                        wbc_name = dtbonus['WeaponBonusDataTable'][1]
                        if wbc_name not in wbcs:
                            wbcs[wbc_name] = WBC(wbc_name, data)
                        wbc = wbcs[wbc_name]
                        row_name = dtbonus['RowName']
                        columns = set()
                        for column in dtbonus['ColumnNames']:
                            # Seems fine.
                            #print('Got actual column, check it: {}'.format(part_name))
                            columns.add(column)
                        for collection in dtbonus['ColumnCollections']:
                            columns |= wbc.get_columns(collection)
                        for column in sorted(columns):
                            attr, val = wbc.get_mod(row_name, column)
                            if attr:
                                report_attrs.add(attr, val)

                # Now BonusCollection (more WBC)
                if 'BonusCollection' in aspect:
                    wbc_name = aspect['BonusCollection'][1]
                    if wbc_name in wbc_skips:
                        # Eh, this actually happens a lot; don't report on it.
                        #reports.add((0, 'Base Weapon Stats: Applied'))
                        continue
                    if wbc_name not in wbcs:
                        wbcs[wbc_name] = WBC(wbc_name, data)
                    wbc = wbcs[wbc_name]
                    for bonus_to_apply in aspect['BonusesToApply']:
                        for attr in wbc.get_bonus_attrs(bonus_to_apply):
                            report_attrs.add(attr)

                # "Common" regular attributes
                for attr in process_common_attrs(data, aspect):
                    report_attrs.add(attr)

                # ComparisonClass stuff
                if 'ComparisonClass' in aspect:
                    comp_class = aspect['ComparisonClass'][0]
                    if comp_class in secondary_aspects:
                        label, inner_attr = secondary_aspects[comp_class]
                        if 'Component' in aspect:
                            component = part[aspect['Component']['export']-1]
                            if inner_attr in component:
                                reports.add((0, '{}: {}'.format(
                                    label,
                                    component[inner_attr],
                                    )))
                            else:
                                reports.add((0, '{}: (unknown)'.format(label)))
                            if 'AttributeEffects' in component:
                                for ae_entry in component['AttributeEffects']:
                                    report_attrs.add(RegularAttribute(data, ae_entry))

                # DamageType!
                if 'DamageType' in aspect:
                    dt = aspect['DamageType'][1]
                    if dt in damage_types:
                        reports.add((0, 'Damage Type: {}'.format(damage_types[dt])))
                    else:
                        reports.add((0, 'Damage Type: {}'.format(dt)))

            # Now report
            report_attrs.report_to(reports)
            for _, report in sorted(reports):
                print(' - {}'.format(report))
            print('')

    # Report if we didn't find a main export
    if not found_main_export:
        print('Did not find main part export for: {}'.format(part_name))
        continue

