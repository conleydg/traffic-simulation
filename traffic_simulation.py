import random


class Road:
    def __init__(self, length=1000):
        self.length = length
        self.road_entrance = 0

    def car_loop(self):
        """Car will return to 0 if motion exceeds road length"""
        pass


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
    def __init__(self, location=(0, 4), speed=0):
        self.location = location
        self.speed = speed
        self.acceleration = 2
        self.size = 5
        self.max_speed = 33
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
        self.last_location = self.location
        self.location = (start, end)

    def update_speed(self, space, next_car):
        print("Space between cars: ", space)
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

# [0, 0, 0, 1, 1, Car, 1, 1, 0, 0, 0, 0, 1, 1, Car, 1, 1, 0, 0]
car_list = []
for number in range(30):
    car_list.append(Vehicle((number * 10, (number * 10) + 4)))

total_car_location = []
for number in range(10):
    car_locations = []
    for index, car in enumerate(car_list):
        car_locations = car_locations + list(car.location)
        try:
            car.move_car(car_list[index + 1])
        except IndexError:
            car.move_car(car_list[0])
    total_car_location.append(car_locations)

print(total_car_location)
#
