# UFC Scrapper

Gather information about UFC events and fighters with BeautifulSoup4

## Usage

Print fighters from next MAIN card

> `gather_next_event_info()[0]`

Print fighters from next PRELIM card

> `gather_next_event_info()[1]`

Print all scheduled upcoming events in order

> `gather_all_upcoming_cards()`

Print matchups from next MAIN card

> `create_matchups(gather_event_info(future_event=0)[0])`

Print matchups from next PRELIM card

> `create_matchups(gather_event_info(future_event=0)[1])`

Print ALL matchups from next event

> `create_matchups(list(itertools.chain.from_iterable(gather_event_info(future_event=0))))`
