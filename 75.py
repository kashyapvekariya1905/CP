nums = [2,0,2,1,1,0]
# temp = nums
# nums = []
# for i in temp:
#     if i == 0:
#         nums.append(i)

# for i in temp:
#     if i == 1:
#         nums.append(i)

# for i in temp:
#     if i == 2:
#         nums.append(i)

zeroes = 0
ones = 0
twos = 0

for num in nums:
    if num == 0:
        zeroes += 1
    elif num == 1:
        ones += 1
    elif num == 2:
        twos += 1

for i in range(zeroes):
    nums[i] = 0
for i in range(zeroes, zeroes+ones):
    nums[i] = 1
for i in range(zeroes+ones, zeroes+ones+twos):
    nums[i] = 2
print(nums)