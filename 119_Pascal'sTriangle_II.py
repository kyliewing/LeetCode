#"Array"
#Pascal's Triangle II, Given an index k, return the kth row of the Pascal's triangle.
#For example, given k = 3, Return [1,3,3,1].

#Your runtime beats 94.10% of python submissions.
class Solution(object):
    def getRow(self, rowIndex):
        res=[[1]]
        for i in range(1,rowIndex+1):
            res+=[[1]+[res[i-1][j-1]+res[i-1][j] for j in range(1,i)] +[1]]
        return res[-1]