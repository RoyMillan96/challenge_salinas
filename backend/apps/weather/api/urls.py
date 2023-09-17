from django.urls import path
from apps.weather.api.wheater_viewsets import (
    CurrentConditionCityViewSets, HourForecastsCityViewSets, DayForecastsCityViewSets
)


urlpatterns = [
    path('current-conditions/', CurrentConditionCityViewSets.as_view(), name='current_conditions'),
    path('conditions-by-hours/', HourForecastsCityViewSets.as_view(), name='conditions_by_hours'),
    path('conditions-by-days/', DayForecastsCityViewSets.as_view(), name='conditions_by_days'),
]