from rest_framework import serializers

from ..models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        exclude = '__all__'

class CurrentConditionCitySerializer(serializers.Serializer):
    search_city = serializers.CharField(max_length=50, required=True)


class DayForecastsCitySerializer(serializers.Serializer):
    search_name = serializers.CharField(max_length=50, required=True)
    days = serializers.IntegerField(required=False)


class HourForecastsCitySerializer(serializers.Serializer):
    search_name = serializers.CharField(max_length=50, required=True)
    hours = serializers.IntegerField(required=False)