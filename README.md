# Randomizer for Metal Gear 1 objects
This program patches the Metal Gear ROM to shuffle all the objects around, and
changes which cards open which doors.  It makes sure that all objects can still
be found, and thus the game is finishable.  It should be impossible to
soft-lock the game, but this has not been extensively tested.

## Public server
As a service to the community, an instance of this program runs on
http://wijnen.mywire.org/mgrandom/. If you just want to try an image, you can
use that.

## Requirements
To run, the program needs:

- Python3
- Python-fhs
- Python-network
- Python-websocketd

The three modules can be found on https://github.com/wijnen/. Without them the
randomizer can still be used as a commandline program.

The modules have only been tested to work on GNU/Linux. They may not work on
Windows systems.

Obviously you will also need some way to play the generated ROM image. I use
the OpenMSX emulator.

## Use from the commandline
If the three Python modules are not installed, running server2.py will generate
an image and place it in the current directory with the name _random.rom_. In
this mode it is not possible to change any settings.

## Use as a server
If the three Python modules are installed, running server2.py will start a web
server on port 9999. This can be reached by pointing your browser to
http://localhost:9999/. This page will show some settings and a button to
generate an image with those settings. 

## The settings
- Base ROM image: There are 3 versions of the game available, and the randomizer allows to use any of them as the basis for its image. _Japanese_ and _English (Original)_ are the officially released games; _English (alternative)_ is a fan translation of the Japanese rom into English.
- Door handling: The randomizer closes all doors at the start of the game, even those that are already open in the original. When a door is opened, it may remain open or it may close behind you. Setting this to _Close_ will mean you need to remember which card was used for which door. Setting it to _Leave open_ means all doors will remain open, making it easier to see where you have already been. Finally _Don't change_ will only close doors that would close in the original game.
- Door code showing: For convenience this option will show the card which will open each door in its corner. Due to space restrictions in the ROM, this has only been implemented for the original English ROM.
- Extreme mode: When enabled, guards don't drop items and only items which are required for reaching places are present. All other spots are empty (so there are no rations, and consumables can also be found only once).

## Notes
The story is ruined by this program.  Don't play the game this way unless you
are familiar with the original.

## What the randomizer does
In the randomizer, every area has an id. Those are shown in map.svg. Doors
separate areas, as do gas chambers, breakable walls and special events such as
the parachute drop. The randomizer contains information about which areas are
connected and how.

First the randomizer randomly accesses areas, starting at the entry point. It
stores the order in which the areas are accessed.

Then it distributes the time when the cards are found approximately evenly over
that list.

It will place each card in the last room that was opened with a card before it
is needed. Every new door is opened using the last card that is supposed to be
found. When something other than a card is required to access an area (for
example explosives to blow up a wall), those are similarly made available.

When all that is done, the items that have not been required are randomly
placed on the map (unless extreme mode is enabled). After that, the remaining
item spots are filled with consumables (unless extreme mode is enabled).

The items that drop when punching guards are also random consumables (unless
extreme mode is enabled).

# Finally
Please send any comments to [wijnen@debian.org](mailto:wijnen@debian.org), or
tweet to @MakerWijnen.

Enjoy this randomizer, or if it's not your thing, ignore it and do something
that you do like.
