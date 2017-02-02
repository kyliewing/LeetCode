#My O(m+n) solution
class Solution(object):
    def searchMatrix(self, matrix, target):
        #:type matrix: List[List[int]]
        #:type target: int
        #:rtype: bool
        if not matrix: return False
        elif not matrix[0]: return False
        n,m=len(matrix),len(matrix[0])
        row,col=0,m-1
        while row<=n-1 and col>=0: #notice it's and
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                col-=1
            else:
                row+=1
        return False

#Divide and Conquer version:
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        elif not matrix[0]: return False
        n,m=len(matrix),len(matrix[0])
        low_n,high_n,low_m,high_m=0,n-1,0,m-1
        return self._helper(low_n,high_n,low_m,high_m,matrix,target)
    
    def _helper(self,low_n,high_n,low_m,high_m,matrix,target):
        if low_n==high_n and low_m==high_m:
            return matrix[low_n][low_m]==target
        elif low_n>high_n or low_m>high_m:
            return False
        mid_n=(low_n+high_n)/2
        mid_m=(low_m+high_m)/2
        if target==matrix[mid_n][mid_m]: return True
        elif target>matrix[mid_n][mid_m]:
            return self._helper(low_n,mid_n,mid_m+1,high_m,matrix,target) or self._helper(mid_n+1,high_n,low_m,mid_m,matrix,target) or self._helper(mid_n+1,high_n,mid_m+1,high_m,matrix,target)
        else:
            return self._helper(low_n,mid_n-1,low_m,mid_m-1,matrix,target) or self._helper(mid_n,high_n,low_m,mid_m-1,matrix,target) or self._helper(low_n,mid_n-1,mid_m,high_m,matrix,target)
        
        
        
        
        
        

            
        
        