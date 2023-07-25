class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        leastval = float('inf')
        ans = []
        dix2 = {}
        for i in range(len(list2)) :
            dix2[list2[i]] = i
        for i in range(len(list1)):
            if list1[i] in dix2:
                aa = list1[i]
                bb = i + dix2[aa]
                if bb == leastval:
                    ans.append(aa)
                elif bb < leastval:
                    leastval = bb
                    ans = [aa]

        return ans
