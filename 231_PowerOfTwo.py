#My math divide version: 
class Solution(object):
    def isPowerOfTwo(self, n):
        #:type n: int
        #:rtype: bool
        if n<=0: return False
        while n%2==0:
            n/=2
        return n==1


#Bit Manipulation version:
class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0: return False
        return not n&(n-1)
        

        