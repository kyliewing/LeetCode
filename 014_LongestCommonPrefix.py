#Your runtime beats 22.45% of python submissions
class Solution(object):
    def longestCommonPrefix(self, strs):
        i=1
        res=""
        if len(strs)==0:
            return ""
        while i:
            Flag=True
            for str in strs:
                if i>len(str) or strs[0][:i]!=str[:i]:
                    Flag=False
            if Flag:
                res=strs[0][:i]
                i+=1
            else:
                break
        return res
        