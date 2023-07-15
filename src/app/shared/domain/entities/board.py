from src.app.shared.domain.entities.battlesnake import Battlesnake
from src.app.shared.domain.entities.coordinate import Coordinate
from typing import List
"""

{
  "height": 11,
  "width": 11,
  "food": [
    {"x": 5, "y": 5}, 
    {"x": 9, "y": 0}, 
    {"x": 2, "y": 6}
  ],
  "hazards": [
    {"x": 0, "y": 0}, 
    {"x": 0, "y": 1}, 
    {"x": 0, "y": 2}
  ],
  "snakes": [
    {"id": "snake-one", ... },
    {"id": "snake-two", ... },
    {"id": "snake-three", ... }
  ]
}


"""



class Board:

    heigth: int
    width: int
    food: List[Coordinate]
    hazards: List[Coordinate]
    snakes: List[Battlesnake]

    def __init__(self, heigth:int, width:int, food:List[Coordinate], hazards:List[Coordinate], snakes:list[Coordinate]):
        self.heigth = heigth
        self.width = width
        self.food = food
        self.hazards = hazards
        self.snakes= snakes

    @staticmethod
    def from_json(json):
        height = json["height"]
        width = json["width"]
        food = [Coordinate.from_json(food) for food in json["food"]]
        snakes = [Battlesnake.from_json(snake) for snake in json["snakes"]]
        hazards = [Coordinate.from_json(hazard) for hazard in json["hazards"]]
        return Board(height, width, food, snakes, hazards)
    