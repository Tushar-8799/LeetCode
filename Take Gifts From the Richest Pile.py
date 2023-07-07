class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = sorted(gifts, reverse = True)
        for i in range(k):
            maxi = max(gifts)
            gifts.remove(max(gifts))
            gifts.append(int(maxi ** 0.5))

        return sum(gifts)
