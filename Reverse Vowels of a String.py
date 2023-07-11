class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = {'a', 'e', 'i' , 'o', 'u', 'A', 'E','I', 'O', 'U'}
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vowel:
                pass
            else:
                i += 1
            if s[j] in vowel:
                pass
            else:
                j -= 1
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
