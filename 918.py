nums = [5, -3, 5]
def max_subarray_sum(nums):
    def kadane(arr):
        ms = float('-inf')
        cs = 0
        for num in arr:
            cs = max(num, cs + num)
            ms = max(ms, cs)
        return ms
    a = kadane(nums)
    wrap = sum(nums) + kadane([-num for num in nums])
    return max(a, wrap) if a > 0 else a
print(max_subarray_sum(nums))