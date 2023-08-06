import requests
from getgeo.base import GetGeoBase


class GetGeoData(GetGeoBase):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

        self.ipv4_ipv6_lookup = "https://api.getgeoapi.com/v2/ip"

    def get_geo_data(self, ip_address: str):
        parameters = {"api_key": self.api_key, "format": "json"}

        url = f"{self.ipv4_ipv6_lookup}/{ip_address}"

        response = requests.get(url, parameters)

        geo_data = response.json()

        return geo_data
