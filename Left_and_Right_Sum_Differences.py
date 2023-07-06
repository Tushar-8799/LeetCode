class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return arr
