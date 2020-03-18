# Ashwini Pandey
# EMP_ID - 142871
# ver1.0

import matplotlib.pyplot as plt
import pandas as pd


# Expected Range_of_car

def read_file():
    """ Read csv file"""
    df = pd.read_csv('CityDrive2.csv')
    return df


def t_mins(df):
    """ convert time in mins"""
    time = df.loc[0:, 'Trip Time(Since journey start)(s)']
    time = time / 60
    return time


def read_dist(df):
    """ Read dist value"""
    dist = df.loc[0:, 'Trip Distance(km)']
    for i in range(0, 63):
        dist[i] = 0
    return dist


def range_of_car(df):
    """ find range of car"""
    fuel_left = df.loc[0:,
                       'Fuel Remaining (Calculated from vehicle profile)(%)'
                       ]
    mileage = df.loc[0:, 'Kilometers Per Litre(Long Term Average)(kpl)']
    rng = fuel_left * mileage
    return rng


def find_fuel_left(df):
    """ finds fuel level"""
    fuel = df.loc[0:,
                  'Fuel Remaining (Calculated from vehicle profile)(%)']
    fuel_left = fuel[len(fuel) - 1]
    return fuel_left


def plot_range(rng, time, dist):
    """ plots range vs time and dist"""
    plt.plot(time, rng, 'r-')
    plt.title('Expected Range vs time')
    plt.xlabel('Time (in mins)')
    plt.ylabel('Expected Range (in KMs)')
    plt.show()

    plt.figure()
    plt.plot(dist, rng)
    plt.title('Expected Range vs distance')
    plt.xlabel('Distance travelled (in KMs)')
    plt.ylabel('Expected Range (in KMs)')
    plt.show()
