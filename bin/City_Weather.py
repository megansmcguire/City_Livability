import variables as v
import get_weather as gw
import analyze_walkability as aw
#used to lookup lat/lon based on city names so we can look up the weather data
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='msmsq_walkability_project')

class City:
    def __init__(self, name):
        location = geolocator.geocode(name)
        self.lat = location.raw['lat']
        self.lon = location.raw['lon']
        self.weather = gw.get_weather(self.lat, self.lon, v.start_date, v.end_date)
        self.weather['walkable'] = self.weather.apply(aw.determine_walkability, axis=1)

citytest = City('Chicago, IL')
print(citytest.weather)