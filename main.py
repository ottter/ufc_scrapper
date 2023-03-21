from ufc.events import *
from ufc.odds import *
from ufc.rankings import *
from ufc.fighters import *

# Example
mw = weightclass_rankings(weightclass='mw', mark_champion=True, numerate_fighters=True)
for x in mw:
    print(x)