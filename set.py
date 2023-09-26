set1 = {"apple", "orange", "banana"}
set2 = {"orange", "mango", "grape"}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
set1.remove("apple")
set2.add("mango")
print("length of set1:", len(set1))
print("length of set2:", len(set2))
print("length of union_set:", len(union_set))
print("length of intersection_set:", len(intersection_set))
