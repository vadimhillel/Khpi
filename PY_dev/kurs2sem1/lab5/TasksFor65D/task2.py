from task1 import MyFunctions


def main(options: list):
    f: MyFunctions = MyFunctions([1, 2, 3, 4, 5, 
                                  6, 7, 8, 9, 10], [1, 2, 3, 8])
    f.source_list()
    
    match input(f"\nChoose 1 option: {options}"):
        case "1":
            assert(f.func1())
            print(f.func1())
        case "2":
            assert(f.func2())
            print(f.func2())
        case "3":
            assert(f.func3())
            print(f.func3())
        case "4":
            assert(f.func4())
            print(f.func4())
        case _:
            raise Exception(f"not in {options}!!")
            
if __name__ == "__main__":
    main(["1, 2, 3, 4"])