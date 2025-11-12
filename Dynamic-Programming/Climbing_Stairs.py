class Solution(object):
    def climbStairs(self, n):

        if n <= 3:
            return n

        arrayList = [0] * (n + 1)
        arrayList[1] = 1
        arrayList[2] = 2

        for i in range(3, n + 1):
            arrayList[i] = arrayList[i - 1] + arrayList[i - 2]

        return arrayList[n]
