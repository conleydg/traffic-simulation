class Road:
    def __init__(self, length=1000):
        self.length = length - 1
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
    def __init__(self, location=(0, 4)):
        self.location = location
        self.speed = 0
        self.acceleration = 2.0
        self.size = 5
        self.max_speed = 33.3333
        self.desired_space = round(self.speed)

    def move_car(self, next_car):
        space = self.get_space_ahead(next_car)
        self.update_speed(space, next_car)
        self.set_location(space)

    def get_space_ahead(self, next_car):
        if next_car.location[0] < self.location[1]:
            return (1000 - self.location[1]) + next_car.location[0]
        else:
            return next_car.location[0] - self.location[1]

    def set_location(self):
        start = self.location[0] + self.speed
        end = self.location[1] + self.speed
        # (993, 998) --> (998, 1003)
        if start > 1000:
            start = start - 1000
        if end > 1000:
            end = end - 1000
        self.location = (start, end)

    def update_speed(self, space, next_car):
        if space >= self.desired_space:
            if self.speed < self.max_speed:
                self.speed += self.acceleration
        elif space < 2:
            self.speed = 0
        else:
            self.speed = next_car.speed
# [0, 0, 0, 1, 1, Car, 1, 1, 0, 0, 0, 0, 1, 1, Car, 1, 1, 0, 0]


red_car = Vehicle(7, 12)

blue_car = Vehicle(0, 4)

# [Car, Car, Car, Car, Car]
