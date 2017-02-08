#My hash table version:
class Solution(object):
    def isHappy(self, n):
        #:type n: int
        #:rtype: bool
        if n==0: return False
        my_hash={}
        while True:
            next_n=0
            while n:
                next_n+=(n%10)**2
                n/=10
            if next_n ==1:
                return True
            elif next_n in my_hash:
                return False
            else:
                my_hash[next_n]=1
                n=next_n        #Don't forget this line, set n as next_n

#O(1) space version, use the concept of Floyd Cycle Detection Algorithm
class Solution(object):
    def isHappy(self, n):
        slow=fast=n
        while True:
            slow=self._helper(slow)
            fast=self._helper(fast)
            fast=self._helper(fast) 
            if slow==fast: 
                break
        return True if slow==1 else False
            
            
    def _helper(self,num):
        result=0
        while num:
            result+=(num%10)**2
            num/=10
        return result
            
            
        