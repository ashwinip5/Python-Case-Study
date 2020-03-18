# Ashwini Pandey
# EMP_ID - 142871
# ver1.0
from statistics import mean
import matplotlib.pyplot as plt



# Road Condition
def find_mean_val(z_val):
    """Finds mean value of z"""
    mean_val = mean(z_val)
    return mean_val


def find_good_roads(z_val, df):
    """Find location of good roads"""
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    plt.figure()
    for i in range(0, len(lat)):
        if z_val[i] < 0.94:
            plt.scatter(lat[i], long[i], color=['green'])

        elif z_val[i] > 0.9:
            plt.scatter(lat[i], long[i], color=['green'])


def find_bad_roads(z_val, df):
    """Find location of bad roads"""
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    for i in range(0, len(lat)):
        if z_val[i] > 1.1:
            plt.scatter(lat[i], long[i], color=['blue'])
        elif z_val[i] < 0.7:
            plt.scatter(lat[i], long[i], color=['blue'])
    plt.title('Road Condition')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    