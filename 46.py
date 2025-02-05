import itertools


nums = [1,2,3]
rst = [list(i) for i in itertools.permutations(nums)]
print(rst)