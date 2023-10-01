from neuralprophet import NeuralProphet
import pandas as pd
from matplotlib import pyplot as plt
import pickle

import calc_optimal_gdd
import gdd_calculator

weather = pd.read_csv("iowa_weather_data.csv")
weather.columns = weather.columns.str.lower()

weather['date'] = pd.to_datetime((weather['date']))
weather['year'] = weather['date'].apply(lambda x : x.year)
weather = weather[weather['year'] >= 2010]

#plt.plot(weather['date'], weather['tmax'])
#plt.show()

#Data
data = weather[['date', 'tmin']]
data.dropna(inplace=True)
data.columns = ['ds', 'y']

#Forecast
with open('tmax_model.pkl', 'rb') as f:
    high_temp = pickle.load(f)

future = high_temp.make_future_dataframe(data, periods=365)
forecast = high_temp.predict(future)

with open('tmin_model.pkl', 'rb') as f:
    low_temp = pickle.load(f)
future2 = low_temp.make_future_dataframe(data, periods=365)
forecast2 = low_temp.predict(future)

corn_base = 50.00

high_temperatures = forecast['yhat1']
low_temperatures = forecast2['yhat1']

gdd_values = gdd_calculator.get_gdd(high_temperatures, low_temperatures, corn_base)
plant_date_index, harvest_date_index = calc_optimal_gdd.find_optimum_days(gdd_values)

plant_date = forecast['ds'].iloc[plant_date_index]
harvest_date = forecast['ds'].iloc[harvest_date_index]

#.plot(forecast['ds'],forecast['yhat1'])
#plt.show()
#print(high_temperatures)
print(gdd_values)
print('The best plant date is ', plant_date)
print('The best harvest date is ', harvest_date)
#print(forecast[["ds", "yhat1"]])
#print(forecast2[['ds', 'yhat1']])