class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for id in details:
            if int(id[-4:-2]) > 60:
                count += 1
        return count 
