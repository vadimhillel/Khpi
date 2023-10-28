import pyinputplus as pyip
from collections import OrderedDict

l1 = [1, 2, 3]
l2 = [4, 1, 3]
l3 = [1, 3]

for i in l2:
    l1=[0 if x==i else x for x in l1]
    print(l1)
i = str([k for k in frozenset(l1).intersection(l2)])
# for k in frozenset(l1).intersection(l2):
#     print(type(k))
# x = OrderedDict.fromkeys(l1)
# y = OrderedDict.fromkeys(l2)
        
d1 = {"v1": 1,
      "v2": 2,
      "v3": 3}
d2 = {"v1": 1,
      "v2": 4,
      "v3": 3}

shared_items = {k: d1[k] for k in d1 if k in d2 and d1[k] == d2[k]}
print((shared_items))
            
#         if v == n:
#             d1[v]==0
#             print(d1)
# a=[1,2,3,1,3,2,1,1]
# a = [0 if x==1 else x for x in l1]
# print(a)
# print(set(l1) & set(l2))
        





