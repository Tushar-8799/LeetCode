class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = []
        ran = str(nums[0])
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            else:
                if int(ran) != nums[i-1]:
                    ran += '->'+ str(nums[i-1]) 
                ans.append(ran)
                ran = str(nums[i])
        if int(ran) != nums[-1]:
            ran += '->'+ str(nums[-1]) 
        ans.append(ran)
        return ans
        
