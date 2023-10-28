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
        amountofpaint = self.c * Cylindr.squarefunc(self)
        return amountofpaint
        
def main():
    res = Cylindr(2, 3.5, 7)
    # print(res.paintfunc())
    print("Surface area of the cylinder:", "%.3f"% res.squarefunc(),
               "\nTotal amount of paint:", "%.3f"% res.paintfunc())
    
if __name__ == "__main__":
    main()