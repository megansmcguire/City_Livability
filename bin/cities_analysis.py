import weather.City_Weather as cw 

with open('city_list.txt') as f:
    cities = [city.rstrip('\n') for city in f]
    for city in cities:
        print(city)
        cw.City(city).aggregate_weather()