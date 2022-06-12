#package imports
import plotly.graph_objects as go
import pandas as pd
import pandas_ta as pta
import matplotlib.pyplot as plt

#local imports
from oanda import OandaAPI

class HistoricalData():

    def __init__(self):
        pass

    def retrieve_forex_historical_data(instrument, data_points, timeframe):
        #oanda api class instance for retrieving historical data
        api = OandaAPI()

        #we fetch the historical data, with input our instrument, the amount of candles we want the timeframe of the candles
        #historical_data = api.fetch_candles('USD_CAD', 1000, 'D')
        historical_data = api.fetch_candles(instrument, data_points, timeframe)

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

        return df
