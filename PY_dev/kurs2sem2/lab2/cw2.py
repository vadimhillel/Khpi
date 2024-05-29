class List:
    def __init__(self, type: type) -> None:
        self.type = type
        self.items = []
        self.count = 0
    
    def add(self, item):
        if not isinstance(item, self.type):
            item_type = "str" if self.type == str else "int" if self.type == int else "float"
            return "This item is not of type: %s" % (item_type)
        else:
            self.items.append(item)
            self.count += 1
            return self

my_list=List(int)
my_list.add(0).add(1)

print(my_list.count)