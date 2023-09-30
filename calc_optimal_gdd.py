import pandas as pd
import gdd_calculator


def get_optimal_gdd(input_file, base_temp):
    # subject to change, just logic down
    # read data from file
    df = pd.read_csv(input_file)

    # set the high and low temps
    high_temp = df['High Temperature']
    low_temp = df['Low Temperature']

    gdd = gdd_calculator.get_gdd(high_temp, low_temp, base_temp)
    return gdd
