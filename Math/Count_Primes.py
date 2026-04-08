class Solution(object):
    def countPrimes(self, n):
        if n == 0: print(0)
        if n == 1: print(0)
        is_prime = [True] * (n+1)
        count = 0
        for i in range(2, n):
            if is_prime[i] == True:
                count += 1
                for j in range(i*2, n, i):
                    is_prime[j] = False
        return count