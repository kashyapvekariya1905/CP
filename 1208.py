s = "abcd"
t = "bcdf"
maxCost = 3
def max_substring_length(s, t, maxCost):
   n = len(s)
   cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
   ml = 0
   left = 0
   cc = 0

   for right in range(n):
       cc += cost[right]
       while cc > maxCost:
           cc -= cost[left]
           left += 1
       ml = max(ml, right - left + 1)
   return ml
print(max_substring_length(s,t,maxCost))