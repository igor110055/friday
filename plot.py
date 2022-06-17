#local imports
#from harmonic_patterns import HarmonicPattern
from oanda import OandaAPI
from technical_analysis import TechnicalAnalysis
#from harmonic_patterns_2 import HarmonicPattern

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

        # harmonic = HarmonicPattern(df)

        # harmonic.find_extremum_points()

        # harmonic.find_and_identify_first_extremum()

        # harmonic.find_and_identify_next_4_points()


    #this method is used to plot a graph that has an xabcd pattern, it will plot the dataframe and also highlight and connect the xabcd points
    def harmonic_pattern(self, df, xabcd, harmonic_pattern):

        #we plot the harmonic points
        x_points = [
            xabcd['index']['x'],
            xabcd['index']['a'],
            xabcd['index']['b'],
            xabcd['index']['c'],
            xabcd['index']['d']
        ]

        y_points = [
            xabcd['coords']['x'],
            xabcd['coords']['a'],
            xabcd['coords']['b'],
            xabcd['coords']['c'],
            xabcd['coords']['d']
        ]

        #plt.scatter(x_points, y_points, c='r')
        plt.plot(x_points, y_points, 'ro-')
       

        #we add a comment to show the harmonic pattern
        plt.figtext(.8, .8, harmonic_pattern)


        #we plot the retracements of the harmonic points
        x_retracements = [
            xabcd['index']['x'],
            xabcd['index']['b'],
            xabcd['index']['d']
        ]

        y_retracements = [
            xabcd['coords']['x'],
            xabcd['coords']['b'],
            xabcd['coords']['d']
        ]

        plt.plot(x_retracements, y_retracements, 'ro-')


        #we plot the partial dataframe
        plt.plot(df.index, df['close'])


        # #we plot the xabcd points
        # xabcd_point_plot = [
        #     go.Scatter(x=[xabcd['index']['x'], xabcd['index']['a']],y=[xabcd['coords']['x'], xabcd['coords']['a']],name="V0"),
        #     go.Scatter(x=[xabcd['index']['a'], xabcd['index']['b']],y=[xabcd['coords']['a'], xabcd['coords']['b']],name="V0"),
        #     go.Scatter(x=[xabcd['index']['b'], xabcd['index']['c']],y=[xabcd['coords']['b'], xabcd['coords']['c']],name="V0"),
        #     go.Scatter(x=[xabcd['index']['c'], xabcd['index']['d']],y=[xabcd['coords']['c'], xabcd['coords']['d']],name="V0")
        # ]     


        print('inside of plot harmonic pattern')
        #plot results
        plt.show() 

        #points x to a
        #point_a_y = xabcd['coords']['x']

        #point a to b

        #point b to c

        #point c to d
