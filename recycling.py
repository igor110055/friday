import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import argrelextrema

# Generate a noisy AR(1) sample
def maxima(df):

    # np.random.seed(0)
    # rs = np.random.randn(200)
    # xs = [0]
    # for r in rs:
    #     xs.append(xs[-1] * 0.9 + r)
    # df = pd.DataFrame(xs, columns=['data'])
    # print(df)
    # print(type(df))

    n = 4  # number of points to be checked before and after

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


#
#
#
list = [1,2,3,2,3,4,2,3,2]

order = 2

for i in range(order, len(list) - order):

    for x in range(order):

        if not list[i - x] <= list[i] <= list[i + x]:
            print(list[i])

#
#
#

#harmonic patterns before switching to the intervals
# this method is used to match the xabcd retracements to the the textbook retracements in the config and see if there is match
def match_xabcd_retracements_to_harmonic_patterns(self):

    #we start by looping through the harmonic patterns inside of the available ones in config
    for pattern in config.harmonic_patterns:

        #we have a counter that will count the number of retracements that are correct, if this number goes up to 4, it means a harmonic pattern has been found
        retracement_counter = 0
        
        #we double loop to get the retracement inside of each pattern
        for retracement in pattern:
            
            # in each retracement we check if the type is a float, if it is we just treat it as a single variable, otherwise we will 
            # loop through the values inside and check all the iterations
            if type(pattern[retracement]) == float:
                
                #we check if the retracement matches the harmonic textbook retracement
                if pattern[retracement] * (1-config.error_rate) <= self.xabcd['retracements'][retracement] <= pattern[retracement] * (1 + config.error_rate):
                    retracement_counter += 1
                
            # if there are multiple retracement choices for the harmonic patterns, we loop through them
            if type(pattern[retracement]) == list:

                #we loop through the different retracement choices
                for retracement_2 in pattern[retracement]:

                    #we check if the retracement matches the harmonic textbook retracement
                    if pattern[retracement_2] * (1-config.error_rate) <= self.xabcd['retracements'][retracement_2] <= pattern[retracement_2] * (1 + config.error_rate):
                        retracement_counter += 1

        #if the counter is equal to 4, it means that there is a match on the xabcd points and the harmonic pattern
        if retracement_counter == 4: