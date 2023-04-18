from itertools import combinations
input = [i for i in range(1, 1000)]

trips = list(combinations(input, 3))
triplets = []
for i in trips:
    if i[0]**2 + i[1]**2 == i[2]**2 and i[0] + i[1] + i[2] == 1000:
        print(i, i[0]*i[1]*i[2])
