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
        