class Mss:
    def __init__(self, arrival_rate: int, t: int) -> None:
        self._arrival_rate = arrival_rate
        self._t = t

    def service_intensity(self) -> list:
        return 1 / (1 + (self._arrival_rate / (60 / self._t)))
    
    def relative_throughput(self):
        return self._arrival_rate*(self._t/60)
        
def main():
    m: Mss = Mss(20, 6)
    # flake8: noqa
    print(f"\nThe service intensity is {m.service_intensity():.2f}" +
          f" and relative throughput is: {m.relative_throughput()}")
    
if __name__ == "__main__":
    main()
