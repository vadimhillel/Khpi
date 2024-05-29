class Quark(object):
    def __init__(self, color: str, flavor: str) -> None:
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1.0 / 3
    
    def interact(self, other):
        self.color, other.color = other.color, self.color
        
        
q1 = Quark("red", "up")
print(q1.color) # -> "red"

print(q1.flavor) # -> "up"

q2 = Quark("blue", "strange")
print(q2.color) # -> "blue"

print(q2.baryon_number) # -> 0.3333333333333333

q1.interact(q2)
print(q1.color) # -> "blue"

print(q2.color) # -> "red"
