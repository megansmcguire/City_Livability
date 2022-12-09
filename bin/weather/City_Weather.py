import variables as v
import get_weather as gw
import analyze_walkability as aw
import pandas as pd

#used to lookup lat/lon based on city names so we can look up the weather data
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='msmsq_walkability_project')

class City:
    def __init__(self, name):
        self.name = name
        location = geolocator.geocode(name)
        self.lat = location.raw['lat']
        self.lon = location.raw['lon']
        self.weather = gw.get_weather(self.lat, self.lon, v.start_date, v.end_date)
        self.weather['walkable'] = self.weather.apply(aw.determine_walkability, axis=1)
        self.weather['date'] = pd.to_datetime(self.weather['time']).dt.normalize()
        self.aggregate_weather()
        #extract date for aggregatin purposes
    def aggregate_weather(self):
        #at the city level
        self.daily_weather = self.weather.groupby('date', as_index=False)['walkable'].aggregate('sum')
        dict = {
            'city': self.name,
            '>0': [sum(self.daily_weather.walkable > 0)],
            '>=2':[sum(self.daily_weather.walkable >= 2)],
            '>=4':[sum(self.daily_weather.walkable >= 4)],
            '>=8':[sum(self.daily_weather.walkable >= 8)],
            '>=12':[sum(self.daily_weather.walkable >= 12)],
            'average':[self.daily_weather.walkable.mean()],
            #'total_hours':self.weather[self.weather.walkable].count(),
            }
        self.summary = dict
         

