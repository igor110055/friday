import config

xabcd = {
    'stage': 'filling',
    'coords': {
        'x': 0.86000,
        'a': 0.82032,
        'b': 0.85119,
        'c': 0.82498,
        'd': 0.87221
    },
    'index': {
        'x': 5,
        'a': 12,
        'b': 19,
        'c': 24,
        'd': 32
    },
    'type': {
        'x': 'max',
        'a': 'min',
        'b': 'max',
        'c': 'min',
        'd': 'max'
    },
    'retracements': {
        'xb': 0.781,
        'ac': 0.849,
        'bd': 1.794,
        'xd': 1.307
    }
}

# this method is used to match the xabcd retracements to the the textbook retracements in the config and see if there is match
def match_xabcd_retracements_to_harmonic_patterns(xabcd):

    print('insider of matching retracements')
    
    #we load up our xabcd dict from the disk
    #self.xabcd = self.disk.load(filename = 'xabcd')

    #we start by looping through the harmonic patterns inside of the available ones in config
    for pattern in config.harmonic_patterns:

        print(pattern)

        #we have a counter that will count the number of retracements that are correct, if this number goes up to 4, it means a harmonic pattern has been found
        retracement_counter = 0
        
        #we double loop to get the retracement inside of each pattern
        for retracement in config.harmonic_patterns[pattern]:

            # in each retracement we check if the type is a float, if it is we just treat it as a single variable, otherwise we will 
            # check both intervals possible
            if type(config.harmonic_patterns[pattern][retracement]) == float:
                
                #we check if the retracement matches the harmonic textbook retracement
                print('lower interval')
                print(config.harmonic_patterns[pattern][retracement])
                print('high interval')
                print(config.harmonic_patterns[pattern][retracement])

                if config.harmonic_patterns[pattern][retracement] * (1 - config.error_rate) <= xabcd['retracements'][retracement] <= config.harmonic_patterns[pattern][retracement] * (1 + config.error_rate):
                    retracement_counter += 1
                
            # if there are multiple retracement choices for the harmonic config.harmonic_patterns[pattern]s, we loop through them
            if type(config.harmonic_patterns[pattern][retracement]) == list:

                print('lower interval')
                print(config.harmonic_patterns[pattern][retracement][0])
                print('high interval')
                print(config.harmonic_patterns[pattern][retracement][1])

                #we check if the retracement matches the harmonic textbook retracement, by comparing it to the lowest interval and the highest interval
                if config.harmonic_patterns[pattern][retracement][0] * (1-config.error_rate) <= xabcd['retracements'][retracement] <= config.harmonic_patterns[pattern][retracement][1] * (1 + config.error_rate):
                    retracement_counter += 1

        print(retracement_counter)
        #if the counter is equal to 4, it means that there is a match on the xabcd points and the harmonic pattern
        if retracement_counter == 4:
            return True
        
    #otherwise, if there is no match we return a false boolean
    return False

print(match_xabcd_retracements_to_harmonic_patterns(xabcd))