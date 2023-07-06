class Solution:
    def splitNum(self, num: int) -> int:
        arr = list(str(num))
        arr.sort()
        a = ""
        b = ""
        print(arr)
        for i in range(0, len(arr), 2):
            print(i)
            a += arr[i]
            if i != len(arr)-1:
                b += arr[i + 1]
        print(a, b)
        return int(a) + int(b)
