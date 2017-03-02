#My solution:
class Solution(object):
    def wordPattern(self, pattern, str):
        #:type pattern: str
        #:type str: str
        #:rtype: bool
        if len(pattern)==0 and len(str)==0: return False
        my_hash={}
        str_hash={}
        i=slow=fast=0
        while i<len(pattern) and fast<len(str):
            while fast<len(str) and str[fast]!=' ':
                    fast+=1
            if pattern[i] not in my_hash and str[slow:fast] not in str_hash:
                my_hash[pattern[i]]=str[slow:fast]
                str_hash[str[slow:fast]]=pattern[i]
            elif pattern[i] in my_hash and str[slow:fast] in str_hash:
                if my_hash[pattern[i]]!=str[slow:fast] or str_hash[str[slow:fast]]!=pattern[i]:
                    return False
            else:
                return False
            i+=1
            slow=fast=fast+1
        return i==len(pattern) and fast==len(str)+1

#My solution
class Solution(object):
    def wordPattern(self, pattern, str):
        words=str.split(" ")
        if len(pattern)==0 and len(words)==0: return False
        if len(pattern)!=len(words): return False
        p_hash={}
        str_hash={}
        for i in range(len(pattern)):
            if pattern[i] not in p_hash and words[i] not in str_hash:
                p_hash[pattern[i]]=str_hash[words[i]]=i
            elif pattern[i] in p_hash and words[i] in str_hash:
                if p_hash[pattern[i]]!=str_hash[words[i]]:
                    return False
            else:
                return False
        return True
        
        
        
                
        
                
        