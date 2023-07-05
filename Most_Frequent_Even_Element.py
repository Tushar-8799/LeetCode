from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        k, v = float('inf'), -1
        flag = 0
        dix = Counter(nums)
        for x, y in dix.items():
            if x % 2 == 0:
                flag = 1
                # print(x, y)
                if y > v: 
                    v = y
                    k = x
                if y == v:
                    k = min(k, x)
        if flag == 0:
            return -1
        return k
