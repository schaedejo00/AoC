from numpy.f2py.crackfortran import previous_context

from D06.Direction import Direction


def wont_leave_map(self, x, y):
    pass


class Map:


    # Constructor
    def __init__(self, map: list[list[chr]]):
        self.map: list[list[chr]] = map
        self.loop: bool = False

    # Get the position of an object in the map and the object itself
    def get_position(self, obstacles: list[str]) -> tuple[int, int, int]:
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if self.map[y][x] in obstacles:
                    return (x, y, self.map[y][x])
        return None

    def get_map(self):
        return self.map

    # get the start position of the guard and its direction
    def get_start(self) -> tuple[int, int, int]:
        return self.get_position([e.value for e in Direction])



    #Move the guard until it leaves the map
    def move(self) -> 'Map':
        x: int
        y: int

        x, y, obstacle = self.get_start()
        direction: Direction = Direction(obstacle)
        #quick and dirty: für den Sonderfall, dass ein Loop entsteht, indem man hin und zurück läuft
        max_steps: int = self.get_width() * self.get_height() * 4
        steps: int = 0
        while steps < max_steps:
            steps += 1
            nx, ny = direction.next_coordinates(x, y)

            if nx < 0 or nx >= self.get_width() or ny < 0 or ny >= self.get_height():
                self.set_value(x, y, direction.value)
                return self
            elif self.get_value(nx, ny) == '#':
                next_direction: Direction = direction.next()
                previous_direction: Direction = direction
                if self.get_value(x, y) in [next_direction.value, previous_direction]:
                    self.loop = True
                    return self
                direction = direction.next()
                self.set_value(x, y, direction.value)
            elif self.get_value(nx, ny) != '#':
                self.set_value(x, y, direction.value)
                x, y = nx, ny

        self.loop = True
        return self

    def has_loop(self) -> bool:
        return self.loop

    # Set value of a cell
    def set_value(self, x, y, value):
        self.map[y][x] = value

    # Get value of a cell
    def get_value(self, x, y):
        return self.map[y][x]

    # Get width of the map
    def get_width(self):
        return len(self.map[0])

    # Get height of the map
    def get_height(self):
        return len(self.map)

    # Print the map
    def print_map(self):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                print(self.map[y][x], end=' ')
            print()

    def count_guarded_steps(self) -> int:
        count: int = 0
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if self.map[y][x] in [e.value for e in Direction]:
                    count += 1
        return count