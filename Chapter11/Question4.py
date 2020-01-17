d1 = {"k1": True, "k2": True, "k3": True, "k4": True}
d2 = {"k6": True, "k2": True, "k5": True, "k1": True, "k8": True, "k4": True}
intersection = {}

for i in d1:
    for j in d2:
        if i == j and d1[i] == d2[j]:
            intersection[i] = d1[i]

print(intersection)