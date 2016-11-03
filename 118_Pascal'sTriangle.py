#"Array"
#Given numRows, generate the first numRows of Pascal's triangle.

#My iterative version, based on the defination of Pascal's triangle, O(n^2)
#Your runtime beats 90.39% of python submissions.
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for row in range(numRows):
            if row<1: res.append([1]) #For the first row
            else: 
                row_list=[1]#The first "1" in the row
                for num in range(row-1): #The intermediate elements
                    row_list.append(res[row-1][num]+res[row-1][num+1])
                row_list.append(1) #Notice it's () not []! #The last "1" in the row
                res.append(row_list)
        return res
        

#My recursive version, append the temp row based on the previous triangle.
#Your runtime beats 98.65% of python submissions.
class Solution(object):
    def generate(self, numRows):
        if numRows==0: return []
        if numRows==1: return [[1]]
        res=self.generate(numRows-1) #The previous triangle.
        res.append([1]+[res[numRows-2][i]+res[numRows-2][i+1] for i in range(len(res[numRows-2])-1)]+[1])#Append the temp row
        return res#Then return res, Notice that can not res.append and return at the same time "return res.append()".
            
                    
                
                
#Iterative version, O(n^2)
#Your runtime beats 90.39% of python submissions.
class Solution(object):
    def generate(self, numRows):
        res=[]
        if numRows==0: return res
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                if j==0 or j==i:  #for the first and the last element in row
                    row.append(1)
                else:
                    row.append(res[i-1][j-1]+res[i-1][j])#for other elements in row
            res.append(row)
        return res
                    
            
 
#Iterative version, using map, using offset sum of the previous row. 1 3 3 1 0  +  0 1 3 3 1 = 1 4 6 4 1
#Your runtime beats 90.39% of python submissions.
class Solution(object):
    def generate(self, numRows):
        res=[[1]]
        for i in range(1,numRows):
            res+=[map(lambda x,y: x+y,res[-1]+[0],[0]+res[-1])]
        return res[:numRows]
        
            

#Iterative version, set new line with all 1s, then update from the second element to the last second element
#Your runtime beats 96.80% of python submissions.
class Solution(object):
    def generate(self, numRows):
        res=[]
        for row in range(numRows):
            res.append([1]*(row+1))
            for col in range(1,row):
                res[row][col]=res[row-1][col-1]+res[row-1][col]
        return res
        
            
 
######??????
#1-line Python Solution
class Solution:
    def generate(self, numRows):
        return map(lambda m: reduce(lambda r, n: r + [r[-1] * (m - n) / (n + 1)], xrange(m), [1]), xrange(numRows))

                
##############################
def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
        res += [[1] + [res[i-1][j]+res[i-1][j+1] for j in range(i-1)] + [1]]
    return res if numRows else []



##############################
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows: return []
        out = [[1 for i in xrange(row)] for row in xrange(1, numRows+1)]
        for row in xrange(1, numRows):
            for i in xrange(1, row): out[row][i] = out[row-1][i-1] + out[row-1][i]
        return out

                
                
                            
                
                
                

                
                
                
                            
                
                
                
        