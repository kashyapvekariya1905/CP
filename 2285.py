from typing import List
def maximumImportance(n: int, roads: List[List[int]]) -> int:
    total = 0
    degree = [0]*n
    for i in roads:
        degree[i[0]]+=1
        degree[i[1]]+=1
    city = list(range(n))
    city.sort(key=lambda x: degree[x], reverse=True)
    val = [0]*n
    for i,c in enumerate(city):
        val[c] = n-i
    for i in roads:
        total+=val[i[0]]+val[i[1]]
    return total

n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(maximumImportance(n,roads))

n = 5
roads = [[0,3],[2,4],[1,3]]
# print(maximumImportance(n,roads))