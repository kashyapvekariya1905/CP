def beautifulSubsets(nums, k):
    def backtrack(start, current):
        if current:
            result[0] += 1

        for i in range(start, len(nums)):
            if not current or all(abs(nums[i] - num) != k for num in current):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

    nums.sort()
    result = [0]
    backtrack(0, [])
    return result[0]

nums1 = [2, 4, 6]
k1 = 2
print(beautifulSubsets(nums1, k1))  # Output: 4

nums2 = [1]
k2 = 1
print(beautifulSubsets(nums2, k2))  
