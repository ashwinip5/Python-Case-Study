#Ashwini Pandey
# EMP_ID - 142871
# ver1.0
import matplotlib.pyplot as plt
import pandas as pd
#import gmplot


# Pot Holes detection
def find_z_val(df):
    """ find accelerometer z value"""
    z_val = df.loc[0:, 'Acceleration Sensor(Z axis)(g)']
    return z_val


def plot_potholes(z_val, df):
    """ plot pot holes"""
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    df2 = pd.DataFrame(columns=['Latitude', 'Longitude'])
 #   gmap2 = gmplot.GoogleMapPlotter(lat[0], long[0], 14)

    for i in range(0, len(lat)):
        if z_val[i] > 1.2:
            plt.scatter(lat[i], long[i], color=['blue'])
            df2.loc[len(df2)] = [lat[i], long[i]]
        elif z_val[i] < 0.6:
            plt.scatter(lat[i], long[i], color=['blue'])
            df2.loc[len(df2)] = [lat[i], long[i]]
    df3 = df2.iloc[0:, 0]
    df4 = df2.iloc[0:, 1]
    plt.legend(['Route', 'Pot Holes'])
    plt.show()
 #   gmap2.plot(lat, long, 'magenta')
 #   gmap2.scatter(df3, df4, 'red', size=50, marker=False)
 #   gmap2.draw("Google_map_pot_holes.html")
    print("Pot Holes are at the following location : -")
    print(df2)


def plot_route(df):
    """ Plot route"""
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    plt.figure()
    plt.plot(lat, long, 'r-')
    plt.title('Pot holes in route')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
 #   gmap1 = gmplot.GoogleMapPlotter(lat[0], long[0], 14)
 #   gmap1.plot(lat, long, 'magenta')
 #  gmap1.draw("Google_map_car_route.html")
    