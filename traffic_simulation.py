class Road:
    def __init__(self):
        self.length = 999
        self.road_entrance = 0

    def car_loop(self):
        """Car will return to 0 if motion exceeds road length"""
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

    def move_car

    def car_space_ahead

    def set_location


#[0, 0, 0, 1, 1, Car, 1, 1, 0, 0, 0, 0, 1, 1, Car, 1, 1, 0, 0]


red_car = Vehicle(7,12)

blue_car = Vehicle(0,4)

[Car, Car, Car, Car, Car]

blue_car.get_space

    next_car.speed
