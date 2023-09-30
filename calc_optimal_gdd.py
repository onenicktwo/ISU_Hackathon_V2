import pandas as pd
import gdd_calculator


def get_optimal_gdd(input_file, base_temp):
    # subject to change, just logic down
    # read data from file
    df = pd.read_csv(input_file)

    # set the high and low temps
    high_temp = df['High Temperature']
    low_temp = df['Low Temperature']

    # gets the optimal gdd from the file
    gdd = [gdd_calculator.get_gdd(high, low, base_temp) for high, low in zip(high_temp, low_temp)]
    return gdd


def find_optimum_days(gdd_values):
    # variable holders
    increasing = False
    optimum_start = None
    optimum_end = None

    # loops through the input
    for i in range(len(gdd_values)-1):
        # gets the plant date
        if gdd_values[i] < gdd_values[i+1]:
            if not increasing:
                optimum_start = i
            increasing = True
        # gets the harvest date
        elif gdd_values[i] > gdd_values[i+1]:
            if increasing:
                optimum_end = i
                break
            increasing = False
    # returns both the plant and harvest dates
    return optimum_start, optimum_end
