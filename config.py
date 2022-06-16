#oanda api config
API_KEY = "647d614e645f5e9baf91dc73fc596580-a5bb88b608640df41b0d857ad569acd8"
ACCOUNT_ID = "101-002-22473635-001"
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}'
}

#telegram login
TELEGRAM_BOT_TOKEN = '5565948030:AAFMpHyoURnFSsPT5IEyVynSSzGR3VT6ITs'
TELEGRAM_NOTIFICATIONS_GROUP_ID = '-796380042'
TELEGRAM_EXCEPTION_GROUP_ID = '-796380042'

#harmonic config
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

black_swan = {
    'black_swan': {
        'xb': [1.382, 2.618],
        'ac': [0.236, 0.5],
        'bc': [1.128, 2],
        'xd': [1.128, ]
    }
}