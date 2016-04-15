

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate

from traffic_simulation import *


car_list = []
for number in range(30):
    car_list.append(Vehicle((number * 33, (number * 33) + 4)))

total_car_location = []
for number in range(120):
    car_locations = []
    for index, car in enumerate(car_list):
        car_locations.append(car.location)
        try:
            car.move_car(car_list[index + 1])
        except IndexError:
            car.move_car(car_list[0])
    total_car_location.append(car_locations)




# print(list(range(total_car_location[0][0][0], total_car_location[0][0][1]+1)))

plot_all_locations = []

for locations in total_car_location:
    iteration_list = []
    for location in locations:
        car_range = list(range(location[0], location[1]+1))
        if len(car_range) == 0:
            car_range = list(range(location[0], 1001)) + list(range(1, location[1] + 1))
        iteration_list += car_range
    plot_all_locations.append(iteration_list)

# print(plot_all_locations)

n = 120
for iteration in plot_all_locations:
    x = iteration
    y = [n] * len(iteration)
    plt.scatter(x, y)
    n -= 1

plt.xlim(1, 1000)
plt.ylim(0, 120)
plt.show()
