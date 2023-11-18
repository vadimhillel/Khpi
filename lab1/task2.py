from dataclasses import dataclass
import numpy as np

@dataclass 
class CylindrInfo:
    d: int
    h: float
    c: int
    
class Cylindr(CylindrInfo):
    
    def squarefunc(self):
        sq = (np.pi*self.d*self.h) + (2*np.pi*((self.d/2)**2))
        return sq
    
    def paintfunc(self):
        amountofpaint = Cylindr.squarefunc(self) * self.c
        return amountofpaint
        
def main():
    res = Cylindr(2, 3.5, 7)
    print("Surface area of the cylinder:", f"{res.squarefunc():.3f}",
               "\nTotal amount of paint:", f"{res.paintfunc():.3f}")
    
if __name__ == "__main__":
    main()