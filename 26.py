nums =  [0,0,1,1,1,2,2,3,3,4]
# occ= {}
# for i in nums:
#     if i not in occ:
#         occ[i] = 1
#     else:
#         occ[i] += 1
# nums = []
# for key,value in occ.items():
#     if value >1:
#         occ[key] = 1
#     nums.append(key)
# print(nums)
k = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]  
        k += 1  
        
print(k)