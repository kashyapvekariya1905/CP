nums = [0,4,3,0,4]

def specialArray(nums):
    nums.sort(reverse=True)
    for i in range(len(nums)+1):
        count = sum(1 for num in nums if num >=i)
        if count==i:
            return i
    return -1
print(specialArray(nums))