import requests
import itertools
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'goofcon 3'
    }

def build_events_url():
    """Send request to the UFC events page"""
    base_url = "https://www.ufc.com/events"
    return requests.get(base_url, headers = headers)

def build_next_card_url(event):
    """Send request to the event page of upcoming card"""
    base_url = "https://www.ufc.com"
    next_card = gather_all_upcoming_cards()[event]
    return requests.get(base_url + next_card, headers = headers)

def gather_all_upcoming_cards():
    """Return a list of all upcoming cards"""
    upcoming_cards = []
    soup = BeautifulSoup(build_events_url().content, features="html.parser")
    for link in soup.find_all('details', {'id': 'events-list-upcoming'}):
        for href in link.find_all('a', href=True):
            if href.has_attr('href') and href['href'].startswith('/event/') and "#" not in href['href']:
                upcoming_cards.append(href['href'])
    return list(dict.fromkeys(upcoming_cards))

def gather_event_info(future_event=0):
    """Gather info about a requested upcoming event
    
    :param int future_event: X events in future to look up, default 0. Max range varies
    """
    main_fighter_list = []
    prelim_fighter_list = []
    if future_event not in range(len(gather_all_upcoming_cards())):
        return "Requested event is not in range of scheduled events"
    soup = BeautifulSoup(build_next_card_url(future_event).content, features="html.parser")
    for x in [[main_fighter_list, 'main-card'], [prelim_fighter_list, 'prelims-card']]:
        # NOTE: Works only for soonest upcoming event. Future events use different format: div class="l-main"
        for matchup in soup.find_all('div', {'id': x[1]}):
            for matchup in matchup.find_all('a', href=True):
                if '/athlete/' in matchup['href']:
                    x[0].append(matchup['href']
                                        .removeprefix('https://www.ufc.com/athlete/')
                                        .replace("-", " ")
                                        .title())
    return list(dict.fromkeys(main_fighter_list)), list(dict.fromkeys(prelim_fighter_list))

def create_matchups(card):
    """Match the fighters with respective opponent (since scraper gets the fighter names and not matchups)    
    
    :param str card: 
    """
    if len(card) % 2 != 0:
        return "Error: Official website has matchups out of order. Check again later"
    matchups = []
    i = 0
    for x in range(len(card) // 2):
        matchups.append(f"{card[i]} vs {card[i+1]}")
        i = i + 2
    return matchups

def gather_odds_matchups(future_event=0, mark_favorite=False):
    """Create list of odds for upcoming event, ordered and unlabeled.
    
    :param int future_event: X events in future to look up, default 0. Max range varies
    :param bool mark_favorite: Choose whether to add betting odds favorite indicator
    """
    main_odds_list = []
    prelim_odds_list = []
    soup = BeautifulSoup(build_next_card_url(future_event).content, features="html.parser")
    for x in [[main_odds_list, 'main-card'], [prelim_odds_list, 'prelims-card']]:
        # NOTE: Works only for soonest upcoming event. Future events use different format: div class="l-main"
        for matchup in soup.find_all('div', {'id': x[1]}):
            for matchup in matchup.find_all('span', {'class': "c-listing-fight__odds-amount"}):
                is_favorite = ''
                if mark_favorite and "-" in matchup.text and len(matchup.text) > 1:
                    is_favorite = " (Favorite)"
                x[0].append(matchup.text + is_favorite)
    return main_odds_list, prelim_odds_list

def create_odds_matchups(card):
    """Match the fighter's odds with respective opponent
    
    :param str card: 
    """
    if len(card) % 2 != 0:
        return "Error: Official website has matchups out of order. Check again later"
    matchups = []
    i = 0
    for x in range(len(card) // 2):
        matchups.append(f"{card[i]} [odds] {card[i+1]}")
        i = i + 2
    return matchups

#### Print matchups from next MAIN card
print(create_matchups(gather_event_info()[0]))
print(create_odds_matchups(gather_odds_matchups()[0]))
