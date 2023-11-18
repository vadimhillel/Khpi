import random


N = ord("V") % 5 + 1
print(f"\n\t Number of variant is {N}")

def validation(lst: list) -> list:
    if not len(lst) < 5:
        return lst
    else:
        raise Exception("\n\ttoo less values!!")
    
def arithm_mean(numsinlist):
    return float(f'{float(sum(numsinlist)) / max(len(numsinlist), 1):.2f}')

def inp_list(listofnums: list):
    listofnums = [arithm_mean(listofnums) if x == listofnums[4] else x for x in listofnums]
    return listofnums

def main(n: int, initial_list: list):
    for _ in range(n):
        initial_list.append(random.randint(0, 100))
    print("Initial list: \n", initial_list)
    print("Final list: \n", inp_list(validation(initial_list)))
        
if __name__ == "__main__":
    main(int(input("\nInput 'n' for list: ")), [])
    
