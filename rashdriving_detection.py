# Ashwini Pandey
# EMP_ID - 142871
# ver1.0

import matplotlib.pyplot as plt


# Rash Driving detection

def pedal_pos_d(df):
    """ Find pedal position"""
    pos_d = df.loc[0:, 'Accelerator PedalPosition D(%)']
    return pos_d


def pedal_pos_e(df):
    """ find pedal position"""
    pos_e = df.loc[0:, 'Accelerator PedalPosition E(%)']
    return pos_e


def detect_rash_driving(df, pos_d, pos_e):
    """Detects rash driving"""
    lat = df.loc[0:, ' Latitude']
    long = df.loc[0:, ' Longitude']
    plt.figure()
    plt.scatter(lat, long)
    plt.title('Rash driving detection')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    for i in range(0, len(lat)):
        if pos_d[i] > 55:
            if pos_e[i] > 27.5:
                plt.scatter(lat[i], long[i], color=['green'])
    plt.legend(['Route', 'Rash driving spots'])
    plt.show()
    print ('The green spots show that the rash driving was done there.')
