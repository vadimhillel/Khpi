import numpy as np
import math

N = ord("V") % 5 + 1
print("\n\tVariant: ", N)

class Function:
    def __init__(self, interval: list) -> None:
        self._interval = interval
    
    def my_func(self) -> None:
        for x in np.arange(self._interval[0], self._interval[1], 0.2):
            if (x > 1):
                y = np.sqrt(math.tan(x**2- 1))
                print("when x =""%.1f" %x, "y = ""%.5f" %y)
            elif (0<=x<=1):
                y = -2*x
                print("when x =""%.1f" %x, "y = ""%.5f" %y)
            elif (x < 0):  
                y = math.exp(np.cos(x))
                print("when x =""%.1f" %x, "y = ""%.5f" %y)

    def inp_range(self) -> list:
        while True:
            press = input("\n\tEnter interval or 'X' or press 'Enter': ")
            self._interval.append(press)
            if press == '':
                self._interval = [-1, 1.5]
                return self._interval
            elif not any(char.isdigit() for char in press) is True:
                print(ValueError, "Try again!")
                continue
            else:
                if len(self._interval) == 2:
                    return self._interval

def main():
    
    f: Function = Function([])
    f.inp_range()
    f.my_func()
    
    
main()