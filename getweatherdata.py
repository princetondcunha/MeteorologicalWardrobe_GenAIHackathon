'''Get Weather Data'''

import os
import dotenv
import requests

dotenv.load_dotenv()

API_URL=os.environ.get('WEATHER_APIURL')
weather_apikey=os.environ.get('WEATHER_APIKEY')

def getweather_today(lat,lon):
    '''Get Weather for Today'''
    method="weather"
    return getweather_restrequest(lat,lon,method)

def getweather_next5days(lat,lon):
    '''Get Weather for Next 5 Days'''
    method="forecast"
    return getweather_restrequest(lat,lon,method)

def getweather_restrequest(lat,lon,method):
    '''Get Weather REST Request'''
    url = f'{API_URL}/{method}?lat={lat}&lon={lon}&cnt=40&appid={weather_apikey}'
    data = requests.get(url, timeout=10).json()
    return data
