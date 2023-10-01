
def get_gdd(high_temperatures, low_temperatures, base):
    gdd_values = []

    for high, low in zip(high_temperatures, low_temperatures):
        mean_temp = float(((min(high, 86.00) + min(low, 50.00)) / 2))
        gdd_value = max(mean_temp - base, 0)
        gdd_values.append(gdd_value)

    return gdd_values