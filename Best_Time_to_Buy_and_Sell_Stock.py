class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        small = 0
        large = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            small = prices[i]
            if small > large:
                large = small
            else:
                maxi = max(maxi, large-small)
        return maxi
