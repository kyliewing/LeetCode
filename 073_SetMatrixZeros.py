
#My O(n) space version
class Solution(object):
    def setZeroes(self, matrix):
        #:type matrix: List[List[int]]
        #:rtype: void Do not return anything, modify matrix in-place instead.
        rows_zero=[]
        cols_zero=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows_zero.append(i)
                    cols_zero.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows_zero or j in cols_zero:
                    matrix[i][j]=0


#O(1) space version
"""
My idea is simple: store states of each row in the first of that row, and store states of
 each column in the first of that column. Because the state of row0 and the state of 
 column0 would occupy the same cell, I let it be the state of row0, and use another variable
  "col0" for column0. In the first phase, use matrix elements to set states in a top-down way.
   In the second phase, use states to set matrix elements in a bottom-up way.
"""
class Solution(object):
    def setZeroes(self, matrix):
        col0,n,m=1,len(matrix),len(matrix[0])
        for i in range(n):
            if matrix[i][0]==0: col0=0
            for j in range(1,m):
                if matrix[i][j]==0: matrix[i][0],matrix[0][j]=0,0
        for i in range(n-1,-1,-1):
            for j in range(m-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col0==0:
                matrix[i][0]=0
                
        










