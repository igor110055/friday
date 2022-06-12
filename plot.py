#local imports
from harmonic_patterns import HarmonicPattern
from oanda import OandaAPI
from technical_analysis import TechnicalAnalysis
from harmonic_patterns import HarmonicPattern
from maxima_testing import maxima

#packages import
import plotly.graph_objects as go
import pandas as pd
import pandas_ta as pta
import matplotlib.pyplot as plt
#import talib as ta

from datetime import datetime

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1) retrieving historical data

#oanda api class instance for retrieving historical data
api = OandaAPI()

#we fetch the historical data, with input our instrument, the amount of candles we want the timeframe of the candles
historical_data = api.fetch_candles('USD_CAD', 1000, 'D')

#endpoints that might be useful later
#candles = historical_data[1]['candles']
#granularity = historical_data[1]['granularity'] #timeframe
#instrument = historical_data[1]['instrument']

#we initiate an empty list to put the data inside
historical_data_list= []

#we retrieve the data by looping through every candle in the historical data
for data_point in historical_data[1]['candles']:

    #we retrieve the date from the data point and convert it to a datetime object
    date = data_point['time']
    date = pd.to_datetime(date)


    #we are going to save all of this data inside of a list
    historical_data_point = {
        'date': date,
        'open': float(data_point['bid']['o']),
        'close': float(data_point['bid']['c']),
        'high': float(data_point['bid']['h']),
        'low': float(data_point['bid']['l'])
    }
    #we append the data point to the list
    historical_data_list.append(historical_data_point)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2) plotting the data as candlestick data

#we convert the list to a dataframe to be used by pandas
df = pd.DataFrame(data = historical_data_list, columns = ['date', 'open', 'close', 'high', 'low'])
#print(df)

#we plot the candlestick graph
fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

#we show the plot ##
#fig.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 3) technical analysis : RSI

# #next we want to calculate the rsi and plot it aswell, first we need to convert the dataframe to a close dataframe
# close_df = df['close']
# print(close_df)

# #ta class instance
# ta = TechnicalAnalysis()

# #we pass the dataframe to the rsi method
# df['rsi'] = ta.rsi(close_df)

# #we plot the rsi
# plt.plot(df['date'], df['rsi'])

# #we show the plot
# plt.show()


# # 3) technical analysis : stoch rsi

# #we pass the dataframe to the rsi method
# df['stoch_rsi'] = ta.stoch_rsi(close_df)

# #we plot the rsi
# plt.plot(df['date'], df['stoch_rsi'])

# #we show the plot
# plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 4) technical analysis : harmonic patterns

harmonic = HarmonicPattern(df)

harmonic.find_pivot_points()

harmonic.find_and_identify_first_extremum()

harmonic.find_and_identify_next_4_points()