class Person:
    def __init__(self, name: str, age: int) -> None:
        self.info = f"{name}s age is {age}"
    
person = Person("john", 16)

print(person.info)