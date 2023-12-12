def main():
    sum_ = 0
    n, m = map(int, input("Enter n, m (n m): ").split())
    while m:
        if (n < 9999):
            sum_ += n % 10
            n //= 10
            m -= 1
        else:
            raise (ValueError, "n < 9999")
        print(sum_)

if __name__ == "__main__":
    main()