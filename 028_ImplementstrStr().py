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
        