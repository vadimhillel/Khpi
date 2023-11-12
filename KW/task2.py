# list1 = [16, 17, 14, 21, 16, 13, 10, 11, 16, 17]
# list2 = [18, 17, 18, 13, 18, 21, 24, 23, 16, 17]
# list3 = [0, 0, 2, 0, 0, 0, 0, 0, 2, 0]

# print("Number\t\tlist1\t\tlist2\t\tlist3")
# print(90*"=")

# for i, element1, element2, element3 in zip(range(9), list1, list2, list3):
#     print('{:^6}\t\t{:^5}\t\t{:^5}\t\t{:^5}'
#           .format(i+1, element1, element2, element3))

            
def function(list1: list, list2: list) -> list:
    print(f"\n1st list is {list1}", 
              f"\n2nd list is {list2}\n")
    for i in list2:
        list1 = [0 if x==i else x for x in list1]
    return list1

print(function([1, 2, 7, 7, 5, 5, 2, 4],
               [3, 8, 9, 4, 2, 2, 1, 5]))
    
  