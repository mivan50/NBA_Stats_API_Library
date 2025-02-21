import requests


class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.base_url = "http://127.0.0.1:5000"

    def get_season_stats(self, year):
        url = f"{self.base_url}/player/{self.first_name}/{self.last_name}/{year}/stats/season"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_career_stats(self):
        url = f"{self.base_url}/player/{self.first_name}/{self.last_name}/stats/career"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None