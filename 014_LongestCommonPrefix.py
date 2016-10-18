#Write a function to find the longest common prefix string amongst an array of strings.
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
        

#Your runtime beats 50.21% of python submissions.
#"Already implemented in python" version: python library
class Solution(object):
    import os
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)


#Your runtime beats 60.60% of python submissions.
#"Zip" version: 
class Solution(object):
    def longestCommonPrefix(self, strs):
        res=""
        for cs in zip(*strs):    #unzip strs, then deal with every char tuple
            if len(set(cs))==1:  #if the char is unique in the tuple, notice the usesage of set 
                res+=cs[0]
            else:
                break
        return res
        
        
        


        