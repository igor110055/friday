API_KEY = "647d614e645f5e9baf91dc73fc596580-a5bb88b608640df41b0d857ad569acd8"
ACCOUNT_ID = "101-002-22473635-001"
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}'
}

minimum_pattern_lenght = 20

maximum_pattern_lenght = 160

error_rate = 0.03



harmonic_patterns = {
    'crab': {
        'xb': [0.382, 0.618],
        'ac': [0.382, 0.886],
        'bd': [2.24, 3.618],
        'xd': 1.618
    },
    'butterfly': {
        'xb': 0.786,
        'ac': [0.382, 0.886],
        'bd': [1.618, 2.618],
        'xd': [1.27, 1.618]
    },
    'bat': {
        'xb': [0.382, 0.50],
        'ac': [0.382, 0.886],
        'bd': [1.618, 2.618],
        'xd': 0.886
    },
    'gartley': {
        'xb': 0.618,
        'ac': [0.382, 0.886],
        'bd': [1.27, 1.618],
        'xd': 0.786
    }
}