#local imports
from harmonic_patterns import HarmonicPattern
from oanda import OandaAPI
from technical_analysis import TechnicalAnalysis
from harmonic_patterns import HarmonicPattern

#packages import
import plotly.graph_objects as go
import pandas as pd
import pandas_ta as pta
import matplotlib.pyplot as plt
#import talib as ta

from datetime import datetime

class Plot():


    def __init__(self):
        pass


    def plot(self, df):

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 2) plotting the data as candlestick data

        #we plot the candlestick graph
        fig = go.Figure(data=[go.Candlestick(x=df['date'],
                        open=df['open'],
                        high=df['high'],
                        low=df['low'],
                        close=df['close'])])

        #we show the plot ##
        fig.show()

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
        #plt.show()

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # 4) technical analysis : harmonic patterns

        harmonic = HarmonicPattern(df)

        harmonic.find_extremum_points()

        harmonic.find_and_identify_first_extremum()

        harmonic.find_and_identify_next_4_points()