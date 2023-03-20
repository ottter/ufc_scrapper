# UFC Scrapper

Gather information about UFC events and fighters with BeautifulSoup4

## Usage

Print fighters from next MAIN card

> `gather_event_info(future_event=0)[0]`

Print fighters from next PRELIM card

> `gather_event_info(future_event=0)[1]`

Print all scheduled upcoming events in order

> `gather_all_upcoming_cards()`

Print matchups from next MAIN card

> `create_fight_matchups(gather_event_info(future_event=0)[0])`

Print matchups from next PRELIM card

> `create_fight_matchups(gather_event_info(future_event=0)[1])`

Print ALL matchups from next event

> `create_fight_matchups(list(itertools.chain.from_iterable(gather_event_info(future_event=0))))`

Print odds for next MAIN card

> `create_odds_matchups(gather_odds_matchup(future_event=0)[0])`

Print odds for next MAIN card and include favorite

> `create_odds_matchups(gather_odds_matchups(mark_favorite=True)[0])`

Print all odds for next card in ordered and unlabelled list

> `gather_odds_matchups()`

Print all weightclasses

> `build_rankings()[0]`

Print rankings in a dictionary where the key is weight class and value is fighters in order. Keys are in same order as `build_rankings()[0]` output

> `build_rankings()[1]`
