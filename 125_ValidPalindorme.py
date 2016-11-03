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
            
        

       