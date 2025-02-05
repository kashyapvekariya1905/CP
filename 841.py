from typing import List
rooms = [[1],[2],[3],[]]
# rooms = [[1,3],[3,0,1],[2],[0]]

def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = set()
    stack = [0]
    while stack:
        room = stack.pop()
        if room not in visited:
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    stack.append(i)
    return len(visited) == len(rooms)
        

    

print(canVisitAllRooms(rooms))