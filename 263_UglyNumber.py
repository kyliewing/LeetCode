#My solution, One Time AC.
class Solution(object):
    def isUgly(self, num):
        #:type num: int
        #:rtype: bool
        while num>=1:
            if num==1:
                return True
            while num%2==0:
                num/=2
                continue
            if num%3==0:
                num/=3
                continue
            if num%5==0:
                num/=5
                continue
            else:
                return False
        return False  #don't forget this line

#More concise version:
class Solution(object):
    def isUgly(self, num):
        if num<=0: return False
        for p in [2,3,5]:
            while num%p==0:
                num/=p
        return num==1






