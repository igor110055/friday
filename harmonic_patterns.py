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
        self.df['min'] = self.df.iloc[argrelextrema(self.df.close.values, np.less_equal,
                            order=n)[0]]['close']
        self.df['max'] = self.df.iloc[argrelextrema(self.df.close.values, np.greater_equal,
                            order=n)[0]]['close']

        # plot results
        plt.scatter(self.df.index, self.df['min'], c='r')
        plt.scatter(self.df.index, self.df['max'], c='g')
        plt.plot(self.df.index, self.df['close'])
        #plt.show()
    

    #this method is used to find the first low or high of a dataframe, it will also identify if it is a low or high
    def find_and_identify_first_extremum(self):

        #we find the first max
        for value in self.df['max']:

            #this line checks if the value is not a number, it will continue to the next iteration if thats the case
            if pd.isna(value) == True:
                continue
            
            #we save the first max value
            self.first_max = value
            print(value)

            #we save the index of the value
            self.index_max = int(self.df[self.df['max']==value].index.values)
            print(self.index_max)

            #we break the loop as we only want the first max
            break

        #we find the first min
        for value in self.df['min']:

            #this line checks if the value is not a number, it will continue to the next iteration if thats the case
            if pd.isna(value) == True:
                continue
            
            #we save the first min value
            self.first_min = value
            print(value)

            #we save the index of the value
            self.index_min = int(self.df[self.df['min']==value].index.values)
            print(self.index_min)

            #we break the loop as we only want the first min
            break

        #next we are going to compare both indexes and save the one that is the first one
        extremum_type = 'max' if self.index_max < self.index_min else 'min'

        #we also save the first value whether its a min or max
        extremum_value = self.first_max if extremum_type == 'max' else self.first_min

        #we save the index of the extremum
        extremum_index = self.index_max if extremum_type == 'max' else self.index_min

        print(extremum_type)

        print(extremum_value)

        #finally we save this point (X) to the dictionary and its extremum type (max or min)
        self.xabcd_points = {
            'x': {
                'extremum_value': extremum_value,
                'extremum_type': extremum_type,
                'extremum_index': extremum_index
            }
        }
        
        print(self.xabcd_points)

    #this method is used to find the next 4 points
    def find_and_identify_next_4_points(self):

        # we find point A, this method below returns the extremum value and extremum type
        a_extremum_type, a_extremum_value, a_extremum_index = self.find_next_extremum(
            extremum_type = self.xabcd_points['x']['extremum_type'], 
            extremum_index = self.xabcd_points['x']['extremum_index']
        )

        #we save the new values to the xabcd dictionary
        self.xabcd_points['a'] = {
            'extremum_value': a_extremum_value,
            'extremum_type': a_extremum_type,
            'extremum_index': a_extremum_index
        }


        #we find point B, with the same method as with point A
        b_extremum_type, b_extremum_value, b_extremum_index = self.find_next_extremum(
            extremum_type = self.xabcd_points['a']['extremum_type'], 
            extremum_index = self.xabcd_points['a']['extremum_index']
        )

        #we save the new values to the xabcd dictionary
        self.xabcd_points['b'] = {
            'extremum_value': b_extremum_value,
            'extremum_type': b_extremum_type,
            'extremum_index': b_extremum_index
        }


        #we find point C, with the same method as with point A
        c_extremum_type, c_extremum_value, c_extremum_index = self.find_next_extremum(
            extremum_type = self.xabcd_points['b']['extremum_type'], 
            extremum_index = self.xabcd_points['b']['extremum_index']
        )

        #we save the new values to the xabcd dictionary
        self.xabcd_points['c'] = {
            'extremum_value': c_extremum_value,
            'extremum_type': c_extremum_type,
            'extremum_index': c_extremum_index
        }


        #we find point D, with the same method as with point A
        d_extremum_type, d_extremum_value, d_extremum_index = self.find_next_extremum(
            extremum_type = self.xabcd_points['c']['extremum_type'], 
            extremum_index = self.xabcd_points['c']['extremum_index']
        )

        #we save the new values to the xabcd dictionary
        self.xabcd_points['d'] = {
            'extremum_value': d_extremum_value,
            'extremum_type': d_extremum_type,
            'extremum_index': d_extremum_index
        }

        # for point in self.xabcd_points:
        #     print(f'{point}: {self.xabcd_points[point]}')


    # this method is used to find the next point
    def find_next_extremum(self, extremum_type, extremum_index):

        # we check the type of the old extremum and choose the inverse for the new one
        new_extremum_type = 'max' if extremum_type == 'min' else 'min'

        # we loop through the database starting an index after the old extremum (hence the +1 )
        for i in range(extremum_index + 1, len(self.df[new_extremum_type])):

            #we check that the number is a real number
            if pd.isna(self.df[new_extremum_type][i]) == True:
                continue
            
            #we also save the first value whether its a min or max
            new_extremum_value = self.df[new_extremum_type][i]

            #we save the index
            new_extremum_index = i

            #we break the loop because we are only looking to save the next point in line
            break

        #finally we return the data to the method that called it
        return new_extremum_type, new_extremum_value, new_extremum_index
