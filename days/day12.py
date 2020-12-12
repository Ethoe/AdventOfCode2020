class Ship:
    def __init__(self):
        self.facing = 0
        self.vert = 0
        self.horz = 0
        self.waypoint = [1, 10]
        self.direct = ((0, 1), (-1, 0), (0, -1), (1, 0))

    def execute(self, action, value):
        if action == 'N':
            self.vert += value
        elif action == 'S':
            self.vert -= value
        elif action == 'E':
            self.horz += value
        elif action == 'W':
            self.horz -= value
        elif action == 'F':
            self.vert += self.direct[self.facing][0] * value
            self.horz += self.direct[self.facing][1] * value
        else:
            turn = 1
            if action == 'L':
                turn = -1
            value = value / 90
            self.facing = int((self.facing + (value * turn))) % 4

    def execute_p2(self, action, value):
        if action == 'N':
            self.waypoint[0] += value
        elif action == 'S':
            self.waypoint[0] -= value
        elif action == 'E':
            self.waypoint[1] += value
        elif action == 'W':
            self.waypoint[1] -= value
        elif action == 'F':
            self.vert += self.waypoint[0] * value
            self.horz += self.waypoint[1] * value
        else:
            turn = True
            if action == 'L':
                turn = False
            value = int(value / 90)

            for _ in range(value):
                x = self.waypoint[0]
                y = self.waypoint[1]
                if turn:
                    self.waypoint = [-y, x]
                else:
                    self.waypoint = [y, -x]

    def distance(self):
        return abs(self.vert) + abs(self.horz)


def p1(directions):
    ship = Ship()
    for action, value in directions:
        ship.execute(action, value)
    return ship.distance()


def p2(directions):
    ship = Ship()
    for action, value in directions:
        ship.execute_p2(action, value)
    return ship.distance()


with open('../inputs/day12in.txt') as read:
    directions_list = [(x[0], int(x.strip()[1:])) for x in read.readlines()]

print(f'P1: {p1(directions_list)} || P2: {p2(directions_list)}')
