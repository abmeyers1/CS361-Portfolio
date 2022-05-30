# Functions for converting units


def unit_convert(value, unit1, unit2):

    emp = {
        'inches':1,             # [0] is order of size, [1] is factor to multiply
        'feet': 12,
        'yards': 36,
        'miles':63360
    }

    metric = {
        'millimeters':1,
        'centimeters':10,
        'meters':1000,
        'kilometers':1000000
    }

    # Same unit, no calculation needed
    if unit1 == unit2:
        # print('EQUAL')
        return value

    # Both empirical
    if unit1 in emp and unit2 in emp:
        # print('BOTH EMP')
        if unit1 != 'inches':
            value /= emp[unit1]        # convert down to inches
        value *= emp[unit2]
        return value
    
    # Both metric
    if unit1 in metric and unit2 in metric:
        # print("BOTH METRIC")
        if unit1 != 'millimeters':
            value /= metric[unit1]         # convert down to inches
        value *= metric[unit2]
        return value
    
    else:                               # units in different standards
        # print("CHANGE STYLES")
        if unit1 in metric:             # convert the value from metric to emperical
            # print('UNIT1 is Metric!')
            if unit1 != 'millimeters':
                value /= metric[unit1]     # convert down to millimeters
            value *= 25.4               # convert inches to millimeter
            value *= emp[unit2]      # convert up from millimeter to unit2

        else:                           # convert the value to emperical
            # print('GGGGGG GUNIT1 is emperical')
            if unit1 != 'inches':
                value /= emp[unit1]
              
            value /= 25.4               # convert mm to inches
            value *= metric[unit2]         # convert up from inches to unit2
        return value

    
# val = 1
# unit1= 'inches'
# unit2= 'centimeters'
# print( unit_convert(val, unit1, unit2))
