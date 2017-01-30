
#My O(n1.5) version, find all primes, TLE
import math as m
class Solution(object):
    def countPrimes(self, n):
        #:type n: int
        #:rtype: int
        primes=[]
        for i in range(2,n):
            if i==2 or i==3: primes.append(i)
            else:
                flag=True
                for j in range(2,int(m.sqrt(i))+1):
                    if i%j==0: flag=False
                if flag==True: primes.append(i)
        return len(primes)


#My O(n1.5) version, use prime before to check prime, TLE
import math as m
class Solution(object):
    def countPrimes(self,n):
        primes=[]
        for i in range(2,n):
            if i==2 or i==3: primes.append(i)
            else:
                flag=True
                for prime in primes:
                    if prime<=(int(m.sqrt(i))+1):
                        if i%prime==0: flag=False
                if flag==True: primes.append(i)
        return len(primes)
        

#My O(n1.5) version, TLE
import math as m
class Solution(object):
    def countPrimes(self,n):
        count,primes=0,[0]*n
        for i in range(2,n):
            if self._isPrime(i,primes)==True: 
                count+=1
                primes[i]=1
        return count
        
    def _isPrime(self,num,primes):
        for i in range(2,int(m.sqrt(num))+1):
            if primes[i]:
                if num%i==0: return False
        return True


#O(nloglogn)  Sieve of Eratosthenes algorithm:
class Solution(object):
    def countPrimes(self,n):
        count,primes=0,[True]*n #firstly mark all numbers as prime
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i,n,i):
                    primes[j]=False
        return sum(primes)-2 if n>=2 else 0

        
        
        
        
        
        
        
        
        