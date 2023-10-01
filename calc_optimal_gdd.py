import pandas as pd
import gdd_calculator

def find_optimum_days(gdd_values, min_threshold=0, window_size=7):
    # sets variables to be used
    increasing = False
    optimum_start = None
    optimum_end = None

    # loops through the list
    for i in range(len(gdd_values)-1):
        current_value = gdd_values[i]
        next_value = gdd_values[i+1]

        if current_value < min_threshold:
            continue

        # checks if the current_val is less than the next one and sets it to the current if it doesn't increase
        if current_value < next_value:
            if not increasing:
                optimum_start = i
            increasing = True # sets increase to true if hte next value is greater
        elif current_value > next_value:
            if increasing:
                optimum_end = i
                if (i - optimum_start + 1) >= window_size:
                    break
            increasing = False

    return optimum_start, optimum_end
