class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':0, 'V':1, 'X':2, 'L':3, 'C':4, 'D':5, 'M':6}
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        x = 0
        ans = value[s[0]]
        for i in range(1, len(s)):
            if symbol[s[i]] > symbol[s[i-1]]:
                ans += value[s[i]] - 2*value[s[i-1]]
            else:
                ans += value[s[i]]
        return ans
