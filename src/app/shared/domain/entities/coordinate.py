

class Coordinate: 
    x: int
    y: int

    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    @staticmethod
    def from_json(json):
        return Coordinate(json['x'], json['y'])

    def move_command(self, move: str):
      moves = {
        "up": Coordinate(self.x, self.y + 1),
        "down": Coordinate(self.x, self.y - 1),
        "left": Coordinate(self.x - 1, self.y),
        "right": Coordinate(self.x + 1, self.y),
    }
      return moves.get(move, Coordinate(self.x, self.y))
