nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = nums1[::-1]
# nums1 = nums1[m:]
# nums1= nums1[::-1]
# nums1 = nums1+nums2
# nums1.sort()
# print(nums1)

p1,p2,p = m-1,n-1,m+n-1
while p1>=0 and p2>=0:
    if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1
    p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1