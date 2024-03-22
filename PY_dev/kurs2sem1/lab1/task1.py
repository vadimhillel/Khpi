import pyinputplus as pyip


def validfunc(inp):
    if (any(char.isdigit() for char in inp) is not False):
        return inp
    else:
        raise Exception("It's not a number!")
        
def inpfunc():
    while True:
        inp = pyip.inputStr("Enter 4symb number: ") 
        validfunc(inp)
        if len(inp) == 4:
            return inp
        
        else: 
            print(ValueError, "\nNumber not valid!")
            continue
            
def getSum(n): 
    nums = list(map(int, n.strip()))
    return sum(nums)

def main():
    print(getSum(inpfunc()))
    
if __name__ == "__main__":
    main()
