class Solution:
    def isHappy(self, n: int) -> bool:
        check = {n}
        while n != 1:
            sm = 0
            n = str(n)
            arr = list(n)
            for i in arr:
                i = int(i)
                sm += i * i
            if sm not in check:
                check.add(sm)
                n = sm
            else:
                return False
        return True
