#My devided by 2 every loop version:
class Solution(object):
    def hammingWeight(self, n):
        #:type n: int
        #:rtype: int
        result=0
        while n:
            result+=n%2
            n/=2
        return result


#Bit Shifting version:
class Solution(object):
    def hammingWeight(self, n):
        result=0
        while n:
            result+=n&1#check the last digit
            n=n>>1 #shift right
        return result

#Python build in funciton version:
class Solution(object):
    def hammingWeight(self,n):
        return bin(n).count('1')
        

#n=n&(n-1) trick to delete one 1 version:
class Solution(object):
    def hammingWeight(self,n):
        result=0
        while n:
            n=n&(n-1)
            result+=1
        return result
        
            
        