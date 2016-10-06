#Your runtime beats 56.70% of python submissions. (Two Times AC)
#Given a roman numeral, convert it to an integer, input is guaranteed to be within the range from 1 to 3999
#Symbol	I	V	X	L	C	D	M
#Value	1	5	10	50	100	500	1,000
class Solution(object):
    def romanToInt(self, s):
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        if len(s)==0:
            return 0
        if len(s)==1:
            return roman_dict[s]
        i=0
        while i<len(s)-1:
            if roman_dict[s[i]]>=roman_dict[s[i+1]]:
                res+=roman_dict[s[i]]
                i+=1
                continue
            else:
                res+=roman_dict[s[i+1]]-roman_dict[s[i]]
                i+=2
                continue
        if roman_dict[s[-2]]>=roman_dict[s[-1]]:
            res+=roman_dict[s[-1]]
        return res
        
                
            
            
            
        
        