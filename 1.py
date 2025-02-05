# occurance
occ = {}
s = ""
for i in s:
    if i not in occ:
        occ[i] = 1
    else:
        occ[i] += 1
# print(occ)

s= ""
# check all elements of strings are same
if len(set(s)) == 1:
    s = 0

# create n lists
n = 5
lists = [[] for _ in range(n)]
print(lists)

# all combinations pf list [1,2,3,4] like
# allcom = [[]]

# for i in range(1, len(candidates) + 1):
#     allcom.extend([list(comb) for comb in itertools.combinations(candidates, i)])
# rst = []
# for i in allcom:
#     for j in allcom:
#         if sum(i) == target:
#             rst.append(i)
        
# print(rst)
# print(allcom)

# find factor
def find_factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

def find_factors_list(int_list):
    factors_dict = {}
    for number in int_list:
        factors_dict[number] = find_factors(number)
    return factors_dict


