#My O(n2) Space Solution:
class Solution(object):
    def rotate(self, matrix):
        #:type matrix: List[List[int]]
        #:rtype: void Do not return anything, modify matrix in-place instead.
        n=len(matrix)
        matrix_copy=[[0 for i in range(n)] for j in range(n)] #initialize matrix_copy and set it as matrix
        for i in range(n):
            for j in range(n):
                matrix_copy[i][j]=matrix[i][j] 
        for i in range(n):                                    #every reverse column of matrix_copy is a row of matrix
            temp=[]
            for j in range(n-1,-1,-1):
                temp.append(matrix_copy[j][i])
            matrix[i]=temp

#My O(1) Space Solution:
class Solution(object):
    def rotate(self, matrix):
        left,right,n=0,len(matrix)-1,len(matrix)
        while left<=right:
            for i in range(left,right):
                one=matrix[left][i]
                two=matrix[i][right]
                three=matrix[right][right-(i-left)]
                four=matrix[right-(i-left)][left]
                matrix[left][i]=four
                matrix[i][right]=one
                matrix[right][right-(i-left)]=two
                matrix[right-(i-left)][left]=three
            left,right=left+1,right-1


#Smart O(1) Space Solution:
#clockwise rotate: first reverse up to down, then transpose || transpose, then reverse row
#anticlockwise rotate: first reverse left to right, then transpose || transpose, then reverse column
class Solution(object):
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        
        
        
        
        

        
        
        