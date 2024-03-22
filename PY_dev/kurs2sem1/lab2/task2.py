import pyinputplus as pyip


class Sides:
    
    def __init__(self, sideslist: list) -> None:
        self._sideslist = sideslist
        
    def inp(self, i: int):
        for i in range(3):
            self._sideslist.append(pyip.inputNum(f"Enter {i+1} side: "))
            
            if len(self._sideslist) != 3:
                continue
            else:
                return self._sideslist
            
def isosceles():
    a, b, c = Sides([]).inp(0)[0:3]
    
    if (a == b or b == c or c == a) & (not a == b == c):
        print("This triangle is isosceles!")
    else:
        print("Not isosceles triangle")
    
def main():

    isosceles()
    
if __name__ == "__main__":
    main()
