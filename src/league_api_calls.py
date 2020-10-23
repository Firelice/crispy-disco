import requests
import config
import json



def name_to_json(name, region="na1"):
    """
    Takes in a summoner name, and requests from the LeagueAPI
    name: valid summoner name in string form
    region: defaults to na1, but can lookup in a variety of regions
    """
    #TODO Add region checking
    request_by_name = requests.get(
        f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={config.DEVELOPER_API_KEY}")
    #TODO Add more error parsing/correcting
    if request_by_name.status_code != 200:
        raise Exception(f"Bad request: {request_by_name.status_code}")
    requested_json = request_by_name.json()
    return requested_json

def json_to_matchlist(json_response, region="na1"):
    json_id = json_response['id']
    
print(name_to_json("AetherfIow"))