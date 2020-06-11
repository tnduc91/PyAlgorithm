class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
            
        strike = [1]*n
        strike[0] = strike[1] = 0

        for i in range(1, n / 2 + 1):
            if strike[i] == 1:
                
                """ Slower
                for j in range(i + i, n, i):
                    strike[j] = 0
                """

                # Faster
                strike[i + i: n: i] = [0] * len(strike[i + i: n: i])

        return sum(strike)