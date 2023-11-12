
def function(list1: list, list2: list) -> list:
    print(f"\n1st list is {list1}", 
              f"\n2nd list is {list2}\n")
    for i in list2:
        list1 = [0 if x==i else x for x in list1]
    return list1

print(function([1, 2, 7, 7, 5, 5, 2, 4],
               [3, 8, 9, 4, 2, 2, 1, 5]))
    
  