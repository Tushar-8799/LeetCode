class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dums = set(nums)
        return False if len(dums) == len(nums) else True
