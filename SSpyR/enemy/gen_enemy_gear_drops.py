from bl3hotfixmod import Mod
from bl3data import BL3Data
import os

# Utils: bpchars.txt
# Re-build DropOnDeathItemPool instead of editing specific array entry
# Don't think it works, need to see what might be causing that (probably the way I build the DropOnDeathPools)
# Turns out I am just stupid see text:

#Anyway, running that against this one char, at least (/Game/Enemies/Enforcer/Gun/_Design/Character/BPChar_EnforcerGun), 
#the script's reporting that it's PlayThroughs that's not found, but the actual KeyError was coming from dropondeath_pools=playthroughs['DropOnDeathItemPools']['ItemPools'] 
#because DropOnDeathitemPools doesn't exist in the main object
#In this case, instead of the try I'd recommend a if 'PlayThroughs' in playthroughs: (and replace the except with an else)
#And then do basically the same with that catch for EquippedItemPoolCollections

mod=Mod('enemy_gear_drops.bl3hotfix',
'Enemy Gear Drops',
'SSpyR',
[
	'Makes enemies drop their items they are using.'
],
lic=Mod.CC_BY_SA_40,
cats='enemy-drops, enemy'
)

data=BL3Data()

dir=os.path.dirname(__file__)
bpchars=open(os.path.join(dir, 'bpchars.txt')).readlines()

for bpchar in bpchars:
	#bpchar='/Game/Enemies/Trooper/_Unique/Bounty01/_Design/Character/BPChar_Trooper_Bounty01'
	bpchar=str.rstrip(bpchar)
	cond=bpchar.split('/')
	name=cond[len(cond)-1]
	cond='.'+cond[len(cond)-1]+'_C'
	bpcharref=bpchar+cond+":AIBalanceState_GEN_VARIABLE"

	try:
		playthroughs=data.get_exports(bpchar, 'AIBalanceStateComponent')[0]
	except IndexError:
		print('No Object Type Export "AIBalanceStateComponent"')
	if 'PlayThroughs' in playthroughs:
		for idx, playthrough in enumerate(playthroughs['PlayThroughs']):
			if 'EquippedItemPoolCollections' in playthrough and len(playthrough['EquippedItemPoolCollections']) > 0 and len(playthrough['EquippedItemPoolCollections'][0]['ItemPools']) > 0:
				if 'ItemPool' in playthrough['EquippedItemPoolCollections'][0]['ItemPools'][0]:
					equipped_pools=playthrough['EquippedItemPoolCollections'][0]['ItemPools'][0]
					if len(equipped_pools['ItemPool']) > 1:
						enemy_gun_pool=equipped_pools['ItemPool'][1]
						if enemy_gun_pool is None:
							break
						if 'DropOnDeathItemPools' in playthroughs and 'ItemPools' in playthroughs['DropOnDeathItemPools']:
							dropondeath_pools=playthroughs['DropOnDeathItemPools']['ItemPools']
							enemy_gun_pool=enemy_gun_pool+'.'+equipped_pools['ItemPool'][0]

							if len(dropondeath_pools) >= 1 and 'export' not in dropondeath_pools[0]['ItemPool']:
								existpool=dropondeath_pools[0]['ItemPool'][1]+'.'+dropondeath_pools[0]['ItemPool'][0]
								existprob=dropondeath_pools[0]['PoolProbability']['BaseValueConstant']
								if len(dropondeath_pools) == 2:
									existpool2=dropondeath_pools[1]['ItemPool'][1]+'.'+dropondeath_pools[1]['ItemPool'][0]
									existprob2=dropondeath_pools[1]['PoolProbability']['BaseValueConstant']
									mod.reg_hotfix(Mod.CHAR, name,
									str.rstrip(bpcharref),
									'DropOnDeathItemPools.ItemPools',
									"""
									(
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant={})
										),
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant={})
										),
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant=0.300000)
										)
									)
									""".format(existpool, existprob, existpool2, existprob2, enemy_gun_pool)
									)
									mod.newline()
								else:
									mod.reg_hotfix(Mod.CHAR, name,
									str.rstrip(bpcharref),
									'DropOnDeathItemPools.ItemPools',
									"""
									(
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant={})
										),
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant=0.300000)
										)
									)
									""".format(existpool, existprob, enemy_gun_pool)
									)
									mod.newline()
							else:
								mod.reg_hotfix(Mod.CHAR, name,
								str.rstrip(bpcharref),
								'DropOnDeathItemPools.ItemPools',
								"""
								(
									(
										ItemPool=ItemPoolData'\"{}\"',
										PoolProbability=(BaseValueConstant=0.300000)
									)
								)
								""".format(enemy_gun_pool)
								)
								mod.newline()
						elif 'DropOnDeathItemPools' in playthrough and 'ItemPools' in playthrough['DropOnDeathItemPools']:
							dropondeath_pools=playthrough['DropOnDeathItemPools']['ItemPools']
							enemy_gun_pool=enemy_gun_pool+'.'+equipped_pools['ItemPool'][0]

							if len(dropondeath_pools) >= 1 and 'export' not in dropondeath_pools[0]['ItemPool']:
								existpool=dropondeath_pools[0]['ItemPool'][1]+'.'+dropondeath_pools[0]['ItemPool'][0]
								existprob=dropondeath_pools[0]['PoolProbability']['BaseValueConstant']
								if len(dropondeath_pools) == 2:
									existpool2=dropondeath_pools[1]['ItemPool'][1]+'.'+dropondeath_pools[1]['ItemPool'][0]
									existprob2=dropondeath_pools[1]['PoolProbability']['BaseValueConstant']
									mod.reg_hotfix(Mod.CHAR, name,
									str.rstrip(bpcharref),
									'PlayThroughs.PlayThroughs[{}].DropOnDeathItemPools.ItemPools'.format(idx),
									"""
									(
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant={})
										),
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant={})
										),
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant=0.300000)
										)
									)
									""".format(existpool, existprob, existpool2, existprob2, enemy_gun_pool)
									)
									mod.newline()
								else:
									mod.reg_hotfix(Mod.CHAR, name,
									str.rstrip(bpcharref),
									'PlayThroughs.PlayThroughs[{}].DropOnDeathItemPools.ItemPools'.format(idx),
									"""
									(
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant={})
										),
										(
											ItemPool=ItemPoolData'\"{}\"',
											PoolProbability=(BaseValueConstant=0.300000)
										)
									)
									""".format(existpool, existprob, enemy_gun_pool)
									)
									mod.newline()
							else:
								mod.reg_hotfix(Mod.CHAR, name,
								str.rstrip(bpcharref),
								'DropOnDeathItemPools.ItemPools',
								"""
								(
									(
										ItemPool=ItemPoolData'\"{}\"',
										PoolProbability=(BaseValueConstant=0.300000)
									)
								)
								""".format(enemy_gun_pool)
								)
								mod.newline()
						else:
							print('No Object Array "DropOnDeathItemPools"')
					else:
						print('No Actual Item Pool in "EquippedItemPoolCollections"')
				else:
					print('No Pool in "EquippedItemPoolCollections"')
			else:
				print('No Object Array "EquippedItemPoolCollections"')
	else:
		print('No Object Array "PlayThroughs"')