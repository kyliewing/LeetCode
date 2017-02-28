
#My intuitive O(n) space version, TLE
class Solution(object):
    def reverseVowels(self, s):
        #:type s: str
        #:rtype: str
        vowels=""
        for c in s:
            if c in ['a','e','i','o','u','A','E','I','O','U']:
                vowels+=c
        i=len(vowels)-1
        res=""
        for j in range(len(s)):
            if s[j] in ['a','e','i','o','u','A','E','I','O','U']:
                res+=vowels[i]
                i-=1
            else:
                res+=s[j]
        return res

#My two pointers version, O(n) time, O(n) space.
class Solution(object):
    def reverseVowels(slef, s):
        left,right=0,len(s)-1
        list_s=list(s)
        while left<right:
            if list_s[left] not in ['a','e','i','o','u','A','E','I','O','U']:
                left+=1
                continue
            if list_s[right] not in ['a','e','i','o','u','A','E','I','O','U']:
                right-=1
                continue
            temp=list_s[left]
            list_s[left]=s[right]
            list_s[right]=temp
            left,right=left+1,right-1
        return ''.join(list_s)
        
#My two pointers version 2, O(n) time, O(n) space.
class Solution(object):
    def reverseVowels(self, s):
        left,right=0,len(s)-1
        list_s=list(s)
        while left<right:
            while left<right and list_s[left] not in ['a','e','i','o','u','A','E','I','O','U']:
                left+=1
            while left<right and list_s[right] not in ['a','e','i','o','u','A','E','I','O','U']:
                right-=1
            temp=list_s[left]
            list_s[left]=list_s[right]
            list_s[right]=temp
            left, right=left+1,right-1
        return ''.join(list_s)
        
        
        
        