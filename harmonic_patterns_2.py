#package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

#local imports
import config
#from disk import Disk
from functools import partial
from historical_data import HistoricalData
from xabcd import upgraded_xabcd

#we set this option since we are going to be slicing through the dataframe provided by pandas and if we dont we get an error at each iteration
pd.set_option('mode.chained_assignment', None)

class HarmonicPattern():

    #def __init__(self, df) -> None:
    def __init__(self) -> None:
        
        #self.df = df
        self.order = 5

        #class instances
        #self.disk = Disk()

    def main(self):

        # first we need to find the first low or high in the first n points (or both) to do this we have to take the first slice of the dataframe
        # using the order number n 

        # we make the first slice
        self.partial_df = self.df.iloc[0:self.order]

        # we find the first low and max in this sample
        self.partial_df['min'] = self.partial_df.iloc[argrelextrema(self.partial_df.close.values, np.less_equal,
                            order = self.order)[0]]['close']
        self.partial_df['max'] = self.partial_df.iloc[argrelextrema(self.partial_df.close.values, np.greater_equal,
                            order = self.order)[0]]['close']

        print(self.partial_df)

        #we find the first low
        for index_max in range(len(self.partial_df['max'])):

            #this line checks if the value is not a number, it will continue to the next iteration if thats the case
            if pd.isna(self.partial_df['max'][index_max]) == True:
                continue 

            #if this is the max then we take note of the index
            index_max = index_max

            #we also save the value
            value_max = self.partial_df['max'][index_max]

            #we break the loop because we only want the first point
            break

        #we find the first max
        for index_min in range(len(self.partial_df['min'])):

            #this line checks if the value is not a number, it will continue to the next iteration if thats the case
            if pd.isna(self.partial_df['min'][index_min]) == True:
                continue 

            #if this is the max then we take note of the index
            index_min = index_min

            #we also save the value
            value_min = self.partial_df['min'][index_min]

            #we break the loop because we only want the first point
            break

        #we compare both extrema and put them in order the xabcd dictionary

        # if the min is the first point
        if index_max > index_min:
            self.xabcd['coords']['x'] = value_min 
            self.xabcd['index']['x'] = index_min
            self.xabcd['type']['x'] = 'min'
            self.xabcd['coords']['a'] = value_max 
            self.xabcd['index']['a'] = index_max
            self.xabcd['type']['a'] = 'max'
        
        #if the max is the first point
        elif index_max < index_min:
            self.xabcd['coords']['x'] = value_max 
            self.xabcd['index']['x'] = index_max
            self.xabcd['type']['x'] = 'max'
            self.xabcd['coords']['a'] = value_min 
            self.xabcd['index']['a'] = index_min
            self.xabcd['type']['a'] = 'min'

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        # first we need to loop through the amount of points in the dataframe, we are going to start the loop at the order, because we cant get any
        # values from a dataframe lower than this number
        for index in range(self.order + 1, len(self.df)):

            # for each point we need to print the dataframe all the way to the i index
            self.partial_df = self.df.iloc[0:index]

            print(self.partial_df)

            # to do this we are going to find the maxs and lows inside of this partial dataframe

            # ~~~~~~~~~~~~~~~
            # finding the first low or high
            # but first we need to find the first low or high in the n first points (where n is the order)

            # Find local peaks
            self.partial_df['min'] = self.partial_df.iloc[argrelextrema(self.partial_df.close.values, np.less_equal,
                                order = self.order)[0]]['close']
            self.partial_df['max'] = self.partial_df.iloc[argrelextrema(self.partial_df.close.values, np.greater_equal,
                                order = self.order)[0]]['close']

            #then we are going to see if the current index is a high or low

            #boolean to keep track of it the current point is a high or low
            is_extremum = False

            #we check if current index is high
            if pd.isna(self.partial_df['min'][index]) == False:

                # we save the data and change the type 
                extremum_value = value_min = self.partial_df['min'][index]

                #we save the extremum type
                extremum_type = 'max'

                is_extremum = True

            elif pd.isna(self.partial_df['max'][index]) == False:

                # we save the data
                value = value_min = self.partial_df['min'][index]

                #we save the extremum type
                extremum_type = 'min'

                is_extremum = True


            #we check what type the last point was

            #to do this we are going to first check if its the first point and just note it down, if its not then we are going to do a reverse for loop through the coords and check the first one
            # that isnt empty


            #if the current point is not an extremum, we just continue on to the next iteration
            if is_extremum == False:
                continue


            #otherwise, we are going to check what the last extremum was by doing a reverse for loop through the coords in xabcd and checking which one is not occupied
            for object in reversed(self.xabcd['type']):
                if self.xabcd['type'][object] == 'na':
                    continue

                #if its not occupied, then we check the type
                old_type = self.xabcd['type'][object]

                #we save the value
                old_value = self.xabcd['coords'][object]

                object = object

                # we break the loop as we only want the last extrema
                break
            
            #we check if the last point type is the same as the current one
            if extremum_type == old_type:

                # if the new value is higher/lower according to the type than the old one then we will replace the point

                #if both are minima, we check the lowest point
                if extremum_type == 'min':

                    if extremum_value <= old_value:

                        #we replace the old point with the new point
                        self.xabcd['coords'][object] == extremum_value
                        self.xabcd['index'][object] == index
                        self.xabcd['type'][object] == extremum_type

                    #if the new point does not represent a new low or high then we will just keep things unchanged and skip to the next iteration
                    elif extremum_value >= old_value:
                        continue

                # same scenario but for 2 maxima
                if extremum_type == 'max':

                    if extremum_value >= old_value:

                        #we replace the old point with the new point
                        self.xabcd['coords'][object] == extremum_value
                        self.xabcd['index'][object] == index
                        self.xabcd['type'][object] == extremum_type

                    #if the new point does not represent a new low or high then we will just keep things unchanged and skip to the next iteration
                    elif extremum_value <= old_value:
                        continue

            #if the extramum is not the same type as the latest point, then we are going to put it into the next dictionary
            
            #if the dictionary is full, then we bump up the points
            self.bump_xabcd_points()

            #this part will loop through the points until it finds a free one and fill one of the points with the one we just found
            #at this point the last point should be free, so this algorithm shoudl also work for that point (2 birds in 1 stone)
            if self.xabcd['stage'] == 'filling':

                # to do this we loop through the values inside of the dictionary until we find one that is empty
                for object in self.xabcd['coords']:

                    if self.xabcd['coords'][object] == 'na':
                        continue

                    #if its empty we are going to replace the point with the new one
                    self.xabcd['coords'][object] == extremum_value
                    self.xabcd['index'][object] == index
                    self.xabcd['type'][object] == extremum_type

                    #also we check that if the object that was filled was d then we have to declare the dictionary closed as the xabcd points ahve been filled
                    if object == 'd':
                        self.xabcd['stage'] == 'filled'

                    #we break the loop as we only wanted the first value
                    break

            #finalyl we have to recalculate the retracements and match them with the textbook harmonic patterns since the xabcd library changed
            
            #we calculate the retracements again
            self.calculate_xabcd_retracements()

            #we check if there is a match on the xabcd harmonic points with the textbook harmonic patterns
            if self.match_xabcd_retracements_to_harmonic_patterns() == True:

                #position open
                pass
            
            #if there is no match, we just skip to the next iteration
            else:
                continue


    #this method bumps the points up and frees the last point
    def bump_xabcd_points(self, xabcd):
        
        #we save the abcd points by making a backup of the dictionary
        xabcd_copy = xabcd.copy()

        print(xabcd_copy)

        #we bump up the points using a for loop, we stop at the last one as this one will be emptied out
        for index in range(len(xabcd_copy['coords']) - 1):
            
            #we replace the value of the current index with that of the old one
            print(index)
            print(xabcd_copy['coords'][index])
            xabcd_copy['coords'][index] = xabcd_copy['coords'][index + 1]
            xabcd_copy['coords'][index] = xabcd_copy['coords'][index + 1]
            xabcd_copy['type'][index] = xabcd_copy['type'][index + 1]

        #we empty out the last point
        xabcd_copy['coords'][-1] = 'na'
        xabcd_copy['coords'][-1] ='na'
        xabcd_copy['type'][-1] = 'na'

        #we empty out the retracements as these are now changed
        for object in xabcd_copy['retracements']:
            xabcd_copy['retracements'][object] == 'na'

        #we change the status of the dictionary from filled to filling as the last point is now empty
        xabcd_copy['stage'] = 'filling'

        #we replace the old xabcd dictionary with the new one
        xabcd = xabcd_copy

        print(xabcd)

    #this method is used to calculate all of the useful retracements we will need to calculate the harmonic patterns
    def calculate_xabcd_retracements(self):
        
        #we load up xabcd
        self.xabcd = self.disk.load(filename = 'xabcd')

        #we calculate all of the segments
        self.xa = abs(self.xabcd_points['coords']['a'] - self.abcd_points['coords']['x'])
        self.ab = abs(self.xabcd_points['coords']['b'] - self.abcd_points['coords']['a'])
        self.bc = abs(self.xabcd_points['coords']['c'] - self.abcd_points['coords']['b'])
        self.cd = abs(self.xabcd_points['coords']['d'] - self.abcd_points['coords']['c'])
        self.ad = abs(self.xabcd_points['coords']['d'] - self.abcd_points['coords']['a'])

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

        #we save the xabcd dictionary to the disk
        self.disk.save(filename = 'xabcd', obj = self.xabcd)

    # this method is used to match the xabcd retracements to the the textbook retracements in the config and see if there is match
    def match_xabcd_retracements_to_harmonic_patterns(self):
        
        #we load up our xabcd dict from the disk
        self.xabcd = self.disk.load(filename = 'xabcd')

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

historical_data = HistoricalData()
#df = historical_data = historical_data.retrieve_forex_historical_data('USD_CAD', 10, 'D')

harmonic = HarmonicPattern()
harmonic.bump_xabcd_points(upgraded_xabcd)

