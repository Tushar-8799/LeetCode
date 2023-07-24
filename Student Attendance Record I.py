class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1:
                    return False
            elif i > 1 and s[i] == 'L':
                if s[i-1] == 'L' and s[i-2] == 'L':
                    return False
        return True
