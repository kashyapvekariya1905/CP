from typing import List
def averageWaitingTime(customers: List[List[int]]) -> float:
    total = 0
    free = 0
    for arr,pre in customers:
        st = max(free,arr)
        fin = st+pre
        wai = fin-arr
        total+=wai
        free = fin
    avgw = total/len(customers)
    return avgw

customers = [[1,2],[2,5],[4,3]]
print(averageWaitingTime(customers))
customers = [[5,2],[5,4],[10,3],[20,1]]
print(averageWaitingTime(customers))