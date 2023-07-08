class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) != 1:
            l = 0
            for i in num:
                l += int(i)
            num = str(l)
        return int(num)
