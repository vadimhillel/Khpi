class Quark(object):
    def __init__(self, color: str, flavor: str) -> None:
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1.0 / 3
    
    def interact(self, other):
        self.color, other.color = other.color, self.color