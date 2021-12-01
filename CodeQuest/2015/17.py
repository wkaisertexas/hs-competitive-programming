import math
class Ship:
    def __init__(self, string):
        self.name = string.split("_")[0]
        self.ship_class = string.split("_")[1].split(":")[0]
        x_and_y = string.split(":")[1].split(",")
        self.x = int(x_and_y[0])
        self.y = int(x_and_y[1])

    def advance(self):
        class_speed = {
                "A":10,
                "B":20,
                "C":30
                }
        self.x -= class_speed[self.ship_class]
    
    def get_compareable_value(self):
        # I know this is a terrible way to compare things, but it should work
        return self.x - self.y / 1000 * math.copysign(1, self.x)

    
    def __str__(self):
        return f"Destroyed Ship: {self.name} xLoc: {self.x}"


if __name__=="__main__":
    pass
    n_cases = int(input())

    for case in range(n_cases):
        n_ships = int(input())

        ships = [Ship(input()) for x in range(n_ships)]
        
        while not len(ships) == 0:
            ranking_list = [ship.get_compareable_value() for ship in ships]
            min_index = ranking_list.index(min(ranking_list))

            print(ships[min_index])
            ships.pop(min_index)
            for ship in ships:
                ship.advance()


