from rest_framework import serializers

from ..models import WeatherData, WeatherDataDay

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class WeatherDataDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataDay
        fields = '__all__'

class CurrentConditionCitySerializer(serializers.Serializer):
    search_city = serializers.CharField(max_length=50, required=True)


class DayForecastsCitySerializer(serializers.Serializer):
    search_name = serializers.CharField(max_length=50, required=True)
    days = serializers.IntegerField(required=False)


class HourForecastsCitySerializer(serializers.Serializer):
    search_name = serializers.CharField(max_length=50, required=True)
    hours = serializers.IntegerField(required=False)