#local imports
from historical_data import HistoricalData
from plot import Plot
from harmonic_patterns import HarmonicPattern
from disk import Disk

#class instances
historical_data = HistoricalData()
plot = Plot()
disk = Disk()

#instrument
instrument = 'USD_CAD'
data_points = 20
timeframe = 'D'

#we start by retrieving the historical data we will need
df = historical_data.retrieve_forex_historical_data_converted(instrument, data_points, timeframe)

#we plot the data
plot.plot(df)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# harmonic part
harmonic = HarmonicPattern(df)

#we find the first 5 points in the data
harmonic.find_extremum_points()

#we find the first extremum
harmonic.find_and_identify_first_extremum()

#we find the next 4 extremum
harmonic.find_and_identify_next_4_points()

#we calculate the xabcd retracements
harmonic.calculate_xabcd_retracements()

if harmonic.match_xabcd_retracements_to_harmonic_patterns() == True:

    #we initiate a position open
    pass

# if there is no match we just contine to the next point
else:
    pass
    #continue

# now we are going to loop throught the remaining points, feeding the programs points as if it was reading it live

# we find the last index of the last point
#xabcd = disk.load('xabcd')





