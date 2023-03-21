# UFC Scrapper

Gather information about UFC events and fighters with BeautifulSoup4

## Usage

| Action   | Request |
|------------|----------|
| Get fighters on next main card    | get_event(card='main', format='fighters', next_event=0)       |
| Get matchups on next main card    | get_event(card='main', format='matchups', next_event=0)       |
| Get matchups on next prelim card  | get_event(card='prelim', format='matchups', next_event=0)     |
| Get all upcoming events           | gather_all_upcoming_cards(schedule=True)                      |
| Get all ranked fighters by class  | ranked_list()                                                 |
| Get all weight classes (incl p4p) | weightclass_rankings(weightclass='ranklist')                  |
| Get all ranked classes (incl p4p) | weightclass_rankings(weightclass='all')                       |
| Get Middleweight rankings         | weightclass_rankings(weightclass='mw')                        |
|    ...and label champion          | weightclass_rankings(weightclass='mw', mark_champion=True)    |
|    ...and/or number fighters      | weightclass_rankings(weightclass='mw', numerate_fighters=True)|

Gather odds for next MAIN card

> `create_odds_matchups(gather_odds_matchups(future_event=0)[0])`

Gather odds for next MAIN card and include favorite

> `create_odds_matchups(gather_odds_matchups(mark_favorite=True)[0])`

Gather all odds for next card in ordered and unlabelled list

> `gather_odds_matchups()`

## Optional Arguments

| Function   | Argument | Action |
|------------|----------|--------|
| get_event                 | card              | (Str) Choose to look at main or prelims. Default: 'main'          |
| get_event                 | format            | (Str) Choose matchups or list fighters. Default: 'matchups'       |
| get_event                 | next_event        | (Int) How many events in future to look at. Default: 0            |
| weightclass_rankings      | weightclass       | (Str) weightclass alias. Default: 'pfp'                           |
| weightclass_rankings      | mark_champion     | (Bool) Label the champion in Rankings list. Default: False        |
| weightclass_rankings      | numerate_fighters | (Bool) Label all ranked fighters. Default: False                  |
| gather_all_upcoming_cards | schedule          | (Bool) Truncate event listing for better viewing                  |
| gather_odds_matchups      | mark_favorite     | (Bool) Label the favorite in a bout. Default: False               |
| gather_odds_matchups      | future_event      | (Int) How many events in future to look* Default: 0 (next event)  |

* Note that the further out the event means the less info about an event is known
