import requests
import config
import json



def name_to_json(name, region):
    """
    Takes in a summoner name, and requests from the LeagueAPI
    name: valid summoner name in string form
    region: defaults to na1, but can lookup in a variety of regions
    """
    #TODO Add region checking function
    request_by_name = requests.get(
        f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={config.DEVELOPER_API_KEY}")
    #TODO Add more error parsing/correcting for requests
    if request_by_name.status_code != 200:
        raise Exception(f"Bad request in name_to_json: {request_by_name.status_code}")
    return request_by_name.json()

def generate_matchlist(name, region="na1"):
    #TODO Add region checking function
    json_response = name_to_json(name, region)
    account_id = json_response['accountId']
    request_response = requests.get(
        f"https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?api_key={config.DEVELOPER_API_KEY}"
    )
    #TODO Add request error checking
    return request_response.json()
    
matches = generate_matchlist('name')['matches']
for match in matches:
    print(match)