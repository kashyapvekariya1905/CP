from sortedcontainers import SortedList
def blockPlacementQueries(queries):
    obstacles = []
    results = []

    for query in queries:
        if query[0] == 1:  
            obstacles.append(query[1])
        else:  
            x, sz = query[1], query[2]
            start = 0
            can_place = False

            for obstacle in obstacles:
                gap = obstacle - start
                if gap >= sz:
                    can_place = True
                    break
                start = obstacle + 1

            if start <= x and x - start + 1 >= sz:
                can_place = True

            results.append(can_place)

    return results
print(blockPlacementQueries(queries=[[1,2],[2,3,3],[2,3,1],[2,2,2]]))