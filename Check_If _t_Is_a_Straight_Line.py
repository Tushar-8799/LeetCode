class Solution:
    def checkStraightLine(self, cor: List[List[int]]) -> bool:
        x1, y1 = cor[0]
        x2, y2 = cor[1]

        for i in range(2, len(cor)):
            x, y = cor[i]
            if (x2 - x1) * (y - y1) != (x - x1) * (y2 - y1):
                return False
        return True
