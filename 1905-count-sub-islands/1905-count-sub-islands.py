class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row,col=len(grid1),len(grid1[0])
        visited=[[0]*col for _ in range(row)]
        
        def isValid(i,j):
            if i>=0 and i<row and j>=0 and j<col and visited[i][j]==0 and grid1[i][j]==1 and grid2[i][j]==1:
                return True
            return False
        
        def dfs(i,j):
            visited[i][j]=1
            grid2[i][j]=0
            for k in [[0,1],[0,-1],[1,0],[-1,0]]:
                ii,jj=i+k[0],j+k[1]
                if isValid(ii,jj):
                    dfs(ii,jj)

        for i in range(row):
            for j in range(col):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    dfs(i,j)
        c= 0
        for i in range(row):
            for j in range(col):
                if isValid(i,j):
                    print(i,j)
                    c+=1
                    dfs(i,j)
        return c