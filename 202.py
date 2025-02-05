n = 19
# true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# if n>=10:
#     while n!=1:
#         n = sum(int(digit) ** 2 for digit in str(n))
#         print(n)
# else:
#     print("fls")

# seen = set()
# while n != 1:
#     if n in seen:
#         return False
#     seen.add(n)
#     n = sum(int(digit) ** 2 for digit in str(n))
# return True