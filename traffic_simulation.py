import random
import statistics as st

class Simulation:
    def __init__(self, speeds, time, trials):
        self.speeds = speeds
        self.time = time
        self.trials = trials

    def make_cars(self, speed):
        car_list = []
        for number in range(30):
            car_list.append(Vehicle(
                            (number * 33, (number * 33) + 4), max_speed=speed))
        return car_list

    def get_location_one_trial(self, speed, time):
        car_list = self.make_cars(speed)

        total_car_location = []
        for number in range(time):
            car_locations = []
            for index, car in enumerate(car_list):
                car_locations.append(car.location)
                try:
                    car.move_car(car_list[index + 1])
                except IndexError:
                    car.move_car(car_list[0])
            total_car_location.append(car_locations)
        return total_car_location

    def get_all_speeds(self, speed, time):
        car_list = self.make_cars(speed)

        total_car_speeds = []
        average_speeds = []
        for number in range(time):
            car_speeds = []
            for index, car in enumerate(car_list):
                car_speeds.append(car.speed)
                try:
                    car.move_car(car_list[index + 1])
                except IndexError:
                    car.move_car(car_list[0])
            total_car_speeds.append(car_speeds)
            average_speeds.append(st.mean(car_speeds))
        return total_car_speeds, st.mean(average_speeds)

    def full_monte(self):
        speeds_list = []
        average_speeds_list = []
        for speed in self.speeds:
            for trial in range(self.trials):
                trial_speeds_list, trial_average_speeds_list = self.get_all_speeds(speed, self.time)
                speeds_list.append(trial_speeds_list)
                average_speeds_list.append(trial_average_speeds_list)
        return speeds_list, average_speeds_list



class Vehicle:
    """ Requirements:
    1 km road
    5m long cars
    120km/h max speed
    2m/s acceleration
    if car would collide, car will stop
    10 percent chance of slowing down 2m/s
    30 cars in simulation, evenly spaced at start.
    """
    def __init__(self, location=(0, 4), speed=0, max_speed=33):
        self.location = location
        self.speed = speed
        self.acceleration = 2
        self.size = 5
        self.max_speed = max_speed
        self.desired_space = self.speed
        self.last_location = location

    def move_car(self, next_car):
        space = self.get_space_ahead(next_car)
        self.update_speed(space, next_car)
        self.random_slowdown()
        self.set_location(next_car)

    def get_space_ahead(self, next_car):
        if next_car.location[0] < self.location[1]:
            return (1000 - self.location[1]) + next_car.location[0]
        else:
            return next_car.location[0] - self.location[1]

    def set_location(self, next_car):
        start = self.location[0] + self.speed
        end = self.location[1] + self.speed
        # (993, 998) --> (998, 1003)
        if start > 1000:
            start = start - 1000
        if end > 1000:
            end = end - 1000
        # (998, 1003) --> (998, 3)
        self.last_location = self.location
        self.location = (start, end)

    def update_speed(self, space, next_car):
        # print("Space between cars: ", space)
        if space <= 2:
            self.speed = 0
        elif space >= self.speed:
            if self.speed < self.max_speed:
                self.speed += self.acceleration
            elif self.speed > self.max_speed:
                self.speed = self.max_speed
        else:
            self.speed = next_car.speed

    def random_slowdown(self):
        if random.random() < .10:
            if self.speed > 2:
                self.speed -= 2

# # [0, 0, 0, 1, 1, Car, 1, 1, 0, 0, 0, 0, 1, 1, Car, 1, 1, 0, 0]
# car_list = []
# for number in range(30):
#     car_list.append(Vehicle((number * 33, (number * 33) + 4)))
#
# total_car_location = []
# for number in range(120):
#     car_locations = []
#     for index, car in enumerate(car_list):
#         car_locations.append(car.location)
#         try:
#             car.move_car(car_list[index + 1])
#         except IndexError:
#             car.move_car(car_list[0])
#     total_car_location.append(car_locations)

# print(total_car_location)
#
tron = Simulation([30], 60, 10)
speeds_list, average_speeds_list = tron.full_monte()
print("Average Speeds: ", average_speeds_list)
