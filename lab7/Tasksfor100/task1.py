from collections import Counter 
from pprint import pprint
import string as s


def test_trans() -> str:
    """task 2.1"""
    with open("lab7/Tasksfor100/text.txt", "r", encoding="latin-1") as file:
        lines = file.readlines()
        mystr = ' '.join([line.strip() for line in lines]).lower()
    return mystr.translate(str.maketrans('', '', s.punctuation))

def mostcommon(str: str) -> dict:
    """task 2.2"""
    return dict(Counter(str.split()).most_common(len(str.split()))) 

def orderedbykeys(d: dict) -> dict:
    """task 2.3"""
    return dict(sorted(d.items()))

def orderedbyvalues(d: dict) -> dict:
    """task 2.4"""
    return d

def main():
    
    print("\n----------------------------TASK 2.1----------------------------\n")
    print(test_trans())
    print("\n----------------------------TASK 2.2----------------------------\n")
    pprint(mostcommon(test_trans()))
    print("\n----------------------------TASK 2.3----------------------------\n")
    print(orderedbykeys(mostcommon(test_trans())))
    print("\n----------------------------TASK 2.4----------------------------\n")
    print(orderedbyvalues(mostcommon(test_trans())))

if __name__ == "__main__":
    main()