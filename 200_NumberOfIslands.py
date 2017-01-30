#sink version, DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        for i in range(len(grid)):#traversal the whole grid
            for j in range(len(grid[0])):
                if grid[i][j]=='1':#every time meet 1, count +=1
                    count+=1
                    self._sink(i,j,grid)#sink all the nodes which are 1 and connected to grid[i][j]
        return count
    
    def _sink(self,i,j,grid):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
            grid[i][j]='0'
            self._sink(i-1,j,grid)#up
            self._sink(i+1,j,grid)#down
            self._sink(i,j-1,grid)#left
            self._sink(i,j+1,grid)#right
        