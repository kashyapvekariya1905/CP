import itertools
from itertools import permutations

nums = [1,2,3]
def generate_permutations(nums):
    perset = set()
    for perm in permutations(nums):
        perset.add(tuple(perm))
    return [list(perm) for perm in perset]
print(generate_permutations(nums))

