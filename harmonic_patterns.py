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
        
        n = 5  # number of points to be checked before and after

        # Find local peaks

        df['min'] = df.iloc[argrelextrema(df.close.values, np.less_equal,
                            order=n)[0]]['close']
        df['max'] = df.iloc[argrelextrema(df.close.values, np.greater_equal,
                            order=n)[0]]['close']

        # Plot results

        plt.scatter(df.index, df['min'], c='r')
        plt.scatter(df.index, df['max'], c='g')
        plt.plot(df.index, df['close'])
        plt.show()

        