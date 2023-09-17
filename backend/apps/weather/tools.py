def convert_fahrenheit_to_celsius(degrees_fahrenheit):
    celsius = round((degrees_fahrenheit - 32) / 1.8, 1)
    unit = 'C'
    return celsius, unit

def clean_data(data_json, user_id, country):
    data = []
    for weather in data_json:
        if weather.get('Temperature').get('Unit') == 'F':
            temperature, unit = convert_fahrenheit_to_celsius(weather.get('Temperature').get('Value'))
        else:
            temperature = weather.get('Temperature').get('Metric').get('Value')
            unit = weather.get('Temperature').get('Metric').get('Unit')

        data_dict = {
            'user': user_id,
            'DateTime': weather.get('LocalObservationDateTime') if weather.get('LocalObservationDateTime') else weather.get('DateTime'),
            'WeatherText': weather.get('WeatherText') if weather.get('WeatherText') else weather.get('IconPhrase'),
            'IsDayTime': weather.get('IsDayTime') if weather.get('IsDayTime') else weather.get('IsDaylight'),
            'Temperature': temperature,
            'Unit': unit,
            'country': country
        }
        data.append(data_dict)
    return data


def clean_data_forecasts(data_json, user_id, country):
    data = []
    for weather in data_json['DailyForecasts']:
        temperature_min, unit = convert_fahrenheit_to_celsius(weather.get('Temperature').get('Minimum').get('Value'))
        temperature_max, unit = convert_fahrenheit_to_celsius(weather.get('Temperature').get('Maximum').get('Value'))

        data_dict = {
            'user': user_id,
            'DateTime': weather.get('Date'),
            'Temperature_min': temperature_min,
            'Temperature_max': temperature_max,
            'Unit':  unit,
            'Day': weather.get('Day').get('IconPhrase'),
            'Night': weather.get('Night').get('IconPhrase'),
            'country': country
        }
        data.append(data_dict)
    return data
