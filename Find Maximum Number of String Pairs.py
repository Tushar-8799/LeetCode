class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = {}
        for i in range(len(words)):
            dic[words[i]] = i
        count = 0
        for word in words:
            if word[::-1] in dic and dic[word[::-1]] != dic[word] and dic[word] != -1:
                count += 1
                dic[word] = -1
                dic[word[::-1]] = -1 
        return count
