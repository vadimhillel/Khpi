class NotUnique:
    def __init__(self, list: list) -> None:
        self._list = list
        
    def rm_unique(self) -> list:
        NotUniqueList = [_ for _ in self._list if self._list.count(_) > 1]
        return NotUniqueList
    
def main():
    u: NotUnique = NotUnique([1, 13, 45, 1, 2, 9, 9, 19, 13])
    
    print(u.rm_unique())
    
if __name__ == "__main__":
    main()