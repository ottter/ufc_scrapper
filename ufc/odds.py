from bs4 import BeautifulSoup
from ufc.events import build_next_card_url

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