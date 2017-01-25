
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


#O(n) twice scans version, use array to simulate hash table
class Solution(object):
    def firstUniqChar(self,s):
        my_dict=[0]*26
        for c in s: 
            my_dict[ord(c)-ord('a')]+=1 #Notie it's 'a' not a
        for i in range(len(s)):
            if my_dict[ord(s[i])-ord('a')]==1: return i
        return -1
        

#O(n) once scan version, use two pointers







#Python build in method version:
class Solution(object):
    def firstUniqChar(self,s):
        for c in s:
            if s.find(c)==s.rfind(c): return s.find(c) #Build in method: s.find and s.rfind







            
        