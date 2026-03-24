import os
from dotenv import load_dotenv
import json
import requests
import time

load_dotenv()
api_key = os.getenv('API_KEY') #retreive api key from dotenv file
url = 'https://api.gamebrain.co/v1/games'

params = {
    'limit' : 10, #api limits ten results per request
    'offset' : 0,
    'filters' : json.dumps([{
        'key': 'platform',
        'values': [{'value': 'pc'}], # only retreive pc games
        'connection': 'OR'
        },
        {
        'key': 'release_date',
        'values': [{'value': 'last_year'}] #games from past year
        }
    ])
}

headers = {
    'x-api-key': api_key
}

all_games = [] #list for games
offset = 0
limit = 10

while True:
    params['offset'] = offset
    params['limit'] = limit
    
    response = requests.get(url, params=params, headers=headers) #get data from the api
    game_data = response.json()
    games = game_data.get('results',[])
    
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break
    
    if not games:
        break
    all_games.extend(games)
    offset += limit
    
    if offset >= game_data.get('total_results', 0) or offset >= 1000: #stop at api limit of 1000
        break
    
    time.sleep(0.5) #time between requests. API only allows 2 per second
    
with open('pc_games_last_year.json', 'w', encoding='utf-8') as f: #store data in local json file
    json.dump(all_games, f, indent=4) 
        
print(len(all_games))
print(response.status_code)