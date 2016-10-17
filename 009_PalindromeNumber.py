#Determine whether an integer is a palindrome. Do this without extra space.

#Your runtime beats 29.83% of python submissions.
class Solution(object):
    def isPalindrome(self, x):
        num_str=str(x)
        i=0
        j=len(num_str)-1
        while i<j:
            if num_str[i]!=num_str[j]:
                return False
            i+=1
            j-=1
        return True
        
#Your runtime beats 59.25% of python submissions.
#Use string
class Solution(object):
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]

#Determine whether an integer is a palindrome. Do this without extra space.
#Your runtime beats 64.33% of python submissions.
#Do not use string, use integer
class Solution(object):
    def isPalindrome(self, x):
        orig,res=x,0
        if x<0: return False
        while x:
            res=res*10+x%10
            x/=10
        return res==orig
        
        