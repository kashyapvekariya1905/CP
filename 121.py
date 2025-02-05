# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
# out : 5
# profit = 0
# buy = min(prices)
# bi = prices.index(buy)
# prices = prices[bi+1:]
# if len(prices) == 0:
#     print(profit)
#     exit()
# else:
#     sel = max(prices)
#     profit = sel - buy
# print(profit)

minp = float('inf')
maxp = 0
for price in prices:
    if price < minp:
        minp = price
    temp = price - minp
    if temp > maxp:
        maxp = temp

# return maxp