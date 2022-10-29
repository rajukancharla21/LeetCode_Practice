class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==1:
                    continue
                grid[i][j]=201
                if(i>0):
                    grid[i][j]=min(grid[i][j],grid[i-1][j]+1)
                if(j>0):
                    grid[i][j]=min(grid[i][j],grid[i][j-1]+1)
        print(*grid,sep='\n')
        res=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if grid[i][j]==1:
                    continue
                if(i<len(grid)-1):
                    grid[i][j]=min(grid[i][j],grid[i+1][j]+1)
                if(j<len(grid)-1):
                    grid[i][j]=min(grid[i][j],grid[i][j+1]+1)
                res=max(grid[i][j],res)
        print(*grid,sep='\n')
        return -1 if res==201 else res-1
            
        