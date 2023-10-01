import pandas as pd
import gdd_calculator
import pickle


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


def find_optimum_days(gdd_values, min_threshold=0, window_size=7):
    # variable holders
    increasing = False
    optimum_start = None
    optimum_end = None

    # loops through the input
    for i in range(len(gdd_values)-1):
        current_value = gdd_values[i]
        next_value = gdd_values[(i+1) % len(gdd_values)]

        if current_value < min_threshold:
            continue

        if current_value < next_value:
            if not increasing:
                optimum_start = i
            increasing = True
        elif current_value > next_value:
            if increasing:
                optimum_end = i
                if (i - optimum_start + 1) >= window_size:
                    break
            increasing = False
    # returns both the plant and harvest dates
    return optimum_start, optimum_end
