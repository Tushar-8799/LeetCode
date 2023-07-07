class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = list(str(num))
        maxi = ""
        mini = ""
        mi = num[0]
        ma = '9'
        for i in range(len(num)):
            if num[i] != '9':
                ma = num[i]
                break
        for i in range(len(num)):
            if num[i] == mi:
                mini += '0'
            else:
                mini += num[i]
            if ma != '9':
                if num[i] == ma:
                    maxi += '9'
                else:
                    maxi += num[i]
            else:
                maxi += num[i]
        return int(maxi) - int(mini)
