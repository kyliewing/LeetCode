#Store the pair chars version.
class Solution(object):
    def isIsomorphic(self, s, t):
        #:type s: str
        #:type t: str
        #:rtype: bool
        s_hash={}
        t_hash={}
        for i in range(len(s)):
            if s[i] not in s_hash:
                s_hash[s[i]]=t[i] 
            elif s[i] in s_hash and s_hash[s[i]]!=t[i]:
                return False
            if t[i] not in t_hash:
                t_hash[t[i]]=s[i]
            elif t[i] in t_hash and t_hash[t[i]]!=s[i]:
                return False
        return True
       
#Store the pair chars version 2.
class Solution(object):
    def isIsomorphic(self, s, t):
        s_hash=[0]*256
        t_hash=[0]*256
        for i in range(len(s)):
            if s_hash[ord(s[i])]==0 and t_hash[ord(t[i])]==0:
                s_hash[ord(s[i])]=t[i]
                t_hash[ord(t[i])]=s[i]
            elif s_hash[ord(s[i])]!=t[i] or t_hash[ord(t[i])]!=s[i]:
                return False
        return True



#Store the index informatoin version.
class Solution(object):
    def isIsomorphic(self, s, t):
        s_hash=[0]*256
        t_hash=[0]*256
        for i in range(len(s)):
            if s_hash[ord(s[i])]!=t_hash[ord(t[i])]:
                return False
            s_hash[ord(s[i])]=i+1  #store the index information
            t_hash[ord(t[i])]=i+1  #store the index information
        return True





        