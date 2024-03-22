class MyClass:
    def __init__(self) -> None:
        pass

def class_name_changer(cls, new_name: str):
    if new_name[0].isupper() and new_name.isidentifier():
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid class name")

# Usage
MyClass.__name__ = ''  # Trying to change the class name to an empty string
print(MyClass.__name__)  # Output should be the original class name "MyClass"

# Changing class name correctly
class_name_changer(MyClass, "NewClassName")
print(MyClass.__name__)  # Output should be "NewClassName"
