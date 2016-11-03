#"String" "Two Pointers"
#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#Note:
#Have you consider that the string might be empty? This is a good question to ask during an interview.
#For the purpose of this problem, we define empty string as valid palindrome.


#My two pointers version.
#Your runtime beats 85.87% of python submissions.
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower().strip()
        if len(s)==0: return True
        head,tail=0,len(s)-1
        while head<tail:
            if not (s[head].isalpha() or s[head].isdigit()): 
                head+=1
                continue
            if not (s[tail].isalpha() or s[tail].isdigit()): 
                tail-=1
                continue
            if s[head]!=s[tail]: return False
            else:
                head,tail=head+1,tail-1
        return True
            
        
#Better
#Your runtime beats 96.53% of python submissions.
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower().strip()
        if len(s)==0: return True
        head,tail=0,len(s)-1
        while head<tail:
            if not (s[head].isalnum()): #The usage of string.isalnum()
                head+=1
                continue
            if not (s[tail].isalnum()): 
                tail-=1
                continue
            if s[head]!=s[tail]: return False
            head,tail=head+1,tail-1
        return True
         
            
#Build in function version
#Your runtime beats 78.80% of python submissions.
class Solution(object):
    def isPalindrome(self, s):
        s=[c.lower() for c in s if c.isalnum()] #Do not miss s.lower()
        return s==s[::-1]
         
            

#Regex Version
#Your runtime beats 78.80% of python submissions.
import re
class Solution(object):
    def isPalindrome(self, s):
        s=re.sub("[^A-Za-z0-9]", "",s).lower()#Do not miss lower
        return s==s[::-1]
         
            
        
        
        
       