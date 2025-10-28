import requests
from project.utils import (
    get_city_from_params, 
    get_lang_from_params, 
    get_unit_from_params,
    
    )
from project.language import (
    print_weather_by_lang, 
    print_forecast_ru, 
    print_forecast_ua, 
    print_forecast_en, 
    print_forecast_by_lang,
    
    )

def build_weather_request(
        appid_key: str,
        mode: str = 'current',
        city: str = '',
        units: str = 'metric',
        lang: str = 'en'
    ) -> tuple:
    """
    Build OpenWeather API request URL and parameters.

    Args:
        appid_key (str): OpenWeather API key.
        mode (str): 'current' or 'forecast'.
        city (str): City name.
        units (str): Units ('metric', 'standard', 'imperial').
        lang (str): Language code ('en', 'ru', 'ua').

    Returns:
        tuple: (URL, params) ready for requests.get
    """
    if mode == 'forecast':
        URL = 'https://api.openweathermap.org/data/2.5/forecast'
    else:
        URL = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'units': units,
        'lang': lang,
        'appid': appid_key
    }

    return URL, params

def fetch_weather(
        url: str, 
        params: dict, 
        timeout: float = 5.0, 
    ):
    """Perform HTTP GET to fetch weather.

    Returns requests.Response on success or raises 
    requests.RequestException on failure.
    """
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        return resp
    except requests.RequestException:
        raise

def error(resp) -> bool:
    ok = getattr(resp, 'status_code', None) == 200
    if not ok:
        print('Oops, sth went wrong :(')
        try:
            print(f'Status code: {resp.status_code} - {resp.text}')
        except Exception:
            pass
    return ok

def parse_weather(resp) -> dict:
    data = resp.json() if resp is not None else {} 
    #{} - защита от ошибки
    main = data.get('main') or {}
    system = data.get('sys') or {}
    wind = data.get('wind') or {}
    weather = (data.get('weather') or [])
    first_weather = weather[0] if weather else {}
    return {
        'city': data.get('name'),
        'country': system.get('country'),
        'temp': main.get('temp'),
        'feels_like': main.get('feels_like'),
        'pressure': main.get('pressure'),
        'humidity': main.get('humidity'),
        'description': first_weather.get('description'),
        'wind_deg': wind.get('deg'),
        'wind_speed': wind.get('speed'),
        '_raw': data,
    }

def parse_forecast(resp) -> dict:
    """Parse 5-day/3-hour forecast response into daily min/max 
    and common description."""
    data = resp.json() if resp is not None else {}
    items = data.get('list') or []
    daily = {}
    for it in items:
        dt_txt = it.get('dt_txt')
        if not dt_txt:
            continue
        day = dt_txt.split(' ')[0]
        main = it.get('main') or {}
        temp = main.get('temp')
        weather = (it.get('weather') or [])
        desc = weather[0].get('description') if weather else None
        rec = daily.setdefault(day, {
            'min': None, 
            'max': None, 
            'desc_counts': {},

        })
        if temp is not None:
            if rec['min'] is None or temp < rec['min']:
                rec['min'] = temp
            if rec['max'] is None or temp > rec['max']:
                rec['max'] = temp
        if desc:
            rec['desc_counts'][desc] = rec['desc_counts'].get(
                desc, 
                0,

            ) + 1
    summary = {}
    for day, rec in daily.items():
        desc_counts = rec.pop('desc_counts', {})
        most = None
        if desc_counts:
            most = max(desc_counts.items(), key=lambda x: x[1])[0]
        summary[day] = {
            'min': rec['min'], 
            'max': rec['max'], 
            'desc': most,
        }
    return summary

def do_current(url_params_pair):
    url, params = url_params_pair
    resp = fetch_weather(url, params)
    data = resp.json()
    city = get_city_from_params(params)
    unit = get_unit_from_params(params)
    lang = get_lang_from_params(params)
    if lang == 'ru':
        print('\n=== Погода Сейчас ===')
    elif lang == 'ua':
        print('\n=== Погода Зараз ===')
    else:
        print('\n=== Current weather ===')
    print_weather_by_lang(city, data, unit, lang)

def do_forecast(url_params_pair):
    url, params = url_params_pair
    resp = fetch_weather(url, params)
    forecast = parse_forecast(resp)
    lang = get_lang_from_params(params)
    if lang == 'ru':
        print('\n=== Прогноз Погоды ===')
        print_forecast_ru(forecast)
    elif lang == 'ua':
        print('\n=== Прогноз Погоди ===')
        print_forecast_ua(forecast)
    else:
        print('\n=== Forecast ===')
        print_forecast_en(forecast)

def run_current(appid, city, units, lang):
    url, params = build_weather_request(
        appid, 
        mode="current", 
        city=city, 
        units=units, 
        lang=lang,
    )
    resp = fetch_weather(url, params)
    if error(resp):
        data = parse_weather(resp)
        print_weather_by_lang(city.title(), data, units, lang)

def run_forecast(appid, city, units, lang):
    url, params = build_weather_request(
        appid, 
        mode="forecast", 
        city=city, 
        units=units, 
        lang=lang,
    )
    resp = fetch_weather(url, params)
    if error(resp):
        forecast = parse_forecast(resp)
        print_forecast_by_lang(forecast, lang)
