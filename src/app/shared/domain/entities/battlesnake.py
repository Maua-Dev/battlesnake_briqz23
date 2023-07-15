from typing import List

from src.app.shared.domain.entities.coordinate import Coordinate
from src.app.shared.domain.entities.customization import Customization


"""
{
  "id": "totally-unique-snake-id",
  "name": "Sneky McSnek Face",
  "health": 54,
  "body": [
    {"x": 0, "y": 0}, 
    {"x": 1, "y": 0}, 
    {"x": 2, "y": 0}
  ],
  "latency": "123",
  "head": {"x": 0, "y": 0},
  "length": 3,
  "shout": "why are we shouting??",
  "squad": "1",
  "customizations":{
    "color":"#26CF04",
    "head":"smile",
    "tail":"bolt"
  }
}

"""

class Battlesnake:
    id_value: str
    name: str
    health: int
    body: List[Coordinate]
    latency: str
    head: Coordinate
    length: int
    shout: str
    squad: str
    customizations: Customization

    def __init__(self, id_value: str, name: str, health: int, body: List[Coordinate], 
                 latency: str, head: Coordinate, length: int, shout: str, squad: str, customizations:Customization):
        
        self.id_value = id_value
        self.name = name
        self.health = health
        self.body = body
        self.latency = latency
        self.head = head
        self.length = length
        self.shout = shout
        self.squad = squad
        self.customizations: Customization


    @staticmethod
    def from_json(json):
        snake_id = json["id"]
        name = json["name"]
        health = json["health"]
        body = [Coordinate.from_json(body) for body in json["body"]]
        latency = json["latency"]
        head = Coordinate.from_json(json["head"])
        length = json["length"]
        shout = json["shout"]
        squad = json.get("squad", "")
        
        customizations_json = json.get("customizations", {})
        customizations = Customization.from_json(customizations_json)
        
        return Battlesnake(snake_id, name, health, body, latency,
                            head, length, shout, squad, customizations)


      



    
