
#O(n) twice scans version, use dictionary, one time AC
class Solution(object):
    def firstUniqChar(self, s):
        my_dict={}
        for c in s:
            if c in my_dict: my_dict[c]+=1
            else: my_dict[c]=1
        for i in range(len(s)):
            if my_dict[s[i]]==1: return i
        return -1


#O(n) twice scans version, use array to simulate hash table, hash table object can not be faster than a simple array
class Solution(object):
    def firstUniqChar(self,s):
        my_dict=[0]*26
        for c in s: 
            my_dict[ord(c)-ord('a')]+=1 #Notie it's 'a' not a
        for i in range(len(s)):
            if my_dict[ord(s[i])-ord('a')]==1: return i
        return -1

        

#O(n) once scan version, use two pointers
class Solution(object):
    def firstUniqChar(self,s):
        n=len(s)
        if n==0: return -1
        if n==1: return 0
        slow,fast=0,1
        my_dict=[0]*26
        my_dict[ord(s[slow])-ord('a')]+=1
        while fast<n:
            my_dict[ord(s[fast])-ord('a')]+=1
            while slow<n and my_dict[ord(s[slow])-ord('a')]>1: slow+=1  #Notice slow<n #Move slow to the next unique char
            if slow>=n: return -1 #no unique char exists
            if my_dict[ord(s[slow])-ord('a')]==0:#not yet visited by the fast pointer
                my_dict[ord(s[slow])-ord('a')]+=1
                fast=slow #reset the fast pointer
            fast+=1
        return slow



#Python build in method version:
class Solution(object):
    def firstUniqChar(self,s):
        for c in s:
            if s.find(c)==s.rfind(c): return s.find(c) #Build in method: s.find and s.rfind
        return -1


#Python build in method + min version(TLE):
class Solution(object):
    def firstUniqChar(self,s):
        return min([ s.find(c) for c in s if s.count(c)==1] or [-1])
        
        
#Python build in method + min + string.ascii_lowercase:
class Solution(object):
    def firstUniqChar(self,s):
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])






            
        