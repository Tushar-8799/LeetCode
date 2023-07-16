class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for word in words[left : right + 1]:
            # print(word)
            if word[0] in vowel and word[-1] in vowel:
                count += 1
        return count
