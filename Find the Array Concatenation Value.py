class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conc = 0
        n = len(nums)
        if n % 2 == 0:
            for i in range(n//2):
                conc += int(str(nums[i]) + str(nums[n-i-1]))
        else:
            for i in range(n//2):
                conc += int(str(nums[i]) + str(nums[n-i-1]))
            conc += nums[n//2]
        return conc
