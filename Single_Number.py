from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for x, y in dic.items():
            if y == 1:
                return x
