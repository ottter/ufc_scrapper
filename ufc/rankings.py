from bs4 import BeautifulSoup
import requests

HEADERS = {
    'User-Agent': 'goofcon 3'
    }

def build_ranking_url():
    """Send request to the UFC events page"""
    base_url = "https://www.ufc.com/rankings"
    return requests.get(base_url, headers = HEADERS)

def gather_champions():
    champions = []
    soup = BeautifulSoup(build_ranking_url().content, features="html.parser")
    for grouping in soup.find_all('div', {'class': 'rankings--athlete--champion'}):
        for group in grouping.find_all('h5'):
            champions.append(group.text)
    return champions

def build_rankings():
    weightclass = []
    fighter_rank = []
    soup = BeautifulSoup(build_ranking_url().content, features="html.parser")
    for grouping in soup.find_all('div', {'class': 'view-athlete-rankings'}):
        # Create the weightclass list
        for group in grouping.find_all('div', {'class': 'view-grouping-header'}):
            weightclass.append(group.text)
        # Create the fighter list
        for group in grouping.find_all('td', {'class': 'views-field-title'}):
            fighter_rank.append(group.text)
    
    # 'i' and 'k' are for weight classes. 'j' is for list of fighters
    i, j, k = 0, 0, 0
    rankings_dict = {}
    for x in range(len(fighter_rank) // 15):
        sublist = []                            # sublist is meant to be emptied after each 15 are iterated through
        for y in range(15):
            sublist.append(fighter_rank[k])     # loop that creates a list of 15 and adds it to matching weightclass
            k = k + 1
        sublist.insert(0, gather_champions()[j])
        rankings_dict[weightclass[j]] = sublist # Update the dictionary with the list of ranked fighters
        i = i + 15                              # Iterate through list by +15 (fighters) and +1 (classes)
        j = j + 1

    return weightclass, rankings_dict