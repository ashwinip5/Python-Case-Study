# Ashwini Pandey
# EMP_ID - 142871
# ver1.0
import matplotlib.pyplot as plt


# Co2 emission
def plot_emission(df):
    """ plot emission of co2 on route"""
    co2 = df.loc[0:, 'CO₂ in g/km (Average)(g/km)']
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    plt.figure()
    plt.plot(lat, long, 'r-')
    plt.title('CO2 emission')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    for i in range(0, len(lat)):
        if co2[i] < 200:
            plt.scatter(lat[i], long[i], color=['blue'])
    plt.legend(['Route', 'Less Co2 emission'])
    plt.show()
    # print("The places marked with blue colour denote less CO2 emission")


def fuel_economy(df):
    """ plot fuel economy on route"""
    fuel_econom = df.loc[0:, 'Kilometers Per Litre(Long Term Average)(kpl)']
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    plt.figure()
    plt.plot(lat, long, 'r-')
    plt.title('Fuel Economy')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    for i in range(0, len(lat)):
        if fuel_econom[i] > 11.5:
            plt.scatter(lat[i], long[i], color=['green'])
    plt.legend(['Route', 'Good fuel economy'])
    plt.show()
    print("Relation :- The places with less CO2 emission has good fuel economy as well")
    