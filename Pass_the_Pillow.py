class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        length = n + n - 2
        time = time % length
        if time >= n:
            return n- (time - n + 1)
        return time + 1
