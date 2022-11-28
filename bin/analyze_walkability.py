import metpy.calc 
from metpy.units import units
from datetime import *
import variables as v 

apparent_temp_min = v.apparent_temp_min * units("degF")
apparent_temp_max = v.apparent_temp_max * units("degF")
hour_min = v.hour_min
hour_max = v.hour_max

def determine_walkability(row):
    time = datetime.strptime(row['time'], "%Y-%m-%dT%H:%M")
    walkable = False 
    if hour_min <= time.hour <= hour_max:
        temp = row['temperature_2m'] * units("degF")
        wind = row['windspeed_10m'] * units("mi/h")
        humidity = row['relativehumidity_2m']/100 
        rain = row['precipitation']
        apparent_temp = metpy.calc.apparent_temperature(temp, humidity, wind)   
        if apparent_temp_min <= apparent_temp <= apparent_temp_max and rain == 0:
            walkable = True
    return walkable
