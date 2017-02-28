#My two hash table version, O(n) time, O(n) space.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        #:type ransomNote: str
        #:type magazine: str
        #:rtype: bool
        r_length=len(ransomNote)
        m_length=len(magazine)
        #if r_length==0 and m_length==0: return True
        if r_length>m_length: return False
        magazine_dict={}
        ransomNote_dict={}
        for c in magazine:
            magazine_dict[c]=magazine_dict.get(c,0)+1
        for c in ransomNote:
            ransomNote_dict[c]=ransomNote_dict.get(c,0)+1
        for c in ransomNote:
            if c not in magazine_dict or ransomNote_dict[c]>magazine_dict[c]:
                return False
        return True

#One hash table version, O(n) time, O(n) space.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        my_dict=[0]*128
        for c in magazine:
            my_dict[ord(c)]+=1
        for c in ransomNote:
            my_dict[ord(c)]-=1
            if my_dict[ord(c)]<0:
                return False
        return True









        
        