#"Math" "String"
#Given two binary strings, return their sum (also a binary string).

#My solution: Convert to integer + build-in function bin()
#Your runtime beats 50.27% of python submissions.
class Solution(object):
    def addBinary(self, a, b):
        numa=numb=0
        for i in xrange(len(a)):  #Convert to integer
            numa+=int(a[i])*pow(2,len(a)-1-i)
        for i in xrange(len(b)):  #Convert to integer
            numb+=int(b[i])*pow(2,len(b)-1-i)
        numres=numa+numb    
        return bin(numres)[2:]    #Convert the sum to binary string, notice "[2:]" because first two chars are '0b'
            
            
 #More smart and clean version:
#No conversion, no build in function version:
#Your runtime beats 28.95% of python submissions.
class Solution(object):
    def addBinary(self, a, b):
        res,cur,i,j="",0,len(a)-1,len(b)-1     
        while i>=0 or j>=0 or cur==1: #Notice these three conditions, cur carrys the carry bit
            cur=cur+int(a[i]) if i>=0 else cur#If in the length of a, then add it's bit, if not, then add 0
            cur=cur+int(b[j]) if j>=0 else cur#If in the length of a, then add it's bit, if not, then add 0
            i,j=i-1,j-1
            res=str(cur%2)+res#Add the sum digit in this bit
            cur/=2#Decide the carry bit
        return res
            
        
#One line python version:
class Solution(object):
    def addBinary(self, a, b):
        #return bin(eval('0b'+a)+eval('0b'+b))[2:]#Your runtime beats 73.36% of python submissions.
        #return bin(int(a,2)+int(b,2))[2:]#Your runtime beats 88.89% of python submissions.
        #return bin(eval('0b'+a+'+0b'+b))[2:]#Your runtime beats 79.29% of python submissions.
        return bin(eval('0b%s+0b%s'%(a,b)))[2:]#Your runtime beats 98.11% of python submissions.
            
        

#Remember
#Recursively version:
#Your runtime beats 57.45% of python submissions.
class Solution(object):
    def addBinary(self, a, b):
        if len(a)==0: return b 
        if len(b)==0: return a
        if a[-1]=='1' and b[-1]=='1':
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1')+'0'#Need to cary one
        if a[-1]=='0' and b[-1]=='0':
            return self.addBinary(a[:-1],b[:-1])+'0'#The last digit is 0
        else:
            return self.addBinary(a[:-1],b[:-1])+'1'#The last digit is 1
            
        
            
            
        

            
        
                    
            
        
                 
        
        