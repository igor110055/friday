import config
from historical_data import HistoricalData
from harmonic_finder_3 import HarmonicPattern

data_point = 400
order = 10

#class instances
historical_data = HistoricalData()

#we are going to loop through all of our desired instruments
for instrument in config.instruments:

    print(f'we are inside of instrument: {instrument}')
    
    #we retrieve the dataframe from the last n data points of the instrument
    df = historical_data.retrieve_forex_historical_data_converted(instrument, data_point, 'D')

    #we start the harmonic pattern finder
    harmonic_pattern = HarmonicPattern(df, order)
    harmonic_pattern.main()