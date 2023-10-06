import urllib.parse
import requests 
import json

class MapApiClient:
    def __init__(self) -> None:
        self.host = 'https://www.mapquestapi.com/'
        self.base_url = 'directions/v2/route'
        self.key = "dPAL0KsdhLcsxbykIwBGuRrweUS57x0I"

    def get_2_location_route(self, orig: str, dest: str) -> dict:
        try:
            json_data = requests.get(self._construct_url(orig, dest)).json()
            json_status = json_data["info"]["statuscode"]
            if json_status == 0:
                return {
                    "status": json_status,
                    "route": json_data["route"]
                }
            elif json_status == 402:
                return {
                    "status": json_status,
                    "error": "Invalid user inputs for one or both locations."
                }
            elif json_status == 611:
                return {
                    "status": json_status,
                    "error": "Missing an Entry for one or both locations."
                }
            
            return {
                "status": json_status,
                "error": "unknown error occured."
            }
        except Exception as ex:
            return {
                    "status": 500,
                    "error": str(ex),
                } 

    def _construct_url(self, orig: str, dest: str) -> str:
        main_api = self.host + self.base_url + "?"
        return main_api + urllib.parse.urlencode({
            "key": self.key, 
            "from": orig, 
            "to": dest
        })
