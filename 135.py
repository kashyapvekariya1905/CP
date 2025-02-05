# ratings = [1,0,2]
ratings = [1,3,2,2,1] 
# allcan = []
# for i in range(len(ratings)):
#     allcan.append(1)
# for k in range(len(ratings)-1):
#     if ratings[k]>ratings[k+1]:
#         allcan[k]+=1
#     elif ratings[k]<ratings[k+1]:
#         allcan[k+1]+=1
#     elif ratings[k]==ratings[k+1]:
#         allcan[k+1]=allcan[k+1]
# candy = sum(allcan)
# print(candy)
# print(allcan)
n = len(ratings)
if n == 0:
    print(0)
    exit()
candies = [1] * n
for i in range(1, n):
    if ratings[i] > ratings[i - 1]:
        candies[i] = candies[i - 1] + 1
for i in range(n - 2, -1, -1):
    if ratings[i] > ratings[i + 1]:
        candies[i] = max(candies[i], candies[i + 1] + 1)
candy = sum(candies)
print(candy)
print(candies)
