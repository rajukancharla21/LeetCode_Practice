class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curMax=0
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for _ in range(m)]
        def dfs(i,j,curRun):
            # print("-->",i,j,curRun)
            curRun+=1
            visited[i][j]=1
            for k in [[0,1],[0,-1],[1,0],[-1,0]]:
                ii,jj=i+k[0],j+k[1]
                if isValid(ii,jj):
                    curRun = dfs(ii,jj,curRun)
            return curRun
        
        def isValid(i,j):
            if i>=0 and i<m and j>=0 and j<n and visited[i][j]==0 and grid[i][j]==1:
                return True
            return False
        for i in range(m):
            for j in range(n):
                if isValid(i,j):
                    # print(i,j)
                    t = dfs(i,j,0)
                    # print("##",t)
                    if curMax<t:
                        curMax=t
        return curMax
                    
                    
            
        