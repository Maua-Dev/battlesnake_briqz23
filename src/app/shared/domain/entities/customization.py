class Customization:
    apiversion = 1  

    def __init__(self, color: str, head: str, tail: str):
        self.color = color
        self.head = head
        self.tail = tail

    @staticmethod
    def from_json(json):
        return Customization(json['color'], json['head'], json['tail'])
