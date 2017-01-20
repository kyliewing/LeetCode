#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.
#Note: A word is defined as a character sequence consists of non-space characters only.


#Your runtime beats 93.34% of python submissions.(7 min)
class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()               #Use strip to eliminate the emptys in the head and in the tail
        if len(s)==0:return 0     #The case when the length of s is 0
        res=0
        for c in s[::-1]:         #Doing backwards
            if c==' ': break      #Meet an blank
            else: res+=1
        return res
            
        
#No build-in function version:
#Your runtime beats 44.78% of python submissions.
class Solution(object):
    def lengthOfLastWord(self, s):
        res,tail=0,len(s)-1
        while tail>=0 and s[tail]==' ':tail-=1 #Ignore all the blanks
        while tail>=0 and s[tail]!=' ':tail,res=tail-1,res+1#Increment the res until meet a blank
        return res
            

#One line version:
#Your runtime beats 33.94% of python submissions.
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.rstrip().split(' ')[-1])#Build-in function
                        


#Build in Function version
class Solution(object):
    def lengthOfLastWord(self,s):
        return len(s.strip().split(' ')[-1])

#None Build in Function version
class Solution(object):
    def lengthOfLastWord(self,s):
        s=s.strip()
        count=0
        for c in s[::-1]:
            if c!=' ':
                count+=1
            else:
                break
        return count
                