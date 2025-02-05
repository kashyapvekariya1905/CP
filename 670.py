class Solution:
    def maximumSwap(self, num: int) -> int:
        num_lst = list(str(num))
        n = len(num_lst)
        for i in range(n-1):
            max_d = num_lst[i]
            max_ind = i
            for j in range(i+1, n):
                if num_lst[j] >= max_d:
                    max_d = num_lst[j]
                    max_ind = j
            if max_d > num_lst[i]:
                num_lst[i], num_lst[max_ind] = num_lst[max_ind], num_lst[i]
                return int(''.join(num_lst))
        return num