class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dix = {}
        n = len(nums)
        for i in range(n):
            dix[nums[i]] = i
        
        for i in range(n):
            rest = target - nums[i]
            if rest in dix and dix[rest] != i:
                return [i, dix[rest]]
        return []
