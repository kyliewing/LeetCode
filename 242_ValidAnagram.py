
#My two hash table version, One Time AC
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t): return False
        s_hash,t_hash=[0]*26,[0]*26
        for i in range(len(s)):
            s_hash[ord(s[i])-ord('a')]+=1
            t_hash[ord(t[i])-ord('a')]+=1
        return s_hash==t_hash
          
#Python build in function version:
class Solution(object):
    def isAnagram(self,s,t):
        return sorted(s)==sorted(t)

#Two hash table version:
class Solution(object):
    def isAnagram(self,s,t):
        s_hash,t_hash=[0]*26, [0]*26
        for c in s:
            s_hash[ord(c)-ord('a')]+=1
        for c in t:
            t_hash[ord(c)-ord('a')]+=1
        return s_hash==t_hash

#One hash table version:
class Solution(object):
    def isAnagram(self,s,t):
        my_hash=[0]*26
        for c in s: my_hash[ord(c)-ord('a')]+=1
        for c in t: my_hash[ord(c)-ord('a')]-=1
        return my_hash==[0]*26
        

#Dictionary version:
class Solution(object):
    def isAnagram(self,s,t):
        dict1,dict2={},{}
        for c in s: dict1[c]=dict1.get(c,0)+1  #dictionary's get method
        for c in t: dict2[c]=dict2.get(c,0)+1
        return dict1==dict2
        
        
        
        
        
    

        