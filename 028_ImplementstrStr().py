#Your runtime beats 46.56% of python submissions.
#Implement strStr().
#Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle) #Python string's find method
        

#Easy O(n*m) algorithm
class Solution(object):
    def strStr(self,heystack,needle):
        for i in range(len(heystack)-len(needle)+1):
            if heystack[i:i+len(needle)]==needle:
                return i
        return -1

#Easy O(n*m) algorithm
class Solution(object):
    def strStr(self,heystack,needle):
        for i in range(len(heystack)-len(needle)+1):
            j=0
            while j<len(needle):
                if heystack[j+i]!=needle[j]:
                    break
                j+=1
            if j==len(needle):
                return i
        return -1
        
#O(n+m) KMP string searching algorithm














