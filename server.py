#!/usr/bin/python3

# treedata is a description of every object, with requirements for which
# objects must be available in order to get to the place where it is normally
# found.
#
# The first word (before the first tab character) are the requirements, then
# there is unused text followed by a colon. Then a comma-separated list of
# address-description pairs.

# The initial items are special:
# The item you start out with. This cannot be a weapon.
# A fake item which requires card 8. This ensures that card 8 can be found.
# Items dropped when punching guards.
# Card 7; you must be able to kill Mr Arnold before picking this up.
# Card 8; you must be able to kill Coward Duck before picking this up.
# Silencer; you must be able to kill the guards in its room before picking it up.

treedata = '''\
!				Initial item: 2dd4:cigarettes with 8 offset
8				Fake non-item: 0000:fake address
%				Dropped items: dbe5:ration, dbe6:ammo
&4uGaRr|1256lRr			Special: dbe7:card 7
*47uGaT|12567lT			Special: dbe8:card 8
=2				Special: dbe9:silencer
23				Room 7a (39): db02:card 3, db05:ammo
				Room 7e (05): dabb:ration
				Room 7f (05): dabf:card 1
				Room 80 (05): dac3:binoculars
				Room 82 (07): db75:handgun
				Room 84 (07): dac7:mine
4|1msGap|2sGap			Room 87 (09): dad3:card 4
2				Room 89 (0d): dacf:smg
1				Room 8a (08): dacb:gas mask
13m|23|34			Room 8b (10): dadb:infrared goggles
13m|23|34			Room 8c (11): dad7:mine
1m|2|4				Room 8e (17 8d 15 15): dae3:plastic explosives, dae6:ammo
13m|123|134			Room 8f (14): dadf:parachute
2				Room 93 (1c): daee:missile
				Room 95 (94 1e): daea:ammo
12				Room 97 (96): daf2:grenade launcher
1m|2|4				Room 99 (20 20): db79:plastic explosives
2				Room 9c (23): dafe:box
1m|12				Room 9d (24): dafa:card 2
2				Room 9e (24): db58:ration
13ms|23s|34s			Room a0 (28): db09:mine detector
1ms|2s|4s			Room a2 (2a): db7d:ammo
13ms|23s|34s			Room a3 (33): db90:missile
@13m|23|34			Room a8 (39): db0d:bag
1mB|2B|4B			Room a9 (3b): db21:uniform
13mB|23B|34B			Room aa (3e): db19:bomb blast suit
4				Room ab (3a): db15:armor
1mB|2B|4B			Room ac (3d): db81:ammo, db84:plastic explosives
4				Room ae (40): db1d:plastic explosives
4				Room af (41): db11:ration
46uGa|12356l			Room b0 (46): db33:flashlight
4u|123456l			Room b1 (46): db29:mine, db2c:ammo, db2f:uniform
24uGa|12356l			Room b2 (4a): db25:antenna
46uGa|12356l			Room b3 (4b): daf6:plastic explosives
14uGa|12356l			Room b5 (4f): db37:ammo, db3a:ammo, db3d:ammo
46uGa|12356l			Room b7 (57): db41:antidote
24uGar|12356lr			Room b8 (57): db45:compass
456uGa|12356l			Room b9 (56): db49:rocket launcher
45uGa|12356l			Room bb (59): db4d:card 5, db50:ammo
12356lm|45uGaBm|12356lBm	Room bc (62 bd): db5c:card 6
12356lm|45uGaBm|12356lBm	Room bf (65): db60:plastic explosives, db63:ammo, db66:ration
14uGaT|12356lT			Room c0 (6e): db6a:ammo, db6d:ammo
12356l|45uGaBm|12356lBm		Room c4 (5d): db94:ammo, db97:ammo
12356lm|45uGaBm|12356lBm	Room c5 (5e): db58:ration
47uGacB|123567lcB		Room c8 (73): db71:oxygen tanks
47uGac|123567lc			Room d6 (68): db7d:ammo
47uGac|123567lc			Room d8 (68): db94:ammo, db97:ammo
47uGac|123567lc			Room da (68): db8c:ration'''

import random

decoder = {
		#    0x00,	# -
		#    0x01,	# Handgun
		#    0x02,	# Smg
		'G': 0x03,	# Grenade launcher
		'R': 0x04,	# Rocket launcher
		'B': 0x05,	# Plastic explosives
		#    0x06,	# Mine
		#    0x07,	# Missile
		#    0x08,	# Silencer
		#    0x09,	# Armor
		's': 0x0a,	# Bomb blast suit
		'l': 0x0b,	# Flashlight
		#    0x0c,	# Infrared goggles
		'm': 0x0d,	# Gas mask
		#    0x0e,	# Cigarettes
		#    0x0f,	# Mine detector
		'r': 0x10,	# Antenna
		#    0x11,	# Binoculars
		'T': 0x12,	# Oxygen tank
		'c': 0x13,	# Compass
		'p': 0x14,	# Parachute
		#    0x15,	# Antidote
		'1': 0x16,	# Card 1
		'2': 0x17,	# Card 2
		'3': 0x18,	# Card 3
		'4': 0x19,	# Card 4
		'5': 0x1a,	# Card 5
		'6': 0x1b,	# Card 6
		'7': 0x1c,	# Card 7
		'8': 0x1d,	# Card 8
		#    0x1e,	# Ration
		#    0x1f,	# Transmitter (picking it up leads to a crash)
		'u': 0x20,	# Uniform
		#    0x21,	# Box
		#    0x22,	# Bag of equipment
		'a': 0x23,	# Ammo
	}

def parse(code):
	return tuple(decoder[x] for x in code)

fixups = ((0xc5, 0x22), (0xd6, 0x2c), (0xd8, 0))
drop_addrs = ((0xdbe9, 0x6e93), (0xdbe7, 0x7b9e), (0xdbe8, 0x576a))

def generate_rom(initial = True, silencer = True, card7 = True, card8 = True, drops = True, bag = True, rom = 'en'):
	roms = {
			'jp': 'Metal Gear (Japan).rom',
			'en': 'Metal Gear (Europe).rom',
			'en2': 'Metal Gear (Europe 2).rom',
		}
	print('rom: ', roms[rom])
	data = list(open(roms[rom], 'rb').read())
	if rom == 'en':
		codeoffset = -0x4c
		itemoffset = -0xd
		firstitemoffset = -0x4f
	else:
		codeoffset = 0
		itemoffset = 0
		firstitemoffset = 0

	for room, code in fixups:
		data[0xd9fc + itemoffset + (room - 0x7a)] = code

	spots = set()	# locations that are not yet assigned an item. (memory address)
	groups = {}	# items that need to be assigned to a spot; key = constraint, value = list of dicts {'addr', 'need'}.
	objects = []	# items that need to be assigned to a spot. (numerical code)
	needed = set()	# objects for which the spot must be accessible before picking them up.
	for line in treedata.split('\n'):
		code, desc = line.split('\t', 1)
		thisitemoffset = itemoffset
		offset = 0
		need = None
		if code == '!':
			if not initial:
				continue
			thisitemoffset = firstitemoffset
			offset = 8
			code = None
		elif code.startswith('&'):
			if not card7:
				desc = 'Fixed: 0000:card 7'
			code = code[1:]
		elif code.startswith('*'):
			if not card8:
				desc = 'Fixed: 0000:card 8'
			code = code[1:]
		elif code.startswith('%'):
			if not drops:
				continue
			code = code[1:]
		elif code.startswith('='):
			if not silencer:
				continue
			code = code[1:]
		elif code.startswith('@'):
			if not bag:
				continue
			code = code[1:]
		if need is not None:
			needed.add(need)
		objs = desc.split(':', 1)[1].split(',')
		addrs = [int(x.split(':', 1)[0], 16) + thisitemoffset for x in objs]
		for addr in addrs:
			if code is None:
				first_item = addr
			else:
				if addr in spots:
					# Some object definitions are used by more than one room.
					# The list is sorted so the first definition is always more important.
					print('double definition of address: %04x' % addr)
					continue
				spots.add(addr)
				numcode = tuple(parse(x) for x in code.split('|'))
				if numcode not in groups:
					groups[numcode] = []
				groups[numcode].append(dict(addr = addr, need = need))
			if addr != 0:
				item = data[addr] + offset
				objects.append(item)

	'''
	Pick option for each group.
	Until done:
		Pick group at random
		find groups that must be done before it
			Pick group at random
			...
		Add groups and group to list
		
		for each group:
			add required items to spots from pool
			add group spots to pool
		
	finally:
		add remaining items to spots from pool
	'''

	# For items which have multiple ways to reach them, pick one option.
	# Merge groups with same constraints.
	new_groups = {}
	for code in tuple(groups.keys()):
		options = groups.pop(code)
		choice = random.choice(code)
		if choice not in new_groups:
			new_groups[choice] = []
		new_groups[choice].extend(options)
	groups = new_groups

	order = []

	def order_groups(selection):
		'''Order the groups in the selection and push them all into order'''
		# Until done:
		while len(selection) > 0:
			# Pick group at random
			pick = random.choice(tuple(selection))
			# Don't allow picking a group with an item that needs to be found later
			if any(x in pick for x in needed):
				continue
			# find groups that must be done before it
			dep = set()
			for g in selection:
				if g is pick:
					continue
				if all(x in pick for x in g):
					dep.add(g)
			# Add groups and group to list
			if len(dep) == 1:
				item = dep.pop()
				order.append(item)
				selection.remove(item)
			elif len(dep) > 1:
				selection.difference_update(dep)
				order_groups(dep)
			order.append(pick)
			selection.remove(pick)
			for group in groups[pick]:
				if group['need'] is not None:
					needed.remove(group['need'])

	order_groups(set(groups))

	accessible = set()
	if initial:
		# Add random first object, because otherwise satisfying the constraints for it is too hard.
		while True:
			item = random.choice(objects)
			if item <= 8 or 0x16 <= item <= 0x1d or item in (0x22, 0x23):
				continue
			data[first_item] = item - 8
			objects.remove(item)
			accessible.add(item)
			break

	pool = set()

	print('\n'.join([' '.join(['%02x' % t for t in x]) for x in order]))

	# for each group:
	for group in order:
		# add required items to spots from pool
		for constraint in group:
			if constraint in accessible:
				continue
			spot = random.choice(tuple(pool))
			data[spot] = constraint
			pool.remove(spot)
			if constraint in objects:
				objects.remove(constraint)
			accessible.add(constraint)
		# add group spots to pool
		new = tuple(x['addr'] for x in groups[group] if x['addr'] != 0)
		pool.update(new)

	# add remaining items to spots from pool
	for spot in pool:
		item = random.choice(objects)
		data[spot] = item
		objects.remove(item)
		accessible.add(item)
	
	for item_addr, check_addr in drop_addrs:
		item = data[item_addr + itemoffset]
		data[check_addr + codeoffset] = 0x20 + item - 1 if item < 8 else 0xa0 + item - 8 - 1
	return data

try:
	import fhs
	import websocketd

	config = fhs.init({'port': 9999})

	server = websocketd.Httpd(config['port'], None, httpdirs = ['html'], tls = False)

	def new_page(connection, path = None):
		if connection.address.path != '/random.rom':
			return default_page(connection, path)
		args = {}
		for arg in ('initial', 'silencer', 'card7', 'card8', 'drops', 'bag'):
			args[arg] = arg not in connection.query or connection.query[arg][0].lower() not in ('0', 'false')
		if 'rom' in connection.query:
			args['rom'] = connection.query['rom'][0]
		data = generate_rom(**args)
		return server.reply(connection, 200, bytes(data), 'application/octet-stream')

	default_page = server.page
	server.page = new_page
	print('server is running')
	websocketd.fgloop()

except ImportError:
	data = generate_rom()
	with open('patched.rom', 'wb') as out:
		out.write(bytes(data))
	print('Unable to import fhs or websocketd; writing output to file')
