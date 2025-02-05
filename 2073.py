from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0 
        while (tickets[k]>0):
            for i in range(len(tickets)):
                if tickets[i]>0:
                    time +=1
                    tickets[i]-=1
                    if i == k and tickets[i] == 0:
                        return time
        return time

s = Solution()
arr = [5,1,1,1]
k = 0
print(s.timeRequiredToBuy(arr, k))