# La Gra doing, GDD Calculator

def get_gdd(high, low, base):
    # place holding statements
    gdd_value = 0
    mean_temp = float(high + low / 2)
    gdd_value = base - mean_temp
    return gdd_value