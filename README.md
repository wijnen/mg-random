# Randomizer for Metal Gear 1 objects
This program patches the Metal Gear ROM to shuffle all the objects around.  It
tries to make sure that all objects can still be found, and thus the game is
finishable.  This may require not picking up some objects immediately.

## Requirements
To run, the program needs:

- Python3
- Openmsx

## Use
Just run _./mgrandom_.  It will shuffle the objects, printing some output about
the shuffle.  Then it will launch openmsx with the generated ROM image.

## Notes
The story is ruined by this program.  Don't play the game this way unless you
are familiar with the original.

Having the silencer, card 7 and card 8 triggers their respective enemies to be
present and thus drop those items in the original game.  Therefore, make sure
that you kill the enemy before picking up their item.  For example, you want to
kill Mr. Arnold before picking up card 7, because after picking up that card,
they will no longer be there and you will not be able to get the object they
drop.

The cigarettes are shuffled with the other objects.  However, when they are
listed as being in a room, they don't actually show up.

# Finally
Please send any comments to [wijnen@debian.org](mailto:wijnen@debian.org), or
tweet to @MakerWijnen.

Enjoy this randomizer, or if it's not your thing, ignore it and do something
that you do like.
