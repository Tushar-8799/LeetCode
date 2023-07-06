class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dix1 = {}
        for x,y in nums1:
            dix1[x] = y
        for x, y in nums2:
            if x in dix1:
                dix1[x] += y
            else:
                dix1[x] = y
        arr = [[k, dix1[k]] for k in dix1]
        arr.sort()
        return arr
