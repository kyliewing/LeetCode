#My intuitive loop version:
class Solution(object):
    def addDigits(self, num):
        #:type num: int
        #:rtype: int
        while num/10:
            temp=0
            while num:
                temp+=num%10
                num/=10
            num=temp
        return num

#Follow up: Could you do it without any loop/recursion in O(1) runtime?
#My O(1) time version
class Solution(object):
    def addDigits(self,num):
        if num==0: return 0
        if num%9==0: return 9
        else: return num%9

#Digit Root version:
#For base b (decimal case b = 10), the digit root of an integer is: dr(n) = 0 if n == 0 ,dr(n) = (b-1) if n != 0 and n % (b-1) == 0, dr(n) = n mod (b-1) if n % (b-1) != 0
class Solution(object):
    def addDigits(self,num):
        if num==0: return 0
        return 1+(num-1)%9
    
    
    
    
    
    
        