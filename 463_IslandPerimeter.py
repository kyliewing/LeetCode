#My intuitive scan version, O(n*m) time, O(1) space, One Time AC.
class Solution(object):
    def islandPerimeter(self, grid):
        #:type grid: List[List[int]]
        #:rtype: int
        perimeter=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    perimeter+=1-grid[i-1][j] if 0<=i-1<=m-1 else 1
                    perimeter+=1-grid[i+1][j] if 0<=i+1<=m-1 else 1
                    perimeter+=1-grid[i][j-1] if 0<=j-1<=n-1 else 1
                    perimeter+=1-grid[i][j+1] if 0<=j+1<=n-1 else 1
        return perimeter

#find number of neighbours version, One Time AC.
#loop over the matrix and count the number of islands;
#if the current dot is an island, count if it has any right neighbour or down neighbour;
#the result is islands * 4 - neighbours * 2
class Solution(object):
    def islandPerimeter(self, grid):
        islands,neighbors=0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    islands+=1
                    if i+1<len(grid) and grid[i+1][j]==1: neighbors+=1
                    if j+1<len(grid[0]) and grid[i][j+1]==1: neighbors+=1
        return 4*islands-2*neighbors

#DFS version:
#The idea here is that each land cell contributes as many lines in perimeter as it's surrounded by water / boundary.
class Solution(object):
    def islandPerimeter(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return self.dfs(grid,i,j)
        return 0
        
    def dfs(self, grid, i, j):
        if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]==0: return 1
        if grid[i][j]==-1: return 0
        grid[i][j]=-1  #mark as visited
        res=self.dfs(grid,i-1,j)+self.dfs(grid,i+1,j)+self.dfs(grid,i,j-1)+self.dfs(grid,i,j+1)
        return res
        










        
        