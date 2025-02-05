nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3

count = 0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]%(nums2[j]*k)==0:
            count += 1
print(count)