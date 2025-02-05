nums = [1,7,3,6,5,6]
ts = sum(nums)
ls = 0
for i in range(len(nums)):
    if ls == (ts-ls-nums[i]):
        print(i)
        break
    ls += nums[i]
        