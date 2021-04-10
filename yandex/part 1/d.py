class Vehicle:

    def __init__(self, number, speed):
        self.number = number
        self.speed = speed


class Car(Vehicle):

    def __init__(self, number, speed, fuel):
        super().__init__(number, speed)
        if fuel == 95:
            self.speed *= 0.9
        elif fuel == 92:
            self.speed *= 0.8


class Motorcycle(Vehicle):

    def __init__(self, number, speed, fuel):
        super().__init__(number, speed)
        if fuel == 95:
            self.speed *= 0.8
        elif fuel == 92:
            self.speed *= 0.6


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    mins = []
    for i in range(n):
        vals = list(map(int, input().split()))
        veh = Vehicle(vals[0], vals[2])
        if vals[1] == 1:
            veh = Car(vals[0], vals[2], vals[3])
        elif vals[1] == 2:
            veh = Motorcycle(vals[0], vals[2], vals[3])
        distance = m - t * veh.speed % m
        if not mins:
            mins = [distance, veh]
        else:
            if distance < mins[0]:
                mins = [distance, veh]
            elif distance == mins[0]:
                if veh.number < mins[1].number:
                    mins = [distance, veh]
    print(mins[1].number)
