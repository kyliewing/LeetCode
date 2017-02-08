#My backwards loop version:
class Solution(object):
    def titleToNumber(self, s):
        #:type s: str
        #:rtype: int
        if len(s)==0: return 0
        base,result=1,0
        for c in s[::-1]:
            result+=(ord(c)-ord('A')+1)*base   #Notice "ord"
            base*=26
        return result

#Forwards loop version:
class Solution(object):
    def titleToNumber(self,s):
        result=0
        for c in s:
            result=result*26+(ord(c)-ord('A')+1)
        return result
        
            