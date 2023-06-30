class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            # print(stack)
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif (s[i] == ')' and stack[-1] == '(') or (s[i] == '}' and stack[-1] == '{') or (s[i] == ']' and stack[-1] == '[')  :
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
