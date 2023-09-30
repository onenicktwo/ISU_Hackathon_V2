from neuralprophet import NeuralProphet
import pandas as pd
from matplotlib import pyplot as plt
import pickle

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
with open('iowa_weather_model.pkl', 'rb') as f:
    m = pickle.load(f)

future = m.make_future_dataframe(data, periods=365)
forecast = m.predict(future)

plt.plot(forecast['ds'],forecast['yhat1'])
plt.show()