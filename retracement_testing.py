xabcd_points = {
    'x': {'extremum_value': 95.742, 'extremum_type': 'max', 'extremum_index': 0},
    'a': {'extremum_value': 90.433, 'extremum_type': 'min', 'extremum_index': 8},
    'b': {'extremum_value': 94.026, 'extremum_type': 'max', 'extremum_index': 13},
    'c': {'extremum_value': 87.302, 'extremum_type': 'min', 'extremum_index': 15},
    'd': {'extremum_value': 96.880, 'extremum_type': 'min', 'extremum_index': 15}
}

#step one we find the retracement from x to b

#first we gotta check if the first point is a max or a min

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