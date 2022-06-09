#package imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema


#this file will be used to find harmonic patterns
class HarmonicPattern():

    def __init__(self, df):

        #we declare our dataframe to be used throughout the class
        self.df = df
        
    def find_pivot_points(self):
        
        #the order is the number of points it will check on the left and right
        order = 5

        #first we start by looping through the data and finding the lows and highs, the range starts after n as it needs to check to the left and right of the data and
        # the data does not exist after 
        for i in range(order, len(self.df['close']) - order):

            #to find a low we need to check if the point is lower than n other points around it
            print(self.df['close'][i])

            try:
                #local maxima (we check around the datapoint and check if it is lower than the other points)
                
                counter = 0
                #we check that the price is lower than the nearby points
                for x in range(order):
                    if self.df['close'][i - x] <= [self.df['close'][i] <= self.df['close'][i + x]:
                        counter += 1

                #we check that the counter passed for every loop
                if counter >= order



            #there will arise a problem where the the points to the left or right dont exist, in that case we 
            # will just skip to the next iteration if its to the left and for the right we will treat it as a 
            # low or high depending on if its a lwo or high
            except:


                break

        #number of points to be checked before and after
        order = 5

        # print(self.df)
        # print(self.df['close'])
        # #close = np.array(self.df['close'], self.df['date'])
        
        # close = pd.DataFrame({'A': self.df['date'], 'B': self.df['close']}).to_numpy()

        # print(1)
        # print(close)
        # print(2)
        
        # # # for local maxima
        # # self.df['max'] = self.df[argrelextrema(close, np.less_equal, order = order)]

        # # # for local minima
        # # self.df['min'] = self.df[argrelextrema(close, np.greater_equal, order = order)]

        # # for local maxima
        # max = list(argrelextrema(close, np.less_equal, order = order)[0])

        # # for local minima
        # min = list(argrelextrema(close, np.greater_equal, order = order)[0])

        # maxima = max + min

        # print(maxima)

        # peaks = price.values[idx]

        # # plt.scatter(df.index, df['min'], c='r')
        # # plt.scatter(df.index, df['max'], c='g')
        # # plt.plot(df.index, df['data'])
        # # plt.show()

        # df = self.df
        # # print(df)
        # # print(df['close'])
        # df = df['close']

        # n = 5  # number of points to be checked before and after

        # # Find local peaks

        # df['min'] = df[argrelextrema(df.data.values, np.less_equal,
        #                     order=n)[0]]['date']
        # df['max'] = df[argrelextrema(df.data.values, np.greater_equal,
        #                     order=n)[0]]['date']

        # # Plot results

        # plt.scatter(df.index, df['min'], c='r')
        # plt.scatter(df.index, df['max'], c='g')
        # plt.plot(df.index, df['close'])
        # plt.show()

        