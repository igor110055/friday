minimum_pattern_lenght = 20

maximum_pattern_lenght = 160

error_rate = 0.06



harmonic_patterns = {
    'crab': {
        'xb_retracement': [0.382, 0.618],
        'ac_retracement': [0.382, 0.886],
        'bd_retracement': [2.24, 3.618],
        'xd_retracement': 1.618
    },
    'butterfly': {
        'xb_retracement': 0.786,
        'ac_retracement': [0.382, 0.886],
        'bd_retracement': [1.618, 2.618],
        'xd_retracement': [1.27, 1.618]
    },
    'bat': {
        'xb_retracement': [0.382, 0.50],
        'ac_retracement': [0.382, 0.886],
        'bd_retracement': [1.618, 2.618],
        'xd_retracement': 0.886
    },
    'gartley': {
        'xb_retracement': 0.618,
        'ac_retracement': [0.382, 0.886],
        'bd_retracement': [1.27, 1.618],
        'xd_retracement': 0.786
    }
}