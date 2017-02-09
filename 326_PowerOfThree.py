
#My iterative version:
class Solution(object):
    def isPowerOfThree(self, n):
        #:type n: int
        #:rtype: bool
        if n==1: return True #corner case
        while n and n%3==0:  # notice n%3==0
            if n==3: return True
            else:
                n/=3
        return False

#My recuesion version:
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0: return False
        if n==1: return True
        return self._helper(n)
    def _helper(self, n):
        if n==3: return True
        if n<3: return False
        return n%3==0 and self._helper(n/3)


#Iterative solution:
class Solution(object):
    def isPowerOfThree(self, n):
        if n>1:
            while(n%3==0):
                n/=3
        return n==1

#Recursive solution:
class Solution(object):
    def isPowerOfThree(self, n):
        return n>0 and (n==1 or n%3==0 and self.isPowerOfThree(n/3))


#Know the max int of 3's power:
class Solution(object):
    def isPowerOfThree(self, n):
        Max3PowerInt = 1162261467
        return n>0 and Max3PowerInt%n==0


import math as m
#Log(n)/log(3) is integer if n is 3's power:
class Solution(object):
    def isPowerOfThree(self, n):
        return n>0 and (m.log(n)/m.log(3))%1==0


            

