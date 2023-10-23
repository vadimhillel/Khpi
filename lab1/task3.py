import pyinputplus as pyip

def main():
    studs = pyip.inputNum("Enter stud: ")
    apples = pyip.inputNum("Enter apples: ")
    print(apples // studs) 
    print(apples % studs)

for i in range(3):
    if __name__ == "__main__":
        main()
