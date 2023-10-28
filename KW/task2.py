import pyinputplus as pyip


class Lists:
    def __init__(self, list1: list, list2: list) -> None:
        self._list1 = list1
        self._list2 = list2

class Work(Lists):
    
    def inpfunc(self):
        for n in range(2):
            print(f"Enter 3 digits for {n+1} list: ")
            for i in range(3):
                inp = pyip.inputNum()
                if len(self._list1) < 3:
                    self._list1.append(inp)
                else: 
                    self._list2.append(inp)
        print(f"\n1st list is {self._list1}", 
              f"\n2nd list is {self._list2}\n")
            
    def function(self) -> list:
        for i in self._list2:
            self._list1 = [0 if x==i else x for x in self._list1]
  
def main():
    w = Work([], [])
    w.inpfunc()
    w.function()
    print(w._list1)
    
main()
    