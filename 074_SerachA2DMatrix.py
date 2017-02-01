#My twice binary search and recursively solution
class Solution(object):
    def searchMatrix(self, matrix, target):
        #:type matrix: List[List[int]]
        #:type target: int
        #:rtype: bool
        n=len(matrix)
        if n>0: m=len(matrix[0]) #notice the condition
        if n==0 or m==0: return False #n=0 or m=0
        elif n==1: row=n-1
        else:
            row=self._findRow(0,n-1,target,matrix,m) #find the rwo number firstly, binary search
        matrix_row=matrix[row]
        return self._findTarget(0,m-1,target,matrix_row) #find the target secondly, binary search
        
    def _findRow(self,begin,end,target,matrix,m): 
        if begin==end: return begin
        mid=(begin+end)/2
        if target==matrix[mid][m-1]: return mid
        elif target<matrix[mid][m-1]: return self._findRow(begin,mid,target,matrix,m) #do not miss return 
        else: return self._findRow(mid+1,end,target,matrix,m)
        
    def _findTarget(self,begin,end,target,matrix_row):
        if begin==end: return matrix_row[begin]==target
        mid=(begin+end)/2
        if target==matrix_row[mid]: return True
        elif target<matrix_row[mid]: return self._findTarget(begin,mid,target,matrix_row) #it's mid not mid-1
        else: return self._findTarget(mid+1,end,target,matrix_row)


#Once binary search (regard the whole lists as a single list)and non-recursively solution:
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix : return False
        rows,cols=len(matrix),len(matrix[0])
        low,high=0,rows*cols-1
        while low<=high:
            mid=(low+high)/2
            num=matrix[mid/cols][mid%cols]
            if num==target: 
                return True
            elif target<num: 
                high=mid-1
            else: 
                low=mid+1
        return False
            
        
        
        
        
        
    
                
                
            
        