# UFC Scrapper

Gather information about UFC events and fighters with BeautifulSoup4

## Usage

| Action   | Request |
|------------|----------|
| Get fighters on next main card    | get_event(card='main', format='fighters', next_event=0)       |
| Get matchups on next main card    | get_event(card='main', format='matchups', next_event=0)       |
| Get matchups on next prelim card  | get_event(card='prelim', format='matchups', next_event=0)     |
|                                   |                                                               |
| Get all upcoming events           | gather_all_upcoming_cards(schedule=True)                      |
|                                   |                                                               |
| Get all ranked fighters in all classes  | ranked_list()                                           |
| Get all weight classes (incl p4p) | weightclass_rankings(weightclass='ranklist')                  |
| Get all ranked classes (incl p4p) | weightclass_rankings(weightclass='all')                       |
| Get Middleweight rankings         | weightclass_rankings(weightclass='mw')                        |
|    ... and label champion         | weightclass_rankings(weightclass='mw', mark_champion=True)    |
|    ... and/or number fighters     | weightclass_rankings(weightclass='mw', numerate_fighters=True)|
|                                   |                                                               |
| Get odds for next MAIN card       | create_odds_matchups(card='main')                             |
|    ... and include favorite       | create_odds_matchups(card='main', mark_favorite=True)         |
| Gather all odds for next card     | gather_odds_matchups()                                        |

### Optional Arguments

| Function   | Argument | Action |
|------------|----------|--------|
| get_event                 | card              | (Str) Choose to look at main or prelims. Default: 'main'          |
| get_event                 | format            | (Str) Choose matchups or list fighters. Default: 'matchups'       |
| get_event                 | next_event        | (Int) How many events in future to look at. Default: 0            |
|                           |                                                                                       |
| weightclass_rankings      | weightclass       | (Str) weightclass alias. Default: 'pfp'                           |
| weightclass_rankings      | mark_champion     | (Bool) Label the champion in Rankings list. Default: False        |
| weightclass_rankings      | numerate_fighters | (Bool) Label all ranked fighters. Default: False                  |
|                           |                                                                                       |
| gather_all_upcoming_cards | schedule          | (Bool) Truncate event listing for better viewing                  |
|                           |                                                                                       |
| create_odds_matchups      | card              | (Str) Choose to look at main or prelims. Default: 'main'          |
| create_odds_matchups      | mark_favorite     | (Bool) Label the favorite in a bout. Default: False               |
| create_odds_matchups      | next_event        | (Int) How many events in future to look* Default: 0 (next event)  |
| gather_odds_matchups      | mark_favorite     | (Bool) Label the favorite in a bout. Default: False               |
| gather_odds_matchups      | next_event        | (Int) How many events in future to look* Default: 0 (next event)  |

* Note that the further out the event means the less info about an event is known

### `create_odds_matchups()` *vs* `gather_odds_matchups()`

```python
print(gather_odds_matchups())       # List of lists of the entire card for the next main event
(['+135', '-155', '-', ... , '+140'], ['+170', '-200', '+190', ... , '-'])
print(create_odds_matchups())       # Combined matchup in a list of the main or prelim card (default is main event)
['+135 [odds] -155', '- [odds] -', '-155 [odds] +135', '+175 [odds] -205', '-165 [odds] +140']
```
