#package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

#local imports
import config
#from disk import Disk
from plot import Plot
from historical_data import HistoricalData
from xabcd import xabcd

#we set this option since we are going to be slicing through the dataframe provided by pandas and if we dont we get an error at each iteration
pd.set_option('mode.chained_assignment', None)

class HarmonicPattern():

    def __init__(self, df, order) -> None:
    #def __init__(self) -> None:
        
        self.df = df
        self.order = order
        self.xabcd = xabcd

        #class instances
        #self.disk = Disk()
        self.plot = Plot()

    def main(self):

        # Find local peaks
        self.df['min'] = self.df.iloc[argrelextrema(self.df.close.values, np.less_equal,
                            order = self.order)[0]]['low']
        self.df['max'] = self.df.iloc[argrelextrema(self.df.close.values, np.greater_equal, 
                            order = self.order)[0]]['high']

        #print(self.df)

        #find the bullish harmonic patterns (3 min and 2 max)

        # print(len(self.df['max']))
        # print(len(self.df['min']))
        # print(len(self.df))

        #we are going to loop through finding both the bearish and bullish patterns
        extremums = ['min', 'max']

        #we loop through the different extrema to find the bullish and bearish patterns
        for extrema in extremums:

            #the anti_extrema is the other extrema, whcih is valuable bnecause when we want the bullish pattern when need 3 mins and 2 maxs
            anti_extrema = 'min' if extrema == 'max' else 'max'

            # ~~~~~~~~~~~~ extrema 1 ~~~~~~~~~~~~~~~~~~~~~
            #we start by finding the first max by looping throuhg the maxes in the dataframe
            for index_extrema_1 in range(len(self.df)):
                
                #this line checks if the value is not a number, it will continue to the next iteration if thats the case, finding the first max
                if pd.isna(self.df[extrema][index_extrema_1]) == True:
                    continue 

                #first min info
                value_1 = self.df[extrema][index_extrema_1]
                #print(f'the {extrema} extrema is {value_1} with index {index_extrema_1}')
                self.xabcd['coords']['x'] = value_1 
                self.xabcd['index']['x'] = index_extrema_1
                self.xabcd['type']['x'] = extrema

                # ~~~~~~~~~~~~ anti-extrema 1 ~~~~~~~~~~~~~~~~~~~~~
                #if it finds the first max then we will loop to find the next extramum that is a minimum, we also need to loop starting after the current index
                for index_extrema_2 in range(index_extrema_1, len(self.df)):

                    #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                    if pd.isna(self.df[anti_extrema][index_extrema_2]) == True:
                        continue

                    #first max info
                    value_2 = self.df[anti_extrema][index_extrema_2]
                    #print(f'the {anti_extrema} extrema is {value_2} with index {index_extrema_2}')

                    self.xabcd['coords']['a'] = value_2 
                    self.xabcd['index']['a'] = index_extrema_2
                    self.xabcd['type']['a'] = anti_extrema

                    # ~~~~~~~~~~~~ extrema 2 ~~~~~~~~~~~~~~~~~~~~~
                    for index_extrema_3 in range(index_extrema_2, len(self.df)):

                        #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                        if pd.isna(self.df[extrema][index_extrema_3]) == True:
                            continue

                        value_3 = self.df[extrema][index_extrema_3]

                        #here we need to check that the second extrema is higher or lower than first anti extrema
                        if extrema == 'max':
                            #we check that the second max is higher than the first anti_extrema
                            if float(value_3) < float(value_2):
                                continue
                        if extrema == 'min':
                            #we check that the second min is lower than the first anti_extrema
                            if float(value_3) > float(value_2):
                                continue

                        #~~~~~~~~~~
                        # we also need to check that there are not points that are higher or lower than each other in between

                        #second min info
                        #print(f'the {extrema} extrema is {value_3} with index {index_extrema_3}')

                        self.xabcd['coords']['b'] = value_3 
                        self.xabcd['index']['b'] = index_extrema_3
                        self.xabcd['type']['b'] = extrema

                        # ~~~~~~~~~~~~ anti-extrema 2 ~~~~~~~~~~~~~~~~~~~~~
                        for index_extrema_4 in range(index_extrema_3, len(self.df)):

                            #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                            if pd.isna(self.df[anti_extrema][index_extrema_4]) == True:
                                continue

                            #second max info
                            value_4 = self.df[anti_extrema][index_extrema_4]

                            #here we need to check that the second extrema is higher or lower than first anti extrema
                            if extrema == 'max':
                                #we check that the second max is higher than the first anti_extrema
                                if float(value_4) > float(value_3):
                                    #if it is not we are going to continue to the next iteration
                                    continue
                            if extrema == 'min':
                                #we check that the second min is lower than the first anti_extrema
                                if float(value_4) < float(value_3):
                                    #if it is not we are going to continue to the next iteration
                                    continue

                            #print(f'the {anti_extrema} extrema is {value_4} with index {index_extrema_4}')

                            self.xabcd['coords']['c'] = value_4 
                            self.xabcd['index']['c'] = index_extrema_4
                            self.xabcd['type']['c'] = anti_extrema

                            # ~~~~~~~~~~~~ extrema 3 ~~~~~~~~~~~~~~~~~~~~~
                            for index_extrema_5 in range(index_extrema_4, len(self.df)):
                                
                                #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                                if pd.isna(self.df[extrema][index_extrema_5]) == True:
                                    continue
                                
                                value_5 = self.df[extrema][index_extrema_5]

                                #here we need to check that the second extrema is higher or lower than first anti extrema
                                if extrema == 'max':
                                    #we check that the second max is higher than the first anti_extrema
                                    if float(value_5) < float(value_4):
                                        #if it is not we are going to continue to the next iteration
                                        continue
                                if extrema == 'min':
                                    #we check that the second min is lower than the first anti_extrema
                                    if float(value_5) > float(value_4):
                                        #if it is not we are going to continue to the next iteration
                                        continue

                                #third mimimum info
                                value_5 = self.df[extrema][index_extrema_5]
                                #print(f'the {extrema} extrema is {value_5} with index {index_extrema_5}')

                                self.xabcd['coords']['d'] = value_5 
                                self.xabcd['index']['d'] = index_extrema_5
                                self.xabcd['type']['d'] = extrema

                                #print(self.xabcd)

                                #since this completes the xabcd point dictionary. we want to go ahead and calculate the retracements 
                                self.calculate_xabcd_retracements()

                                #and we also want to check if there is a match on the xabcd  to harmonic pattern
                                if self.match_xabcd_retracements_to_harmonic_patterns() == True:
                                    print(self.xabcd)
                                    self.plot.harmonic_pattern(self.df, self.xabcd)


    #this method bumps the points up and frees the last point
    def bump_xabcd_points(self):
        
        #we save the abcd points by making a backup of the dictionary
        xabcd_copy = self.xabcd.copy()

        #we make a list of the differents points since we wil be attributing an index to them
        xabcd_points = ['x','a','b','c','d']

        print(xabcd_copy)

        #we bump up the points using a for loop, we stop at the last one as this one will be emptied out
        for index in range(len(xabcd_copy['coords']) - 1):
            
            #we replace the value of the current index with that of the old one

            #updated using the xabcd points list
            xabcd_copy['coords'][xabcd_points[index]] = xabcd_copy['coords'][xabcd_points[index + 1]]
            xabcd_copy['index'][xabcd_points[index]] = xabcd_copy['index'][xabcd_points[index + 1]]
            xabcd_copy['type'][xabcd_points[index]] = xabcd_copy['type'][xabcd_points[index + 1]]

        #we empty out the last point
        xabcd_copy['coords'][xabcd_points[-1]] = 'na'
        xabcd_copy['index'][xabcd_points[-1]] ='na'
        xabcd_copy['type'][xabcd_points[-1]] = 'na'

        #we empty out the retracements as these are now changed
        for object in xabcd_copy['retracements']:
            xabcd_copy['retracements'][object] = 'na'

        #we change the status of the dictionary from filled to filling as the last point is now empty
        xabcd_copy['stage'] = 'filling'

        #we replace the old xabcd dictionary with the new one
        self.xabcd = xabcd_copy


    #this method is used to calculate all of the useful retracements we will need to calculate the harmonic patterns
    def calculate_xabcd_retracements(self):
        
        #print('inside of calculating retracements')

        #we load up xabcd
        #self.xabcd = self.disk.load(filename = 'xabcd')

        #we calculate all of the segments
        self.xa = abs(float(self.xabcd['coords']['a']) - float(self.xabcd['coords']['x']))
        self.ab = abs(float(self.xabcd['coords']['b']) - float(self.xabcd['coords']['a']))
        self.bc = abs(float(self.xabcd['coords']['c']) - float(self.xabcd['coords']['b']))
        self.cd = abs(float(self.xabcd['coords']['d']) - float(self.xabcd['coords']['c']))
        self.ad = abs(float(self.xabcd['coords']['d']) - float(self.xabcd['coords']['a']))

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

        #print(self.xabcd)

        #we save the xabcd dictionary to the disk
        #self.disk.save(filename = 'xabcd', obj = self.xabcd)


    # this method is used to match the xabcd retracements to the the textbook retracements in the config and see if there is match
    def match_xabcd_retracements_to_harmonic_patterns(self):

        #print('insider of matching retracements')
        
        #we load up our xabcd dict from the disk
        #self.xabcd = self.disk.load(filename = 'xabcd')

        #we start by looping through the harmonic patterns inside of the available ones in config
        for pattern in config.harmonic_patterns:

            #we have a counter that will count the number of retracements that are correct, if this number goes up to 4, it means a harmonic pattern has been found
            retracement_counter = 0
            
            #we double loop to get the retracement inside of each pattern
            for retracement in config.harmonic_patterns[pattern]:

                # in each retracement we check if the type is a float, if it is we just treat it as a single variable, otherwise we will 
                # check both intervals possible
                if type(config.harmonic_patterns[pattern][retracement]) == float:
                    
                    #we check if the retracement matches the harmonic textbook retracement
                    if config.harmonic_patterns[pattern][retracement] * (1-config.error_rate) <= self.xabcd['retracements'][retracement] <= config.harmonic_patterns[pattern][retracement] * (1 + config.error_rate):
                        retracement_counter += 1
                    
                # if there are multiple retracement choices for the harmonic config.harmonic_patterns[pattern]s, we loop through them
                if type(config.harmonic_patterns[pattern][retracement]) == list:

                    #we check if the retracement matches the harmonic textbook retracement, by comparing it to the lowest interval and the highest interval
                    if config.harmonic_patterns[pattern][retracement][0] * (1-config.error_rate) <= self.xabcd['retracements'][retracement] <= config.harmonic_patterns[pattern][retracement][1] * (1 + config.error_rate):
                        retracement_counter += 1

            #if the counter is equal to 4, it means that there is a match on the xabcd points and the harmonic pattern
            if retracement_counter == 4:
                return True
            
        #otherwise, if there is no match we return a false boolean
        return False


# historical_data = HistoricalData()
# df = historical_data = historical_data.retrieve_forex_historical_data_converted('USD_CAD', 1000, 'D')

# harmonic = HarmonicPattern(df, 5)
# harmonic.main()

# # harmonic = HarmonicPattern(df, 90)
# # harmonic.main()

# # harmonic = HarmonicPattern(df, 100)
# # harmonic.main()


'''
#package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

#local imports
import config
#from disk import Disk
from plot import Plot
from historical_data import HistoricalData
from xabcd import xabcd
from harmonic_patterns_2 import HarmonicPattern

#class instances
harmonic_pattern = HarmonicPattern()
historical_data = HistoricalData()

#we retrieve the dataframe from historical dat
df = historical_data = historical_data.retrieve_forex_historical_data_converted('USD_CAD', 150, 'D')

#config variables
order = 5

# Find local peaks
df['min'] = df.iloc[argrelextrema(df.close.values, np.less_equal,
                    order = order)[0]]['low']
df['max'] = df.iloc[argrelextrema(df.close.values, np.greater_equal, 
                    order = order)[0]]['high']

#print(df)

#find the bullish harmonic patterns (3 min and 2 max)

print(len(df['max']))
print(len(df['min']))
print(len(df))

#we are going to loop through finding both the bearish and bullish patterns
extremums = ['min', 'max']

#we loop through the different extrema to find the bullish and bearish patterns
for extrema in extremums:

    #the anti_extrema is the other extrema, whcih is valuable bnecause when we want the bullish pattern when need 3 mins and 2 maxs
    anti_extrema = 'min' if extrema == 'max' else 'max'

    # ~~~~~~~~~~~~ extrema 1 ~~~~~~~~~~~~~~~~~~~~~
    #we start by finding the first max by looping throuhg the maxes in the dataframe
    for index_extrema_1 in range(len(df)):
        
        #this line checks if the value is not a number, it will continue to the next iteration if thats the case, finding the first max
        if pd.isna(df[extrema][index_extrema_1]) == True:
            continue 

        #first min info
        value = df[extrema][index_extrema_1]
        print(f'the {extrema} extrema is {value} with index {index_extrema_1}')
        xabcd['coords']['x'] = value 
        xabcd['index']['x'] = index_extrema_1
        xabcd['type']['x'] = extrema

        # ~~~~~~~~~~~~ anti-extrema 2 ~~~~~~~~~~~~~~~~~~~~~
        #if it finds the first max then we will loop to find the next extramum that is a minimum, we also need to loop starting after the current index
        for index_extrema_2 in range(index_extrema_1, len(df)):

            #this line checks if the value is not a number, it will continue to the next iteration if thats the case
            if pd.isna(df[anti_extrema][index_extrema_2]) == True:
                continue

            #first max info
            value = df[anti_extrema][index_extrema_2]
            print(f'the {anti_extrema} extrema is {value} with index {index_extrema_2}')

            xabcd['coords']['a'] = value 
            xabcd['index']['a'] = index_extrema_1
            xabcd['type']['a'] = anti_extrema

            # ~~~~~~~~~~~~ extrema 2 ~~~~~~~~~~~~~~~~~~~~~
            for index_extrema_3 in range(index_extrema_2, len(df)):

                #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                if pd.isna(df[extrema][index_extrema_3]) == True:
                    continue

                #second min info
                value = df[extrema][index_extrema_3]
                print(f'the {extrema} extrema is {value} with index {index_extrema_3}')

                xabcd['coords']['b'] = value 
                xabcd['index']['b'] = index_extrema_1
                xabcd['type']['b'] = extrema

                # ~~~~~~~~~~~~ anti-extrema 2 ~~~~~~~~~~~~~~~~~~~~~
                for index_extrema_4 in range(index_extrema_3, len(df)):

                    #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                    if pd.isna(df[anti_extrema][index_extrema_4]) == True:
                        continue

                    #second max info
                    value = df[anti_extrema][index_extrema_4]
                    print(f'the {anti_extrema} extrema is {value} with index {index_extrema_4}')

                    xabcd['coords']['c'] = value 
                    xabcd['index']['c'] = index_extrema_1
                    xabcd['type']['c'] = anti_extrema

                    # ~~~~~~~~~~~~ extrema 3 ~~~~~~~~~~~~~~~~~~~~~
                    for index_extrema_5 in range(index_extrema_4, len(df)):

                        #this line checks if the value is not a number, it will continue to the next iteration if thats the case
                        if pd.isna(df[extrema][index_extrema_5]) == True:
                            continue

                        #third mimimum info
                        value = df[extrema][index_extrema_5]
                        print(f'the {extrema} extrema is {value} with index {index_extrema_5}')

                        xabcd['coords']['d'] = value 
                        xabcd['index']['d'] = index_extrema_1
                        xabcd['type']['d'] = extrema

                        print(xabcd)

                        #since this completes the xabcd point dictionary. we want to go ahead and calculate the retracements 

                        #and we also want to check if there is a match on the xabcd  to harmonic pattern


                        break
                    break
                break
            break
        break
'''
instrument = 'EUR_GBP'
data_point = 160

print(f' isntrument is {instrument} and data point is {data_point}')
historical_data = HistoricalData()
df = historical_data.retrieve_forex_historical_data_converted(instrument, data_point, 'D')

harmonic_pattern = HarmonicPattern(df, 5)
harmonic_pattern.main()