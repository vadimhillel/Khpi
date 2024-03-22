import math


class Prodsum:

    def __init__(self, k: int, res_sum: float, res_prod: float, abs_res: float) -> None:
        self._k = k
        self._res_sum = res_sum
        self._res_prod = res_prod
        self._abs_res = abs_res

    def FormulaSum(self, i):

        for i in range(i, self._k + 5, 1):
            
            denominator = i - 11
            if denominator == 0 or denominator == math.inf:
                continue  # Skip terms equal to zero or infinity
            
            numerator = math.pow(i + 5, 1 / 5)
            if numerator == 0 or numerator == math.inf:
                continue  # Skip terms equal to zero or infinity
            
            """term of the series sum"""
            self._res_sum += (numerator / denominator) - math.pow(self._k, 5 * i)
        print(f"res_sum: {self._res_sum:.3f}")
            
    def FormulaMul(self, j):
        Prodsum.FormulaSum(self, j)
        for j in range(j, self._k, 1):
            
            denominator = j - 3
            if denominator == 0 or denominator == math.inf:
                continue  # Skip terms equal to zero or infinity
            
            numerator = self._k**(j + 2) * j
            if numerator == 0 or numerator == math.inf:
                continue  # Skip terms equal to zero or infinity
            
            """term of the series prod"""
            self._res_prod = numerator / denominator
            
            
            self._abs_res *= self._res_prod * self._res_sum

        print(f"res_prod: {self._res_prod:.3f}")
            
def main():
    k = int(input("enter k: "))
    
    if k >-4 and k != 0: 
        ps = Prodsum(k, 0, 1, 1)
        ps.FormulaMul(-4)
        print(f"re: {ps._abs_res:.3f}")
    else:
        raise ValueError("k can't be 0 or less than -4!!")
    
if __name__ == "__main__":
    main()