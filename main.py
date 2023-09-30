from neuralprophet import NeuralProphet
import pandas as pd
from matplotlib import pyplot as plt
import pickle

weather = pd.read_csv("iowa_weather_data.csv")
weather.columns = weather.columns.str.lower()

weather['date'] = pd.to_datetime((weather['date']))
weather['year'] = weather['date'].apply(lambda x : x.year)

plt.plot(weather['date'], weather['tmax'])
plt.show()