from math import gcd
nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3
count = 0
lcm_nums2 = nums2[0]
for num in nums2[1:]:
    lcm_nums2 = (lcm_nums2 * num) // gcd(lcm_nums2, num)

lcm_div = lcm_nums2 * k

for num in nums1:
    if lcm_div % num == 0:
        count += 1

print(count)