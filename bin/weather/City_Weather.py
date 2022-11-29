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
        #extract date for aggregatin purposes
    def aggregate_weather(self):
        #at the city level
        walkable_hours = self.weather[self.weather.walkable].count()   
        print(walkable_hours)
        #total walkable hours
        #average walkable hours per day
        #days with >1 walkable hours, #2, #3, #6, #12
        #return self.weather.groupby('date')['walkable'].sum()

#citytest = City('Chicago, IL')
#print(citytest.aggregate_weather())