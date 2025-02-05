import itertools


num = 310
# num = -7605

def smallestNumber(num: int) -> int:
    # if str(num).startswith("-"):
    #     num = int(str(num)[1:])
    #     digits = str(num)
    #     permutations = itertools.permutations(digits)
    #     permutation_numbers = [int(''.join(p)) for p in permutations]
    #     unique_permutation_numbers = list(set(permutation_numbers))

    #     max_permutation = max(unique_permutation_numbers)
    #     negative_max_permutation = -max_permutation

    #     return negative_max_permutation
    # else:
    #     num_str = str(num)
    #     permutations = itertools.permutations(num_str)
    #     validPermutations = set(int(''.join(p)) for p in permutations if p[0] != '0')
    #     print(validPermutations)
    #     return min(validPermutations)

    if num == 0:
        return 0
    if num < 0:
        num = -num
        digits = sorted(str(num), reverse=True)
        return -int(''.join(digits))
    else:
        digits = sorted(str(num))
        if digits[0] == '0':
            for i in range(1, len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
        return int(''.join(digits))

print(smallestNumber(num))