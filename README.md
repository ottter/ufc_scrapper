# UFC Scrapper

Gather information about UFC events and fighters with BeautifulSoup4

## Usage

Gather fighters from next MAIN card

> `gather_event_info(future_event=0)[0]`

Gather fighters from next PRELIM card

> `gather_event_info(future_event=0)[1]`

Gather all scheduled upcoming events in order

> `gather_all_upcoming_cards()`

Gather matchups from next MAIN card

> `create_fight_matchups(gather_event_info(future_event=0)[0])`

Gather matchups from next PRELIM card

> `create_fight_matchups(gather_event_info(future_event=0)[1])`

Gather ALL matchups from next event

> `create_fight_matchups(list(itertools.chain.from_iterable(gather_event_info(future_event=0))))`

Gather odds for next MAIN card

> `create_odds_matchups(gather_odds_matchups(future_event=0)[0])`

Gather odds for next MAIN card and include favorite

> `create_odds_matchups(gather_odds_matchups(mark_favorite=True)[0])`

Gather all odds for next card in ordered and unlabelled list

> `gather_odds_matchups()`

Gather all weightclasses

> `build_rankings()[0]`

Gather rankings in a dictionary where the key is weight class and value is fighters in order. Keys are in same order as `build_rankings()[0]` output

> `build_rankings()[1]`

Gather ordered list of all currently ranked fighters

> `ranked_list()`

Gather ranking order of specific weightclasses. Certain aliases are accepted in place of full key name in rank dictionary

> `weightclass_rankings(weightclass='mw', mark_champion=True, numerate_fighters=True)`

## Optional Arguments

| Function   | Argument | Action |
|------------|----------|--------|
| weightclass_rankings | weightclass   | (Str) weightclass alias. Default: 'pfp'    |
| weightclass_rankings | mark_champion   | (Bool) Label the champion in Rankings list. Default: False    |
| weightclass_rankings | numerate_fighters      | (Bool) Label all ranked fighters. Default: False    |
| gather_odds_matchups     | mark_favorite      | (Bool) Label the favorite in a bout. Default: False   |
| gather_odds_matchups     | future_event      | (Int) How many events in future to look* Default: 0 (next event)  |

* Note that the further out the event means the less info about an event is known
