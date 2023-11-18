from task1 import create_dict

def sum_dict_vals(d: dict, s: str) -> dict:
    return {**d, s: sum(d.values())}

def main():
    print(sum_dict_vals(create_dict(10), 'total'))

if __name__ == "__main__":
    main()



