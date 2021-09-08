#!/usr/bin/python3
# vim: set foldmethod=marker :

import random

itemname = (
	None,
	'handgun',
	'smg',
	'grenade launcher',
	'rocket launcher',
	'plastic explosives',
	'mine',
	'missile',
	'silencer',
	'armor',
	'bomb blast suit',
	'flashlight',
	'infrared goggles',
	'gas mask',
	'cigarettes',
	'mine detector',
	'antenna',
	'binoculars',
	'oxygen tanks',
	'compass',
	'parachute',
	'antidote',
	'card 1',
	'card 2',
	'card 3',
	'card 4',
	'card 5',
	'card 6',
	'card 7',
	'card 8',
	'ration',
	'transceiver',
	'uniform',
	'box',
	'bag',
	'ammo',
)

def parse_line(line):	# {{{
	parts = line.split()
	if len(parts) == 0:
		return []
	area = int(parts[0])
	addr = int(parts[1], 16)
	if parts[2] == '!':
		extra = int(parts[3], 16)
		return {'area': area, 'addr': addr, 'extra': extra}
	return {'area': area, 'addr': addr}
# }}}

# Items. {{{
# Removed equipment bag:
# 21	db0d 22 20 88 ff	14
items = [parse_line(line) for line in '''
-1	dbe5	# dropped items
-1	dbe6	# dropped items
13	dbe9 ! 6e93	# silencer
117	dbe7 ! 7b9e	# card 7
116	dbe8 ! 576a	# card 8
0	dabb 1e 50 50 ff	01
0	dabf 16 50 70 ff	02
0	dac3 11 40 70 ff	03
0	dac7 06 40 60 ff	04
1	dacb 0d 20 48 ff	05
19	dacf 02 20 40 ff	06
45	dad3 19 60 80 ff	07
36	dad7 06 20 48 ff	08
38	dadb 0c 20 48 ff	09
30	dadf 14 20 48 ff	0a
32	dae3 05 80 50		0b
31	dae6 23 80 b0 ff	0b
2	daea 23 20 a0 ff	0c
11	daee 07 20 48 ff	0d
14	daf2 03 20 80 ff	0e
69	daf6 05 20 88 ff	0f
9	dafa 17 20 48 ff	10
16	dafe 21 60 48 ff	11
22	db02 18 70 42		12
22	db05 23 40 a0 ff	12
43	db09 0f 20 48 ff	13
48	db11 1e 40 60 ff	15
80	db15 09 20 88 ff	16
26	db19 0a 20 48 ff	17
48	db1d 05 60 60 ff	18
23	db21 20 20 48 ff	19
67	db25 10 20 48 ff	1a
51	db29 06 70 80		1b
51	db2c 23 40 40		1b
51	db2f 20 20 48 ff	1b
66	db33 0b 20 48 ff	1c
86	db37 23 30 70		1d
86	db3a 23 40 38		1d
86	db3d 23 80 b8 ff	1d
88	db41 15 20 48 ff	1e
89	db45 13 20 48 ff	1f
84	db49 04 20 40 ff	20
56	db4d 1a 20 48		21
56	db50 23 80 a8 ff	21
73	db54 1e 20 48 ff	22
10	db58 1e 20 48 ff	23
63	db5c 1b 20 48 ff	24
65	db60 05 48 28		25
65	db63 23 48 c0		25
65	db66 1e 60 c0 ff	25
115	db6a 23 18 68		26
115	db6d 23 50 40 ff	26
97	db71 12 20 88 ff	27
0	db75 01 60 40 ff	28
7	db79 05 38 30 ff	29
41	db7d 23 30 68 ff	2a
24	db81 23 2a 40		2b
24	db84 05 70 a8 ff	2b
40	db90 07 20 48 ff	2e
75	db94 23 50 60		2f
75	db97 23 70 a8 ff	2f
'''.split('\n') if line.split() != []]
# Get rid of those, because they don't seem to work well.
#93	db88 23 50 18 ff	2c
#93	db8c 1e 40 48 ff	2d
# }}}

'''	Original item data. {{{
changed: room c5 (set to 22), d6 (set to 2c), d8 (set to empty)

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
# }}}

doors = [ # {{{
		{'addr': 0xb048, 'from': 45, 'to': 47},
		{'addr': 0xb049, 'from': 45, 'to': 0},
		{'addr': 0xb049, 'from': 0, 'to': 45},
		{'addr': 0xb04a, 'from': 0, 'to': 15},
		{'addr': 0xb046, 'from': 0, 'to': 1},
		{'addr': 0xb04c, 'from': 45, 'to': 46},
		{'addr': 0xb04a, 'from': 15, 'to': 0},
		{'addr': 0xb04b, 'from': 15, 'to': 48},
		{'addr': 0xb04d, 'from': 15, 'to': 20},
		{'addr': 0xb04e, 'from': 15, 'to': 19},
		{'addr': 0xb04f, 'from': 15, 'to': 18},
		{'addr': 0xb05a, 'from': 35, 'to': 38},
		{'addr': 0xb05b, 'from': 35, 'to': 29},
		{'addr': 0xb05c, 'from': 35, 'to': 37},
		{'addr': 0xb0be, 'from': 35, 'to': 36},
		{'addr': 0xb0bf, 'from': 35, 'to': 34},
		{'addr': 0xb05e, 'from': 29, 'to': 15},
		{'addr': 0xb05b, 'from': 29, 'to': 35},
		{'addr': 0xb0e0, 'from': 29, 'to': 30},
		{'addr': 0xb0c1, 'from': 15, 'to': 32},
		{'addr': 0xb0c2, 'from': 15, 'to': 31},
		{'addr': 0xb05e, 'from': 15, 'to': 29},
		{'addr': 0xb05f, 'from': 15, 'to': 28},
		{'addr': 0xb05d, 'from': 15, 'to': 33},
		{'addr': 0xb060, 'from': 15, 'to': 27},
		{'addr': 0xb062, 'from': 5, 'to': 6},
		{'addr': 0xb063, 'from': 5, 'to': 11},
		{'addr': 0xb064, 'from': 5, 'to': 4},
		{'addr': 0xb064, 'from': 4, 'to': 5},
		{'addr': 0xb065, 'from': 4, 'to': 3},
		{'addr': 0xb066, 'from': 0, 'to': 12},
		{'addr': 0xb0c3, 'from': 0, 'to': 2},
		{'addr': 0xb0c4, 'from': 5, 'to': 7},
		{'addr': 0xb0c5, 'from': 8, 'to': 7},
		{'addr': 0xb068, 'from': 0, 'to': 13},
		{'addr': 0xb06b, 'from': 0, 'to': 15},
		{'addr': 0xb06b, 'from': 15, 'to': 0},
		{'addr': 0xb06c, 'from': 15, 'to': 16},
		{'addr': 0xb06d, 'from': 8, 'to': 10},
		{'addr': 0xb06e, 'from': 8, 'to': 9},
		{'addr': 0xb06f, 'from': 15, 'to': 17},
		{'addr': 0xb071, 'from': 39, 'to': 43},
		{'addr': 0xb072, 'from': 39, 'to': 42},
		{'addr': 0xb0c7, 'from': 39, 'to': 41},
		{'addr': 0xb073, 'from': 39, 'to': 40},
		{'addr': 0xb052, 'from': 21, 'to': 77},
		{'addr': 0xb052, 'from': 77, 'to': 21},
		{'addr': 0xb053, 'from': 77, 'to': 78},
		{'addr': 0xb0c8, 'from': 77, 'to': 113},
		#{'addr': 0xb054, 'from': 21, 'to': 15},
		{'addr': 0xb08f, 'from': 21, 'to': 22},
		#{'addr': 0xb054, 'from': 15, 'to': 21},
		{'addr': 0xb056, 'from': 15, 'to': 80},
		{'addr': 0xb058, 'from': 25, 'to': 26},
		{'addr': 0xb04b, 'from': 48, 'to': 15},
		{'addr': 0xb077, 'from': 50, 'to': 51},
		{'addr': 0xb078, 'from': 50, 'to': 52},
		{'addr': 0xb079, 'from': 53, 'to': 66},
		{'addr': 0xb078, 'from': 52, 'to': 50},
		{'addr': 0xb07a, 'from': 114, 'to': 53},
		{'addr': 0xb07a, 'from': 53, 'to': 114},
		{'addr': 0xb07d, 'from': 53, 'to': 70},
		{'addr': 0xb07c, 'from': 53, 'to': 67},
		{'addr': 0xb07e, 'from': 53, 'to': 69},
		{'addr': 0xb07f, 'from': 53, 'to': 92},
		{'addr': 0xb080, 'from': 70, 'to': 71},
		{'addr': 0xb07d, 'from': 70, 'to': 53},
		{'addr': 0xb081, 'from': 53, 'to': 68},
		{'addr': 0xb0cc, 'from': 85, 'to': 86},
		{'addr': 0xb082, 'from': 85, 'to': 87},
		{'addr': 0xb086, 'from': 85, 'to': 81},
		{'addr': 0xb089, 'from': 111, 'to': 81},
		{'addr': 0xb0b7, 'from': 111, 'to': 90},
		{'addr': 0xb086, 'from': 81, 'to': 85},
		{'addr': 0xb087, 'from': 81, 'to': 81},
		{'addr': 0xb088, 'from': 81, 'to': 112},
		{'addr': 0xb089, 'from': 81, 'to': 111},
		{'addr': 0xb08a, 'from': 81, 'to': 82},
		{'addr': 0xb087, 'from': 81, 'to': 81},
		{'addr': 0xb088, 'from': 112, 'to': 81},
		{'addr': 0xb08d, 'from': 111, 'to': 91},
		{'addr': 0xb08a, 'from': 82, 'to': 81},
		{'addr': 0xb08b, 'from': 82, 'to': 83},
		{'addr': 0xb08e, 'from': 82, 'to': 84},
		{'addr': 0xb08c, 'from': 81, 'to': 88},
		{'addr': 0xb092, 'from': 54, 'to': 55},
		{'addr': 0xb093, 'from': 54, 'to': 56},
		#{'addr': 0xb06a, 'from': 54, 'to': 57},
		{'addr': 0xb075, 'from': 74, 'to': 76},
		{'addr': 0xb0cd, 'from': 74, 'to': 75},
		{'addr': 0xb095, 'from': 72, 'to': 73},
		#{'addr': 0xb097, 'from': 118, 'to': 64},
		{'addr': 0xb09a, 'from': 60, 'to': 110},
		{'addr': 0xb098, 'from': 64, 'to': 63},
		{'addr': 0xb099, 'from': 72, 'to': 62},
		#{'addr': 0xb097, 'from': 64, 'to': 118},
		{'addr': 0xb09a, 'from': 110, 'to': 60},
		{'addr': 0xb09b, 'from': 110, 'to': 59},
		#{'addr': 0xb09c, 'from': 110, 'to': 58},
		#{'addr': 0xb09d, 'from': 110, 'to': 64},
		#{'addr': 0xb09d, 'from': 64, 'to': 110},
		{'addr': 0xb0ce, 'from': 72, 'to': 61},
		{'addr': 0xb0cf, 'from': 64, 'to': 65},
		{'addr': 0xb07f, 'from': 92, 'to': 53},
		{'addr': 0xb09e, 'from': 93, 'to': 94},
		{'addr': 0xb0e1, 'from': 94, 'to': 95},
		{'addr': 0xb09e, 'from': 94, 'to': 93},
		{'addr': 0xb0a1, 'from': 100, 'to': 116},
		{'addr': 0xb0d0, 'from': 99, 'to': 115},
		{'addr': 0xb0a4, 'from': 96, 'to': 102},
		{'addr': 0xb0a4, 'from': 102, 'to': 96},
		{'addr': 0xb0a5, 'from': 102, 'to': 103},
		{'addr': 0xb0a5, 'from': 103, 'to': 102},
		{'addr': 0xb084, 'from': 104, 'to': 105},
		{'addr': 0xb0a7, 'from': 105, 'to': 106},
		{'addr': 0xb084, 'from': 105, 'to': 104},
		{'addr': 0xb0a3, 'from': 96, 'to': 101},
		{'addr': 0xb0a7, 'from': 106, 'to': 105},
		{'addr': 0xb08f, 'from': 22, 'to': 21},
		{'addr': 0xb0c8, 'from': 113, 'to': 77},
		{'addr': 0xb075, 'from': 76, 'to': 74},
		{'addr': 0xb048, 'from': 47, 'to': 45},
		{'addr': 0xb04c, 'from': 46, 'to': 45},
		{'addr': 0xb04f, 'from': 18, 'to': 15},
		{'addr': 0xb04d, 'from': 20, 'to': 15},
		{'addr': 0xb04e, 'from': 19, 'to': 15},
		{'addr': 0xb046, 'from': 1, 'to': 0},
		{'addr': 0xb05a, 'from': 38, 'to': 35},
		{'addr': 0xb0be, 'from': 36, 'to': 35},
		{'addr': 0xb0bf, 'from': 34, 'to': 35},
		{'addr': 0xb0c0, 'from': 34, 'to': 33},
		{'addr': 0xb05d, 'from': 33, 'to': 15},
		{'addr': 0xb0c0, 'from': 33, 'to': 34},
		{'addr': 0xb0c1, 'from': 32, 'to': 15},
		{'addr': 0xb0c2, 'from': 31, 'to': 15},
		{'addr': 0xb0e0, 'from': 30, 'to': 29},
		{'addr': 0xb05f, 'from': 28, 'to': 15},
		{'addr': 0xb060, 'from': 27, 'to': 15},
		{'addr': 0xb062, 'from': 6, 'to': 5},
		{'addr': 0xb063, 'from': 11, 'to': 5},
		{'addr': 0xb065, 'from': 3, 'to': 4},
		{'addr': 0xb0ab, 'from': 3, 'to': 2},
		{'addr': 0xb0ab, 'from': 2, 'to': 3},
		{'addr': 0xb0c3, 'from': 2, 'to': 0},
		{'addr': 0xb068, 'from': 13, 'to': 0},
		{'addr': 0xb069, 'from': 13, 'to': 14},
		{'addr': 0xb069, 'from': 14, 'to': 13},
		{'addr': 0xb066, 'from': 12, 'to': 0},
		{'addr': 0xb0c5, 'from': 7, 'to': 8},
		{'addr': 0xb0c4, 'from': 7, 'to': 5},
		#{'addr': 0xb06a, 'from': 57, 'to': 54},
		{'addr': 0xb06c, 'from': 16, 'to': 15},
		{'addr': 0xb06e, 'from': 9, 'to': 8},
		{'addr': 0xb06d, 'from': 10, 'to': 8},
		{'addr': 0xb06f, 'from': 17, 'to': 15},
		{'addr': 0xb071, 'from': 43, 'to': 39},
		{'addr': 0xb072, 'from': 42, 'to': 39},
		{'addr': 0xb0c7, 'from': 41, 'to': 39},
		{'addr': 0xb073, 'from': 40, 'to': 39},
		{'addr': 0xb053, 'from': 78, 'to': 77},
		{'addr': 0xb058, 'from': 26, 'to': 25},
		{'addr': 0xb056, 'from': 80, 'to': 15},
		{'addr': 0xb079, 'from': 66, 'to': 53},
		{'addr': 0xb077, 'from': 51, 'to': 50},
		{'addr': 0xb07c, 'from': 67, 'to': 53},
		{'addr': 0xb07e, 'from': 69, 'to': 53},
		{'addr': 0xb081, 'from': 68, 'to': 53},
		{'addr': 0xb0cc, 'from': 86, 'to': 85},
		{'addr': 0xb082, 'from': 87, 'to': 85},
		{'addr': 0xb08c, 'from': 88, 'to': 81},
		{'addr': 0xb08e, 'from': 84, 'to': 82},
		{'addr': 0xb092, 'from': 55, 'to': 54},
		{'addr': 0xb093, 'from': 56, 'to': 54},
		{'addr': 0xb098, 'from': 63, 'to': 64},
		{'addr': 0xb0de, 'from': 63, 'to': 62},
		{'addr': 0xb099, 'from': 62, 'to': 72},
		{'addr': 0xb0de, 'from': 62, 'to': 63},
		{'addr': 0xb0ce, 'from': 61, 'to': 72},
		{'addr': 0xb0cf, 'from': 65, 'to': 64},
		{'addr': 0xb0d0, 'from': 115, 'to': 99},
		{'addr': 0xb0a1, 'from': 116, 'to': 100},
		{'addr': 0xb0a3, 'from': 101, 'to': 96},
		{'addr': 0xb05c, 'from': 37, 'to': 35},
		{'addr': 0xb0cd, 'from': 75, 'to': 74},
		{'addr': 0xb095, 'from': 73, 'to': 72},
		{'addr': 0xb08b, 'from': 83, 'to': 82},
		{'addr': 0xb0e1, 'from': 95, 'to': 94},
		{'addr': 0xb0b7, 'from': 90, 'to': 111},
		{'addr': 0xb09b, 'from': 59, 'to': 110},
		{'addr': 0xb08d, 'from': 91, 'to': 111},
		{'addr': 0xb080, 'from': 71, 'to': 70},
		#{'addr': 0xb09c, 'from': 58, 'to': 110},
	] # }}}

open_doors = {0xb06a, 0xb09c, 0xb09d, 0xb097, 0xb054}

prisoners = {3, 6, 17, 18, 20, 21, 79, 37, 28, 42, 47,	# building 1 {{{
		68, 55, 59, 61, 83, 87, 90,		# building 2
		101}					# building 3 }}}
# 3 prisoners only with card 8: 116

explodes = [ # {{{
		(15, 23),
		(15, 24),
		(15, 25),
		(60, 72),
		(72, 74),
		(78, 79),
		(94, 96),
		(96, 97),
		(102, 104),
		(107, 108),
	] # }}}

electric = [ # {{{
		(15, 8),
		(98, 99),
		(98, 100),
		(99, 100),
		(106, 107),
	] # }}}

gas = (4, 72, 60, 64, 102, 105,)

# Special connections. {{{
oneway = [
		{'type': 'parachute', 'from': 44, 'to': 45, 'need': (0x14,)},
		{'type': 'bb-suit', 'from': 15, 'to': 39, 'need': (0xa,)},
		{'type': 'hind d', 'from': 39, 'to': 44, 'need': (0x3, 0x23), 'level': 2, 'return': True},
		{'type': 'bulldozer', 'from': 52, 'to': 114, 'return': True, 'need': (0x3, 0x23)},
		{'type': 'tank', 'from': 48, 'to': 49, 'need': (0x6,), 'level': 3},
		{'type': 'tank', 'from': 49, 'to': 48, 'need': None},
		{'type': 'uniform', 'from': 49, 'to': 50, 'need': (0x20,)},
		{'type': 'uniform', 'from': 50, 'to': 49, 'need': None},
		{'type': 'oxygen', 'from': 53, 'to': 98, 'need': (0x12,)},
		{'type': 'oxygen', 'from': 98, 'to': 53, 'need': (0x12,)},
		{'type': 'compass', 'from': 92, 'to': 93, 'need': (0x13,)},
		{'type': 'compass', 'from': 93, 'to': 92, 'need': None},
		{'type': 'light', 'from': 76, 'to': 113, 'need': (0xb,)},
		{'type': 'light', 'from': 113, 'to': 76, 'need': (0xb,)},
		{'type': 'big boss', 'from': 108, 'to': 109, 'need': (0x4, 0x10, 0x23), 'return': True},
		{'type': 'capture', 'from': 15, 'to': 21, 'need': None},
		{'type': 'lorry', 'from': 48, 'to': 45, 'need': None},
		{'type': 'lorry', 'from': 45, 'to': 0, 'need': None},
		{'type': 'lorry', 'from': 93, 'to': 48, 'need': None},
		{'type': 'lorry', 'from': 93, 'to': 45, 'need': None},
		{'type': 'lift', 'from': 118, 'to': 53, 'need': None},
		{'type': 'lift', 'from': 71, 'to': 58, 'need': None},
		{'type': 'lift', 'from': 53, 'to': 81, 'need': None},
		{'type': 'lift', 'from': 91, 'to': 71, 'need': None},
		{'type': 'lift', 'from': 81, 'to': 54, 'need': None},
		{'type': 'lift', 'from': 57, 'to': 91, 'need': None},
		{'type': 'arnold', 'from': 81, 'to': 117, 'need': (0x4, 0x10, 0x23), 'return': True},
		{'type': 'jennifer', 'from': 112, 'to': 89, 'need': (0x10,), 'level': 4},
		{'type': 'hack', 'from': 58, 'to': 110, 'need': None},
		{'type': 'hack', 'from': 110, 'to': 64, 'need': None},
		{'type': 'hack', 'from': 64, 'to': 118, 'need': None},
		{'type': 'hack', 'from': 54, 'to': 57, 'need': None},
		{'type': 'hack', 'from': 21, 'to': 15, 'need': None},
	]
# }}}

versions = {'English (original)': ('Metal Gear (Europe).rom', True), # {{{
	'English (alternative)': ('Metal Gear (Europe 2).rom', False),
	'Japanese': ('Metal Gear (Japan).rom', False)} # }}}

rocketlauncher = 0x4
explosive = 0x5
missile = 0x7
gasmask = 0xd

def get_items(spots, area): # {{{
	last_area = []
	for item in items:
		if item['area'] != area:
			continue
		spots.append(item)
		last_area.append(item)
	return last_area
# }}}

def close_door_num(close_doors, orig): # {{{
	assert close_doors in (True, False, None)
	if close_doors is True:
		return 0x40
	if close_doors is False:
		return 0
	return orig & 0x40
# }}}

def default_door(max_card, close_doors, orig): # {{{
	return max_card + 1 + close_door_num(close_doors, orig)
	#return random.randrange(max_card) + 1 + close_door_num(close_doors, orig) + 1
# }}}

def default_item(): # {{{
	return random.sample([5, 6, 7, 0x1e, 0x23], 1)[0]
# }}}

def add_item(data, item, spots, item_offset, code_offset, spot = None): # {{{
	if spot is None:
		spot = random.sample(spots, 1)[0]
		if item in [5, 6, 7, 0x1e, 0x23]:
			while spot in items[2:5]:
				spot = random.sample(spots, 1)[0]
	spots.remove(spot)
	data[spot['addr'] + item_offset] = item
	print('putting %s at %04x (area %d)' % (itemname[item], spot['addr'], spot['area']))
	if 'extra' in spot:
		data[spot['extra'] + code_offset] = 0x20 + item - 1 if item < 8 else 0xa0 + item - 8 - 1
# }}}

def get_spots(areas, spots): # {{{
	for a in range(len(areas) - 1, -1, -1):
		options = [x for x in areas[a] if x in spots]
		if len(options) == 0:
			continue
		return random.sample(options, 1)[0]
	raise AssertionError('no spots available')
# }}}

def randomize(version = None, close_doors = None, show_doors = False, extreme = False): # {{{
	if version is None:
		version = 'English (original)'
	data = list(open(versions[version][0], 'rb').read())
	code_offset, item_offset, first_item_offset = (-0x4c, -0xd, -0x4f) if versions[version][1] else (0, 0, 0)
	# Fix item tables so each item definition is only used once.
	# There are 3 duplicates, and 2 unused entries; the third location is made empty.
	for room, code in ((0xc5, 0x22), (0xd6, 0x2c), (0xd8, 0)):
		data[0xd9fc + item_offset + (room - 0x7a)] = code
	# Permanently open doors in building 2 to prevent getting stuck.
	for hack in open_doors:
		data[hack + 0x1f000 - 0xb000] = 0x81
	# Show door numbers.
	if show_doors and version == 'English (original)':
		showcode = (0xd1, 0x2b, 0x2b, 0x2b, 0x2b, 0xe5, 0x21, 0xce, 0xbf, 0xe5, 0xd5, 0xc3, 0xea, 0x41, 0xe1, 0x7e, 0x3d, 0x3d, 0xe6, 0xbf, 0xfe, 0x08, 0xd0, 0xed, 0x5b, 0x00, 0xec, 0x3c, 0x87, 0x87, 0x87, 0x67, 0x2e, 0x40, 0x3e, 0x40, 0x01, 0x08, 0x08, 0xc3, 0x11, 0x50)
		for i, c in enumerate(showcode):
			data[0x7fc0 + i] = c
		data[0x373a] = 0xc0
		data[0x373b] = 0xbf
	# Generate order in which regions can be visited.
	regions = set(range(1, 119))
	order = [('start', 0, None)]
	used = [0]
	rescued = 0
	used_doors = 0
	have_explode = False
	have_missile = False
	while len(regions) > 0:
		# Find reachable regions.
		reachable = []
		for door in doors:
			if door['from'] in used and door['to'] not in used:
				reachable.append(('door', door['to'], door))
		if not have_explode:
			for e in explodes:
				if e[0] in used and e[1] not in used:
					reachable.append(('explode', e[1], e[0]))
				if e[1] in used and e[0] not in used:
					reachable.append(('explode', e[0], e[1]))
		if not have_missile:
			for e in electric:
				if e[0] in used and e[1] not in used:
					reachable.append(('electric', e[1], e[0]))
				if e[1] in used and e[0] not in used:
					reachable.append(('electric', e[0], e[1]))
		for one in oneway:
			if one['from'] in used and one['to'] not in used \
					and ('level' not in one or one['level'] <= 1 + rescued // 5) \
					and (one['need'] is None or rocketlauncher not in one['need'] or ((82 in used or 112 in used) and 4 <= 1 + rescued // 5)):
				reachable.append(('oneway', one['to'], one))
		# Pick one
		#print('reachable:', reachable, 'regions:', regions)
		target = random.sample(reachable, 1)[0]
		if target[1] in prisoners:
			rescued += 1
		regions.remove(target[1])
		used.append(target[1])
		if target[0] == 'electric':
			have_missile = True
		if target[0] == 'explode':
			have_explode = True
		order.append(target)
		def connect_test(type, old, new):
			if old not in used or new in used:
				return False
			regions.remove(new)
			used.append(new)
			order.append((type, new, old))
			return True
		# Add electric connections.
		if have_missile:
			while True:
				for e in electric:
					if connect_test('electric', e[0], e[1]) or connect_test('electric', e[1], e[0]):
						break
				else:
					break
		# Add explosive connections.
		if have_explode:
			while True:
				for e in explodes:
					if connect_test('explode', e[0], e[1]) or connect_test('explode', e[1], e[0]):
						break
				else:
					break
		while True:
			for e in oneway:
				if e['need'] is None and e['from'] in used and e['to'] not in used:
					regions.remove(e['to'])
					used.append(e['to'])
					order.append(('oneway', e['to'], e))
					break
			else:
				break
		if target[0] == 'door':
			used_doors += 1
	# Distribute items such that the order works.
	spots = []
	get_items(spots, -1)
	found = set()
	last_card = 0
	doors_done = 0
	cards = [0]
	for c in range(1, 8):
		cards.append(random.randrange(used_doors * (len(cards) - 1) // 7 + 1, used_doors * len(cards) // 7))
	# Assign non-unique items to drops.
	if extreme:
		drops = [0, 0]
	else:
		drops = [default_item(), default_item()]
		while drops[0] == drops[1]:
			drops[1] = default_item()
	for spot in range(2):
		add_item(data, drops[spot], spots, item_offset, code_offset, items[spot])
		found.add(drops[spot])
	doors_used = set()
	last_areas = []
	for type, area, info in order:
		allow_new_area = True
		if type == 'start':
			pass
		elif type == 'door':
			# Set card or default thing; place card if it's new.
			card_addr = info['addr'] + 0x1f000 - 0xb000
			assert card_addr not in doors_used
			doors_used.add(card_addr)
			if doors_done in cards:
				last_card += 1
				# Put the new card in the last explored area, or the one before that until it is possible.
				new_spot = get_spots(last_areas, spots)
				add_item(data, 0x15 + last_card, spots, item_offset, code_offset, new_spot)
				found.add(0x15 + last_card)
				data[card_addr] = last_card + 1 + close_door_num(close_doors, data[card_addr])
			else:
				assert doors_done > 0 and last_card > 0
				data[card_addr] = default_door(last_card, close_doors, data[card_addr])
				if (data[card_addr] - 1) & 0xf != last_card:
					allow_new_area = False
			doors_done += 1
		elif type == 'explode':
			if explosive not in found:
				add_item(data, explosive, spots, item_offset, code_offset)
				found.add(explosive)
		elif type == 'electric':
			if missile not in found:
				add_item(data, missile, spots, item_offset, code_offset)
				found.add(missile)
		elif type == 'oneway':
			# Do whatever is needed.
			if info['need'] is not None:
				for item in info['need']:
					if item not in found:
						add_item(data, item, spots, item_offset, code_offset)
						found.add(item)
		else:
			print('invalid type', type)
			raise AssertionError('invalid type')
		if area in gas and gasmask not in found:
			add_item(data, gasmask, spots, item_offset, code_offset)
			found.add(gasmask)
		print('access new area %d using %s (%s)' % (area, type, info))
		new_area = get_items(spots, area)
		if len(new_area) > 0 and allow_new_area:
			last_areas.append(new_area)
	# Other doors.
	for d in doors:
		card_addr = d['addr'] + 0x1f000 - 0xb000
		if card_addr in doors_used:
			continue
		data[card_addr] = default_door(last_card, close_doors, data[card_addr])
	# Fill other spots.
	all_items = set(range(1, 0x24))
	all_items.difference_update({5, 6, 7, 0xe, 0x1e, 0x1f, 0x22, 0x23})
	for i in found:
		if i in all_items:
			all_items.remove(i)
	for spot in range(2, 5):
		if items[spot] not in spots:
			continue
		item = random.sample(all_items, 1)[0]
		all_items.remove(item)
		add_item(data, 0 if extreme else item, spots, item_offset, code_offset, items[spot])
		found.add(item)
	for i in all_items:
		add_item(data, 0 if extreme else i, spots, item_offset, code_offset)
		found.add(i)
	while len(spots) > 0:
		add_item(data, 0 if extreme else default_item(), spots, item_offset, code_offset)
	return bytes(data)
# }}}

try:
	import fhs
	import websocketd

	fhs.option('port', 'port to listen on', default = '9999')
	config = fhs.init()

	server = websocketd.Httpd(config['port'], None, httpdirs = ['html'], tls = False)

	def new_page(connection, path = None):
		if connection.address.path != '/random.rom':
			return default_page(connection, path)
		close_doors = None if 'doors' not in connection.query or connection.query['doors'][-1] == 'keep' else True if connection.query['doors'][-1] == 'close' else False
		show_doors = 'showdoor' in connection.query and connection.query['showdoor'][-1].lower() == 'true'
		extreme = 'extreme' in connection.query and connection.query['extreme'][-1].lower() == 'true'
		print(connection.query, close_doors, show_doors, extreme)
		data = randomize(connection.query['rom'][0] if 'rom' in connection.query else None, close_doors, show_doors, extreme)
		return server.reply(connection, 200, bytes(data), 'application/octet-stream')

	default_page = server.page
	server.page = new_page
	print('server is running')
	websocketd.fgloop()

except ImportError:
	data = randomize()
	with open('random.rom', 'wb') as out:
		out.write(bytes(data))
	print('Unable to import fhs or websocketd; writing output to file')
