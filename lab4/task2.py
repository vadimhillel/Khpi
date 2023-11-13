import random

    
class Lists:
    def __init__(self, lst1: list, lst2: list) -> None:
        self._lst1 = lst1
        self._lst2 = lst2

    def list_func(self, n: int, m: int) -> None:
        for _ in range(n):
            self._lst1.append(random.randint(0, 100))
        for _ in range(m):
            self._lst2.append(random.randint(0, 100))
         
        print("\n1st list: \n", self._lst1)
        print("2nd list: \n", self._lst2)

def main():
    l: Lists = Lists([], [])
    l.list_func(int(input("\nInput 'n' for 1st list: ")),
                int(input("\nInput 'm' for 2nd list: ")))
    lst3 = list(l._lst1 + l._lst2)
    lst3.sort(reverse=True)
    print("\nDecreasing order sorted list of 2 previous: ", lst3)
    
if __name__ == "__main__":
    main()
    
    
