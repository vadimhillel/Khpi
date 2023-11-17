from task1 import create_dict
from task2 import sum_dict_vals

def change_key(d: dict, s_old: str, s_new: str) -> dict:
    d = sum_dict_vals(create_dict(10), 'total')
    if not s_old in d.keys():
        raise (KeyError, "No key like that in d!")
    d[s_new] = d.pop(s_old)
    return d
    
def main():
    print(change_key({}, 'total', 'sum'))

if __name__ == "__main__":
    main()
