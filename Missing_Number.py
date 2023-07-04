class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        total = n * (n + 1) // 2
        calc = sum(nums)
        if total == nums:
            return 0
        return total - calc
