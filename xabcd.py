xabcd = {
    'coords': {
        'x': 'na',
        'a': 'na',
        'b': 'na',
        'c': 'na',
        'd': 'na'
    },
    'index': {
        'x': 'na',
        'a': 'na',
        'b': 'na',
        'c': 'na',
        'd': 'na'
    },
    'type': {
        'x': 'max',
        'a': 'na',
        'b': 'na',
        'c': 'na',
        'd': 'na'
    },
    'retracements': {
        'xb': 'na',
        'ac': 'na',
        'bd': 'na',
        'xd': 'na'
    }
}

#this upgraded version will have methods checking if the spots are filled and if they're not it keeps looking for the next point
# if its full then it will look for the next and bump up the points
upgraded_xabcd = {
    'stage': 'filling',
    'coords': {
        'x': '1',
        'a': '2',
        'b': '3',
        'c': '4',
        'd': '5'
    },
    'index': {
        'x': '2',
        'a': '5',
        'b': '6',
        'c': '7',
        'd': '8'
    },
    'type': {
        'x': 'max',
        'a': 'min',
        'b': 'max',
        'c': 'min',
        'd': 'max'
    },
    'retracements': {
        'xb': '2',
        'ac': '5',
        'bd': '2',
        'xd': '5'
    }
}

#otherwise, we are going to check what the last extremum was by doing a reverse for loop through the coords in xabcd and checking which one is not occupied
for object in reversed(xabcd['type']):
    if xabcd['type'][object] == 'na':
        continue

    #if its not occupied, then we check the type
    type = xabcd['type'][object]
    print(type)
            