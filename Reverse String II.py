class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s
        ans = ""
        for i in range(0,len(s),2*k):
            ans += s[i : i+k][::-1]
            if len(s[i+k:]) < k:
                ans += s[i+k:]
                break
            else:
                ans += s[i+k: i+k+k]

        return ans
