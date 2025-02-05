from typing import List
def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    count = 0
    i = 0
    j = len(people)-1
    while i<=j:
        if people[i]+people[j]<=limit:
            i+=1
        j-=1
        count+=1
    return count

people = [3,2,2,1]
limit = 3
print(numRescueBoats(people,limit))