from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.weather.models import WeatherData, WeatherDataDay

from apps.weather.api.serializers import (
    CurrentConditionCitySerializer, DayForecastsCitySerializer, HourForecastsCitySerializer,
    WeatherDataSerializer, WeatherDataDaySerializer
)
from apps.weather.integrations import (
    SearchCity, CurrentConditionCity, DayForecastsConditionCity, HourForecastsConditionCity
)


class CurrentConditionCityGeneric(GenericAPIView):
    serializer_class = CurrentConditionCitySerializer
    integration_search_city = SearchCity()
    integration_current_location = CurrentConditionCity()

    def post(self, request, *args, **kwargs):
        """
            Obtains the current climate of a location and saved data of weather by user.
        """
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            return Response({'message': 'User Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        search = request.query_params.get('search_city', None)
        city_key = self.integration_search_city.get_city_key(search, user_id)

        if city_key:
            current_condition = self.integration_current_location.get_current_condition(city_key, user_id, search)
            if current_condition:
                serializer = WeatherDataSerializer(data=current_condition, many=True)
                if serializer.is_valid():
                    for data in current_condition:
                        DateTime = data['DateTime']
                        country = data['country']
                        if not WeatherData.objects.filter(user_id=user_id, country=country, DateTime=DateTime).exists():
                            serializer.save()
                    return Response(
                        {
                            'data': serializer.data,
                            'message': 'Data saved successfully'
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response({'message': 'there are data already recorded with this information'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data condition current location not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Data city search not found or an error occurred '}, status=status.HTTP_404_NOT_FOUND)



class DayForecastsCityGeneric(GenericAPIView):
    serializer_class = DayForecastsCitySerializer
    integration_day_forecats = DayForecastsConditionCity()
    integration_search_city = SearchCity()

    def post(self, request, *args, **kwargs):
        """
            Gets the weather per day, since it is a test, the Weather api only allows us up to 12 hours per request only.
        """
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        search = request.query_params.get('search_name', None)
        days = request.query_params.get('days', 1)
        city_key = self.integration_search_city.get_city_key(search, user_id)

        if city_key:
            forecasts_days = self.integration_day_forecats.get_forecasts_by_day(city_key, days, user_id, search)
            if forecasts_days:
                serializer = WeatherDataDaySerializer(data=forecasts_days, many=True)
                if serializer.is_valid():
                    for data in forecasts_days:
                        DateTime = data['DateTime']
                        country = data['Country']
                        if not WeatherDataDay.objects.filter(user_id=user_id, Country=country, DateTime=DateTime).exists():
                            serializer.save()
                    return Response(
                        {
                            'data': serializer.data,
                            'message': 'Data saved successfully'
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response({'message': 'there are data already recorded with this information'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data forecasts by days not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Data city search not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)


class HourForecastsCityGeneric(GenericAPIView):
    serializer_class = HourForecastsCitySerializer
    integration_hours_forecasts = HourForecastsConditionCity()

    def post(self, request, *args, **kwargs):
        """
            gets the weather per hour, since it is a test, the Weather api only allows us up to 12 hours 
            per request only and saved data of weather by user.
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
            forecasts_hours = self.integration_hours_forecasts.get_forecasts_by_hour(city_key, hour, user_id, search)
            if forecasts_hours is not None:
                serializer = WeatherDataSerializer(data=forecasts_hours, many=True)
                if serializer.is_valid():
                    for data in forecasts_hours:
                        DateTime = data['DateTime']
                        country = data['country']
                        if not WeatherData.objects.filter(user_id=user_id, country=country, DateTime=DateTime).exists():
                            serializer.save()
                    return Response(
                        {
                            'data': serializer.data,
                            'message': 'Data saved successfully'
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response({'message': 'there are data already recorded with this information'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Data forecasts by hours not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Data city search not found or an error occurred'}, status=status.HTTP_404_NOT_FOUND)
    

class UserDetailWeatherCurrents(generics.ListAPIView):
    """
        Gets all the searches made by the user on the current weather and can be filtered by day and city.
    """
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        else:
            return WeatherData.objects.none()

        queryset = WeatherData.objects.filter(user_id=user_id)

        country = self.request.query_params.get('country', None)
        date = self.request.query_params.get('datetime', None)

        if country:
            queryset = queryset.filter(country=country)
        if date:
            queryset = queryset.filter(DateTime=date)

        if not queryset.exists():
            return None

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if queryset is None:
            return Response({'message': 'Response not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class UserDetailWeatherForecasts(generics.ListAPIView):
    """
        Gets all the searches made by the user on the forecasts and can be filtered by day and city.
    """
    serializer_class = WeatherDataDaySerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        else:
            return WeatherDataDay.objects.none()

        queryset = WeatherDataDay.objects.filter(user_id=user_id)
        country = self.request.query_params.get('country', None)
        date = self.request.query_params.get('datetime', None)

        if country:
            queryset = queryset.filter(Country=country)
        if date:
            queryset = queryset.filter(DateTime=date)

        if not queryset.exists():
            return None

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if queryset is None:
            return Response({'message': 'Response not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    