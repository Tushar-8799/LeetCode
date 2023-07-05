from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dix = Counter(nums)
        k = 0
        v = -1
        for x, y in dix.items():
            # print(x,y)
            if y > v:
                v = y
                k = x
        return k
