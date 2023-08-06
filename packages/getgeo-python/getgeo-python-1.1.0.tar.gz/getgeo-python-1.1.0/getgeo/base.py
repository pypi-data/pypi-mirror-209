import requests


class GetGeoBase:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

        self.requester_ip_lookup = "https://api.getgeoapi.com/v2/ip/check"

    def get_my_geo_data(self):
        parameters = {"api_key": self.api_key, "format": "json"}

        url = self.requester_ip_lookup

        response = requests.get(url, parameters)

        geo_data = response.json()

        return geo_data
