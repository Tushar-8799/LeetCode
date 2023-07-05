class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        six = {}
        tix = {}
        for x, y in zip(s, t):
            if x not in six:
                six[x] = y
            elif six[x] != y:
                return False
            
            if y not in tix:
                tix[y] = x
            elif tix[y] != x:
                return False
        return True

