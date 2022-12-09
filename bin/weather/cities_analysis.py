import City_Weather as cw 
import pandas as pd

city_df = pd.DataFrame()

with open('city_list.txt') as f:
    cities = [city.rstrip('\n') for city in f]
    for city in cities:
        c = cw.City(city)
        #print(c.summary)
        city_df = pd.concat([city_df, pd.DataFrame(c.summary)])
        #city_df = pd.concat((city_df, c.summary), axis = 0)

#print(city_df)
city_df.to_csv('weather_analysis.csv')