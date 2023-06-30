class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        sec = strs[-1]
        ans = 0
        for i in range(min(len(first), len(sec))):
            if first[i] == sec[i]:
                ans += 1
            else:
                return first[:ans]
        return first[:ans]
