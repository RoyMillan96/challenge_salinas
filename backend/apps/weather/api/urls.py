from django.urls import path
from apps.weather.api.weather_viewsets import (
    CurrentConditionCityGeneric, HourForecastsCityGeneric, DayForecastsCityGeneric
)


urlpatterns = [
    path('current-conditions/', CurrentConditionCityGeneric.as_view(), name='current_conditions'),
    path('conditions-by-hours/', HourForecastsCityGeneric.as_view(), name='conditions_by_hours'),
    path('conditions-by-days/', DayForecastsCityGeneric.as_view(), name='conditions_by_days'),
]