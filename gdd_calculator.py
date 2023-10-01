
def get_gdd(high, low, base):

    # calculate mean temp
    mean_temp = float(((min(high, 86.00) + min(low, 50.00)) / 2))

    # calculates the gdd
    gdd_value = max(mean_temp - base, 0)

    # returns the gdd
    return gdd_value
