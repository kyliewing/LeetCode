#Your runtime beats 56.70% of python submissions. (Two Times AC)
#Given a roman numeral, convert it to an integer, input is guaranteed to be within the range from 1 to 3999
#Symbol I   V   X   L   C   D   M
#Value  1   5   10  50  100 500 1,000
class Solution(object):
    def romanToInt(self, s): 
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  #Dictionary to sotre pairs of symbols and values
        res=0
        if len(s)==0: 
            return 0
        if len(s)==1:
            return roman_dict[s]
        i=0
        while i<len(s)-1:
            if roman_dict[s[i]]>=roman_dict[s[i+1]]: #if the former one is greater than the later one, then just add it
                res+=roman_dict[s[i]]
                i+=1
                continue
            else:
                res+=roman_dict[s[i+1]]-roman_dict[s[i]]#if the former one is less than the later one, then these two are a pair 
                i+=2
                continue
        if roman_dict[s[-2]]>=roman_dict[s[-1]]:# don't miss the last single symbol
            res+=roman_dict[s[-1]]
        return res

#Your runtime beats 58.58% of python submissions.
#Backwards make the rule easier, usage of dictionary map
class Solution(object):
    def romanToInt(self, s): 
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  #Dictionary to sotre pairs of symbols and values
        res,length=0,len(s)
        if length==0: return 0
        if length==1: return roman_dict[s]
        res+=roman_dict[s[-1]]
        for i in xrange(length-2,-1,-1):  #Instead of upwards, we use backwards and can make the rule easier
            if roman_dict[s[i]]>=roman_dict[s[i+1]]:
                res+=roman_dict[s[i]]
            else:
                res-=roman_dict[s[i]]
        return res

#Your runtime beats 7.51% of python submissions.
#A more concise solution
class Solution(object):
    def romanToInt(self, s): 
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  #Dictionary to sotre pairs of symbols and values
        res,pre=0,'I'
        for c in s[::-1]:  #Instead of upwards, we use backwards and can make the rule easier
            res,pre=res+roman_dict[c] if roman_dict[c]>=roman_dict[pre] else res-roman_dict[c],c
        return res
        
                
            
            
            
        
        
        
                
            
            
            
        
        
        
                
            
            
            
        
        