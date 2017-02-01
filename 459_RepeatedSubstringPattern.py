#My compare iteratively by factor version:
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if len(str)==0 or len(str)==1: return False
        for i in range(1,len(str)/2+1):
            if len(str)%i==0:
                sub_string=str[:i]
                flag=True
                for j in range(i,len(str),i):
                    if sub_string!=str[j:j+i]: flag=False
                if flag==True: return True
        return False