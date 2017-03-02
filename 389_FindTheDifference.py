#Hash Table version.
class Solution(object):
    def findTheDifference(self, s, t):
        #:type s: str
        #:type t: str
        #:rtype: str
        my_hash=[0]*256
        for c in s:
            my_hash[ord(c)]+=1
        for c in t:
            my_hash[ord(c)]-=1
        for c in t:
            if my_hash[ord(c)]<0:
                return c

#Bit Manipulation version.
class Solution(object):
    def findTheDifference(self, s, t):
        res=0
        for c in s:
            res^=ord(c)
        for c in t:
            res^=ord(c)  #notice ord()
        return chr(res)  #notice chr()


#Bit Manipulation version2.
class Solution(object):
    def findTheDifference(self, s, t):
        res=0
        for c in s+t:
            res^=ord(c)
        return chr(res)
        
        
        



        