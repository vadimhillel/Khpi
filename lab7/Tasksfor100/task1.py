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
    return dict(Counter(str.split()).most_common(1))

def orderedbykeys(str: str) -> dict:
    """task 2.3"""
    d = dict(Counter(str.split()).most_common(len(str.split())))
    return dict(sorted(d.items()))

def orderedbyvalues(str: str) -> dict:
    """task 2.4"""
    return dict(Counter(str.split()).most_common(len(str.split())))

def main():
    
    print("\n----------------------------TASK 2.1----------------------------\n")
    print(test_trans())
    print("\n----------------------------TASK 2.2----------------------------\n")
    print(mostcommon(test_trans()))
    print("\n----------------------------TASK 2.3----------------------------\n")
    pprint(orderedbykeys(test_trans()))
    print("\n----------------------------TASK 2.4----------------------------\n")
    print(orderedbyvalues(test_trans()))

if __name__ == "__main__":
    main()
