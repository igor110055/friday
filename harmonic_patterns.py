#package imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

#local imports
import config


#this file will be used to find harmonic patterns
class HarmonicPattern():

    def __init__(self, df):

        #we declare our dataframe to be used throughout the class
        self.df = df
        
    def find_extremum_points(self):
        
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
        plt.show()
    

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


    #this method is used to calculate all of the useful retracements we will need to calculate the harmonic patterns
    def calculate_xabcd_retracements(self):

        #we calculate all of the segments
        self.xa = abs(self.xabcd_points['a']['extremum_value'] - self.abcd_points['x']['extremum_value'])
        self.ab = abs(self.xabcd_points['b']['extremum_value'] - self.abcd_points['a']['extremum_value'])
        self.bc = abs(self.xabcd_points['c']['extremum_value'] - self.abcd_points['b']['extremum_value'])
        self.cd = abs(self.xabcd_points['d']['extremum_value'] - self.abcd_points['c']['extremum_value'])
        self.ad = abs(self.xabcd_points['d']['extremum_value'] - self.abcd_points['a']['extremum_value'])

        #xb retracement
        self.xb_retracement = abs(self.ab / self.xa)

        #ac retracement calculation
        self.ac_retracement = abs(self.bc / self.ab)

        #bd retracement
        self.bd_retracement = abs(self.cd / self.bc)

        # the last retracement is just calculating the retracement from xa to ad
        self.xd_retracement = abs(self.ad / self.xa)

        #we store everything inside of the xabcd dictionary
        self.xabcd['retracements']['xb'] = self.xb_retracement
        self.xabcd['retracements']['ac'] = self.ac_retracement
        self.xabcd['retracements']['bd'] = self.bd_retracement
        self.xabcd['retracements']['xd'] = self.xd_retracement


    # this method is used to match the xabcd retracements to the the textbook retracements in the config and see if there is match
    def match_xabcd_retracements_to_harmonic_patterns(self):

        #we start by looping through the harmonic patterns inside of the available ones in config
        for pattern in config.harmonic_patterns:

            #we have a counter that will count the number of retracements that are correct, if this number goes up to 4, it means a harmonic pattern has been found
            retracement_counter = 0
            
            #we double loop to get the retracement inside of each pattern
            for retracement in pattern:
                
                # in each retracement we check if the type is a float, if it is we just treat it as a single variable, otherwise we will 
                # check both intervals possible
                if type(pattern[retracement]) == float:
                    
                    #we check if the retracement matches the harmonic textbook retracement
                    if pattern[retracement] * (1-config.error_rate) <= self.xabcd['retracements'][retracement] <= pattern[retracement] * (1 + config.error_rate):
                        retracement_counter += 1
                    
                # if there are multiple retracement choices for the harmonic patterns, we loop through them
                if type(pattern[retracement]) == list:

                    #we check if the retracement matches the harmonic textbook retracement, by comparing it to the lowest interval and the highest interval
                    if pattern[retracement][0] * (1-config.error_rate) <= self.xabcd['retracements'][retracement] <= pattern[retracement][1] * (1 + config.error_rate):
                        retracement_counter += 1

            #if the counter is equal to 4, it means that there is a match on the xabcd points and the harmonic pattern
            if retracement_counter == 4:
                return True
            
            #otherwise, if there is no match we return a false boolean
            return False

            # yoyooyoyoyo looking good man, just loop through the different retracmeents possible in the harmonic pattern dict (make sure to differentiate float and list values)
            # then you are going to match them with the harmonic retracements library (make sure to add the error rate interval)