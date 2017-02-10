#My solution, python build in function split and join version, O(n) Space: 
class Solution(object):
    def reverseWords(self, s):
        #:type s: str
        #:rtype: str
        s_list=s.split()
        return ' '.join(s_list[::-1])

#Python build in function split and join version 2, O(n) Space:
class Solution(object):
    def reverseWords(self, s):
        return " ".join(reversed(s.split()))


#Python bulid in function split and join version 2, O(n) Space
#Rverse the whole string then reverse word by word
class Solution(object):
    def reverseWords(self, s):
        words=s[::-1].split()
        return " ".join([word[::-1] for word in words])





        
        