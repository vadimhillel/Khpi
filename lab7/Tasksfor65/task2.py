from task1 import create_dict

def sum_dict_vals(dict1: dict, str: str) -> dict:
    return {**dict1, str: sum(dict1.values())}

def main():
    print(sum_dict_vals(create_dict(10), 'total'))

if __name__ == "__main__":
    main()



