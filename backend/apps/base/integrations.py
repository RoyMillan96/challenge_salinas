from backend.settings.base import BASE_URL_WEATHER, API_KEY_WEATHER

class ExternalApi:
    def __init__(self):
        self.api_key = API_KEY_WEATHER
        self.api_url = BASE_URL_WEATHER
