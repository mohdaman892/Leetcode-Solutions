class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = 10**6
        prime = [True for i in range(n+1)]
        for i in range(2,int(sqrt(n))+1):
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j] = False
        prime[1] = False
        primes = []
        i = left
        while i<=right:
            if prime[i]:
                primes.append(i)
            i+=1
        if len(primes)<2:
            return [-1,-1]
        k = primes[1]-primes[0]
        ans = [primes[0],primes[1]]
        # print(primes)
        if len(primes)>2:
            for i in range(2,len(primes)):
                if primes[i]-primes[i-1]<k:
                    k = primes[i]-primes[i-1]
                    ans = [primes[i-1],primes[i]]
        return ans