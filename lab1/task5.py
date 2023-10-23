import numpy as np
import pyinputplus as pyip

def heronfunc(i: int, sides: list):
    while True:
        inp = pyip.inputNum(f"Enter {i+1} side: ")
        sides.append(inp)
        if len(sides) != 3:
            continue
        else:
            return sides
        
def main():
    a, b, c = heronfunc(0, [])[0:3]
    
    s = int(a+b+c)/2
    Area = np.sqrt(s* (s-a)* (s-b)* (s-c))
    print("s = ", s, "\nArea = %.3f" % Area)

if __name__ == "__main__":
    main()
