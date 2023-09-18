from django.urls import path
from apps.weather.api.weather_viewsets import (
    CurrentConditionCityGeneric, HourForecastsCityGeneric, DayForecastsCityGeneric,
    UserDetailWeatherCurrents, UserDetailWeatherForecasts
)


urlpatterns = [
    path('current-conditions/', CurrentConditionCityGeneric.as_view(), name='current_conditions'),
    path('conditions-by-hours/', HourForecastsCityGeneric.as_view(), name='conditions_by_hours'),
    path('conditions-by-days/', DayForecastsCityGeneric.as_view(), name='conditions_by_days'),
    path('currents-user-detail/', UserDetailWeatherCurrents.as_view(), name='weatherdata-list'),
    path('forecast-user-detail/', UserDetailWeatherForecasts.as_view(), name='weatherdata-list'),
]