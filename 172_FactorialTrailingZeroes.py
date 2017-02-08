#My log5(n) iterative version:
class Solution(object):
    def trailingZeroes(self, n):
        #:type n: int
        #:rtype: int
        result=0
        temp=5
        while n>=temp:
            result+=n/temp
            temp*=5
        return result


#My recursive version:1
class Solution(object):
    def trailingZeroes(self, n):
        if n==0: return 0
        else: 
            return n/5+self.trailingZeroes(n/5)
        