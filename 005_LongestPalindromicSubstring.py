#O(n^2) Solution, staring from the left side to check
class Solution(object):
    def longestPalindrome(self, s):
        #:type s: str
        #:rtype: str
        res=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.check(s[i:j+1]):
                    if (j-i+1)>len(res):
                        res=s[i:j+1]
        return res
    def check(self,s):
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
        
#O(n^2) Solution, staring from the middle to check, AC.
class Solution(object):
    def longestPalindrome(self,s):
        res=""
        for i in range(len(s)):
            #check for odd substrings
            temp=self.check(s,i,i)
            if len(temp)>len(res):
                res=temp
            #check for even substrings
            temp=self.check(s,i,i+1)
            if len(temp)>len(res):
                res=temp
        return res
    def check(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]


#O(n^2) Solution, starting from the middle to check and starting check the longest one, AC:
class Solution(object):
    def longestPalindrome(self,s):
        r_len=len(s)
        while r_len>0:
            for i in range(len(s)-r_len+1):
                left,right=i,i+r_len-1
                flag=True
                while left<right:
                    if s[left]!=s[right]:
                        flag=False
                        break
                    left+=1
                    right-=1
                if flag==True: 
                    return s[i:i+r_len]
            r_len-=1
        return ""
         
#O(N) Solution, Manacher's Algorithm.           
                












        
        
        
        