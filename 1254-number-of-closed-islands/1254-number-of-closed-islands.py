class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for _ in range(m)]
        def dfs(i,j):
            # print("-->",i,j,curRun)
            visited[i][j]=1
            grid[i][j]=1
            for k in [[0,1],[0,-1],[1,0],[-1,0]]:
                ii,jj=i+k[0],j+k[1]
                if isValid(ii,jj):
                    dfs(ii,jj)
        
        def isValid(i,j):
            if i>=0 and i<m and j>=0 and j<n and visited[i][j]==0 and grid[i][j]==0:
                return True
            return False
        
        # Border Top & Bottom
        for i in [0,m-1]:
            for j in range(n):
                if isValid(i,j):
                    dfs(i,j)
        # Border Left & Right
        for i in [0,n-1]:
            for j in range(m):
                if isValid(j,i):
                    dfs(j,i)
        # for i in grid:
        #     print(*i,sep=" ")
        c=0
        for i in range(m):
            for j in range(n):
                if isValid(i,j):
                    c+=1
                    dfs(i,j)
        return c