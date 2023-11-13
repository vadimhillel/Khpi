N = ord("V") % 5 + 1
print(f"\n\t Number of variant is {N}\n")

class MyFunctions:
    def __init__(self, list1: list, list2: list) -> None:
        self._list1 = list1
        self._list2 = list2

    def func1(self) -> list:
        """for Loop + List comprehension"""
        for i in self._list2:
            self._list1 = [0 if x==i else x for x in self._list1]
        return self._list1
    
    def func2(self) -> list:
        """for Loop + mapping/lambda, in return list"""
        for i in self._list2:
            self._list1 = list(map(lambda x: x if x != i else 0, self._list1))
        return self._list1
    
    def func3(self) -> list:
        """for Loop + while loop + .index"""
        my_idx = -1
        for i in self._list2:
            while True:
                try:
                    my_idx = self._list1.index(i, my_idx + 1)
                    self._list1[my_idx] = 0
                except ValueError:
                    break
        
        return self._list1
    
    def func4(self) -> list:
        """for Loop + for Loop + List Slicing"""
        for i in range(len(self._list2)):
            for j in self._list2:
                if self._list1[i] == j:
                    self._list1 = self._list1[:i] + [0] + self._list1[i+1]
        return self._list1
    
    def source_list(self) -> None:
        print("Source list is: ", self._list1)
