# Ashwini Pandey
# EMP_ID - 142871
# ver1.0
import expected_range as exp
import pothole_detection as pot
import roadcondition_detection as road
import CO2_emission as CO2
import rashdriving_detection as rash

df = exp.read_file()

# Range of car as per the fuel left
print("\n Feature 1 :- Range of car ")
rng = exp.range_of_car(df)
time = exp.t_mins(df)
dist = exp.read_dist(df)
X = exp.find_fuel_left(df)
Y = rng[len(rng) - 1]
print("The fuel left in the car is : {0:.2f} Litres".format(X))
print('Expected distance it can travel more is : {0:.2f} KMs'.format(Y))
exp.plot_range(rng, time, dist)

# Pot Holes detection
print("\n Feature 2 :- Pot Holes detection ")
z_val = pot.find_z_val(df)
pot.plot_route(df)
pot.plot_potholes(z_val, df)

# Road Condition detection
print("\n Feature 3 :- Road Condition detection ")
mean_val = road.find_mean_val(z_val)
road.find_good_roads(z_val, df)
road.find_bad_roads(z_val, df)
road.plt.legend(['Good Road condition', 'Bad Road condition'])
road.plt.show()

# Co2 emission
print("\n Feature 4 :- Co2 emission ")
CO2.plot_emission(df)
CO2.fuel_economy(df)

# Rash driving
print("\n Feature 5 :- Rash driving")
pos_d = rash.pedal_pos_d(df)
pos_e = rash.pedal_pos_e(df)
rash.detect_rash_driving(df, pos_d, pos_e)
