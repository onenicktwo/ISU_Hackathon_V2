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
    h = pickle.load(f)

future = h.make_future_dataframe(data, periods=365)
forecast = h.predict(future)

with open('tmin_model.pkl', 'rb') as f:
    l = pickle.load(f)
future2 = l.make_future_dataframe(data, periods=365)
forecast2 = l.predict(future)



gdd_values = [gdd_calculator.get_gdd(high, low, 50) for high, low in zip(high_temperatures, low_temperatures)]
plant_date, harvest_date = calc_optimal_gdd.find_optimum_days(gdd_values)
#.plot(forecast['ds'],forecast['yhat1'])
#plt.show()
print(forecast[["ds", "yhat1"]])
print(forecast2[['ds', 'yhat1']])