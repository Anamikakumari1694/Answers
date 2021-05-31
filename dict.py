from collections import Counter
dict1 = {'1': 100, '2': 200, '3':70}
dict2 = {'1': 300, '2': 200, '3':400}
d = Counter(dict1) + Counter(dict2)
print(d)
