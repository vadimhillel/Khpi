from task1 import MyFunctions
import random
import time


def main():
    f: MyFunctions = MyFunctions([random.randint(100, 1_000) for _ in range(100, 1_000)], [random.randint(100, 1_000) for _ in range(100, 1_000)])
    
    start1 = time.perf_counter()
    f.func1()
    print(f"Time for job 1: {time.perf_counter() - start1}")
    start2 = time.perf_counter()
    f.func2()
    print(f"Time for job 2: {time.perf_counter() - start2}")
    start3 = time.perf_counter()
    f.func3()
    print(f"Time for job 3: {time.perf_counter() - start3}")
    start4 = time.perf_counter()
    f.func4()
    print(f"Time for job 4: {time.perf_counter() - start4}")
    
if __name__=="__main__":
    main()