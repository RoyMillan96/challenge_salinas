from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.weather.api.serializers import (
    CurrentConditionCitySerializer, DayForecastsCitySerializer, HourForecastsCitySerializer
)
from apps.weather.integrations import (
    SearchCity, CurrentConditionCity, DayForecastsConditionCity, HourForecastsConditionCity
)


class CurrentConditionCityViewSets(GenericAPIView):
    serializer_class = CurrentConditionCitySerializer
    integration_search_city = SearchCity()
    integration_current_location = CurrentConditionCity()

    def get(self, request, *args, **kwargs):
        """
            Obtains the current climate of a location.
        """
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            return Response({'message': 'User Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        
        search = request.query_params.get('search_city', None)
        city_key = self.integration_search_city.get_city_key(search, user_id)

        if city_key:
            current_condition = self.integration_current_location.get_current_condition(city_key, user_id)
            if current_condition:
                return Response(current_condition, status=status.HTTP_200_OK)
            return Response({'message': 'Data condition current location not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Data city search not found or an error occurred '}, status=status.HTTP_404_NOT_FOUND)



class DayForecastsCityViewSets(GenericAPIView):
    serializer_class = DayForecastsCitySerializer
    integration_day_forecats = DayForecastsConditionCity()

    def get(self, request, *args, **kwargs):
        """
            Gets the weather per day, since it is a test, the Weather api only allows us up to 12 hours per request only.
        """
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        integration_search_city = SearchCity()
        search = request.query_params.get('search_name', None)
        days = request.query_params.get('days', 1)
        city_key = integration_search_city.get_city_key(search, user_id)
        if city_key:
            forecasts_days = self.integration_day_forecats.get_forecasts_by_day(city_key, days, user_id)
            if forecasts_days is not None:
                return Response(forecasts_days, status=status.HTTP_200_OK)
            return Response({'message': 'Data forecasts by days not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Data city search not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)


class HourForecastsCityViewSets(GenericAPIView):
    serializer_class = HourForecastsCitySerializer
    integration_hours_forecasts = HourForecastsConditionCity()

    def get(self, request, *args, **kwargs):
        """
            gets the weather per hour, since it is a test, the Weather api only allows us up to 12 hours per request only.
        """
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        integration_search_city = SearchCity()
        search = request.query_params.get('search_name', None)
        hour = request.query_params.get('hours', 1)
        city_key = integration_search_city.get_city_key(search, user_id)
        if city_key:
            forecasts_hours = self.integration_hours_forecasts.get_forecasts_by_hour(city_key, hour, user_id)
            if forecasts_hours is not None:
                return Response(forecasts_hours, status=status.HTTP_200_OK)
            return Response({'message': 'Data forecasts by hours not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Data city search not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)