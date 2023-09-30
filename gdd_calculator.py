# Just an outline of a GDD Calculator

def get_gdd(high, low, base):
    # calculate mean temperature
    mean_temp = float((high + low) / 2)

    # calculates the gdd
    gdd_value = max(mean_temp - base, 0)

    # returns the gdd
    return gdd_value
