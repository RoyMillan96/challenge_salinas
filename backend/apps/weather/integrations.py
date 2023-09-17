import requests
from requests.exceptions import HTTPError

from django.core.cache import cache
from django.http import HttpResponse

from apps.base.integrations import ExternalApi
from apps.weather.tools import clean_data, clean_data_forecasts

class SearchCity:
    client = ExternalApi()
    api_key = client.api_key
    api_url = client.api_url + 'locations/v1/cities/search'

    def get_city_key(self, name_city, user_id):
        cache_key = 'user_search_city_key_{}_{}'.format(user_id, name_city)
        user_has_city_key = cache.get(cache_key, {})
        if not user_has_city_key:
            params = {
                'q': name_city,
                'apikey': self.api_key
            }
            try:
                response = requests.get(self.api_url, params=params)
                if response.ok:
                    data = response.json()
                    user_has_city_key = data[0]['Key']
                    cache.set(cache_key, user_has_city_key, 60 * 60)
            except HTTPError as http_error:  # Captura específicamente excepciones HTTP
                return HttpResponse('Error HTTP: ' + str(http_error), status=500)
            except Exception as error:
                return HttpResponse('Error HTTP: ' + str(error), status=400)
        return user_has_city_key


class CurrentConditionCity:
    client = ExternalApi()
    api_key= client.api_key
    api_url = client.api_url + 'currentconditions/v1/'

    def get_current_condition(self, key_location, user_id):
        cache_key = 'user_current_condition_{}_{}'.format(user_id, key_location)
        user_has_current_condition = cache.get(cache_key, {})
        if not user_has_current_condition:
            self.api_url += key_location
            params = {
                'apikey': self.api_key
            }

            try:
                response = requests.get(self.api_url, params=params)
                if response.ok:
                    user_has_current_condition = clean_data(response.json())
                    cache.set(cache_key, user_has_current_condition, 60 * 60)
            except HTTPError as http_error:  # Captura específicamente excepciones HTTP
                return HttpResponse('Error HTTP: ' + str(http_error), status=500)
            except Exception as error:
                return HttpResponse('Error HTTP: ' + str(error), status=400)
        return user_has_current_condition


class DayForecastsConditionCity:
    client = ExternalApi()
    api_key= client.api_key
    api_url = client.api_url + 'forecasts/v1/daily/'

    def get_forecasts_by_day(self, key_location, days, user_id):
        cache_key = 'user_forecast_by_day_{}_{}'.format(key_location, user_id)
        user_has_forecast = cache.get(cache_key, {})
        if not user_has_forecast:
            self.api_url += '{}day/{}'.format(days, key_location)
            params = {
                'apikey': self.api_key
            }
            try:
                response = requests.get(self.api_url, params=params)
                if response.ok:
                    user_has_forecast = clean_data_forecasts(response.json())
                    cache.set(cache_key, user_has_forecast, 60 * 60)
            except HTTPError as http_error:  # Captura específicamente excepciones HTTP
                return HttpResponse('Error HTTP: ' + str(http_error), status=500)
            except Exception as error:
                return HttpResponse('Error HTTP: ' + str(error), status=400)
        return user_has_forecast


class HourForecastsConditionCity:
    client = ExternalApi()
    api_key= client.api_key
    api_url = client.api_url + 'forecasts/v1/hourly/'

    def get_forecasts_by_hour(self, key_location, hour, user_id):
        cache_key = 'user_forecast_by_hour_{}_{}'.format(key_location, user_id)
        user_has_forecast_hours = cache.get(cache_key, {})
        if not user_has_forecast_hours:
            self.api_url += '{}hour/{}'.format(hour, key_location)
            params = {
                'apikey': self.api_key
            }
            try:
                response = requests.get(self.api_url, params=params)
                if response.ok:
                    user_has_forecast_hours = clean_data(response.json())
                    cache.set(cache_key, user_has_forecast_hours, 60 * 60)
            except HTTPError as http_error:  # Captura específicamente excepciones HTTP
                return HttpResponse('Error HTTP: ' + str(http_error), status=500)
            except Exception as error:
                return HttpResponse('Error HTTP: ' + str(error), status=400)
        return user_has_forecast_hours