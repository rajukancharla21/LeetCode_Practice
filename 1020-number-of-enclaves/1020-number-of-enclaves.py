class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=[[0]*col for _ in range(row)]
        
        def dfs(i,j,c):
            c+=1
            visited[i][j]=1
            grid[i][j]=0
            for k in [[0,1],[0,-1],[-1,0],[1,0]]:
                ii,jj=i+k[0],j+k[1]
                if isValid(ii,jj):
                    c = dfs(ii,jj,c)
            return c
        
        def isValid(i,j):
            if i>=0 and i<row and j>=0 and j<col and\
            visited[i][j]==0 and grid[i][j]==1:
                return True
            return False
        
        for i in [0,row-1]:
            for j in range(col):
                if isValid(i,j):
                    dfs(i,j,0)
        for i in grid:
            print(*i,sep=" ")
        print("##")
        for i in range(row):
            for j in [0,col-1]:
                if isValid(i,j):
                    dfs(i,j,0)
        for i in grid:
            print(*i,sep=" ")
        res=0
        for i in range(row):
            for j in range(col):
                if isValid(i,j):
                    res += dfs(i,j,0)
        return res
        