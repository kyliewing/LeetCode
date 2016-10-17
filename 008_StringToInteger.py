#Your runtime beats 61.78% of python submissions.
#Implement atoi to convert a string to an integer.Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#Related to "Integer", need to check 32 bits overflow
#My solution is not clean
class Solution(object): 
    def myAtoi(self, str):
        nstr=str # Must have this line, otherwise "UnboundLocalError: local variable 'nstr' referenced before assignment"
        if len(str)==0:return 0               #Need to consider the case where the string is empty
        
        i=0
        while i<len(nstr) and nstr[i]==" ":   #Elimate all the blankets
            i+=1
        if i==len(nstr):return 0
        nstr=nstr[i:]
        nstr_1=nstr    
        if nstr[0]=='+' or nstr[0]=='-': nstr_1=nstr[1:]#Didn't consider the case where the first character is "+" or "-"
        if len(nstr_1)==0:return 0
            
        i=0
        while i<len(str) and nstr_1[i]=="0":
            i+=1
        if i==len(nstr_1):return 0
        nstr_2=nstr_1[i:]
        
        if len(nstr_2)==0 or nstr_2[0].isdigit()==False : return 0#If the firest character is not digit, return 0, and need "len(nstr)==0"
        
        i=0
        while i<len(nstr_2) and nstr_2[i].isdigit():     # Loop until the firest character that is not digit
            i+=1
            
        digit_str=nstr_2[:i]       # Slice until the first character that is not digit
        
        if nstr[0]=='-':
            if (-int(digit_str)<-(1<<31)): return -(1<<31)   #Need to check overflow
            else: return -int(digit_str)
        else:
            if (int(digit_str)>((1<<31)-1)): return (1<<31)-1
            else: return int(digit_str)
            


#Your runtime beats 78.60% of python submissions.
#The version that do not use RegEx:
class Solution(object):
    def myAtoi(self, str):
        str=str.strip()      #Use str.strip() to elimate the blanks
        if len(str)==0:return 0 #if str is empty, return 0
        sign,res="",""       #Initialize sign to be an empty string
        if str[0] in "+-":   #If str[0] is + or -, set sign to be str[0]
            sign=str[0]
            str=str[1:]      #New str
        for c in str:        #Loop every char
            if c.isdigit(): res+=c  #Append if it's digit
            else: break
        if len(res)==0: return 0 #Notice that if length of res is 0 after the sign, return 0
        res=int(sign+res)    #res=sign+res
        return max(min(res,2147483647),-2147483648) #Notice to check the overflow, and the usage of min, max
        
        
#Your runtime beats 61.78% of python submissions.
#The version that use RegEx:
class Solution(object):
    import re
    def myAtoi(self, str):
        ress=re.findall('^[\+\-]?0*\d+',str.strip()) #Use regular expression
        return max(min(int(ress[0]),2147483647),-2147483648) if ress else 0#Notice to check overflow
        
        
        

        