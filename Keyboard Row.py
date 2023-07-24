class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        # print(first)
        ans = []
        for word in words:
            if len(word) == 1:
                ans.append(word)
                continue
            if word[0].lower() in first:
                for j in word[1:]:
                    if j.lower() not in first:
                        break
                else:
                    ans.append(word)
            elif word[0].lower() in second:
                for j in word[1:]:
                    if j.lower() not in second:
                        break
                else:
                    ans.append(word)
            else:
                for j in word[1:]:
                    if j.lower() not in third:
                        break
                else:
                    ans.append(word)
        return ans

