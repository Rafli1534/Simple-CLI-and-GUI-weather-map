def wind_direction(deg: float, lang: str = 'en') -> str:
    if lang == 'ru':
        dirs = [
            'Северный', 
            'Северо-Восточный', 
            'Восточный', 'Юго-Восточный', 
            'Южный', 
            'Юго-Западный', 
            'Западный', 
            'Северо-Западный',

        ]
    elif lang == 'ua':
        dirs = [
            'Північний', 
            'Північно-Східний', 
            'Східний', 
            'Південно-Східний', 
            'Південний', 
            'Південно-Західний', 
            'Західний', 
            'Північно-Західний',
        
        ]
    else:
        dirs = [
            'North', 
            'North-East', 
            'East', 
            'South-East', 
            'South', 
            'South-West', 
            'West', 
            'North-West',
        
        ]
    ix = int((deg + 22.5) // 45) % 8
    return dirs[ix]

def russian(city, data, unit, lang) -> None:
    print('\n')
    print(f"Местоположение: {city}, {data['country']}")
    if unit == 'metric':
        print(f"Температура: {data['temp']}°C")
        print(f"Ощущается как: {data['feels_like']}°C")
    elif unit == 'imperial':
        print(f"Температура: {data['temp']}°F")
        print(f"Ощущается как: {data['feels_like']}°F")
    else:
        print(f"Температура: {data['temp']}°K")
        print(f"Ощущается как: {data['feels_like']}°K")
    print(f"Погода: {data['description'].title()}")
    print(f"Давление: {data['pressure']} гПа")
    print(f"Влажность: {data['humidity']}%")
    print(f"Направление ветра: {wind_direction(
        data['wind_deg'], 
        lang,
        )} Ветер")
    print(f"Скорость ветра: {data['wind_speed']} м/с")

def ukrainian(city, data, unit, lang) -> None:
    print('\n')
    print(f"Місцеположення: {city}, {data['country']}")
    if unit == 'metric':
        print(f"Температура: {data['temp']}°C")
        print(f"Відчувається як: {data['feels_like']}°C")
    elif unit == 'imperial':
        print(f"Температура: {data['temp']}°F")
        print(f"Відчувається як: {data['feels_like']}°F")
    else:
        print(f"Температура: {data['temp']}°K")
        print(f"Відчувається як: {data['feels_like']}°K")
    print(f"Погода: {data['description'].title()}")
    print(f"Тиск: {data['pressure']} гПа")
    print(f"Вологість: {data['humidity']}%")
    print(f"Напрям вітру: {wind_direction(
        data['wind_deg'],
        lang,
        )} Вітер")
    print(f"Швидкість вітру: {data['wind_speed']} м/с")

def english(city, data, unit, lang) -> None:
    print('\n')
    print(f"Location: {city}, {data['country']}")
    if unit == 'metric':
        print(f"Temperature: {data['temp']}°C")
        print(f"Feels like: {data['feels_like']}°C")
    elif unit == 'imperial':
        print(f"Temperature: {data['temp']}°F")
        print(f"Feels like: {data['feels_like']}°F")
    else:
        print(f"Temperature: {data['temp']}°K")
        print(f"Feels like: {data['feels_like']}°K")
    print(f"Weather: {data['description'].title()}")
    print(f"Pressure: {data['pressure']} hPa")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind direction: {wind_direction(
        data['wind_deg'], 
        lang,
        )}")
    print(f"Wind speed: {data['wind_speed']} mps")

def print_weather_by_lang(city, data, unit, lang):
    lang_map = {'ru': russian, 'ua': ukrainian}
    printer = lang_map.get(lang, english) 
    # если нету lang, поумолчанию - en
    printer(city, data, unit, lang)

def print_forecast_ru(forecast) -> None:
    print('\nПрогноз:')
    for day, info in sorted(forecast.items()):
        min_t = info.get('min')
        max_t = info.get('max')
        desc = info.get('desc') or ''
        print(f"{day}: {min_t}..{max_t}, {desc}")

def print_forecast_ua(forecast) -> None:
    print('\nПрогноз:')
    for day, info in sorted(forecast.items()):
        min_t = info.get('min')
        max_t = info.get('max')
        desc = info.get('desc') or ''
        print(f"{day}: {min_t}..{max_t}, {desc}")

def print_forecast_en(forecast) -> None:
    print('\nForecast:')
    for day, info in sorted(forecast.items()):
        min_t = info.get('min')
        max_t = info.get('max')
        desc = info.get('desc') or ''
        print(f"{day}: {min_t}..{max_t}, {desc}")

def print_forecast_by_lang(forecast, lang):
    if lang == "ru":
        print_forecast_ru(forecast)
    elif lang == "ua":
        print_forecast_ua(forecast)
    else:
        print_forecast_en(forecast)
