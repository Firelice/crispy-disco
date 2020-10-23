import requests
import config
import json

class LeagueRequests:
    def request_by_name(self, name, region="na1"):
        request_by_name = requests.get(
            f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={config.DEVELOPER_API_KEY}")
        if request_by_name.status_code != 200:
            raise Exception("Bad request")
        requested_json = request_by_name.json()
        print(requested_json['id'])
    
s = LeagueRequests()
s.request_by_name("fleets300")