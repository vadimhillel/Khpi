import pyinputplus as pyip

def triangle():
    a = pyip.inputNum("Enter 1st angle: ")
    b = pyip.inputNum("Enter 2nd angle: ")
    print(f"3rd angle = {180- (a+b)}")
    
for i in range(3):
    if __name__ == "__main__":
        triangle()