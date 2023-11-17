def create_dict(n) -> dict:
    d={}
    for i in range(1,n+1):
        d.__setitem__(i,i)
    return d

def main():
    print(create_dict(10))

if __name__ == "__main__":
    main()